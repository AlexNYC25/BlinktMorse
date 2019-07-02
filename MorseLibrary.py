import blinkt
import time

class MorseLibrary:

    def __init__(self):
        blinkt.set_clear_on_exit()

    def allPixels(self, onState):
        for i in range(blinkt.NUM_PIXELS):
            rgbValue = onState * 255
            blinkt.set_pixel(i, rgbValue, rgbValue, rgbValue)
        blinkt.show()


    def dot(self):
        allPixels(1)
        time.sleep(0.05)
        allPixels(0)
        time.sleep(0.2)

    def dash(self):
        allPixels(1)
        time.sleep(0.2)
        allPixels(0)
        time.sleep(0.2)

    def space(self):
        time.sleep(0.2)


