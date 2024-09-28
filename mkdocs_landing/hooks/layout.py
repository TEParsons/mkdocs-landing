import re
from mkdocs.structure import pages, files
from mkdocs import config


def _do_sub(match: re.Match):
    """
    Function to substitute article / section pointers in markdown with article / section tags in HTML.

    Parameters
    ----------
    match : re.Match
        Match containing params and content
    
    Returns
    -------
    str
        Replacement text
    """
    # extract matches
    tag = match.group(1)
    params = match.group(2)
    content = match.group(3)

    # get tag
    tag = {
        '%': "section",
        '@': "article",
    }[tag]
    # handle no params
    if params is None:
        params = ""
    # add markdown block spec
    params += " markdown=block"
    # handle # syntax
    params = re.sub(
        pattern="(#)(\w*)",
        string=params,
        repl=_expand_attr,
        flags=re.DOTALL
    )
    # handle . syntax
    params = re.sub(
        pattern="(\.)(\w*)",
        string=params,
        repl=_expand_attr,
        flags=re.DOTALL
    )

    return (
        f"<{tag} {params}>\n"
        f"{content}\n"
        f"</{tag}>"
    )

def _expand_attr(match: re.Match):
    """
    Function to expand #id and .class syntax into full attr=val syntax.

    Parameters
    ----------
    match : re.Match
        Match for concise syntax

    Returns
    -------
    str
        Expanded syntax
    """
    # get value and type
    attr = match.group(1)
    val = match.group(2)
    # get attribute name
    attr = {
        '#': "id",
        '.': "class",
    }[attr]
    # expand it
    return f"{attr}={val}"


def on_page_markdown(markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
    """
    Parses expanded markdown syntax to add sections and articles.

    Add a section like so:
    ```
    $$${#id .class other_param=1}
    # Heading
    Content content content
    $$$
    ```

    Add an article like so:
    ```
    @@@{id .class other_param=1}
    # Heading
    Content content content
    @@@
    ```

    Parameters
    ----------
    markdown : str
        Markdown text
    page : pages.Page
        MkDocs page object
    config : config.Config
        MkDocs configutation object
    files : files.File
        MkDocs file object

    Returns
    -------
    str
        Parsed markdown text
    """
    # do sections
    markdown = re.sub(
        pattern="\%\%(\%)(?:\{(.*)\})?(.*?)\%\%\%",
        string=markdown, 
        repl=_do_sub,
        flags=re.DOTALL
    )
    # do articles
    markdown = re.sub(
        pattern="\@\@(\@)(?:\{(.*)\})?(.*?)\@\@\@",
        string=markdown, 
        repl=_do_sub,
        flags=re.DOTALL
    )

    return markdown
