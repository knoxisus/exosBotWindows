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

SLEEP_TIME = 1.1

def set_position(runas):
    positions = RUNA_POSITIONS
    i = 0
    while i < len(runas):
        runas[i].POSITION = positions[i]
        i = i + 1
        
def set_stat_target(statsFileName, runas):
    file = open(statsFileName)
    csvreader = csv.reader(file)
    for row in csvreader:
        for runa in runas:
            if row[0] == runa.NAME:
                runa.STAT_TARGET = int(row[1])
    file.close()

def cleaner():
    os.remove("stat_windows_img.png")

def capture_screen(window_size=WINDOW_SIZE):
    img = ImageGrab.grab(bbox=window_size)
    img.save("stat_windows_img.png")
    return cv.imread("stat_windows_img.png", 0)

def nav_position(position):
    pt.moveTo(position[0], position[1], duration = 0.1)
    sleep(SLEEP_TIME)

def single_click():
    pt.click()
    sleep(SLEEP_TIME)

def double_click():
    pt.doubleClick()
    sleep(SLEEP_TIME)

def nav_forge_button_position():
    position = (FORGE_BUTTON_POSITION[0] + randint(-12,12), FORGE_BUTTON_POSITION[1] + randint(-6,6))
    nav_position(position=position)

def f_exit():
    nav_position(EXIT_POSITION)
    print("Quiere salir?")
    sleep(1)
    single_click()
    sleep(1)

def forge_runa():
    print("         click")
    single_click()

def discard_runa():
    position = (DISCARD_RUNA_POSITION[0] + randint(-9,9), DISCARD_RUNA_POSITION[1] + randint(-9,9))
    nav_position(position=position)
    double_click()

def select_runa(runa_position):
    position = (runa_position[0] + randint(-9,9), runa_position[1] + randint(-9,9))
    nav_position(position=position)
    double_click()

def img_debug(img):
    winname = "Dofu Window"
    cv.namedWindow(winname)
    cv.imshow(winname, img)
    cv.waitKey()

def resize(cvImage, factor):
    new_size = tuple(map(lambda x: x * factor, cvImage.shape[::-1]))
    return cv.resize(cvImage, new_size)

def stat_from_window(runa):
    if "ALA RESISTENCIA" in runa.NAME or "RESIS" in runa.NAME:
        probabilidad = 0.9
    else:
        probabilidad = 0.77
    
    window = capture_screen()
    needle = cv.imread(runa.STAT_IMG, 0)
    result = cv.matchTemplate(window, needle, cv.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv.minMaxLoc(result)
    max_val = round(max_val, 3)
    
    if max_val < probabilidad:
        return 0, max_val

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

    return number, max_val

def get_intentos(runa):
    statFromWindow, probabilidad = stat_from_window(runa)
    intentos = int(math.ceil((runa.STAT_TARGET-statFromWindow)/runa.CANT))
    if intentos < 0:
        intentos = 0
    elif intentos > 6:
        intentos = randint(3, 6)
    print(" ", runa.NAME+":", runa.STAT_TARGET, statFromWindow, probabilidad, " -->", intentos, "intentos")
    return intentos

def forge_runa_low(runa):
    intentos = get_intentos(runa)
    if intentos > 0:
        discard_runa()
        select_runa(runa.POSITION)
        nav_forge_button_position()
        intento = 0
        while intento < intentos:
            forge_runa()
            intento = intento + 1
        return True
    else:
        return False

def check_adjust(runas, maxLossStat):
    count = 0
    for runa in runas:
        stat, _ = stat_from_window(runa)
        if stat == 0:
            count = count + 1
    
    if count >= maxLossStat:
        return True
    else:
        return False

def forge_obj(inventory, runas, maxLossStat):
    runa = 0
    while runa < len(runas):
        if forge_runa_low(runas[runa]):
            f_exit()
            if check_adjust(inventory, maxLossStat):
                adjust_obj(inventory)
            runa = 0
        else:
            runa = runa + 1

def adjust_obj(runas):
    print("Adjusting....")
    for runa in runas:
        statFromWindow, probabilidad = stat_from_window(runa)
        intentos = int(math.ceil((runa.STAT_TARGET-statFromWindow)/runa.CANT))
        if statFromWindow > round(runa.STAT_TARGET*(2/3)):
            intentos = 0
        else:
            intentos = int(math.ceil((round(runa.STAT_TARGET*(2/3))-statFromWindow)/runa.CANT))
        print(" ", runa.NAME+":", runa.STAT_TARGET, statFromWindow, probabilidad, " -->", intentos, "intentos")
        if intentos > 0:
            discard_runa()
            select_runa(runa.POSITION)
            nav_forge_button_position()
            intento = 0
            while intento < intentos:
                forge_runa()
                intento = intento + 1

def maguear_blite():
    maxLossStat = 2
    runas = [RUNA_DANIO(), RUNA_CRITICO(), RUNA_SABIDURIA(), RUNA_ALA_RESISTENCIA_TIERRA(),
             RUNA_RESIS_TIERRA(), RUNA_INICIATIVA(), RUNA_PP(), RUNA_VITALIDAD(),
             RUNA_INTELIGENCIA(), RUNA_SUERTE()]
    check_adjust(runas, maxLossStat)
    set_position(runas)
    set_stat_target("stats/blite.csv", runas)
    adjust_obj(runas)
    os.system('cls')
    
    round = runas[:4]
    forge_obj(runas, round, maxLossStat)

    round = runas[:3] + runas[4:5]
    forge_obj(runas, round, maxLossStat)

    round = runas[:3] + runas[5:]
    forge_obj(runas, round, maxLossStat)

def main():
    maguear_blite()
    cleaner()

if __name__ == "__main__":
    main()