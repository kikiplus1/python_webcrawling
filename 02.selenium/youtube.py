from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')  #exe 생략 가능
driver.get("https://www.youtube.com/")

time.sleep(3)

#검색어 창을 찾아 seartch 변수에 저장
search = driver.find_element_by_name('search_query')

search.send_keys('반원 코딩')
time.sleep(1)
search.send_keys(Keys.ENTER)

