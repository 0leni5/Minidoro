import tkinter as tk
from tkinter import colorchooser
from playsound import playsound as ps
import threading

class Settings:
    def __init__(self, settingsWindow, callback):
        self.bgcolor = "#e83a3a"
        self.textcolor = "white"
        self.callback = callback
        self.settingsWindow = settingsWindow
        self.settingsWindow.title("Minidoro")
        self.settingsWindow.config(bg=self.bgcolor)

        self.current_sound = "beepshort.wav"
        self.selected_sound = tk.Button(self.settingsWindow, text=self.current_sound, command=self.chooseSound, font=("JetBrainsMono NFM Regular", 10))
        self.selected_sound.pack()

        self.select_sound = None
        self.list = None
        self.select_color = None

        self.color_button = tk.Button(self.settingsWindow, text="Timer background color", font=("JetBrainsMono NFM Regular", 10), command=lambda: self.colorPicker("background"))
        self.color_button.pack()

        self.textcolor_button = tk.Button(self.settingsWindow, text="Timer text color",
                                      font=("JetBrainsMono NFM Regular", 10),
                                      command=lambda: self.colorPicker("text"))
        self.textcolor_button.pack()

        self.save_settings = tk.Button(self.settingsWindow, text="Save", font=("JetBrainsMono NFM Regular", 10), command=self.saveSettings)
        self.save_settings.pack()

    def chooseSound(self):
        if self.select_sound and self.select_sound.winfo_exists():
            self.select_sound.lift()  # Bring window to front
            self.select_sound.focus_force()  # Give it focus
            return

        self.select_sound = tk.Toplevel(self.settingsWindow)
        self.select_sound.title("Minidoro")
        self.select_sound.config(bg=self.bgcolor)
        self.list = tk.Listbox(self.select_sound, font=("JetBrainsMono NFM Regular", 10))
        self.list.pack()
        self.list.insert(1, "beepshort.wav")
        self.list.insert(2, "chime_1.wav")
        self.list.insert(3, "chime_2.wav")
        self.list.insert(4, "chime_3.wav")

        play_sound = tk.Button(self.select_sound, font=("JetBrainsMono NFM Regular", 10), command=self.playSound, text="Play")
        play_sound.pack()

        select = tk.Button(self.select_sound, font=("JetBrainsMono NFM Regular", 10), command=self.selectSound, text="Select")
        select.pack()

    def selectSound(self):
        self.current_sound = self.list.get(self.list.curselection())
        self.selected_sound.config(text=self.current_sound)
        self.select_sound.destroy()

    def playSound(self):
        sound = self.list.get(self.list.curselection())
        threading.Thread(target=lambda: ps(sound), daemon=True).start()

    def colorPicker(self, target):
        _, color = colorchooser.askcolor(title="Choose background color")
        if target == "background":
            self.bgcolor = color
        elif target == "text":
            self.textcolor = color

    def saveSettings(self):
        settings = [self.current_sound, self.bgcolor, self.textcolor]
        self.callback(settings)
        self.settingsWindow.destroy()