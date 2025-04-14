import tkinter as tk
from tkinter import messagebox

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

# Het script doet niets als het zelfstandig wordt uitgevoerd
if __name__ == "__main__":
    print("Dit script kan niet direct worden uitgevoerd.")
