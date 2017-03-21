import util
import time


fps_cnt = 0
fps_t = time.time()

while True:
    util.screenshot(region=(708, 391, 120, 30))
    fps_cnt += 1
    now_t = time.time()

    if now_t - fps_t > 1:
        print('fps %.2f' % (fps_cnt / (now_t - fps_t)), end='\r')
        fps_cnt = 0
        fps_t = time.time()
