from base.base import Base
from data.page_data import *


class LoginPage(Base):
    # 跳转至登录按钮
    def page_login(self):
        # 点击去登录
        self.base_click(el_login_page)
        # 点击账号登录
        self.base_click(el_account_page)
    # 登录
    def login(self, account, password):
        # 输入账号
        self.base_send_text(el_account, account)
        # 输入密码
        self.base_send_text(el_password, password)
        # 点击隐私按钮
        self.base_click(el_agree)
        # 点击登录按钮
        self.base_click(el_login_btn)
    def login_assert(self):
        result = self.base_get_text(el_error)
        print(result)
        return result



