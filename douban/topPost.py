import os,random
import douban.ip
import time
import requests
from bs4 import BeautifulSoup

from douban.DistinguishImage import get_captcha
from douban.login import login

def get_cookies():
    # 获取豆瓣登录Cookie信息
    cookies = {}
    with open("doubancookie.txt", "r") as f_cookie:
        douban_cookies = f_cookie.readlines()[2].replace('Set-Cookie3:','').split("; ")
        for line in douban_cookies:
            try:
                key, value = line.split("=", 1)
                key=key.strip()
                cookies[key] = value
            except Exception as e:
                pass
        return cookies

def get_form_ck_from_cookie():
    # 从cookie中获取ck值（ck: post操作表单隐藏字段）
    douban_cookies = get_cookies()
    return douban_cookies["ck"]

def comment_topic(topic_url, comment_dict,obj):
    # 在一个帖子下发表回复
    print(topic_url)

    #header['cookie'] = cookies=get_cookies()
    r = obj.session.post(topic_url,headers=obj.getheader(),data=comment_dict,proxies=douban.ip.getip())
    print("in func comment_topic(), " +
                           str(comment_dict) + ", status_code: " + str(r.status_code))
    return r

def gerenate_str():
    str = 'ABCDEFGHYGK';
    strs = []
    for i in range(5):
        strs.append(random.choice(str))
    return ''.join(strs)


def post(response_text=None,is_yz=False):
    #comment_dict = comment.make_comment_dict(topic_url, comment_str)
    comment_dict = {
        "ck": get_form_ck_from_cookie(),
        "rv_comment": gerenate_str(),
        "start": 0,
        "img":"",
        #"captcha-solution": verify_code,
        #"captcha-id": pic_id,
        "submit_btn": "发送"
    }
    if response_text:
        couent = BeautifulSoup(response_text.text, 'html.parser')
        captcha_image = couent.find('img', {'id': 'captcha_image'})
        captcha_id = couent.find('input', {'name': 'captcha-id'})
        if captcha_image != None and captcha_id != None:
            captchaid = captcha_id['value']
            imageurl = captcha_image['src']

            captcharesponse = requests.get(imageurl)

            if is_yz:
                with open('plcode.jpg', 'wb') as f:
                    f.write(captcharesponse.content)
                    f.close()
                os.startfile('plcode.jpg')
                textss = input('自动识别失败，请手动输入验证码 :')
            else:
                #textss = douban.baidu.getImageString1('plcode.jpg')
                textss = get_captcha(captcharesponse.content)
                print(textss)
                if textss == None:
                    print('可能需要手动输入验证码')
                    textss = input('请输入验证码 :')
            test = textss
            print(test)
            comment_dict['captcha-solution'] = test  # 验证码
            comment_dict['captcha-id'] = captchaid,  # 隐藏列页面取
            print("参数 ：")
            print(comment_dict)
    return comment_dict

# div class = attn  '请正确输入图片中的单词'

def execute_add_comment(query_url,comment_url,obj,is_yz=False):
    time.sleep(6)
    r = obj.session.get(query_url, headers=obj.getheader(), proxies=douban.ip.getip(), verify=False)
    add_date = post(r,is_yz=is_yz)
    print(add_date)
    time.sleep(4)
    result = obj.session.post(comment_url, headers=obj.getheader(),
                              data=add_date,
                              proxies=douban.ip.getip(), verify=False)
    couent = BeautifulSoup(result.text, 'html.parser')
    attn = couent.find('div', {'class': 'attn'})
    if attn:
        print(attn.text)
        execute_add_comment(query_url, comment_url, obj,is_yz=True)
    else:
        is_add_success = couent.find('a', {'id': 'last'})
        if is_add_success:
            print('添加成功')
            print(is_add_success.text)

#{"117435813","117557176","117556862","117557070","117430014"}
obj = login()
urls = ['https://www.douban.com/group/topic/122105787/',
        'https://www.douban.com/group/topic/122105711/',
        'https://www.douban.com/group/topic/122105621/',
        'https://www.douban.com/group/topic/122105560/',
        'https://www.douban.com/group/topic/122105249/']

add_comment_urls=['https://www.douban.com/group/topic/122105787/add_comment',
                  'https://www.douban.com/group/topic/122105711/add_comment',
                  'https://www.douban.com/group/topic/122105621/add_comment',
                  'https://www.douban.com/group/topic/122105560/add_comment',
                  'https://www.douban.com/group/topic/122105249/add_comment']


for i in range(len(urls)):
    print(urls[i])
    print(add_comment_urls[i])
    execute_add_comment(urls[i],add_comment_urls[i],obj)


# print('122105787')
# time.sleep(11)
# r = obj.session.get("https://www.douban.com/group/topic/122105711/",headers=obj.getheader(),verify=False)
# time.sleep(5)
# result = obj.session.post('https://www.douban.com/group/topic/122105711/add_comment', headers=obj.getheader(),data=post(),
#                          proxies=douban.ip.getip(),verify=False)
# print('122105711')
# time.sleep(10)
# r = obj.session.get("https://www.douban.com/group/topic/122105621/",headers=obj.getheader(),verify=False)
# time.sleep(5)
# result = obj.session.post('https://www.douban.com/group/topic/122105621/add_comment', headers=obj.getheader(),data=post(),
#                          proxies=douban.ip.getip(),verify=False)
# print('122105621')
# time.sleep(12)
# r = obj.session.get("https://www.douban.com/group/topic/122105560/",headers=obj.getheader(),verify=False)
# time.sleep(5)
# result = obj.session.post('https://www.douban.com/group/topic/122105560/add_comment', headers=obj.getheader(),data=post(),
#                          proxies=douban.ip.getip(),verify=False)
# print('122105560')
# time.sleep(14)
# r = obj.session.get("https://www.douban.com/group/topic/122105249/",headers=obj.getheader(),verify=False)
# time.sleep(5)
# result = obj.session.post('https://www.douban.com/group/topic/122105249/add_comment', headers=obj.getheader(),data=post(),
#                          proxies=douban.ip.getip(),verify=False)
# print('122105249')

# comment_topic_url = {"117435813","117557176","117556862","117557070","117430014"}
# count=1
# random_sleep = 3600
# while count<=10:
#     for url in comment_topic_url:
#         if url!="":
#             comment_topic("https://www.douban.com/group/topic/"+url+"/add_comment#last", post("11"),obj)
#             time.sleep(15)
#     #time.sleep(1800)
#     count=count+1

#print(get_form_ck_from_cookie())