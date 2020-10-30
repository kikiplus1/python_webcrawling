from selenium import webdriver
import time
from urllib.request import urlretrieve

#화면 창 닫기
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('chromedriver')  #exe 생략 가능
driver.get("https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie")
time.sleep(3)

url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)

#클립 제목과 날짜 확인
title_element1 = driver.find_element_by_class_name('tw-ellipsis')
vid_title = title_element1.text


urlretrieve(vid_url, vid_title+".mp4")

driver.close()

