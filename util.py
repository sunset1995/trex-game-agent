import time
from PIL import Image
from mss import mss

# Fast screenshot
# Usage just like pyautogui
# Parameter:
#     region: optional, four-integer tuple (left, top, width, height)
def screenshot(region=None):
    im = None
    with mss() as sct:
        # Retrieve monitors informations:
        monitors = sct.enum_display_monitors()

        # Region to capture
        monitor = dict(monitors[1])
        if region != None:
            monitor['left'] = int(region[0])
            monitor['top'] = int(region[1])
            monitor['width'] = int(region[2])
            monitor['height'] = int(region[3])

        # Get pixels on image
        sct.get_pixels(monitor)
        im = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    
    # Crop if needed
    if region != None and type(region)==tuple and len(region)==4:
        # To make this function pyautogui like
        im = im.crop((region[0], region[1], region[0]+region[2], region[1]+region[3]))

    return im


# Evaluate screenshot time in seconds
def evaluate_screenshot_time(region=None):
    t = time.time()
    im = screenshot(region)
    return time.time() - t
