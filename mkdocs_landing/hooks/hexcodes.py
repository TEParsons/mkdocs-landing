"""
Add previews in front of all hex codes
"""

import re


def on_page_markdown(markdown, **kwargs):
    markdown = re.sub(
        pattern=r"#([\dabcdefABCDEF]{6}|[\dabcdefABCDEF]{8})",
        string=markdown,
        repl=r"<i style='color: #\g<1>' class='fa-solid fa-circle color-preview'></i>#\g<1>",
    )

    return markdown