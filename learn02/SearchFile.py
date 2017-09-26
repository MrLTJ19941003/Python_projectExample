
import os,threading,datetime,multiprocessing

class searchFile(object):
    def __init__(self,path='.'):
        self.T = []
        self.L=[]
        self._path=path
        self.abspath=os.path.abspath(self._path)

    def findfile(self,filename,root=''):
        if root=='':
            root=self.abspath
        dirs=os.listdir(root)
        index=0
        for x in range(len(dirs)//4):
            #print(dirs[index:index+4])
            p = multiprocessing.Process(target=self.poolfind,args=(filename,root,dirs[index:index+4]))
            p.start()
            #p.apply_async(self.poolfind,args=(self,filename,root,dirs[index:index+4]))
            index=index+4
            p.join()
       # return 'can not %s filenam  e on file' % filename

    def poolfind(self,filename,root,dirs=''):
        if dirs=='':
            dirs = os.listdir(root)

        for d in dirs:
            try:
                # print(os.path.join(root,d))
                data = os.path.join(root, d)
                if os.path.isfile(data):
                    # print('this is file %s' % d)
                    if d.find(filename) != -1:
                        self.L.append(data)
                        # yield os.path.join(root,d)
                        print('%s ' % data)
                if os.path.isdir(data):
                    # print('this is dir %s ' % d)
                    # root=os.path.join(root,d)
                    # print('this is root %s ' % root)
                    #self.p.apply_async(self.findfile, args=(filename, data))
                    t=threading.Thread(target=self.findfile,args=(filename,data))
                    t.start()
                    self.T.append(t)
                    #self.poolfind(filename,data)
            except:
                continue

    def __call__(self):
        while True:
            name = input("please the keyword you want to find:")
            self.L.clear()
            if name=='':
                break
            now=datetime.datetime.now().timestamp();
            self.findfile(name)

            #for t in self.threads:
                #t.join()
            endnow=datetime.datetime.now().timestamp();
            print('datatime has ', endnow-now)
            if self.L:
                for i in self.L:
                    #print(i)
                    pass
            else:
                print(' %s file not found ' % name)

if __name__ == '__main__':
    search=searchFile('f:/')
    search()
