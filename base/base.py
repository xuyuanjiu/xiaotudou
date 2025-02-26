import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 显示等待查找元素方法
    def base_find_element(self, *feature, timeout=15, poll=0.1):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                lambda x: x.find_element(*feature))
        except TimeoutError:
            print(f"{feature}元素未在规定时间{time}秒内找到元素")

    # 发送文本方法
    def base_send_text(self, feature, text):
        return self.base_find_element(*feature).send_keys(text)

    # 点击方法
    def base_click(self, feature):
        return self.base_find_element(*feature).click()

    # 获取文本方法
    def base_get_text(self, feature):
        return self.base_find_element(*feature).text

    # 截图方法
    def base_get_image(self):
        now = time.localtime()
        time_name = time.strftime('%Y-%m-%d_%H:%M:%S', now)
        image = "./screenshot/" + time_name + ".png"
        self.driver.get_screenshot_as_file(image)

    # 切换句柄方法
    def base_switch_handles(self, n=1):
        self.driver.switch_to.window(self.driver.window_handles[n])

    # 切换iframe框架
    def base_switch_iframe(self):
        self.driver.switch_to.frame()
