from pathlib import Path

import yaml

from .profile_registry import PROFILE_REGISTRY


def load_yaml(filename):

    with Path(filename).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_profile(document):

    if len(document) != 1:
        raise ValueError(
            "Expected exactly one RACF profile wrapper."
        )

    wrapper = next(iter(document))

    try:
        schema, planner = PROFILE_REGISTRY[wrapper]
    except KeyError:
        raise ValueError(
            f"Unsupported profile type '{wrapper}'."
        )

    return (
        schema,
        document[wrapper],
    )
