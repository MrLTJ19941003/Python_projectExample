import hashlib

md5=hashlib.md5()
md5.update('bbbb'.encode('utf-8'))
print(md5.hexdigest())
md51=hashlib.md5()
md51.update('bb'.encode('utf-8'))
md51.update('bb'.encode('utf-8'))
print(md51.hexdigest())

sha1=hashlib.sha1()
sha1.update('bbbb'.encode('utf-8'))
print(sha1.hexdigest())