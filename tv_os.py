class TVOS:
    def __init__(self, apps=None):
        self.powered_on = False
        self.current_channel = 1
        self.current_app = None
        self.apps = apps or ["Live TV", "YouTube", "Netflix", "Settings"]

    def boot(self):
        self.powered_on = True
        return "TV OS booted"

    def open_app(self, app_name):
        if app_name not in self.apps:
            raise ValueError(f"App not installed: {app_name}")
        self.current_app = app_name
        return f"Opened {app_name}"

    def close_app(self):
        if not self.current_app:
            return "No app is currently open"
        app_name = self.current_app
        self.current_app = None
        return f"Closed {app_name}"

    def change_channel(self, channel):
        if not isinstance(channel, int) or not 1 <= channel <= 999:
            raise ValueError("Channel must be an integer between 1 and 999")
        self.current_channel = channel
        return f"Changed to channel {channel}"

    def status(self):
        return {
            "powered_on": self.powered_on,
            "current_channel": self.current_channel,
            "current_app": self.current_app,
            "apps": list(self.apps),
        }


def main():
    tv = TVOS()
    print(tv.boot())
    print(tv.open_app("Live TV"))
    print(tv.change_channel(7))
    print(tv.status())


if __name__ == "__main__":
    main()
