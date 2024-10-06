---
template: article.html
title: Configuration options
---

# Site information
### `favicon`
Image in the browser tab, should be a path to an image file, ideally a 16x16px .png file.

### `avatar`
Image of yourself, this will appear in the heading of the main page.

### `footer`
Markdown content to include in the page footer

### `socials`
List of social links to include, should be in the format:
```
- label: <text to display if the icon doesn't load>
  link: <url to link to when clicked>
  icon: <name of the icon to use, from fontawesome>
```
All of the free fontawesome icons are supported, you can also use `["brands", <icon name>]` to use a brand logo instead (such as GitHub, Facebook, BlueSky, etc.)

# Style configuration
### `header_layout`
This defines the order in which elements in the header are laid out. Elements available are:

- avatar
- tagline
- title
- socials

You can also include a blank element to put an empty div tag to fill a slot

### `background`
Background for the whole page, this will be behind the content box. Syntax is the same as the CSS `background` property.

### `background_color`
Color override for `background`. Whatever value is in here will be used for the CSS `background-color` property (which overrides any color set in `background`)

### `background_image`
Image override for `background`. Whatever value is in here will be used for the CSS `background-image` property (which overrides any color set in `background`). Unlike `background`, you do not need to include the `url(...)` wrapper - just a file path will suffice.

### `content_box_opacity`
The box containing your site content will be your base color, this parameter controls how opaque it is over the background.

### `content_box_padding`
The distance between the horizontal edges of your content and the edges of the content box.

### `avatar_size`
The width of the avatar, default is 8rem.

### `round_avatar`
If True, then the avatar will be cropped into a circle.

### `border_left` / `border_right`
The border on either side of the content box (defined using the same syntax as in `border-left`/`border-right` in CSS)

# Colors
The following attributes affect the colors used in your site.

## Scheme colors
These are the colors which define your theme, ordered by importance.

### `primary_color`
The first scheme color, this will be used for the footer and the tagline.

### `secondary_color`
The second scheme color, this will be used for links.

### `tertiary_color`
The third scheme color, this will be used for links when hovered.

## Shades
Various shades of white to use for backgrounds

### `base_color`
The base color, the background of the content box.

### `mantle_color`
Slightly darker than the base color, used for subtle highlights

### `crust_color`
Slighter darker than the mantle color, used for second-level highlights

### `overlay_color`
Significantly darker than the crust color, used for subtle outlines which need to stand out

### `footer_color`
Specific shade to use for the footer

## Text colors
### `text_color`
Basic text color

### `hltext_color`
Basic text color for display against dark backgrounds

### `footer_text_color`
Specific text color used for the footer

## Background-specific text colors
Each of the colors above has a matching parameter which is its name with `_color` replaced by `_text_color` (e.g. `primary_text_color` rather than `primary_color`), which defines the color for text when against that background color. These default to being either `text_color` or `hltext_color`, with the following defaults:

- primary_text_color: hltext
- secondary_text_color: hltext
- tertiary_text_color: hltext
- base_text_color: text
- mantle_text_color: text
- crust_text_color: text
- overlay_text_color: hltext

## Darkmode colors
To define the colors which are used in darkmode, use the same parameter names but with `_dark` on the end (e.g. `primary_color_dark` rather than `primary_color`)

# Fonts
The following attributes define the font faces used in your site. Each of these can be the name of any font from [Google Fonts](https://fonts.google.com)

### `heading_font`
Font to use for headings, default is Poppins

### `body_font`
Font to use for most text, default is Hind

### `mono_font`
Monospace font to use for code, default is JetBrains Mono
