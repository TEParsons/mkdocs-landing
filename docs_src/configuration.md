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
The theme has an attribute `colors`, which has the following sub-attributes.

## Scheme colors
These are the colors which define your theme, ordered by importance.

### `primary`
The first scheme color, this will be used for the footer and the tagline.

### `secondary`
The second scheme color, this will be used for links.

### `tertiary`
The third scheme color, this will be used for links when hovered.

## Shades
Various shades of white to use for backgrounds

### `base`
The base color, the background of the content box.

### `mantle`
Slightly darker than the base color, used for subtle highlights

### `crust`
Slighter darker than the mantle color, used for second-level highlights

### `overlay`
Significantly darker than the crust color, used for subtle outlines which need to stand out

## Text colors
### `text`
Basic text color

### `hltext`
Basic text color for display against dark backgrounds

## Background-specific text colors
Each of the colors above has a matching parameter which is its name followed by `_text` (e.g. `primary_text` rather than `primary`), which defines the color for text when against that background color. These default to being either `text` or `hltext`, with the following defaults:

- primary_text: hltext
- secondary_text: hltext
- tertiary_text: hltext
- base_text: text
- mantle_text: text
- crust_text: text
- overlay_text: hltext

## Darkmode colors
To define the colors which are used in darkmode, use `colors_dark` in place of `colors`. Other names are all the same.

# Fonts
The theme has an attribtue `fonts`, which has the following sub-attributes. Each of these can be the name of any font from [Google Fonts](https://fonts.google.com)

### `heading`
Font to use for headings, default is Poppins

### `body`
Font to use for most text, default is Hind

### `mono`
Monospace font to use for code, default is JetBrains Mono