# -*- coding: UTF-8 -*-

from aip import AipOcr
import json

# 定义常量
APP_ID = '11300545'
API_KEY = 'RrZMNHUGrOyGmUu1zsHCh3um'
SECRET_KEY = 'OitzrdVI6nIkBq1HANcfuc9zXEudXZrf'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)



def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
        # 定义参数变量




# 调用通用文字识别接口
def getImageString(filePath):
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    if result['words_result'] != None and result['words_result'] != []:
        text = result['words_result'][0]['words']
        print(text)
        return text
# 调用通用文字识别接口
def getImageString1(filePath):
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }
    result = aipOcr.basicAccurate(get_file_content(filePath), options)
    if result['words_result'] != None and result['words_result'] != []:
        text=result['words_result'][0]['words']
        #print(text)
        return text

# 读取图片
# filePath = "checkcode.jpg"
# string=getImageString1(filePath)
# print(json.dumps(string))
# if string['words_result']!=None and string['words_result']!=[]:
#     print(string['words_result'][0]['words'])
