#coding=utf-8
from tkinter import *
#导入tk模块
top = Tk()
#初始化Tk
top.title('定时更换图片')

# 获取屏幕的宽度和高度，并且在高度上考虑到底部的任务栏，为了是弹出的窗口在屏幕中间
screenwidth = top.winfo_screenwidth()
screenheight = top.winfo_screenheight() - 100
top.resizable(False, False)

bm1 = PhotoImage(file='rest.gif')

label = Label(top, image=bm1)
label.bm = bm1
label.configure(image = bm1)

label.pack(fill=X,expand=1)
#top.update_idletasks()
#top.deiconify()    #now window size was calculated
#top.withdraw()     #hide window again
b=Button(top,text='sss')
b.pack()

top.deiconify()
top.mainloop()