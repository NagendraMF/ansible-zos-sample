from dataclasses import dataclass


@dataclass
class GroupModel:
    meta: dict
    state: str
    content: dict
