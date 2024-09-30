import markdown
from jinja2.filters import FILTERS


def jinja_filter(tag):
    def register_filter(fcn):
        FILTERS[tag] = fcn
    
    return register_filter


# if config event not run, use parser with default config
md = markdown.Markdown()


def on_config(config, **kwargs):
    """
    Still figuring out how to connect to this event, but if I manage to, I can replace the markdown 
    parser with one which respects the user's config.
    """
    global md
    # create markdown interpreter
    md = markdown.Markdown(extensions=config.markdown_extensions)


# define conversion function
@jinja_filter("markdown")
def parse_markdown(text, id=""):
    """
    Parse markdown in injected jinja content (and give its block an ID)
    """
    # parse markdown
    html = md.convert(text)
    # assign id to first paragraph (if there is one)
    if id:
        html = html.replace("<p>", f"<p id=\"{id}\">", 1)
    
    return html
