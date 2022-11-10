# This is a sample Python script.

# Key.alt_l: Left ALT
# Key.backspace: Backspace
# Key.ctrl_l: Left Ctrl
# Key.delete: Delete
# Key.enter: Enter
# Key.esc: Escape
# Key.f1: F1
# Key.f5: F5
# Key.media_play_pause: Play/Pause
# Key.page_down: Page Down
# Key.up: Up Arrow Key
# keyboard.press(Key.ctrl)

import time
from pynput.keyboard import Key, Controller
import random
import string

keyboard = Controller ()
counter = 0
sleepTyping = 0.1
sleepMove = 0.3

time.sleep(5)

for i in range(10):
    #nový záznam
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(sleepMove)
    #potvrzení
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(sleepMove)

    #kompenzace bugu v ais
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(sleepMove)

    icpzadatele = random.randint(00000000, 99999999)
    print(icpzadatele)


    for char in str(icpzadatele):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(sleepTyping)

    #doprava
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)

    #odbornost žadatele
    odbzadatele = random.randint(100, 999)
    print(odbzadatele)
    for char in str(odbzadatele):
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(sleepTyping)

    # 4xdoprava
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)

    #nahodne jmeno
    companyname = string.ascii_letters
    companyname = (''.join(random.choice(companyname) for i in range(10)))
    print(companyname)

    #python vypíše jmeno do tabulky
    for char in companyname:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(sleepTyping)

    # 1xdoprava
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)

    # nahodný neexistující titul
    titul = string.ascii_letters
    titul = (''.join(random.choice(titul) for i in range(3)))
    print(titul)

    # python vypíše jmeno do tabulky
    for char in titul:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(sleepTyping)

    # 1xdoprava
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)

    # nahodné příjmení
    surname = string.ascii_letters
    surname = (''.join(random.choice(surname) for i in range(3)))
    print(surname)

    # python vypíše jmeno do tabulky
    for char in surname:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(sleepTyping)

    # 1xdoprava
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(sleepMove)

    # nahodne jmeno
    name = string.ascii_letters
    name = (''.join(random.choice(name) for i in range(10)))
    print(name)

    # python vypíše jmeno do tabulky
    for char in name:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(sleepTyping)

    # 8xzpět
    keyboard.press(Key.shift_l)
    for i in range(8):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(sleepMove)
    keyboard.release(Key.shift_l)
    time.sleep(sleepMove)