def option(keyword, value):

    if value is None:
        return None

    return f"{keyword}({value})"


def options(*values):

    return " ".join(v for v in values if v)

def segment(name, *values):

    opts = options(*values)

    if not opts:
        return None

    return f"{name}({opts})"
