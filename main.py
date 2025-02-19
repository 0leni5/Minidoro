from methods import GUI
import tkinter as tk
from timer import TimerApp as TA

def processValues(studyTime, breakTime):
    timer = TA(studyTime, breakTime)

def main():
    setupWindow = tk.Tk()
    pomo = GUI(setupWindow, processValues)
    setupWindow.mainloop()

if __name__ == "__main__":
    main()
