---
title: Links
template: links.html
---

# Links pages

Landing includes a page template for an array of links, similar to [LinkTree](https://linktr.ee/) or [Campsite](https://campsite.bio/). 

## Specify page as a links page
To specify any page on your site (including the homepage!) as a links page, just add the following in the [frontmatter](https://dev.to/dailydevtips1/what-exactly-is-frontmatter-123g) of the page:

```
template: links.html
```

## Add links

In the links page, any links which are top level headings (`# [title](url)` in markdown) are styled like this:

# [Landing](https://TEParsons.github.io/mkdocs-landing)

You can also include an image within the link title (`# [![](image url) title](url)` in markdown) and it will be styled as a thumbnail:

# [![](https://teparsons.github.io/mkdocs-landing/assets/branding/logo.png) Landing](https://TEParsons.github.io/mkdocs-landing)