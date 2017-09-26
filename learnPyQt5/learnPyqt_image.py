import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QPalette,QIcon,QBrush

class image(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

    def initUI(self):
        #self.setStyleSheet("QFrame {background-image:url(img.jpg)}")
        #self.square = QFrame(self)
        #self.square.setGeometry(150, 20, 500, 500)
        #self.square.setStyleSheet("QWidget { background-image:url(left.gif) }")

        palenet1=QPalette()
        palenet1.setBrush(self.backgroundRole(),QBrush(QPixmap('image.jpg')))  # 设置背景图片
        self.setPalette(palenet1)
        self.setGeometry(340, 80, 600, 600)
        self.setWindowTitle('实用搜索工具 1.0.0002_alpha测试版')
        self.setWindowIcon(QIcon('util.jpg'))
        self.inputText=QLabel('input')
        self.editline=QLineEdit()

        self.inputLayout=QHBoxLayout()
        self.inputLayout.addWidget(self.inputText)
        self.inputLayout.addWidget(self.editline)
        self.setLayout(self.inputLayout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    i=image()
    i.show()
    sys.exit(app.exec_())