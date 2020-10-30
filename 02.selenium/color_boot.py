from selenium import webdriver
import time
from pprint import pprint
from selenium.webdriver.common.keys import Keys
from collections import Counter
import time

driver = webdriver.Chrome('chromedriver')  #exe 생략 가능
driver.get("http://zzzscore.com/color/")
driver.implicitly_wait(300)

start = time.time()

while time.time() - start <=60:
    try :
        btn = driver.find_element_by_class_name("main")
        btn.click()
    except:
        pass
