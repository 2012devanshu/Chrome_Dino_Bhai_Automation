import pyautogui as pag
from PIL import Image,ImageGrab
import time

def hit(key):
    pag.keyDown(key)
    return True


def check(data):
    for i in range(130,330+75):
            for j in range(440,459):
                if data[i,j] < 100:
                    hit('up')
                    return True
    for i in range(245,400):
            for j in range(160,370):
                if data[i,j] < 100:
                    hit('down')
                    return True
    return Flase

if __name__ == "__main__":
    time.sleep(3)
    hit('up')
    
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        check(data)
    '''
        for i in range(130,330+75):
                for j in range(440,459):
                    data[i,j] = 0

        for i in range(245,400):
                for j in range(160,370):

                    data[i,j] = 171
        
        image.show()
        break'''

        

