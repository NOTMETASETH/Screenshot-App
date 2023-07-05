from PIL import ImageGrab
import time
import tkinter as tk

class ScreenShotApp:
    def __init__(self, root):
        self.root = root
        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        button = tk.Button(frame, text="Take Screenshot", command=self.screenshot)
        button.pack(side=tk.LEFT)

        close = tk.Button(frame, text="Quit", command=self.quit_app)
        close.pack(side=tk.LEFT)

    def screenshot(self):
        name = f'/Users/m1/Developer/Projects/Screenshot-App/screen_files/{int(time.time())}.png'
        img = ImageGrab.grab()
        img.save(name)
        img.show()

    def quit_app(self):
        self.root.quit()

def main():
    root = tk.Tk()
    app = ScreenShotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
