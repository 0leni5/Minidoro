import tkinter as tk
from timer import TimerApp

class GUI:
    def __init__(self, setupWindow, callback):
        self.callback = callback
        self.setupWindow = setupWindow
        # self.setupWindow.geometry("200x200")
        self.setupWindow.config(bg="#e83a3a")

        tk.Label(self.setupWindow, text="Study sessions duration (min): ", bg="#e83a3a", fg = "white").grid(row=0, column=0)
        self.setStudyTime = tk.Entry(self.setupWindow)
        self.setStudyTime.grid(row=0, column=1)
        tk.Label(self.setupWindow, text="Break sessions duration (min): ", bg="#e83a3a", fg = "white").grid(row=1, column=0)
        self.setBreakTime = tk.Entry(self.setupWindow)
        self.setBreakTime.grid(row=1, column=1)
        self.submitButton = tk.Button(self.setupWindow, text="Enter", command=self.submit)
        self.submitButton.grid(row=2, column=0, columnspan=2)

    def submit(self):
        try:
            studyTime = int(self.setStudyTime.get())  # Convert to int
            breakTime = int(self.setBreakTime.get())  # Convert to int

            self.callback(studyTime, breakTime)
            self.setupWindow.destroy()  # Close setup window
        except ValueError:
            print("Please enter valid numbers!")  # Handle invalid inputs