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
        money_list=[]
        for x in tag:
        	#print(type(x))
        	#print(type(x.get_text()))
        	#print((x.get_text())[:-50])
        	strs=((x.get_text())[:-50]).strip().replace(',','')
        	#print(strs)
        	money=float(strs)
        	if(money>=0 and money<500):
        		money_list.append(money)
        	#return money

        	#print(money)


        	#print(str(x))
        	#for y in x:
        		#soupx=BeautifulSoup(x, 'html.parser')
        		#print(soupx.find_all)
        #print(str(tag[0]))
        return money_list

def main():
	itchat.login()
	url = 'https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2F%23%2F'#'http://sports.qq.com/articleList/rolls/' #要访问的网址
	
	#想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
	users = itchat.search_friends(name='林乖乖')
	#获取好友全部信息,返回一个列表,列表内是一个字典
	print(users)
	#获取`UserName`,用于发送消息
	userName = users[0]['UserName']
	#itchat.send("hello",toUserName = userName)
	while True:
		html = getHTMLText(url) #获取HTML
		money_list=fillUnivlist(html)
		for money in money_list:
			if(money>0 and money<=500):
				print(money)
				itchat.send('有可投资项目，投资金额为:'+str(money),'filehelper')
				itchat.send('有可投资项目，投资金额为:'+str(money),toUserName=userName)
		time.sleep(60)


if __name__ == '__main__':
    main()

#C:\Users\Administrator\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin
#webaddress='''https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2F%23%2F'''
#response = getHTMLText(webaddress)
#print(type(response))
#print(str(response))