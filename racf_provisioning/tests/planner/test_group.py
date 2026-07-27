from racf.planner.group import plan

from racf.operations.group import (
    EnsureGroup,
    EnsureGroupOMVS,
)


def test_plan_group():
    model = {
        "state": "present",
        "content": {
            "base": {
                "group": "DEV",
                "owner": "SYS1",
                "superior_group": "IBMUSER",
                "universal_access": "READ",
            }
        },
    }

    operations = plan(model)

    assert operations == [
        EnsureGroup(
            group="DEV",
            owner="SYS1",
            superior_group="IBMUSER",
            universal_access="READ",
        )
    ]


def test_plan_group_with_omvs():
    model = {
        "state": "present",
        "content": {
            "base": {
                "group": "DEV",
            },
            "omvs": {
                "gid": 100,
            },
        },
    }

    operations = plan(model)

    assert operations == [
        EnsureGroup(
            group="DEV",
        ),
        EnsureGroupOMVS(
            group="DEV",
            gid=100,
        ),
    ]
