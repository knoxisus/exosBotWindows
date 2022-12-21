import os
import csv
import math
import cv2 as cv
import pyautogui as pt
import pyscreenshot as ImageGrab
from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"""C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"""

from time import sleep
from random import randint

from Runas import *
from Coordinates import *

def set_position(runas):
    positions = RUNA_POSITIONS
    i = 0
    while i < len(runas):
        runas[i].POSITION = positions[i]
        i = i + 1

def cleaner():
    os.remove("stat_windows_img.png")

def capture_screen(window_size=WINDOW_SIZE):
    img = ImageGrab.grab(bbox=window_size)
    img.save("stat_windows_img.png")
    return cv.imread("stat_windows_img.png", 0)

def nav_position(position):
    #pt.moveTo(position[0], position[1], duration = 0.1)
    sleep(0.3)

def single_click():
    #pt.click()
    sleep(0.3)

def double_click():
    #pt.doubleClick()
    sleep(0.3)

def nav_forge_button_position():
    position = (FORGE_BUTTON_POSITION[0] + randint(-9,9), FORGE_BUTTON_POSITION[1] + randint(-6,6))
    nav_position(position=position)

def forge_runa():
    print("         click")
    single_click()

def discard_runa():
    position = (DISCARD_RUNA_POSITION[0] + randint(-9,9), DISCARD_RUNA_POSITION[1] + randint(-9,9))
    nav_position(position=position)
    double_click()

def select_runa(runa_position):
    position = (runa_position[0] + randint(-3,3), runa_position[1] + randint(-3,3))
    nav_position(position=position)
    double_click()

def load_stats_from_csv(filename):
    file = open(filename)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows

def img_debug(img):
    winname = "Dofu Window"
    cv.namedWindow(winname)
    cv.imshow(winname, img)
    cv.waitKey()

def resize(cvImage, factor):
    new_size = tuple(map(lambda x: x * factor, cvImage.shape[::-1]))
    return cv.resize(cvImage, new_size)

def stat_from_csv(runas, runaName):
    for runa in runas:
        if runa[0] == runaName:
            return int(runa[1])

def stat_from_window(runa):
    if "ALA RESISTENCIA" in runa.NAME or "RESIS" in runa.NAME:
        probabilidad = 0.9
    else:
        probabilidad = 0.77
    
    window = capture_screen()
    needle = cv.imread(runa.STAT_IMG, 0)
    result = cv.matchTemplate(window, needle, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    #img_debug(window)
    #print(min_val, max_val, min_loc, max_loc)

    if max_val < probabilidad:
        return 0

    w = needle.shape[1]
    h = needle.shape[0]
    xloc, yloc = max_loc[0], max_loc[1]

    if runa.SIGNO:
        x_init = 17
    else:
        x_init = 0
    
    if "AUMENTO DANIO" in runa.NAME:
        x_init = w - 2
        xloc = x_init + 25
    
    minWindow = window[yloc:yloc + h, x_init:xloc]
    img = resize(minWindow, 6)
    number = pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 6')

    try:
        number = int(number)
    except:
        number = 0

    return number

def get_intentos(runas, runaTarget):
    statFromCsv = stat_from_csv(runas=runas, runaName=runaTarget.NAME)
    statFromWindow = stat_from_window(runa=runaTarget)
    intentos = int(math.ceil((statFromCsv-statFromWindow)/runaTarget.CANT))
    if intentos > 0:
        if intentos > 6:
            intentos = randint(3, 6)
    else:
        intentos = 0
    print(" ", runaTarget.NAME+":", statFromCsv, statFromWindow, " -->", intentos, "intentos")
    return intentos

def forge_runa_low(runas, runa):
    intentos = get_intentos(runas, runa)
    if intentos > 0:
        discard_runa()
        select_runa(runa_position=runa.POSITION)
        nav_forge_button_position()
        intento = 0
        while intento < intentos:
            forge_runa()
            intento = intento + 1
        return True
    else:
        return False

def forge_obj(stats, runas):
    runa = 0
    while runa < len(runas):
        if forge_runa_low(stats, runas[runa]):
            runa = 0
        else:
            runa = runa + 1

def maguear_blite():
    runas = [RUNA_DANIO(), RUNA_CRITICO(), RUNA_SABIDURIA(), RUNA_ALA_RESISTENCIA_TIERRA(),
             RUNA_RESIS_TIERRA(), RUNA_INICIATIVA(), RUNA_PP(), RUNA_VITALIDAD(),
             RUNA_INTELIGENCIA(), RUNA_SUERTE()]
    set_position(runas)
    statsTarget = load_stats_from_csv("stats/blite.csv")
    
    round = runas[:4]
    forge_obj(statsTarget, round)

    round = runas[:3] + runas[4:5]
    forge_obj(statsTarget, round)

    round = runas[:3] + runas[5:]
    forge_obj(statsTarget, round)

def main():
    #maguear_blite()
    cleaner()

if __name__ == "__main__":
    main()