import markdown
from jinja2.filters import FILTERS

def on_config(config, **kwargs):
    # create markdown interpreter
    md = markdown.Markdown(extensions=config.markdown_extensions)
    # define conversion function
    def parse_markdown(text, id=""):
        # parse markdown
        html = md.convert(text)
        # assign id to first paragraph (if there is one)
        if id:
            html = html.replace("<p>", f"<p id=\"{id}\">")
        
        return html
    # assign conversion function
    FILTERS['markdown'] = parse_markdown
