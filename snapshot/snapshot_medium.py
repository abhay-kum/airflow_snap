from splinter import Browser
from datetime import datetime
import os

with Browser(driver_name="chrome",headless=True) as browser:
    # Visit URL
    if not os.path.exists('data/'):
    	os.mkdir("data/")

    current_directory = os.getcwd()
    print(current_directory)

    image_file_path = "data/medium_" + datetime.strftime(datetime.now(),'%Y_%m_%d') + ".png"

    url = "https://www.medium.com/"

    browser.visit(url)
    screenshot_path = browser.screenshot(current_directory + "/data/", full=True)
    os.rename(screenshot_path, image_file_path)
