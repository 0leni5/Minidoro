import datetime as dt
import threading
import tkinter as tk
from playsound import playsound as ps

class TimerApp:
    def __init__(self, study_time, break_time):
        self.root = tk.Tk()
        self.root.title("Minidoro")
        self.root.config(bg='#e83a3a')
        # self.root.geometry("200x160")
        self.study_time = study_time * 60
        self.break_time = break_time * 60
        self.time_left = self.study_time
        self.on_break = False
        self.running = False
        self.round = 1

        # UI Elements
        self.mainLabel = tk.Label(self.root, text="Pomodoro Timer", font=("Arial", 10), bg='#e83a3a', fg="white")
        self.mainLabel.pack(pady=10)

        self.timer_display = tk.Label(self.root, text="00:00:00", font=("Arial", 30), fg = 'white', bg = '#e83a3a')
        self.timer_display.pack(pady=10)

        self.roundLabel = tk.Label(self.root, text=f"Round {self.round}", font=("Arial", 10), bg='#e83a3a', fg="white")
        self.roundLabel.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer, font=("Arial", 14))
        self.stop_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.update_display()

    def start_timer(self):
        if not self.running:
            self.mainLabel.config(text=f"Focus time!")
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.mainLabel.config(text=f"Timer stopped")
        self.running = False

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                time_display = str(dt.timedelta(seconds=self.time_left))
                self.timer_display.config(text=time_display)
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.play_sound()
                self.switch_mode()

    def update_display(self):
        time_display = str(dt.timedelta(seconds=self.time_left))
        self.timer_display.config(text=time_display)

    def switch_mode(self):
        if self.on_break:
            self.round += 1
            self.mainLabel.config(text=f"Focus time!")
            self.roundLabel.config(text=f"Round {self.round}")
            self.time_left = self.study_time
        else:
            self.mainLabel.config(text="Break Time!")
            self.time_left = self.break_time

        self.on_break = not self.on_break
        self.update_timer()

    def play_sound(self):
        threading.Thread(target=lambda: ps("beepshort.wav"), daemon=True).start()