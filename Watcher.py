class Watcher:
    def __init__(self, naam):
        self.naam = naam
        self.total_watchtime_seconden = 0
        self.watchset = set()

    def total_watchtime(self):
        sec = str(self.total_watchtime_seconden % 60)
        if len(sec) < 2:
            sec = "0" + sec
        minuten = self.total_watchtime_seconden // 60

        min = str(minuten % 60)
        if len(min) < 2:
            min = "0" + min

        uren = minuten // 60

        u = str(uren % 24)
        if len(u) < 2:
            u = "0" + u

        dagen = str(uren // 24)
        if len(dagen) < 2:
            dagen = "0" + dagen

        return dagen + " dagen, " + u + " uur, " + min + " minuten, " + sec + " seconden"

    def add_watchtime(self, watchtime_in_seconden):
        self.total_watchtime_seconden += watchtime_in_seconden

    def get_watchtime_voor_titel(self, titel):
        dummy_watcher = Watcher("dummy")
        for idx, e in enumerate(self.watchset):
            if e.title == titel:
                dummy_watcher.total_watchtime_seconden += e.duration_to_int()
        return dummy_watcher.total_watchtime()