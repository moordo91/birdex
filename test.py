from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

# driver = webdriver.Chrome() :라이브러리에서 가져온 webdriver라는 함수를 통해서 크롬드라이버를 driver라는 함수에 저장

#에러 대비 함수
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
# assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
# elem.clear()
elem.send_keys('"조코딩"')
elem.send_keys(Keys.RETURN)

# 스크롤바를 다 내려주는 코드

SCROLL_PAUSE_TIME = 1
#Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    try:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height
    except:
        pass
time.sleep(3)

img = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for i in img:
    try:
        i.click()
        time.sleep(2)
        url = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, "test"+str(count)+".jpg")
        count = count +1
    except:
        pass
driver.close()
print("end")