from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import urllib.request
import os, sys

def crawling(bird_name: str) -> None:
    dataset = f"C:/Users/moord/Documents/Project/Dataset/{bird_name}/"
    if not os.path.isdir(dataset):
        os.makedirs(dataset)
    
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get("https://www.google.co.kr/imghp?hl=ko")
    driver.implicitly_wait(time_to_wait=10)
    keyElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keyElement.send_keys(bird_name)
    keyElement.send_keys(Keys.RETURN)

    bodyElement = driver.find_element(By.TAG_NAME, 'body')
    time.sleep(5)
    for _ in range(30):
        bodyElement.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
    
    images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img" )
    imageURL = []
    try:
        for image in images:
            if image.get_attribute('src') is not None:
                imageURL.append(image.get_attribute('src'))
                
        for seq, urlImg in enumerate(imageURL):
            urllib.request.urlretrieve(urlImg, dataset + f"{seq:0>3}.jpg")
    except:
        pass
    
    print("Crawling End")


if __name__ == "__main__":
    args = sys.argv
    
    if len(args) == 2:
        crawling(args[1])
    else:
        print("Error: inappropriate Argument")