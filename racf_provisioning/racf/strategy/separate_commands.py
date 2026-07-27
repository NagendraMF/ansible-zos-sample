class SeparateCommandsStrategy:

    def __init__(self):
        self._commands = []

    def adduser(self, userid, body=None):
        command = f"ADDUSER {userid}"

        if body:
            command += " " + " ".join(body)

        self._commands.append(command)

    def addgroup(self, group, body=None):
        command = f"ADDGROUP {group}"

        if body:
            command += " " + " ".join(body)

        self._commands.append(command)

    def segment(self, userid, segment, body):
        command = (
            f"ALTUSER {userid} "
            f"{segment}("
            f"{' '.join(body)}"
            f")"
        )

        self._commands.append(command)

    def group_segment(self, group, segment, body):
        command = (
            f"ALTGROUP {group} "
            f"{segment}("
            f"{' '.join(body)}"
            f")"
        )

        self._commands.append(command)

    def commands(self):
        return self._commands
