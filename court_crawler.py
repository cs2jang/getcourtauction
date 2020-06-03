from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import time

def check_car_exist():
    try:
        driver.find_element_by_class_name('layer_window layer_sm')
    except NoSuchElementException:
        return True
    return False


driver = webdriver.Chrome("C:\\Users\\jk\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(3)
driver.get('https://www.courtauction.go.kr')
time.sleep(2)

mainframe = driver.find_elements_by_tag_name('frame')[0]
driver.switch_to_frame(mainframe)
driver.find_element_by_id('master')
driver.find_element_by_css_selector('#menu > h1:nth-child(5) > a > img').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="contents"]/form/div[2]/a[1]/img').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)
