# 点击去登录
from selenium.webdriver.common.by import By

el_login_page = By.XPATH, '//*[@ class="u-button bd-login-button__wrapper u-button--primary"]'

el_account_page = By.CSS_SELECTOR, "#TANGRAM__PSP_11__changePwdCodeItem"

el_account = By.CSS_SELECTOR, '#TANGRAM__PSP_11__userName'

el_password = By.CSS_SELECTOR, '#TANGRAM__PSP_11__password'

el_agree = By.CSS_SELECTOR, '#TANGRAM__PSP_11__isAgree'

el_login_btn = By.CSS_SELECTOR, '#TANGRAM__PSP_11__submit'

el_error = By.CSS_SELECTOR, '#TANGRAM__PSP_11__error'
