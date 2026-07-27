"""
Schema definition for RACF group profiles.
"""

from __future__ import annotations

from .common import Field, Section, ValueType


GROUP_SCHEMA = Section(

    fields={

        "state": Field(
            type=ValueType.ENUM,
            required=True,
            choices=(
                "present",
                "absent",
            ),
        ),

    },

    sections={

        "meta": Section(

            fields={

                "object_type": Field(
                    type=ValueType.STRING,
                    required=True,
                    default="group",
                ),

                "schema_version": Field(
                    type=ValueType.STRING,
                    required=True,
                ),

                "zos_version": Field(
                    type=ValueType.STRING,
                    required=True,
                ),

            }

        ),

        "content": Section(

            sections={

                "group": Section(

                    fields={

                        "group": Field(
                            type=ValueType.STRING,
                            required=True,
                        ),

                        "owner": Field(
                            type=ValueType.STRING,
                        ),

                        "superior_group": Field(
                            type=ValueType.STRING,
                        ),

                        "universal_access": Field(
                            type=ValueType.ENUM,
                            choices=(
                                "none",
                                "read",
                                "update",
                                "control",
                                "alter",
                            ),
                        ),

                    }

                ),

                "omvs": Section(

                    fields={

                        "gid": Field(
                            type=ValueType.INTEGER,
                            minimum=1,
                        ),

                    }

                ),

            }

        ),

    },

)
