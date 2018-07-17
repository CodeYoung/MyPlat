import sys
import io
from urllib import request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网站
url = 'https://www.hfax-fintech.com/lending.html#/p2pdetail/LH180423000528'#'https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2Flogin.html%23%2F%3F'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'forever=1; gr_user_id=21e0aea3-87d6-4adb-8e4b-e55a1890efe4; acw_tc=AQAAAMxuxzi06AYABHC23kJkyxu4gvoi; hqbsta=0; fofsta=0; b9485b47ab6676bd_gr_session_id=8a4bcc1f-4d46-4c26-b2db-7786b6673853; SESSION=6e6e7d01-cf12-45b2-8104-7f3464f94b87'

#登录后才能访问的网页
#url = 'https://www.hfax-fintech.com/lending.html#/lending/1?rsrc=https%3A%2F%2Fwww.hfax.com%2Flogin.html%23%2F%3F'

req = request.Request(url)
#设置cookie
req.add_header('cookie', cookie_str)
#设置请求头
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

resp = request.urlopen(req)

print(resp.read().decode('utf-8'))