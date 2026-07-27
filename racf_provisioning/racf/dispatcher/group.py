# dispatcher/group.py

from racf.operations.group import (
    EnsureGroup,
    EnsureGroupOMVS,
)


def dispatch_group(op: EnsureGroup, strategy):

    body = []

    if op.owner:
        body.append(f"OWNER({op.owner})")

    if op.superior_group:
        body.append(f"SUPGROUP({op.superior_group})")

    if op.universal_access:
        body.append(f"UACC({op.universal_access.upper()})")

    strategy.addgroup(
        op.group,
        body,
    )


def dispatch_group_omvs(op: EnsureGroupOMVS, strategy):

    body = []

    body.append(f"GID({op.gid})")

    strategy.group_segment(
        op.group,
        "OMVS",
        body,
    )
