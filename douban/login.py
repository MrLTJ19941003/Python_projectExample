import requests,time,json
import os
from bs4 import BeautifulSoup
import douban.baidu
import douban.ip
import time

# cookies的自动化管理。
# 获取的服务器的Set-Cookie用session直接自动解析并保存，在后续的请求中，会在请求头中自动携带这些cookie
# LWPCookieJar:对cookie进行自动操作，load() save()
from http.cookiejar import LWPCookieJar

class login:
    def __init__(self):
        self.url="https://accounts.douban.com/login"
        self.session=requests.Session()
        self.session.cookies = LWPCookieJar(filename='doubancookie.txt')
        try:
            self.session.cookies.load(filename='doubancookie.txt', ignore_expires=True, ignore_discard=True)
        except Exception as e:
            print('加载失败')

    def logins(self):
        count =1
        while count<=3:
            result=self.session.post("https://accounts.douban.com/login",data=self.getDate(),headers=self.getheader(),proxies=douban.ip.getip(),verify=False)
            if result.status_code==200:
                #results = requests.get("https://www.douban.com/")

                couent=BeautifulSoup(result.text, 'html.parser')
                text = couent.find('div', {'class': 'toast-msg error-msg'})
                print(text)
                if text!=None:
                    text1 = text.string.strip()
                    print(text1)
                    time.sleep(15)
                    count = count + 1
                else:
                    print('登录成功')
                    self.session.cookies.save(ignore_discard=True, ignore_expires=True)
                    break
            else:
                print('登录失败')




    def getDate(self):
        r = self.session.get(self.url,headers=self.getheader(),proxies=douban.ip.getip(),verify=False)
        if r.status_code == 200:
            #print(BeautifulSoup(r.text, 'html.parser'))
            responetest = BeautifulSoup(r.text, 'html.parser')
            source = responetest.find('input', {'name': 'source'})['value']
            redir = responetest.find('input', {'name': 'redir'})['value']
            captchaids = responetest.find('input', {'name': 'captcha-id'})
            imageurls = responetest.find('img', {'id': 'captcha_image'})
            date={
                'source': 'None',#self.source,#隐藏列 页面取
                'redir':'https://www.douban.com/group/topic/122105249/',#self.redir,#隐藏列 页面取
                'form_email': "18569517764",#账号
                'form_password': "liu01234",#密码
                'login': "登录"
            }
            if imageurls != None and captchaids != None:
                captchaid = captchaids['value']
                imageurl = imageurls['src']

                captcharesponse = self.session.get(imageurl)
                with open('checkcode.jpg', 'wb') as f:
                    f.write(captcharesponse.content)
                    f.close()
                os.startfile('checkcode.jpg')
                textss = douban.baidu.getImageString1('checkcode.jpg')
                print(textss)
                if textss==None:
                    print('可能需要手动输入验证码')
                    input('请输入验证码')
                test = textss
                print(test)
                date['captcha-solution']= test  # 验证码
                date['captcha-id']=  captchaid,  # 隐藏列页面取
                print("参数 ：" )
                print(date)
        return date

    def getheader(self):
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
        headers = {
            "Host": "www.douban.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Referer": "http://accounts.douban.com/login",
            "User-Agent": agent
        }
        return headers
if __name__ == '__main__':
    # obj = login()
    # obj.logins()
    # time.sleep(10)
    # print('sss')
    pass
