from PIL import ImageGrab
import time

def screenshot():
    # time.sleep(5)
    name = str(int(time.time()))
    name = '/Users/m1/Developer/Projects/Screenshot-App/screen_files/{}.png'.format(name)
    img = ImageGrab.grab()
    img.save(name)
    img.show()

screenshot()
