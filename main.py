import numpy as np
import pandas as pd
from Watcher import *
from WatchEntry import *


def make_watcher_dict(df):
    watchers = set()
    ret = dict()

    for watcher in df["Profile Name"]:
        watchers.add(watcher)

    for watcher in watchers:
        ret[Watcher(watcher)] = dict()

    return ret


def add_durations(dur1, dur2):
    pass


def add_watch_entries(watchers, df):
    for idx, t in enumerate(df["Title"]):
        title = t.split(":")[0]
        watcher_name = df["Profile Name"][idx]
        watcher = ""
        for w in watchers:
            if w.naam == watcher_name:
                watcher = w
        duration = df["Duration"][idx]
        watch_entry = WatchEntry(title, watcher, duration)
        watcher.watchset.add(watch_entry)

        if title in watchers[watcher]:
            watchers[watcher][title].add(watch_entry)
            watcher.add_watchtime(watch_entry.duration_to_int())


        else:
            watchers[watcher][title] = set()
            watchers[watcher][title].add(watch_entry)
            watcher.add_watchtime(watch_entry.duration_to_int())


def main():
    df = pd.read_csv("ViewingActivity.csv")

    watchers = make_watcher_dict(df)
    add_watch_entries(watchers, df)

    for w in watchers:
        print(w.naam, w.total_watchtime())
        for t in watchers[w]:
            print("   " + t, w.get_watchtime_voor_titel(t))


if __name__ == "__main__":
    main()
