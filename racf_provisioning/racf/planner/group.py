from ..operations import (
    EnsureGroup,
    EnsureGroupOMVS,
)


def plan(model):

    content = model.get("content", {})

    if "base" not in content:
        return []

    if model.get("state", "present") != "present":
        return []

    group = content["base"]

    operations = [
        EnsureGroup(
            group=group["group"],
            owner=group.get("owner"),
            superior_group=group.get("superior_group"),
            universal_access=group.get("universal_access"),
        )
    ]

    omvs = content.get("omvs")

    if omvs:
        operations.append(
            EnsureGroupOMVS(
                group=group["group"],
                gid=omvs["gid"],
            )
        )

    return operations
