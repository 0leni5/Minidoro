import time as t
import datetime as dt

class Timer():
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def studytimer(self):
        totalSeconds = self.m * 60 - 1
        print("\rTime to focus!", end="")
        t.sleep(1)
        while totalSeconds >= 0:
            timeleft = dt.timedelta(seconds = totalSeconds)
            display = f"\r{timeleft}"
            print(display, end="")
            t.sleep(1)
            totalSeconds -= 1
        self.breaktimer()

    def breaktimer(self):
        totalSeconds = self.b*60 - 1
        print("\rBreak!", end="")
        t.sleep(1)
        while totalSeconds >= 0:
            timeleft = dt.timedelta(seconds=totalSeconds)
            display = f"\r{timeleft}"
            print(display, end="")
            t.sleep(1)
            totalSeconds -= 1
        self.studytimer()

