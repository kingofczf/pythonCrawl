#coding:utf-8
from urllib import urlopen
from bs4 import BeautifulSoup

import re
import os
import os.path
import json

import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

rootdir = "F:\data\hyperlinks"  # ָ???????????ļ???
i=1

for parent,dirnames,filenames in os.walk(rootdir):     #???????????ֱ𷵻?1.??Ŀ¼ 2.?????ļ??????֣?????·???? 3.?????ļ?????
        for filename in filenames:                     #?????ļ???Ϣ
            sourceDir = os.path.join(parent,filename)  #?????ļ?·????Ϣ
            fopen = open(sourceDir,'r')
            while True:
                datadic={}
                line = fopen.readline()
                if line == "":
                    break
                try:
                    html = urlopen(line).read()
                    soup = BeautifulSoup(html)
                    filestr ="F:/data/raw_data/" + str(i)+ ".txt"
                    titlestr =""
                    fromstr=""
                    articlestr=""

                    tilist = soup.find_all("h1", id="main_title")
                    if len(tilist):#????
                        titlestr=str(tilist[0])#????

                    sourlist = soup.find_all("span",id="media_name")
                    if len(sourlist):
                        fromstr =str(sourlist[0])#??Դ

                    arlist = soup.find_all("div",id="artibody")
                    if len(arlist):
                        for z in range(len(arlist[0].find_all('p'))):
                            articlestr = articlestr + str(arlist[0].find_all('p')[z])#????

                    soup_title = BeautifulSoup(titlestr)
                    soup_from = BeautifulSoup(fromstr)
                    soup_article = BeautifulSoup(articlestr)           
                    datadic['title']=soup_title.get_text()
                    datadic['from']=soup_from.get_text()
                    datadic['article']=soup_article.get_text()
                    if not (not datadic['title'].strip() and not datadic['from'].strip() and not datadic['article'].strip()):
                        json.dump(datadic, open(filestr, 'w'),encoding="UTF-8", ensure_ascii=False)
                        i = i+1
                except IOError.errno:
                    print ("*** file open error",e)
            fopen.close()
   