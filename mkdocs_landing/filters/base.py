from jinja2.filters import FILTERS

def jinja_filter(tag):
    def register_filter(fcn):
        FILTERS[tag] = fcn
    
    return register_filter