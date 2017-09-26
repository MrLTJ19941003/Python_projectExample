import os,time,asyncio

NUMBERS=range(22)
paths='f:\\{}'

async def aa(path,filename='SVN'):
    pass


async def getFile(path,filename='SVN') :
    #获取目录下的文件list
    fileList = []
    for root, dirs, files in list(os.walk(paths.format(path))):
        # print('root {}'.format(root))
        for i in files:
            if i.find(filename) != -1:
                print(root + "\\\\" + i)
                # fileList.append(root + "\\" + i)
    return fileList
listfile=os.listdir('f:/')
print(listfile)
now=time.time()
loop=asyncio.get_event_loop()
tasks = [getFile(listfile[num],'SVN') for num in NUMBERS]
loop.run_until_complete(asyncio.gather(*tasks))
endnow=time.time()
print(endnow-now)