# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
import itchat

def getHTMLText(url):
        driver = webdriver.PhantomJS(executable_path='C:\\Users\\Administrator\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')  # phantomjs的绝对路径
        time.sleep(2)
        driver.get(url)  # 获取网页
        time.sleep(2)
        return driver.page_source

def fillUnivlist(html):
        soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
        #tag = soup.find_all('div', attrs={'class': 'listInfo'})
        tag = soup.find_all('li', attrs={'class': 'li5'})


        #tag=soup.find_all('span',attrs=)
        for x in tag:
        	#print(type(x))
        	#print(type(x.get_text()))
        	#print((x.get_text())[:-50])
        	strs=((x.get_text())[:-50]).strip().replace(',','')
        	#print(strs)
        	money=float(strs)
        	if(money>=0):
        		return money

        	#print(money)


        	#print(str(x))
        	#for y in x:
        		#soupx=BeautifulSoup(x, 'html.parser')
        		#print(soupx.find_all)
        #print(str(tag[0]))
        return 0

def main():
	itchat.login()
	url = 'https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2F%23%2F'#'http://sports.qq.com/articleList/rolls/' #要访问的网址
	html = getHTMLText(url) #获取HTML
	while True:
		money=fillUnivlist(html)
		if(money>0):
			print(money)
			itchat.send(str(money),'filehelper')
			time.sleep(10)


if __name__ == '__main__':
    main()

#C:\Users\Administrator\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin
#webaddress='''https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2F%23%2F'''
#response = getHTMLText(webaddress)
#print(type(response))
#print(str(response))