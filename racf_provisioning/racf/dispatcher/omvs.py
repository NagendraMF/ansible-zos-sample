from .helpers import (
    option, 
    options,
    segment,
)

def render_omvs(operation, strategy):

    return [
        " ".join(filter(None, [
            f"ALTUSER {operation.userid}",
            segment(
                "OMVS",
                option("UID", operation.uid),
                option("HOME", operation.home),
                option("PROGRAM", operation.program),
            ),
        ]))
    ]    
