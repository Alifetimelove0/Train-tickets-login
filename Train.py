#coding=utf-8
from selenium import webdriver
#print (help(webdriver.Firefox))
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

browesr=webdriver.Firefox()
        #(executable_path="D:\Program Files (x86)\geckodriver")
#url_1="http://www.baidu.com"
#browesr.get(url_1)
#print browesr.title
#sleep(3)
url_2="http://www.12306.cn/mormhweb/"
browesr.get(url_2)
sleep(3)
first_handle=browesr.current_window_handle
element1=browesr.find_element_by_xpath("/html/body/div[1]/div[4]/div[3]/div[1]/ul/li[3]/a")
ActionChains(browesr).double_click(element1).perform()
sleep(3)
allhandles=browesr.window_handle
for handle in allhandles:
    if handle!= frist_handle:
        sencond_handle= handle
browesr.switch_to_window(sencond_handle)
browesr.find_element_by_id("fromStationText").send_keys(u"重庆")
sleep(2)
browesr.find_element_by_id("toStationText").send_keys(u"桂林")
sleep(2)
browesr.find_element_by_id("train_date")
'''JavascriptExecutor removeAttribute = (JavascriptExcutor) browesr
removeAttribute.executeScript("var setDate=document.getElmentbyId(\"train_date\");setDate.removeAttribute('readonly')")
'''
'''browesr.switch_to_frame("iframe")
js="document.getElementbyid"'''
#browesr.quit()