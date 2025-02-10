import time as t
import datetime as dt
import sys

class Timer():
    def __init__(self, m, b):
        self.studyTime = m*60 - 1
        self.breakTime = b*60 - 1

    def studytimer(self):
        totalSeconds = self.studyTime
        sys.stdout.write("\rTime to focus!", end="") #ta sama błędna komenda
        sys.stdout.flush()
        t.sleep(1)
        while totalSeconds >= 0:
            timeleft = dt.timedelta(seconds = totalSeconds)
            display = f"\r{timeleft}"
            sys.stdout.write(display, end="") #ta komenda chyba nie jest odpowiednia, wywala error
            sys.stdout.flush()
            t.sleep(1)
            totalSeconds -= 1
        self.breaktimer()

    def breaktimer(self):
        totalSeconds = self.breakTime
        sys.stdout.write("\rBreak!", end="")
        sys.stdout.flush()
        t.sleep(1)
        while totalSeconds >= 0:
            timeleft = dt.timedelta(seconds=totalSeconds)
            display = f"\r{timeleft}"
            sys.stdout.write(display, end="") #tak samo tutaj
            sys.stdout.flush()
            t.sleep(1)
            totalSeconds -= 1
        self.studytimer()

