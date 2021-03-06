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
y = int(dragonPos[1] + dragonSize[1])
w = None
h = int(1)

def hasObstacle():
    im = util.screenshot(region=(x, y, w, h))
    return (83, 83, 83) in im.im

# Adjust scan area as speed up
s_time = time.time()
level = (100, 110, 125, 150, 160, 190, 200, 230, )
upgrade_time = (-1, 30, 40, 60, 70, 140, 170, 300, )
now_level = 0

# FPS measure
fps_cnt = 0
fps_t = time.time()


# Start game
pyautogui.click(dragonPos)
pyautogui.press(' ')

while True:
    if now_level < len(level) and time.time() - s_time > upgrade_time[now_level]:
        w = level[now_level]
        now_level += 1
        print('level %d\n' % w)

    if hasObstacle():
        pyautogui.press(' ')

    # FPS measure
    fps_cnt += 1
    now_t = time.time()
    if now_t - fps_t > 1:
        print('%4d fps %.2f' % (now_t - s_time, fps_cnt / (now_t - fps_t)), end='\r')
        fps_cnt = 0
        fps_t = time.time()
