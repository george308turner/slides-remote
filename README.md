# Slides Remote website

The product site for Slides Remote, served by GitHub Pages: a landing page in 14 languages, help, privacy policies and terms.

Edit the sources in `src/` (`template.html`, `body.html`, `doc.html`, `strings/*.json`, `pages/*.md`), then run:

```sh
python3 build.py           # builds index.html, <lang>/index.html and the help, privacy and terms pages
python3 build.py --check   # checks the translations only
```

Commit the generated pages too: GitHub Pages serves this folder as it is.
