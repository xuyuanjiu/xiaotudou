import time

import pytest
from page.page_case import LoginPage
from tools.driver_tools import BrowDriver
from tools.read_data import read_data


class Test:
    driver = None

    @classmethod
    def setup_method(cls):
        cls.driver = BrowDriver().get_driver()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def teardown_method(cls):
        BrowDriver().quit_driver()

    # 登录case

    @pytest.mark.parametrize("data", read_data("data.json"))
    def test_login(self, data):
        self.login_page.page_login()
        self.login_page.login(account=data["account"], password=data["password"])
        msg = self.login_page.login_assert()
        assert data["expected"] in msg
