from PIL import ImageGrab
import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle
import time

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot App")

        style = ThemedStyle(self.root)
        style.set_theme("black")  # Hacker theme

        self.save_label = ttk.Label(self.root, text='Save location', foreground='white') # Text color
        self.save_label.pack()

        self.save_entry = ttk.Entry(self.root)
        self.save_entry.pack()

        self.save_button = ttk.Button(self.root, text='Browse', command=self.browse)
        self.save_button.pack()

        self.name_label = ttk.Label(self.root, text='File name', foreground='white') # Text color
        self.name_label.pack()

        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack()

        self.delay_label = ttk.Label(self.root, text='Delay (s)', foreground='white') # Text color
        self.delay_label.pack()

        self.delay_entry = ttk.Entry(self.root)
        self.delay_entry.pack()

        self.screenshot_button = ttk.Button(self.root, text='Take screenshot', command=self.screenshot)
        self.screenshot_button.pack()

    def browse(self):
        folder = filedialog.askdirectory()
        self.save_entry.delete(0, tk.END)
        self.save_entry.insert(tk.END, folder)

    def screenshot(self):
        delay = int(self.delay_entry.get())
        time.sleep(delay)
        name = self.name_entry.get()
        save_location = self.save_entry.get()
        path = '{}/{}.png'.format(save_location, name)
        img = ImageGrab.grab()
        img.save(path)
        img.show()

def main():
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
