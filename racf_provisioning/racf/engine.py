from .validator import validate
from .planner import plan
from .dispatcher import dispatch
from .loader import load_yaml, extract_profile
from .strategy import SeparateCommandsStrategy
from pathlib import Path

def generate_commands(model, schema=None, strategy=None):

    if schema is None:
        from .profile_registry import PROFILE_REGISTRY

        object_type = model["meta"]["object_type"]

        schema, _ = PROFILE_REGISTRY[
            f"racf_{object_type}"
        ]

    if strategy is None:
        strategy = SeparateCommandsStrategy()

    result = validate(
        model,
        schema,
    )

    if not result.valid:
        raise ValueError(
            format_validation_errors(result)
        )

    plan_result = plan(model)

    return dispatch(
        plan_result.operations,
        strategy,
    )

def generate_commands_from_file(filename, strategy=None):

    document = load_yaml(filename)

    schema, model = extract_profile(document)

    return generate_commands(
        model,
        schema,
        strategy=strategy,
    )

def generate_commands_from_directory(directory, strategy=None):

    commands = []
    path = Path(directory)

    for filename in sorted(path.rglob("*.yml")):

        commands.extend(
            generate_commands_from_file(
                filename,
                strategy=strategy,
            )
        )

    return commands

def format_validation_errors(result):

    return "\n".join(
        f"{error.path}: {error.message}"
        for error in result.errors
    )
