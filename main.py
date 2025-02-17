import tkinter as tk
from timer import TimerApp

def main():
    root = tk.Tk()
    root.title("Pomodoro Timer")
    root.geometry("300x200")
    root.config(bg = '#1c3d25')
    child = tk.Toplevel(root)
    child.title('Pomodoro Timer')
    child.geometry('300x200')
    child.config(bg = '#1c3d25')

    #make the entry for study time and break time
    entry = tk.Entry(child)
    entry.pack()

    study_minutes = int(input("Enter the length of one study session (min): "))
    break_minutes = int(input("Enter the length of the break (min): "))

    app = TimerApp(root, study_minutes, break_minutes)
    root.mainloop()

if __name__ == "__main__":
    main()
