from tkinter import *
from queue import Queue
from PIL import Image, ImageTk
from multiprocessing import Pool
import tkinter.messagebox as messagebox
import os,time,threading,ctypes,inspect

queue = Queue(10)#声明队列
T = []
#按钮点击功能提供类
class session:
    def getFile(path, filename):
        # 获取目录下的文件list
        for root, dirs, files in list(os.walk(path)):
            for i in files:
                if i.find(filename) != -1:
                    print(root + "\\" + i)
                    queue.put(root + "\\" + i)#将数据放入队列中，这样其他线程就可以随机取出
    #搜索
    def sarech(path=''):
        global T
        listbox.delete(0,listbox.size())
        filename=entry.get()
        path=variable.get()
        try:
            dirs = os.listdir(path)
            listpath = []
            for x in dirs:
                listpath.append(os.path.join(path, x))
            print(listpath)
            now = time.time()
            #p=Pool()
            for x in range(len(listpath)):
                t = threading.Thread(target=session.getFile, args=(listpath[x], filename))
                t.setDaemon(True)
                t.start()
                T.append(t)
            tGet=threading.Thread(target=session.setListBox,args=())
            tGet.setDaemon(True)
            tGet.start()

            endnow = time.time()
            print(endnow - now)
        except:
            print('error')
    #从队列中读书数据插入列表项中
    def setListBox():
        while True:
            result=queue.get()
            listbox.insert(END, result)
    #根据文件夹路径打开文件
    def openfile(path=''):
        if path=='':
            pass
        os.system(path)
    #
    def getWin():
        L=[]
        for i in range(65, 91):
            vol = chr(i) + ':'
            if os.path.isdir(vol):
                L.append(vol+'\\')
        return L
    #打开文件
    def messageList(event):
        os.system('explorer.exe %s' % listbox.get(listbox.curselection()))
    #复制
    def onCopy():
        text = listbox.get(listbox.curselection())
        root.clipboard_append(text)
    #打开文件夹路径
    def onOpen():
        os.system('explorer.exe %s' % os.path.split(listbox.get(listbox.curselection()))[0])

    def quits():
        root.quit()

#创建一个窗口
root = Tk()
root.title('实用搜索工具 1.0.0001_alpha测试版')#设置窗口标题
#root.resizable(False,False)#设置窗口不能放大及缩放
root.geometry('660x450+320+60')#设置窗口的大小及显示位置

canvas = Canvas(root,
                        width=660,  # 指定Canvas组件的宽度
                        height=30,  # 指定Canvas组件的高度
                        bg='white')  # 指定Canvas组件的背景色
# im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片
image = Image.open("img.jpg")
im = ImageTk.PhotoImage(image)

canvas.create_image(300, 50, image=im)  # 使用create_image将图片添加到Canvas组件中
canvas.create_text(312, 15,  # 使用create_text方法在坐标（302，77）处绘制文字
                   text='请输入搜索内容'  # 所绘制文字的内容
                   , fill='gray')  # 所绘制文字的颜色为灰色
canvas.create_text(310, 13,
                   text='请输入搜索内容',
                   fill='blue')
canvas.pack()  # 将Canvas添加到主窗口
#下拉选择按钮
variable = StringVar(root)
win=session.getWin()
variable.set(win[0])
w = OptionMenu(root, variable ,win[0],win[1],win[2],win[3])
w.pack()
#文本输入框
show=StringVar()
entry = Entry(root, textvariable=show, width='30')
entry.pack()
#搜索按钮
Button(root, text='search',command=session.sarech).pack(pady='9')
#滚动条
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
#查询结果显示框
listbox =Listbox(root,yscrollcommand=scrollbar.set,width='92',height='10')
#给列表框添加值（测试用）
#for i in range(200):
    #listbox.insert(END, [str(i),str(i)])
#显示列表框，并设置列表框的属性信息
listbox.pack(side=LEFT, fill='both',pady='9')
#将滚动条绑定至列表框（listbox）
scrollbar.config(command=listbox.yview)
listbox.bind('<Double-Button-1>',session.messageList)
#列表项的右键菜单
menu = Menu(root, tearoff=0)
menu.add_command(label="复制", command=session.onCopy)
menu.add_separator()
menu.add_command(label="打开文件所在目录", command=session.onOpen)
def popupmenu(event):
    if listbox.get(0)=='':
        messagebox.showinfo('Message', '当前列表为空！')
        return
    try:
        if tuple(listbox.curselection())[0]>=0:
            menu.post(event.x_root, event.y_root)
    except:
        messagebox.showinfo('Message', '需要选中列表中的值！')
listbox.bind("<Button-3>", popupmenu)
#退出按钮
menubar = Menu(root)
menubar.add_command(label="退出", command=session.quits)
menubar.add_separator()
root.config(menu=menubar)
#整个窗口显示
root.mainloop()