import datetime as dt
import threading
import tkinter as tk
from playsound import playsound as ps
from time import *
from pynput import keyboard
import pyxhook

class TimerApp:
    def __init__(self, study_time, break_time, settings):
        self.toggle_minimalistic = False
        # listener = keyboard.Listener(on_press=self.on_hotkey)
        # listener.start()
        self.sound = settings[0]
        self.show_clock = settings[1]
        self.bgcolor = settings[2]
        self.textcolor = settings[3]
        self.manual_toggle = settings[4]
        self.waiting_for_manual_toggle = None

        self.root = tk.Tk()
        self.root.title("Minidoro")
        self.root.config(bg=self.bgcolor)
        # self.root.geometry("200x300")
        self.study_time = study_time * 60
        self.break_time = break_time * 60
        self.time_left = self.study_time
        self.on_break = False
        self.running = False
        self.round = 1

        # UI Elements
        self.mainLabel = tk.Label(self.root, text="Minidoro!", font=("JetBrainsMono NFM Regular", 15), bg=self.bgcolor, fg=self.textcolor)
        self.mainLabel.pack(pady=10)

        self.timer_display = tk.Label(self.root, text="0:00:00", font=("digital-7 Mono", 30), fg = self.textcolor, bg = self.bgcolor)
        self.timer_display.pack(padx=10, pady=10)

        self.roundLabel = tk.Label(self.root, text=f"Round {self.round}", font=("JetBrainsMono NFM Regular", 15), bg=self.bgcolor, fg=self.textcolor)
        self.roundLabel.pack(pady=10)

        self.clock_display = tk.Label(self.root, font=("digital-7 Mono", 17), fg=self.textcolor,
                                      bg=self.bgcolor)
        self.clock_display.pack()

        self.button_width = 10
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer, font=("JetBrainsMono NFM Regular", 10), width=self.button_width)
        self.start_button.pack(pady=(10,0), padx=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer, font=("JetBrainsMono NFM Regular", 10), width=self.button_width)
        self.stop_button.pack(pady=(0,10), padx=5)

        self.minimalistic_button = tk.Button(self.root, text="Minimalistic", command=self.switch_minimalistic, font=("JetBrainsMono NFM Regular", 10))
        # self.minimalistic_button.pack(pady=10)

        self.root.bind("<space>", self.start_stop_keyboard_timer)

        self.update_display()

        self.root.lift()  # Bring window to front
        self.root.focus_force()  # Give it focus

        # x = self.root.winfo_width()
        # y = self.root.winfo_height()
        # geometry = f"{x}x{y}"
        # self.root.geometry(geometry)
        

    def start_stop_keyboard_timer(self, event=None):
        if self.waiting_for_manual_toggle:  
            # Resume the timer in the next mode when manually confirmed
            self.waiting_for_manual_toggle = False
            self.switch_mode()
            self.start_timer()
        elif self.running:
            self.stop_timer()
        else:
            self.start_timer()

    def start_timer(self):
        if not self.running:
            if self.waiting_for_manual_toggle:
                self.waiting_for_manual_toggle = False
                self.switch_mode()
                if self.on_break:
                    self.mainLabel.config(text=f"Break time!")
                else:
                    self.mainLabel.config(text=f"Focus time!")
                self.running = True
                self.update_timer()
            else:
                if self.on_break:
                    self.mainLabel.config(text=f"Break time!")
                else:
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
                # time_str = strftime("%H:%M")
                # self.clock_display.config(text=time_str)
                self.root.after(1000, self.update_timer)
            else:
                self.play_sound()
                if self.manual_toggle == "Off":
                    self.switch_mode()
                else:
                    self.waiting_for_manual_toggle = True  # Enable manual start/stop mode
                    self.running = False  # Stop the automatic countdown
                    self.mainLabel.config(text="Break time!")

    def clock(self):
            time_str = strftime("%H:%M")
            self.clock_display.config(text=time_str)
            self.root.after(1000, self.clock)

    def update_display(self):
        time_display = str(dt.timedelta(seconds=self.time_left))
        self.timer_display.config(text=time_display)
        self.clock()

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
        threading.Thread(target=lambda: ps(self.sound), daemon=True).start()

    def on_hotkey(key):
        if key == keyboard.Key.M:  # F1 key detected
            # self.toggle_minimalistic()
            pass

    def switch_minimalistic(self):
        self.toggle_minimalistic = not self.toggle_minimalistic
        x = self.root.winfo_width()
        y = self.root.winfo_height()
        if self.toggle_minimalistic:
            # Make the window always on top and semi-transparent
            self.root.attributes("-topmost", True)  # Always on top
            self.root.attributes("-alpha", 0.5)  # 50% transparency
            
            # Hide window decorations
            self.root.overrideredirect(True)
            # self.root.resizable(False, False)

            self.mainLabel.pack_forget()
            self.timer_display.pack_forget()
            self.roundLabel.pack_forget()
            self.clock_display.pack_forget()
            self.start_button.pack_forget()
            self.stop_button.pack_forget()
            self.minimalistic_button.pack_forget()
            
            self.timer_display.pack()
            if self.show_clock:
                self.clock_display.pack()
            self.start_button.pack(side=tk.LEFT)
            self.stop_button.pack(side=tk.LEFT)
            self.minimalistic_button.pack(side=tk.LEFT)

            self.start_button.config(bg=self.bgcolor, fg=self.textcolor, text=">", width=1)
            self.stop_button.config(bg=self.bgcolor, fg=self.textcolor, text="||", width=1)
            self.minimalistic_button.config(bg=self.bgcolor, fg=self.textcolor, text="M", width=1)

            # Update window size
            # self.root.update_idletasks()
            self.root.geometry(f"{x}x100")
            self.root.geometry(f"{self.root.winfo_width()}x{self.root.winfo_height()}")  # Resize window if needed

        else:
            # Restore the window back to normal
            self.root.attributes("-topmost", False)  # Remove "always on top"
            self.root.attributes("-alpha", 1)  # Full opacity
            
            # Show window decorations
            self.root.overrideredirect(False)  # Restore borders and buttons
            self.root.resizable(True, True)

            self.timer_display.pack_forget()
            if self.show_clock:
                self.clock_display.pack_forget()
            self.start_button.pack_forget()
            self.stop_button.pack_forget()
            self.minimalistic_button.pack_forget()

            self.mainLabel.pack(pady=10)
            self.timer_display.pack(padx=10, pady=10)
            self.roundLabel.pack(pady=10)
            self.clock_display.pack()
            self.start_button.pack(pady=(10,0), padx=5)
            self.stop_button.pack(pady=(0,10), padx=5)
            self.minimalistic_button.pack(pady=10)

            self.start_button.config(bg="white", fg="black", text="Start", width=self.button_width)
            self.stop_button.config(bg="white", fg="black", text="Stop", width=self.button_width)
            self.minimalistic_button.config(bg="white", fg="black", text="Minimalistic", width=self.button_width)

            self.root.update_idletasks()
            self.root.geometry(f"{x}x{y}")
            self.root.geometry(f"{self.root.winfo_width()}x{self.root.winfo_height()}")  # Resize window if needed