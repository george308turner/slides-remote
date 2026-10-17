#!/usr/bin/env python3
"""Copies the help pages from the app repos into src/pages, then run build.py.

    python3 sync-docs.py   # then: python3 build.py

The app repos' docs/help.md are the source of truth. The site's copies differ only in the
changes below: the sentence saying where the page is hosted goes, the email and the privacy
links become site links, and the Play price (still a placeholder) is left out.
"""
import re
import sys
from pathlib import Path

REPOS = Path("/Users/georgeturner/Developer/swift-projects/Slides Remote Notes")
PAGES = Path(__file__).parent / "src" / "pages"
EMAIL = "georgeturner308@icloud.com"
SITE = "https://slidesremote.app/"

DOCS = [
    (REPOS / "Slides Remote" / "docs" / "help.md", "help-apple.md", [
        (" This page is the app's help, hosted at https://slidesremote.app/support/apple/.", ""),
        ("Full policy: https://slidesremote.app/privacy/.", "Full policy: [Privacy Policy]({{URL:privacy/}})."),
    ]),
    (REPOS / "Slides Remote Android" / "docs" / "help.md", "help-android.md", [
        (" This page is the Android app's support page (https://slidesremote.app/support/android/).", ""),
        ("one-time purchase of {{PRICE}} on Google Play", "one-time purchase on Google Play"),
        ("Full policy: https://slidesremote.app/privacy/android/.", "Full policy: [Privacy Policy for Android and Wear OS]({{URL:privacy/android/}})."),
    ]),
]


def main():
    for source, name, changes in DOCS:
        text = source.read_text(encoding="utf-8")
        for old, new in changes:
            if old not in text:
                sys.exit(f"{source}: expected text not found, update sync-docs.py: {old!r}")
            text = text.replace(old, new)
        text = text.replace(EMAIL, "{{EMAIL}}")
        text = re.sub(re.escape(SITE) + r"([\w/-]*)", lambda m: "{{URL:" + m.group(1) + "}}", text)
        left = sorted(set(re.findall(r"\{\{(?!EMAIL\}\}|URL:)[^}]+\}\}", text)))
        if left:
            sys.exit(f"{source}: placeholders the site can't fill: {left}")
        (PAGES / name).write_text(text, encoding="utf-8")
        print("synced", name, "from", source.relative_to(REPOS))


if __name__ == "__main__":
    main()
