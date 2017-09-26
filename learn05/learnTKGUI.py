from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel=Label(self,text='hello,word！')
        self.helloLabel.pack()
        self.helloInput=Entry(self)
        self.helloInput.pack()
        self.helloButton=Button(self,text='Quit;',command=self.hello)
        self.helloButton.pack()

    def hello(self):
        name=self.helloInput.get() or 'world'
        messagebox.showinfo('Message','hello , %s'% name)

app=Application()
app.master.title('hello,word!')
app.mainloop()