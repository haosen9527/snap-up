# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 淘宝秒杀脚本，扫码登录版
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datetime
import time
import sys


target = "https://detail.tmall.com/item.htm?spm=a1z0d.6639537.1997196601.4.25d874848K02pR&id=526177665200"

def login():
    # 打开淘宝登录页，并进行扫码登录
    print('start login')
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("登录"):
        browser.find_element_by_link_text("登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get(target)
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times):

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= times:
            #browser.refresh()
            browser.get(target)
            time.sleep(0.2)
            while True:
                try:
                    if browser.find_element_by_link_text('立即购买'):
                        print('find 立即购买')
                        browser.find_element_by_link_text('立即购买').click()
                        time.sleep(1)
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    browser.get(target)
                    print("刷新页面")
                    # time.sleep(0.5)
                time.sleep(0.7)
        else:
            print('时间不到')
            time.sleep(0.02)


if __name__ == "__main__":
    # times = input("请输入抢购时间，格式如(2018-09-06 11:26:00.000000):")
    # 时间格式："2019-06-18 09:00:00.000000"
    times = "2019-06-18 13:59:00.000000"
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)


    browser = webdriver.Chrome('/usr/bin/chromedriver')
    print('start chrome done')
    # browser.maximize_window()
    print('maximize chrome done,gonna login')
    login()
    buy(times)
