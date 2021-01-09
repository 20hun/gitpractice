from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.naver.com")

driver.find_element_by_css_selector("#NM_RTK_ROLLING_WRAP").click()

rnks = driver.find_elements_by_css_selector(".filter_item.NM_RTK_VIEW_filter")
for rnk in rnks:
    rnk.find_elements_by_css_selector(".range.NM_RTK_VIEW_filter_range")[3].click()

driver.find_elements_by_css_selector(".age_item")[1].click()
driver.find_element_by_css_selector("#NM_RTK_VIEW_set_btn").click()
time.sleep(2)
keyws = driver.find_elements_by_css_selector(".realtime_item")
cnt = 0
for keyw in keyws:
    print(keyw.find_elements_by_xpath('.//span[@class = "keyword"]')[0].text)
    cnt = cnt + 1
    if cnt == 10:
        break

driver.close()