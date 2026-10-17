#!/usr/bin/env python3
"""Builds the site: index.html (US English) and <lang>/index.html for each translation.

    python3 build.py           # build every language
    python3 build.py --check   # only check the translations; exit 1 on problems

Edit src/body.html, src/template.html and src/strings/*.json, never the generated pages.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
# The address the site is served from, for the hreflang and canonical links. Change it if
# you use a custom domain.
BASE = "https://george308turner.github.io/slides-remote/"

# Shown on the help, privacy and terms pages.
SUPPORT_EMAIL = "georgeturner308@icloud.com"

# English-only documents: Markdown source in src/pages, page folder.
DOCS = [
    ("support.md", "support"),
    ("help-apple.md", "support/apple"),
    ("help-android.md", "support/android"),
    ("privacy.md", "privacy"),
    ("privacy-android.md", "privacy/android"),
    ("terms.md", "terms"),
]

# A page opened from disk (file://) shows a folder listing for a link to a folder, where a
# server would serve its index.html, so add index.html to such links when opened from disk.
FILE_LINKS_JS = r"""  if (location.protocol === "file:") {
    document.querySelectorAll("a[href]").forEach(a => {
      const href = a.getAttribute("href");
      if (/^([a-z]+:|#|\/\/)/i.test(href)) return;
      const [path, hash = ""] = href.split("#");
      if (path.endsWith("/")) a.setAttribute("href", path + "index.html" + (hash && "#" + hash));
    });
  }"""

# The app's languages (Claude Notes/Localisation): code, folder, name in that language, og:locale.
LANGS = [
    ("en",      "",        "English (US)",        "en_US"),
    ("en-GB",   "en-gb",   "English (UK)",        "en_GB"),
    ("de",      "de",      "Deutsch",             "de_DE"),
    ("es",      "es",      "Español",             "es_ES"),
    ("fr",      "fr",      "Français",            "fr_FR"),
    ("it",      "it",      "Italiano",            "it_IT"),
    ("ja",      "ja",      "日本語",               "ja_JP"),
    ("ko",      "ko",      "한국어",               "ko_KR"),
    ("nl",      "nl",      "Nederlands",          "nl_NL"),
    ("pl",      "pl",      "Polski",              "pl_PL"),
    ("pt-BR",   "pt-br",   "Português (Brasil)",  "pt_BR"),
    ("ru",      "ru",      "Русский",             "ru_RU"),
    ("zh-Hans", "zh-hans", "简体中文",             "zh_CN"),
    ("zh-Hant", "zh-hant", "繁體中文",             "zh_TW"),
]

PLACEHOLDER = re.compile(r"\{\w+\}")
TAG = re.compile(r"</?\w+[^>]*>")


def load(code):
    path = SRC / "strings" / f"{'en' if code == 'en' else code}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_")}


def check(english, code, strings):
    problems = []
    for key, en in english.items():
        if key not in strings:
            problems.append(f"{code}: missing {key}")
            continue
        text = strings[key]
        if sorted(PLACEHOLDER.findall(en)) != sorted(PLACEHOLDER.findall(text)):
            problems.append(f"{code}: {key}: placeholders differ ({PLACEHOLDER.findall(text)})")
        if sorted(TAG.findall(en)) != sorted(TAG.findall(text)):
            problems.append(f"{code}: {key}: HTML tags differ ({TAG.findall(text)})")
        if '"' in text and not key.startswith("js."):
            problems.append(f'{code}: {key}: use typographic quotes, not "')
    for key in strings:
        if key not in english:
            problems.append(f"{code}: unknown key {key}")
    return problems


def slug(text):
    """GitHub-style heading anchors, so the docs' existing #links keep working."""
    text = re.sub(r"<[^>]+>", "", html.unescape(text)).lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def inline(text):
    """Markdown inline: `code`, [links](url), **bold**, *italic*. HTML is escaped."""
    parts = re.split(r"(`[^`]+`)", text)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            out.append("<code>" + html.escape(part[1:-1], quote=False) + "</code>")
            continue
        t = html.escape(part, quote=False)
        t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
        out.append(t)
    return "".join(out)


LIST_ITEM = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def markdown(source):
    """The Markdown the docs use: headings, paragraphs, rules and nested lists."""
    lines = source.split("\n")
    out, para, stack = [], [], []  # stack: [indent, tag] of open lists, each with an open <li>

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists(to_indent=-1):
        while stack and stack[-1][0] > to_indent:
            out.append(f"</li></{stack.pop()[1]}>")

    for i, line in enumerate(lines):
        item = LIST_ITEM.match(line)
        if item:
            flush_para()
            indent, tag = len(item.group(1)), "ol" if item.group(2)[0].isdigit() else "ul"
            close_lists(indent)
            if stack and stack[-1][0] == indent:
                if stack[-1][1] != tag:
                    close_lists(indent - 1)
                else:
                    out.append("</li>")
            if not stack or stack[-1][0] < indent:
                out.append(f"<{tag}>")
                stack.append([indent, tag])
            out.append("<li>" + inline(item.group(3)))
        elif not line.strip():
            flush_para()
            following = next((l for l in lines[i + 1:] if l.strip()), "")
            if stack and not (LIST_ITEM.match(following) or following.startswith(" ")):
                close_lists()
        elif stack and line.startswith(" "):
            out.append(" " + inline(line.strip()))
        else:
            close_lists()
            heading = re.match(r"^(#{1,3})\s+(.*)$", line)
            if heading:
                flush_para()
                level, text = len(heading.group(1)), inline(heading.group(2))
                out.append(f'<h{level} id="{slug(text)}">{text}</h{level}>')
            elif re.match(r"^-{3,}\s*$", line):
                flush_para()
                out.append("<hr>")
            else:
                para.append(line.strip())
    flush_para()
    close_lists()
    return "\n".join(out)


def build_doc(doc_template, style, name, folder):
    source = (SRC / "pages" / name).read_text(encoding="utf-8")
    depth = folder.count("/") + 1
    root = "../" * depth
    source = re.sub(r"\{\{URL:([^}]*)\}\}", lambda m: root + m.group(1), source)
    title = re.search(r"^# (.+)$", source, re.M).group(1)
    first_para = next(p for p in source.split("\n\n") if p.strip() and not p.startswith(("#", "*", "-")))
    description = re.sub(r"\[([^\]]+)\]\([^)]*\)|[*`]", lambda m: m.group(1) or "", first_para).strip().replace("{{EMAIL}}", SUPPORT_EMAIL)
    content = markdown(source).replace(
        "{{EMAIL}}", f'<a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>')
    back = ""
    if folder.count("/"):
        parent = folder.rsplit("/", 1)[0]
        label = {"support": "Help", "privacy": "Privacy Policy"}[parent]
        back = f'<a class="back" href="../">‹ {label}</a>'
    page = (doc_template.replace("{{STYLE}}", style).replace("{{CONTENT}}", content)
            .replace("{{BACK}}", back).replace("{{FILE_LINKS}}", FILE_LINKS_JS)
            .replace("{{TITLE}}", html.escape(title)).replace("{{DESCRIPTION}}", html.escape(description))
            .replace("{{CANONICAL}}", BASE + folder + "/").replace("{{HOME}}", root)
            .replace("{{A}}", root + "assets/").replace("{{R}}", root))
    leftover = re.findall(r"\{\{[^}]+\}\}", page)
    if leftover:
        sys.exit(f"{name}: unfilled {leftover}")
    return page


def href(from_folder, to_folder):
    up = "../" if from_folder else ""
    return up + (to_folder + "/" if to_folder else "") or "./"


def build_page(template, body, english, code, folder, og_locale, all_strings):
    strings = {**english, **(all_strings[code] or {})}
    prefix = "../" if folder else ""

    def fill(text):
        text = text.replace("{{A}}", prefix + "assets/").replace("{{R}}", prefix)
        return re.sub(r"\{\{([a-z0-9_]+\.[a-z0-9_.]+)\}\}",
                      lambda m: strings[m.group(1)].replace('"', "&quot;"), text)

    page_body = fill(body).replace("{total}", '<span id="total">6</span>')

    options = "".join(
        f'<option value="{c}"{" selected" if c == code else ""} lang="{c}">{html.escape(name)}</option>'
        for c, _, name, _ in LANGS)
    page_body = page_body.replace("{{LANG_OPTIONS}}", options)

    alternates = "\n".join(
        [f'<link rel="canonical" href="{BASE}{folder + "/" if folder else ""}">']
        + [f'<link rel="alternate" hreflang="{c}" href="{BASE}{f + "/" if f else ""}">' for c, f, _, _ in LANGS]
        + [f'<link rel="alternate" hreflang="x-default" href="{BASE}">'])

    js_strings = {k[3:]: v for k, v in strings.items() if k.startswith("js.")}
    js_langs = {}
    for c, f, _, _ in LANGS:
        other = {**english, **(all_strings[c] or {})}
        js_langs[c] = {"href": href(folder, f), "banner": other["lang.banner"],
                       "go": other["lang.banner_go"], "close": other["lang.banner_close"]}
    as_js = lambda obj: json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

    page = template.replace("{{BODY}}", page_body)
    page = page.replace("{{JS_STRINGS}}", as_js(js_strings)).replace("{{JS_LANGS}}", as_js(js_langs))
    page = page.replace("{{ALTERNATES}}", alternates).replace("{{OG_LOCALE}}", og_locale)
    page = page.replace("{{BASE}}", BASE).replace("{{LANG}}", code).replace("{{FILE_LINKS}}", FILE_LINKS_JS)
    page = fill(page)
    leftover = re.findall(r"\{\{[^}]+\}\}", page)
    if leftover:
        sys.exit(f"{code}: unfilled {leftover}")
    return page


def main():
    english = load("en")
    all_strings = {code: load(code) for code, *_ in LANGS}
    problems = []
    for code, *_ in LANGS[1:]:
        if all_strings[code] is None:
            problems.append(f"{code}: no src/strings/{code}.json (English is used)")
        else:
            problems += check(english, code, all_strings[code])
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    if "--check" in sys.argv:
        sys.exit(1 if problems else 0)

    template = (SRC / "template.html").read_text(encoding="utf-8")
    body = (SRC / "body.html").read_text(encoding="utf-8")
    for code, folder, _, og_locale in LANGS:
        out = ROOT / folder / "index.html" if folder else ROOT / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(build_page(template, body, english, code, folder, og_locale, all_strings), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))

    style = re.search(r"<style>(.*?)</style>", template, re.S).group(1)
    doc_template = (SRC / "doc.html").read_text(encoding="utf-8")
    for name, folder in DOCS:
        out = ROOT / folder / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build_doc(doc_template, style, name, folder), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
