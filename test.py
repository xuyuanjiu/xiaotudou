import time

from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.implicitly_wait(15)
dr.maximize_window()
dr.get("https://pan.baidu.com/")
dr.find_element(By.XPATH, '//*[@ class="u-button bd-login-button__wrapper u-button--primary"]').click()
dr.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_11__changePwdCodeItem").click()
dr.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__userName').send_keys("1234")
dr.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__password').send_keys("121313")
dr.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__isAgree').click()
dr.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__submit').click()
time.sleep(8)
result = dr.find_element(By.CSS_SELECTOR, '#TANGRAM__PSP_11__error').text
print(result)
