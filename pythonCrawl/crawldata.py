#coding:utf-8   
import time
import sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8') 


browser = webdriver.Firefox()
time.sleep(3)
browser.get('http://ent.sina.com.cn/film/')
time.sleep(2)
browser.maximize_window() 
time.sleep(1)
js="var q=document.documentElement.scrollTop=150000"
browser.execute_script(js)
time.sleep(1)
browser.execute_script(js)
time.sleep(1)
browser.execute_script(js)
time.sleep(1)

i = 1
urlfilename="F:\data\hyperlinks"+str(i)+".txt"
elem =browser.find_elements_by_class_name("feed-card-item")
fileurl = open(urlfilename,'w')
for w in range(len(elem)):
    EL = elem[w].find_element_by_tag_name("h2").find_elements_by_tag_name("a")
    print(EL[0].get_attribute("href"))
    fileurl.write(EL[0].get_attribute("href")+'\n')
    
fileurl.close()

xpathstr1="//*[@id='feedCardContent']/div[3]/span[7]/a"
xpathstr2="//*[@id='feedCardContent']/div[3]/span[8]/a"

while(1):
    if i<=5:
        browser.find_element_by_xpath(xpathstr1).click()
        time.sleep(1)  
    elif i<=140:
        browser.find_element_by_xpath(xpathstr2).click()
        time.sleep(1)
    elif i>140:
        browser.find_element_by_xpath(xpathstr1).click()
        time.sleep(1) 
        
    js="var q=document.documentElement.scrollTop=150000"
    browser.execute_script(js)
    time.sleep(1)
    browser.execute_script(js)
    time.sleep(1)
    browser.execute_script(js)
    time.sleep(1)

    i = i + 1
    urlfilename='D:\data\hyperlinks'+str(i)+'.txt'
    elem =browser.find_elements_by_class_name("feed-card-item")
    fileurl = open(urlfilename,'w')
    for w in range(len(elem)):
        EL = elem[w].find_element_by_tag_name("h2").find_elements_by_tag_name("a")
        print(EL[0].get_attribute("href"))
        fileurl.write(EL[0].get_attribute("href")+'\n')
    fileurl.close()
