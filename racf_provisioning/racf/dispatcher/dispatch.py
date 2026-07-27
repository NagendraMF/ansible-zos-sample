from racf.operations.user import EnsureUser
from racf.operations.omvs import EnsureOMVS
from racf.operations.tso import EnsureTSO
from racf.operations.group import (
    EnsureGroup,
    EnsureGroupOMVS,
)

from .user import (
    dispatch_user,
    dispatch_omvs,
    dispatch_tso,
)

from .group import (
    dispatch_group,
    dispatch_group_omvs,
    )    


def dispatch(operations, strategy):

    for op in operations:

        if isinstance(op, EnsureGroup):
            dispatch_group(op, strategy)

        elif isinstance(op, EnsureGroupOMVS):
            dispatch_group_omvs(op, strategy)

        elif isinstance(op, EnsureUser):
            dispatch_user(op, strategy)

        elif isinstance(op, EnsureOMVS):
            dispatch_omvs(op, strategy)

        elif isinstance(op, EnsureTSO):
            dispatch_tso(op, strategy)    

    return strategy.commands()
