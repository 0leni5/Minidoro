import time as t
import datetime as dt
from playsound import playsound as ps

class Timer():
    def __init__(self, m, b):
        self.studyTime = m*60 - 1
        self.breakTime = b*60 - 1
        self.round = 0

    def studytimer(self):
        totalSeconds = self.studyTime
        self.round += 1
        print("\rTime to focus!", end="")
        t.sleep(1)
        print(f"\rRound {self.round}")
        while totalSeconds >= 0:
            timeleft = dt.timedelta(seconds = totalSeconds)
            display = f"\r{timeleft}"
            print(display, end="")
            t.sleep(1)
            totalSeconds -= 1
        ps('beepshort.wav')
        self.breaktimer()

    def breaktimer(self):
        totalSeconds = self.breakTime
        print("\rBreak!", end="")
        t.sleep(1)
        while totalSeconds >= 0:
            timeleft = dt.timedelta(seconds=totalSeconds)
            display = f"\r{timeleft}"
            print(display, end="")
            t.sleep(1)
            totalSeconds -= 1
        ps('beepshort.wav')
        self.studytimer()

