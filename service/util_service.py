def to_bool(val):
    return val.lower in ("true", "1")

def get_props(object):
    props = {}
    for prop, value in vars(object).items():
        props[prop] = value
    return props






