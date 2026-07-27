from .helpers import (
    option, 
    options,
    segment
)    

def render_tso(operation, strategy):

    return [
        " ".join(filter(None, [
            f"ALTUSER {operation.userid}",
            segment(
                "TSO",
                option("ACCTNUM", operation.account_number),
                option("PROC", operation.procedure),
                option("COMMAND", operation.command),
                option("DEST", operation.destination),
                option("HOLDCLASS", operation.hold_class),
                option("JOBCLASS", operation.job_class),
                option("MSGCLASS", operation.message_class),
            ),
        ]))
    ]    
