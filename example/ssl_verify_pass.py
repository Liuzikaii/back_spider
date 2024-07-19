# 三方库
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 数据包过SSL证书验证
def requests_pass_ssl():
    requests.get(url="填写你要请求的URL", verify=False)  # 忽略SSL证书


# (selenium)模拟浏览器过SSL证书验证
def selenium_pass_ssl():
    options = Options()
    options.add_argument('--ignore-certificate-errors')  # 忽略SSL证书验证
    browser = webdriver.Chrome(options=options)  # 初始化浏览器
    browser.get('填写你要请求的URL')  # 发起请求
    browser.implicitly_wait(30)  # 隐式等待30s
                                                  