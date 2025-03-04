import tkinter as tk
from tkinter import colorchooser
from playsound import playsound as ps
import threading

class Settings:
    def __init__(self, settingsWindow, callback):
        self.default_settings = ["AE86 Chime", False, "#e83a3a", "white", "Off"]
        self.current_sound = self.default_settings[0]
        self.show_clock = self.default_settings[1]
        self.bgcolor = self.default_settings[2]
        self.textcolor = self.default_settings[3]
        self.manual_toggle = self.default_settings[4]
        self.callback = callback
        self.sounddic = {
            "Beep": "beepshort.wav",
            "Chime 1":"chime_1.wav",
            "AE86 Chime":"chime_2.wav",
            "Chime 3":"chime_3.wav"
        }
        self.settingsWindow = settingsWindow
        self.settingsWindow.title("Minidoro")
        self.settingsWindow.config(bg=self.bgcolor)

        self.selected_sound = tk.Button(self.settingsWindow, text=self.current_sound, command=self.chooseSound, font=("JetBrainsMono NFM Regular", 10))
        self.selected_sound.grid(row=0, column=0, sticky="ew", padx=5, pady=(5,0))

        self.select_sound = None
        self.list = None
        self.select_color = None

        self.show_clock = False
        self.clockM_button = tk.Button(self.settingsWindow, text=f"Show clock in minimalistic mode: {self.show_clock}", font=("JetBrainsMono NFM Regular", 10), command=self.toggleClockM, width=30)
        self.clockM_button.grid(row=1, column=0, sticky="ew", padx=5)

        self.manual_start_stop = tk.Button(self.settingsWindow, text=f"Manual START/STOP: {self.manual_toggle}", font=("JetBrainsMono NFM Regular", 10), command=self.manualSSToggle)
        self.manual_start_stop.grid(row=2, column=0, padx=5, sticky='ew')

        self.color_button = tk.Button(self.settingsWindow, text=f"Timer background color: {self.bgcolor}", font=("JetBrainsMono NFM Regular", 10), command=lambda: self.colorPicker("background"))
        self.color_button.grid(row=3, column=0, sticky="ew", padx=5)

        self.textcolor_button = tk.Button(self.settingsWindow, text=f"Timer text color: {self.textcolor}",
                                      font=("JetBrainsMono NFM Regular", 10),
                                      command=lambda: self.colorPicker("text"))
        self.textcolor_button.grid(row=4, column=0, sticky="ew", padx=5)

        self.example_text = tk.Label(self.settingsWindow, text="The timer will look like this.", font=("JetBrainsMono NFM Regular", 10), bg=self.bgcolor, fg=self.textcolor, borderwidth=2, relief="solid")
        self.example_text.grid(row=5, column=0, padx = 5, pady=10)

        self.reset_settings = tk.Button(self.settingsWindow, text="Reset", font=("JetBrainsMono NFM Regular", 10),
                                       command=self.resetSettings, width=15)
        self.reset_settings.grid(row=6, column=0, padx=5, pady=(5, 5))

        self.save_settings = tk.Button(self.settingsWindow, text="Save", font=("JetBrainsMono NFM Regular", 10), command=self.saveSettings, width=15)
        self.save_settings.grid(row=7, column=0, padx=5, pady=(20, 5))

    def chooseSound(self):
        if self.select_sound and self.select_sound.winfo_exists():
            self.select_sound.lift()  # Bring window to front
            self.select_sound.focus_force()  # Give it focus
            return

        self.select_sound = tk.Toplevel(self.settingsWindow)
        self.select_sound.title("Minidoro")
        self.select_sound.config(bg=self.bgcolor)
        self.list = tk.Listbox(self.select_sound, font=("JetBrainsMono NFM Regular", 10))
        self.list.pack(padx=5, pady=5)
        self.list.insert(1, "Beep")
        self.list.insert(2, "Chime 1")
        self.list.insert(3, "AE86 Chime")
        self.list.insert(4, "Chime 3")
        self.list.select_set(2)

        play_sound = tk.Button(self.select_sound, font=("JetBrainsMono NFM Regular", 10), command=self.playSound, text="Play")
        play_sound.pack(padx=5, pady=(5,0), fill="x")

        select = tk.Button(self.select_sound, font=("JetBrainsMono NFM Regular", 10), command=self.selectSound, text="Select")
        select.pack(padx=5, pady=(0,5), fill="x")

    def selectSound(self):
        self.current_sound = self.sounddic[self.list.get(self.list.curselection())]
        self.selected_sound.config(text=self.list.get(self.list.curselection()))
        self.select_sound.destroy()

    def playSound(self):
        sound = self.sounddic[self.list.get(self.list.curselection())]
        threading.Thread(target=lambda: ps(sound), daemon=True).start()

    def toggleClockM(self):
        self.show_clock = not self.show_clock
        self.clockM_button.config(text=f"Show clock in minimalistic mode: {self.show_clock}")

    def colorPicker(self, target):
        _, color = colorchooser.askcolor(title="Choose background color")
        if color is None:
            return

        if target == "background":
            self.bgcolor = color
            self.color_button.config(text=f"Timer background color: {color}")
            self.example_text.config(bg=self.bgcolor)
            self.settingsWindow.lift()  # Bring window to front
            self.settingsWindow.focus_force()  # Give it focus
        elif target == "text":
            self.textcolor = color
            self.textcolor_button.config(text=f"Timer text color: {color}")
            self.example_text.config(fg=self.textcolor)
            self.settingsWindow.lift()  # Bring window to front
            self.settingsWindow.focus_force()  # Give it focus

    def resetSettings(self):
        self.show_clock = self.default_settings[1]
        self.bgcolor = self.default_settings[2]
        self.textcolor = self.default_settings[3]

        self.example_text.config(bg=self.bgcolor, fg=self.textcolor)

    def manualSSToggle(self):
        if self.manual_toggle == "On":
            self.manual_toggle = "Off"
            self.manual_start_stop.config(text=f"Manual START/STOP: {self.manual_toggle}")
        else:
            self.manual_toggle = "On"
            self.manual_start_stop.config(text=f"Manual START/STOP: {self.manual_toggle}")

    def saveSettings(self):
        settings = [self.current_sound, self.show_clock, self.bgcolor, self.textcolor, self.manual_toggle]
        self.callback(settings)
        self.settingsWindow.destroy()