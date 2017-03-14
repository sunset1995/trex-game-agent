import time
from PIL import Image
from mss import mss

# Fast screenshot
# Usage just like pyautogui
# Parameter:
#     region: optional, four-integer tuple (left, top, width, height)
def screenshot(region=None):
    # Example is modified from https://python-mss.readthedocs.io/en/dev/examples.html
    im = None
    with mss() as sct:
        # We retrieve monitors informations:
        monitors = sct.enum_display_monitors()

        # Get rid of the first, as it represents the "All in One" monitor:
        for num, monitor in enumerate(monitors[1:], 1):
            # Get raw pixels from the screen.
            # This method will store screen size into `width` and `height`
            # and raw pixels into `image`.
            sct.get_pixels(monitor)

            # Create an Image:
            im = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    
    # Crop if needed
    if region != None and type(region)==tuple and len(region)==4:
        # To make this function pyautogui like
        im = im.crop((region[0], region[1], region[0]+region[2], region[1]+region[3]))

    return im


# Evaluate screenshot time in seconds
def evalutae_screenshot_time():
    t = time.time()
    im = screenshot()
    return time.time() - t
