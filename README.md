# Eggs Your Way

Four-page static site for a pasteurised egg and liquid egg business.
Plain HTML, one shared stylesheet, a little vanilla JavaScript. No build step,
no dependencies, no npm.

```
index.html     home — range, why pasteurised, converter, who it's for
process.html   how it's made — the temperature trick, both production lines,
               shelf life, and the section aimed at people who train
about.html     about us (mostly placeholder copy, see below)
contact.html   order form that composes a WhatsApp message, plus FAQs
style.css      every style, shared by all four pages
logo.png       the logo, trimmed
favicon.png    tab icon
build.py       optional — regenerates the four pages from shared header/footer
```

## Putting it live

Push everything to the repo root, then **Settings → Pages → Build and deployment**,
Source *Deploy from a branch*, branch `main`, folder `/ (root)`. Live at
`https://manuaishika.github.io/eggs-your-way/` within a minute or two.

Preview locally with `python3 -m http.server` in this folder, then open
`localhost:8000`.

## build.py

The nav and footer are identical on all four pages, which is exactly the kind of
thing that drifts out of sync after a few edits. `build.py` holds them once and
writes the pages out. Edit the page bodies in `build.py` and run `python3 build.py`,
or ignore it entirely and edit the HTML directly — the site works either way. If you
stop using it, delete it so nobody overwrites their own edits by running it later.

## Fill these in before it goes live

| Placeholder | Where | What to put |
|---|---|---|
| `910000000000` | every WhatsApp link, and `phone` in contact.html's script | Number with country code, no `+` or spaces |
| `+91 00000 00000` | footers, contact page | Same number, formatted for reading |
| `hello@eggsyourway.in` | footers, contact page | Real email |
| `[city]` | footers, contact page | Delivery area |
| `[number]` | footer | FSSAI licence number |
| Opening hours | footers, contact page | Real hours |
| Pack sizes | home, "Getting it to you" | Real tray and pouch sizes |
| All `[bracketed text]` | about.html, contact FAQs | His actual story and answers |

`about.html` is deliberately a skeleton — an about page written by someone who has
never met him is worse than no about page. The prompts in brackets say what each
paragraph should do.

## Things worth checking with him

The process page states 57°C for about an hour for shell eggs, and 60–64°C for a few
minutes for liquid egg. Those are the standard figures, but if his equipment runs a
different schedule, correct them. Same for the shelf-life bars — they say "weeks,
see the pack" rather than a number, on purpose. Put a real number in once you know it.

## Brand colours

Sampled from the logo, set as CSS variables at the top of `style.css`.

| | |
|---|---|
| Sky | `#84C8EE` |
| Deep teal | `#105E82` |
| Ink | `#0B4560` — small text on the blue background; the deep teal fails contrast there |
| Yolk | `#FFD447` |
| Pale sky | `#E9F5FC` |

## The converter

Per large egg: 50 ml whole, 33 ml white, 17 ml yolk; protein and calories scale from
the same table. It lives in the `data` object in index.html's script — one place to
change if his cartons are sized to a different egg.
