import struct,io

s=struct.pack('>I',10240099)
print(s)
s=struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')
print(s)

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

print(struct.unpack('<ccIIIIIIHH', bmp_header))

def checkBmp(filename):

    with open(filename,'rb') as op:
        o=op.read(30)
        print(o)
    result=struct.unpack('<ccIIIIIIHH',o)
    if result[0]==b'B' and (result[1]==b'M' or result[1]==b'A'):
        print('the file is bmp file')
        print('widht : %s ,height: %s ,color : %s' , (result[6],result[7],result[9]))
    else:
        print('this file not is bump file')

if __name__ == '__main__':
    path='d:/learn/a.bmp'
    path1 = 'd:/learn/b.png'
    checkBmp(path)
    checkBmp(path1)