from dataclasses import dataclass


@dataclass(frozen=True)
class EnsureGroup:
    group: str
    owner: str | None = None
    superior_group: str | None = None
    universal_access: str | None = None


@dataclass(frozen=True)
class EnsureGroupOMVS:
    group: str
    gid: int
