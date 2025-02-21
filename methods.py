import tkinter as tk
from timer import TimerApp
from settings import Settings as st

class GUI:
    def __init__(self, setupWindow, callback):
        self.sound = "beepshort.wav"
        self.bgcolor = "#e83a3a"
        self.textcolor = "white"
        self.settings = [self.sound, self.bgcolor]

        self.callback = callback
        self.setupWindow = setupWindow
        self.setupWindow.title("Minidoro")
        # self.setupWindow.geometry("200x200")
        self.setupWindow.config(bg=self.bgcolor)

        self.settingsButton = tk.Button(self.setupWindow, text="Settings", command=self.open_settings, font=("JetBrainsMono NFM Regular", 10))
        self.settingsButton.grid(row=2, column=1)

        tk.Label(self.setupWindow, text="Study sessions duration (min): ", bg=self.bgcolor, fg = self.textcolor, font=("JetBrainsMono NFM Regular", 10)).grid(row=0, column=0)
        self.setStudyTime = tk.Entry(self.setupWindow)
        self.setStudyTime.grid(row=0, column=1)

        tk.Label(self.setupWindow, text="Break sessions duration (min): ", bg=self.bgcolor, fg = self.textcolor, font=("JetBrainsMono NFM Regular", 10)).grid(row=1, column=0)
        self.setBreakTime = tk.Entry(self.setupWindow)
        self.setBreakTime.grid(row=1, column=1)

        self.submitButton = tk.Button(self.setupWindow, text="Enter", command=self.submit, font=("JetBrainsMono NFM Regular", 10))
        self.submitButton.grid(row=2, column=0)

        self.settingsWindow = None

        self.setupWindow.bind("<Return>", self.submit)

    def submit(self, event=None):
        try:
            studyTime = int(self.setStudyTime.get())  # Convert to int
            breakTime = int(self.setBreakTime.get())  # Convert to int

            self.callback(studyTime, breakTime, self.settings)
            self.setupWindow.destroy()  # Close setup window
        except ValueError:
            print("Please enter valid numbers!")  # Handle invalid inputs

    def unpackSetting(self):
        self.sound = self.settings[0]
        self.bgcolor = self.settings[1]
        self.textcolor = self.settings[2]

    def updateSettings(self, settings):
        self.settings = settings
        self.unpackSetting()

    def open_settings(self):
        if self.settingsWindow and self.settingsWindow.winfo_exists():
            self.settingsWindow.lift()  # Bring window to front
            self.settingsWindow.focus_force()  # Give it focus
            return

        self.settingsWindow = tk.Toplevel(self.setupWindow)
        settings_window = st(self.settingsWindow, self.updateSettings)

