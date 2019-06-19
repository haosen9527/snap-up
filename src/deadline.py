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
        browser.get("https://cart.taobao.com/cart.htm?spm=a21bo.2017.1997525049.1.5af911d9YEd2En&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times, choose):
    # 点击购物车里全选按钮
    if choose == 2:
        print("请手动勾选需要购买的商品")
        time.sleep(2)
    elif choose == 1:
        print('choose == 1')
        try:
            print('look for J_SellectAll1')
            if browser.find_element_by_id("J_SelectAll1"):
                print('find SelectAll button')
                browser.find_element_by_id("J_SelectAll1").click()
        except:
            print("找不到全选按钮")

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= times:
            #print("time : ",now)
            #print("times : ",tomes)
            #print('时间到了。。。。。')

            # 点击结算按钮
            try:
                #print('looking for J_Go')
                if browser.find_element_by_id("J_Go"):
                    print('find J_Go')
                    browser.find_element_by_id("J_Go").click()
                    print("结算成功")
            except KeyboardInterrupt:
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
    # choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    choose = 1
    buy(times, choose)
