import tkinter as tk
from timer import TimerApp

class GUI:
    def __init__(self, setupWindow, callback):
        self.callback = callback
        self.setupWindow = setupWindow
        self.setupWindow.title("Minidoro")
        # self.setupWindow.geometry("200x200")
        self.setupWindow.config(bg="#e83a3a")

        tk.Label(self.setupWindow, text="Study sessions duration (min): ", bg="#e83a3a", fg = "white", font=("JetBrainsMono NFM Regular", 10)).grid(row=0, column=0)
        self.setStudyTime = tk.Entry(self.setupWindow)
        self.setStudyTime.grid(row=0, column=1)
        tk.Label(self.setupWindow, text="Break sessions duration (min): ", bg="#e83a3a", fg = "white", font=("JetBrainsMono NFM Regular", 10)).grid(row=1, column=0)
        self.setBreakTime = tk.Entry(self.setupWindow)
        self.setBreakTime.grid(row=1, column=1)
        self.submitButton = tk.Button(self.setupWindow, text="Enter", command=self.submit, font=("JetBrainsMono NFM Regular", 10))
        self.submitButton.grid(row=2, column=0, columnspan=2)
        self.setupWindow.bind("<Return>", self.submit)

    def submit(self, event=None):
        try:
            studyTime = int(self.setStudyTime.get())  # Convert to int
            breakTime = int(self.setBreakTime.get())  # Convert to int

            self.callback(studyTime, breakTime)
            self.setupWindow.destroy()  # Close setup window
        except ValueError:
            print("Please enter valid numbers!")  # Handle invalid inputs