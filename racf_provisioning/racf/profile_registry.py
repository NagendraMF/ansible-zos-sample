from .schema import USER_SCHEMA, GROUP_SCHEMA

PROFILE_REGISTRY = {
    "racf_user": (
        USER_SCHEMA,
        "user",
    ),
    "racf_group": (
        GROUP_SCHEMA,
        "group",
    ),
}
