#coding=utf-8
#import urllib.request, urllib.parse
from selenium import webdriver
import time
import http.cookiejar

get_url = 'https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2Flogin.html%23%2F%3F'
#cookie_filename = 'cookie.txt'
#cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
#cookie_aff.load(cookie_filename,ignore_discard=True,ignore_expires=True)

#handler = urllib.request.HTTPCookieProcessor(cookie_aff)
#opener = urllib.request.build_opener(handler)
#使用cookie登陆get_url
#get_request = urllib.request.Request(get_url)
#get_response = opener.open(get_request)
#print(get_response.read().decode())
driver=webdriver.PhantomJS(executable_path='C:\\Users\\Administrator\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')
#forever=1; gr_user_id=21e0aea3-87d6-4adb-8e4b-e55a1890efe4; acw_tc=AQAAAMxuxzi06AYABHC23kJkyxu4gvoi; hqbsta=0; fofsta=0; b9485b47ab6676bd_gr_session_id=8a4bcc1f-4d46-4c26-b2db-7786b6673853; SESSION=6e6e7d01-cf12-45b2-8104-7f3464f94b87
driver.get(get_url)
cookie_aff={'forever':'1','gr_user_id':'21e0aea3-87d6-4adb-8e4b-e55a1890efe4','acw_tc':'AQAAAMxuxzi06AYABHC23kJkyxu4gvoi','hqbsta':'0','fofsta':'0','b9485b47ab6676bd_gr_session_id':'8a4bcc1f-4d46-4c26-b2db-7786b6673853','SESSION':'6e6e7d01-cf12-45b2-8104-7f3464f94b87'}
driver.add_cookie(cookie_aff)

time.sleep(2)
driver.refresh()
print(driver.page_source)
