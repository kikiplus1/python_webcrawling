from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')  #exe 생략 가능
driver.get("http://zzzscore.com/1to50/")
driver.implicitly_wait(300)

#전역변수, 현재 찾아야 할 숫자
num = 1

def ClickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    for btn in btns:
        if btn.text == str(num):
            btn.click()
            num +=1


while num<=50:
    ClickBtn()