import sys,os
from concurrent.futures import ThreadPoolExecutor,wait,as_completed
from queue import Queue
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QPalette,QIcon,QBrush,QColor,QFont
from  PyQt5 import QtGui,QtCore
import multiprocessing,time,threading
queue = Queue(10)#声明队列
class searchFiles(object):
    def run(path,filename):
        # 获取目录下的文件list
        for root, dirs, files in list(os.walk(path)):
            for i in files:
                if i.find(filename) != -1:
                    #print(root + "\\" + i)
                    queue.put(root + "\\" + i)  # 将数据放入队列中，这样其他线程就可以随机取出
class util(object):
    def getWindowDrive():
        L = []
        for i in range(65, 91):
            vol = chr(i) + ':'
            if os.path.isdir(vol):
                L.append(vol + '\\')
        return L
    # 打开文件夹路径
    def onOpen(self):
        pass
class searchPyQt(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.pool=True
        self.initWindowsize()
        self.initsearchImage()
        self.initsearchInput()
        self.initsearchResult()
        self.inituUI()
    def initWindowsize(self):
        palenet1 = QPalette()
        palenet1.setBrush(self.backgroundRole(), QColor(240,255,255))#设置背景颜色 #QBrush(QPixmap('image.jpg')))  # 设置背景图片
        self.setPalette(palenet1)
        self.setGeometry(340, 120, 600, 400)
        self.setWindowTitle('实用搜索工具 1.0.0002_alpha测试版')
        self.setWindowIcon(QIcon('image/util.jpg'))
    def initsearchImage(self):
        exitAction = QAction(QIcon('image/exit.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+N')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(self.exit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&tools')
        fileMenu.addAction(exitAction)
    def initsearchInput(self):
        self.inputLabel = QLabel('请输入要搜索的文件名:')
        self.combo = QComboBox(self)
        DriveList=util.getWindowDrive()
        for drive in DriveList:
            self.combo.addItem(drive)
        self.editLine = QLineEdit()
        self.printButton = QPushButton('search')
        self.printButton.setShortcut('Ctrl+Enter')
        self.printButton.clicked.connect(self.search)
    def initsearchResult(self):
        self.table = QListWidget()
        self.table.setSortingEnabled(1)
        self.table.itemClicked.connect(self.initMenu)
        # 把列表项添加到listwidget中
        #for i in range(100):
            #self.table.insertItem(i, str(i))
    def initMenu(self,obj):
        self.selectText=obj.text()
        rightMenu = QMenu(self.table)
        removeAction = QAction(QIcon('image/openfile.jpg'),u"open", self, triggered=self.openfile)
        rightMenu.addAction(removeAction)
        removeAction = QAction(QIcon('image/copy.ico'),u"copy", self, triggered=self.copyfilepath)
        rightMenu.addAction(removeAction)
        rightMenu.exec_(QtGui.QCursor.pos())
    ##### 打开文件
    def openfile(self):
        print()
        os.system('explorer.exe %s' % self.selectText)
    def copyfilepath(self):####复制
        #print('copyfilepath')
        clipboard = QApplication.clipboard()
        clipboard.setText(self.selectText)
    def inituUI(self):
        centerWindow = QWidget()
        self.setCentralWidget(centerWindow)
        inputLayout=QHBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.combo)
        inputLayout.addWidget(self.editLine)
        inputLayout.addWidget(self.printButton)
        tableLayout=QHBoxLayout()
        tableLayout.addWidget(self.table)
        self.searchResultName=QLabel()
        labelLayout = QHBoxLayout()
        labelLayout.addWidget(self.searchResultName)
        mainLayout=QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(tableLayout)
        mainLayout.addLayout(labelLayout)
        centerWindow.setLayout(mainLayout)
        centerWindow.show()
    def search(self):
        try:
            self.table.clear()
            self.searchResultName.setText('<font color=red>搜索中...</font>')
            filepath=self.combo.currentText()
            filename=self.editLine.text()
            t=threading.Thread(target=self.poolT, args=(filepath, filename))
            t.setDaemon(True)
            t.start()
            queueT=threading.Thread(target=self.getData,args=())
            queueT.setDaemon(True)
            queueT.start()
        except:
            print('error')
    def getData(self):
        while True:
            data=queue.get()
            print(data)
            self.table.addItem(data)
    def poolT(self,filepath,filename):
        now = time.time()
        dirs = os.listdir(filepath)
        listpath = []
        for x in dirs:
            listpath.append(os.path.join(filepath, x))
        print(len(listpath))
        with ThreadPoolExecutor(25) as executor:
            self.pool = False
            futures = [executor.submit(searchFiles.run, path, filename) for path in listpath]
            #futures.add_done_callback(self.exit())
        wait(futures)
        self.searchResultName.setText('<font color=red>搜索完毕</font>')
        self.pool = True
        end = time.time() - now
        print(end)

    def exit(self):
        if self.pool:
            qApp.quit()
        else:
            QMessageBox.information(self, "Information",self.tr("正在搜索中...请稍后关闭程序!"))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    search=searchPyQt()
    search.show()
    sys.exit(app.exec_())