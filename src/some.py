# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 淘宝秒杀脚本，扫码登录版
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datetime
import time
import sys


def login():
    # 打开淘宝登录页，并进行扫码登录
    print('start login')
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("登录"):
        browser.find_element_by_link_text("登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("http://miao.item.taobao.com/596816283715.htm?ft=t&spm=a1z10.10672-b-s.0.0.167f4d27pTylal&mt=&ft=t&spm=a1z10.10672-b-s.0.0.4ca74d27RLB9Og")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times):

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= times:
            browser.refresh()
            #print("time : ",now)
            #print("times : ",tomes)
            #print('时间到了。。。。。')

            # 点击结算按钮
            try:
                assert(browser.find_element_by_link_text("刷新抢宝").click())
                #print('looking for J_Go')
                # if browser.find_element_by_id("J_LinkBuy"):
                #     print('find J_LinkBuy')
                #     browser.find_element_by_id("J_LinkBuy").click()
                #     print("结算成功")
                if browser.find_element_by_link_text("刷新抢宝"):
                    browser.find_element_by_link_text("刷新抢宝").click()
            except KeyboardInterrupt:
                print("刷新失败 !!!")
                browser.refresh()
                sys.exit(0)

            while True:
                try:
                    print('looking for 提交订单按钮')
                    if browser.find_element_by_link_text('提交订单'):
                        print('find 提交订单按钮')
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    print("再次尝试提交订单")
                time.sleep(0.01)
        else:
            print('时间不到')
            time.sleep(0.02)


if __name__ == "__main__":
    times = input("请输入抢购时间，格式如(2018-09-06 11:26:00.000000):")
    # 时间格式："2019-06-14 09:59:00.000000"
    #"2019-06-14 10:00:00.000000"
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
