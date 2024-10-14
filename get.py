'''
Date:   2024/10/14
Time:   20:34
Author: mzy
Usage:  not a nice thing to say
注意事项：
24，36，37三行（后续可能有变动，以行末是否有说明为准）需要根据自己电脑的情况进行修改
'''
from operator import ifloordiv
from time import sleep
import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
from drawa import draw

start_x, start_y = 275, 659
end_x, end_y = 275, 705
left_x, left_y = 258, 682
right_x, right_y = 291, 682

pytesseract.pytesseract.tesseract_cmd = r'G:\Program Files\Tesseract-OCR\tesseract.exe'#请修改为你电脑tesseract.exe的路径


def capture_and_recognize(x1, y1, x2, y2):
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
    _, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    digits = pytesseract.image_to_string(img, config=custom_config)
    return digits.strip()


def get():
        a = capture_and_recognize(794, 325, 866, 408)#需要根据实际情况修改
        b = capture_and_recognize(1011,346, 1090,404)#https://zh.pixspy.com/
        return a, b



