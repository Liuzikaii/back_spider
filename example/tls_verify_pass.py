# 三方库
import undetected_chromedriver as uc
from curl_cffi import requests
from selenium.webdriver.chrome.options import Options


# 数据包过TLS校验
def requests_pass_tls():
    # requests发送get请求
    requests.get(url="填写你要请求的URL")


# (selenium)模拟浏览器过TLS校验
def selenium_pass_tls():
    options = Options()  # 创建一个Chrome配置对象
    # options.add_argument('--headless')  # 无头模式
    options.add_argument('--no-sandbox')  # 禁用沙箱模式
    options.add_argument('--window-size=1300,1000')  # 设置窗口大小, 窗口大小会有影响
    browser = uc.Chrome(options=options)  # 初始化浏览器

    browser.get(url="填写你要请求的URL")


