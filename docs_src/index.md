Landing is an mkdocs theme geared towards making a personal landing page, with simpler navigation and heavily customisable style options.

# Configuration
With Landing I've tried to expose as much of the styling as possible to mkdocs, so that you can change up the theme to your own personal style as much as possible. Of course, there's nothing more flexible than writing your own css, so if you hit a wall with the config file I've also tried to make the html as simple as possible so you can easily add your own custom CSS.

Click [here](configuration.md) for a full list of configuration options available.

# History
Landing came out of me wanting to use mkdocs for [my own personal landing page](#todd-parsons) - I made a custom .css file to sit alongside a generic mkdocs file and style it the way I wanted it. When implementing a [similar page for a friend](#ben-ambrose) I realised that this basic structure could be fairly easily modified with a few key parameters to match a variety of different aesthetics.

# Gallery

Below are some implementations of Landing with various styles, as an example.

## Todd Parsons
The configuration I've got on my own personal site - not all that different than default Landing, but I've added a hook to turn content framed by `@@@` into articles, and a snazzy little line on the left.

<iframe src=https://toddparsons.co.uk class=zoomed-out></iframe>
[<i class="fa-regular fa-file-code"></i>   mkdocs.yaml file](https://github.com/TEParsons/toddparsons/blob/main/mkdocs.yaml)

## Ben Ambrose
A site I built for a friend - I added the same hook for articles as my personal site, and got a little funky with the gradients (overlaying them on top of a background image Ben made).

<iframe src=https://benjaminambrose.github.io/benambrose/ class=zoomed-out></iframe>
[<i class="fa-regular fa-file-code"></i>   mkdocs.yaml file](https://github.com/benjaminambrose/benambrose/blob/main/mkdocs.yaml)

## Catppuccin example
I'm a big fan of Catppuccin, so of course the first example I made was in latte/mocha!

<iframe src=https://teparsons.github.io/mkdocs-landing/gallery/catppuccin class=zoomed-out></iframe>
[<i class="fa-regular fa-file-code"></i>   mkdocs.yaml file](https://github.com/TEParsons/mkdocs-landing/blob/main/gallery/catppuccin/mkdocs.yaml)
