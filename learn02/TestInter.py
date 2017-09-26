from multiprocessing import Pool
import os,time,threading

def getFile(path,filename) :
  #获取目录下的文件list
  fileList = []
  for root, dirs, files in list(os.walk(path)) :
    for i in files :
      if i.find(filename)!=-1:
        print(root + "\\" + i)
        #fileList.append(root + "\\" + i)
  return fileList

def init_params(path,filename):
  dirs = os.listdir(path)
  listpath = []
  for x in dirs:
    listpath.append(os.path.join(path, x))
  print(listpath)
  now=time.time()
  #p=Pool()
  T=[]
  for x in range(len(listpath)):
    t=threading.Thread(target=getFile,args=(listpath[x],filename))
    t.start()
    T.append(t)
  for x in T:
    x.join()
    #re = p.apply_async(getFile,args=(listpath[x],filiname))
  #p.close()
  #p.join()
  #print(re)
  endnow=time.time()
  print(endnow-now)
