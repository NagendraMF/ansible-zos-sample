from .user import plan as plan_user
from .group import plan as plan_group

PLANNERS = {
    "user": plan_user,
    "group": plan_group,
}
