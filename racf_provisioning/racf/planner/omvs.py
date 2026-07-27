from ..operations import EnsureOMVS

def plan(model):

    if "omvs" not in model["content"]:
        return []

    userid = model["content"]["base"]["userid"]
    omvs = model["content"]["omvs"]

    return [
        EnsureOMVS(
            userid=userid,
            uid=omvs["uid"],
            home=omvs["home"],
            program=omvs["program"],
        )
    ]
