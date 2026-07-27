from .common import Plan
from .registry import PLANNERS

def plan(model):

    if "base" in model.get("content", {}):
        if "userid" in model["content"]["base"]:
            object_type = "user"

        elif "group" in model["content"]["base"]:
            object_type = "group"

        else:
            raise ValueError(
                "Unable to determine RACF object type"
            )

    else:
        raise ValueError(
            "Missing content.base"
        )

    planner = PLANNERS[object_type]

    return Plan(
        operations=planner(model)
    )
