import base64

b=base64.b64encode(b'binary\x00string')
print(b)

b=base64.b64decode(b)
print(b)

b=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)

b=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(b)

b=base64.urlsafe_b64decode(b)
print(b)

def safe_base64_decode(s):
    if len(s)%4!=0:
        print(s)
        s+=b'='*(len(s)%4)
        print(s)
    return base64.b64decode(s)
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')