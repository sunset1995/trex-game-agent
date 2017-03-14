import util
import time
import pyautogui

# Find dragon on screen
dragon = pyautogui.locateOnScreen('dragon.png')
while dragon is None:
    print('Cute dragon not found !!!')
    dragon = pyautogui.locateOnScreen('dragon.png')
dragonPos = dragon[0:2]
dragonSize = dragon[2:4]
print('Dragon Position:', dragonPos)


# Scan area
x = int(dragonPos[0] + dragonSize[0] + 25)
y = int(dragonPos[1])
w = 120
h = int(dragonSize[1] * 2)

def hasObstacle():
    im = screenshot(region=(x, y, w, h))
    return (83, 83, 83) in im.im


# Adjust scan area as speed up
s_time = time.time()
level = (130, 150, 175, 200, 240, 280, )
upgrade_time = (30, 40, 55, 70, 100, 300, )
now_level = 0


# Start game
pyautogui.click(dragonPos)
pyautogui.press(' ')

while True:
    if hasObstacle():
        pyautogui.press(' ')

    if now_level < len(level) and time.time() - s_time > upgrade_time[now_level]:
        w = level[now_level]
        now_level += 1
        print('upgrade', w)