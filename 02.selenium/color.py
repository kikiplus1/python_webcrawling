from selenium import webdriver
import time
from pprint import pprint
from selenium.webdriver.common.keys import Keys
from collections import Counter
import time

driver = webdriver.Chrome('chromedriver')  #exe 생략 가능
driver.get("http://zzzscore.com/color/")
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
print(len(btns))

def analysis():
    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    result = Counter(btns_rgba)

    for key, value in result.items():
        if value == 1:
            answer = key
            break
    else:
        answer = None
        print("정답을 찾을 수 없습니다.")

    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()


start = time.time()
while time.time() - start <=60:
    analysis()