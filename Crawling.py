from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os, sys

def crawling(bird_name: str) -> None:
    if not os.path.isdir(f"Dataset/{bird_name}/"):
        os.makedirs(f"Dataset/{bird_name}/")
    
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko")

    search = bird_name
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
    last_height = new_height
    
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 1

    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH, "//*[@id='islrg']/div[1]/div[1]/a[1]/div[1]/img").get_attribute('src')
            urllib.request.urlretrieve(imgUrl, f"{bird_name}/{count:0>3}.jpg")
            print(f"Image saved: {count:0>3}.jpg")
            count += 1
        except:
            pass

    driver.close()


if __name__ == "__main__":
    args = sys.argv
    
    if len(args) == 2:
        crawling(args[1])
    else:
        print("Error: Unappropriate Argument")