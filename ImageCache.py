from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from PIL import Image
import os
import configparser

FILEPATH = os.path.dirname(__file__)
FILENAME = "brHeatMapGRB.png"

COMPATH = os.path.join(FILEPATH,'ImageCache/' ,FILENAME)

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless=new") # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)


def ImCache():
    print("Caching BR Heatmap")
    start_url = "https://wt.controlnet.space/#br-heatmap"
    driver.get(start_url)
    sleep(10)

    driver.execute_script("document.body.style.zoom='75%'")

    driver.get_screenshot_as_file(COMPATH)
    driver.quit()
    print("Exited Page")

    # Opens a image in RGB mode
    im = Image.open(COMPATH)

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    left = 0
    top = 90
    right = 615
    bottom = height

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    im1.save(COMPATH)
    print("Heatmap Cached")
    return