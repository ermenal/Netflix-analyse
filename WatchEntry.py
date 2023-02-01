class WatchEntry:
    def __init__(self, title, watcher, duration):
        self.title = title
        self.watcher = watcher
        self.duration = duration

    def duration_to_int(self):
        uren_min_sec = self.duration.split(":")
        seconden = int(uren_min_sec[2])
        seconden += int(uren_min_sec[1]) * 60
        seconden += int(uren_min_sec[0]) * 60 * 60
        return seconden
