from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data=f.read()
    print('Status ' ,f.status,f.reason)
    for x,y in f.getheaders():
        print('key: %s,value:%s '% (x,y))
    print('data : ' , data.decode('utf-8'))