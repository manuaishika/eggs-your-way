# Eggs Your Way

Static site for a pasteurised egg and liquid egg business.
Plain HTML, one shared stylesheet, a little vanilla JavaScript. No build step,
no dependencies, no npm.

```
index.html         home — range teaser, why pasteurised, reviews, converter, who it's for
shop.html          the four products, each with a photo placeholder and a WhatsApp order link
why-it-works.html  the pasteurisation science — the temperature trick, both production lines, shelf life
recipes.html       recipe ideas that get simpler with pasteurised egg (placeholder copy, see below)
business.html      pitch + ordering info for cafés, hotels, cloud kitchens and meal-prep services
about.html         about us (mostly placeholder copy, see below) plus the certifications section
contact.html       order form that composes a WhatsApp message, plus FAQs
style.css          every style, shared by all pages
logo.png           the logo, trimmed
favicon.png        tab icon
fonts/             New Spirit (self-hosted, see licensing note below)
build.py           optional — regenerates every page from shared header/footer templates
```

## Putting it live

Push everything to the repo root, then **Settings → Pages → Build and deployment**,
Source *Deploy from a branch*, branch `main`, folder `/ (root)`. Live at
`https://manuaishika.github.io/eggs-your-way/` within a minute or two.

Preview locally with `python3 -m http.server` in this folder, then open
`localhost:8000`.

## Font licensing

`fonts/NewSpirit-*.otf` need a genuine licence for New Spirit (Sharp Type /
Adobe Fonts) before this goes out on the live, public site. Confirm the
files in this folder came from an actual purchase or an active Adobe Fonts
subscription — not a redistribution site — before deploying.

## build.py

The nav and footer are identical on every page, which is exactly the kind of
thing that drifts out of sync after a few edits. `build.py` holds them once and
writes the pages out. Edit the page bodies in `build.py` and run `python3 build.py`,
or ignore it entirely and edit the HTML directly — the site works either way. If you
stop using it, delete it so nobody overwrites their own edits by running it later.

## Fill these in before it goes live

| Placeholder | Where | What to put |
|---|---|---|
| `[FSSAI number]` | about.html certifications section | Real FSSAI licence number |
| Cold-chain / batch-testing copy | about.html certifications section | What's actually done, or which lab/standard is used |
| `[Price]` / `[Price per tray]` | shop.html, one per product | Real prices per pack size |
| `[Confirm the largest pack size...]`, standing-order schedule | business.html | Real bulk pack sizes and whether standing orders exist |
| Recipe text marked `[Real recipe and quantities to come.]` | recipes.html, six cards | Actual recipes with quantities |
| Review quotes and names | index.html "What people say" | Real customer quotes, or remove the section until there are some |
| All other `[bracketed text]` | about.html, contact.html FAQs | His actual story, minimum order, delivery speed, and answers |
