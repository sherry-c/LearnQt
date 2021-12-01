import sys
import time

from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QGuiApplication, QIcon, QPalette, QColor, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGroupBox, QFileDialog
import image_rc


class LearnQLabel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.groupBox = QGroupBox(self.centralwidget)

        self.pushButton = QPushButton(self.centralwidget)
        self.UiInit()

    def UiInit(self):
        self.resize(640, 480)
        self.centralwidget.resize(700, 800)

        self.pushButton.setGeometry(QRect(1, 1, 100, 50))
        # QRect(x坐标,y坐标，按钮宽度,按钮高度)

        # 设置
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(10)
        font1.setItalic(False)

        self.pushButton.setFont(font1)

        # clicked（bool）只是当按钮的setCheckable()设置为True时才有可能使得status为True
        # （即设置后按钮想点灯开关一样，能够按一下保持一直开，再按下保持一直关），否则开关点击一下后仍为关闭状态，status一直为False
        self.pushButton.setCheckable(False)

        # 设置字体颜色
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, QColor(Qt.black))
        self.pushButton.setPalette(palette)

        # 设置按钮的文本/
        self.pushButton.setText('按钮设置')
        # 设置按钮的图标
        # self.pushButton.setIcon(QIcon(r'C:\Users\15516\Desktop\testui\a.png'))

        # 按钮--->连接信号和槽
        self.pushButton.clicked.connect(self.onClickButton)

        # self.pushButton.setStyleSheet(u"background-image: url(:/image/a.png);")

        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(200, 200, 201, 191))
        self.groupBox.setStyleSheet(u"background-image: url(:/image/a.png);")

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Learn QPushbutton")

        self.Center()

    def onClickButton(self):
        print('按钮被按下')
        # dir = QFileDialog.getExistingDirectory()
        # dir = QFileDialog.getOpenFileName(
        #     self.centralwidget,  # 父窗口对象
        #     "选择你要上传的图片",  # 标题
        #     r"C:\Users\15516\Desktop\testui",  # 起始目录
        #     "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        # )
        # print(dir[0])
        # time.sleep(2)

        dir2 = QFileDialog.getSaveFileName(
            self.centralwidget,  # 父窗口对象
            "保存文件",  # 标题
            r"C:\Users\15516\Desktop\testui",  # 起始目录
            "json类型 (*.txt)"  # 选择类型过滤项，过滤内容在括号中
        )
        f = open(dir2[0], 'a', encoding='utf8')
        f.write('aaaaaa')
        f.close()
        print(dir2)

        # filePaths, _ = QFileDialog.getOpenFileNames(
        #     self.centralwidget,  # 父窗口对象
        #     "选择你要上传的图片",  # 标题
        #     r"d:\\data",  # 起始目录
        #     "图片类型 (*.png *.jpg *.bmp)"  # 选择类型过滤项，过滤内容在括号中
        # )
        # print(filePaths)

    def Center(self):
        # 获取屏幕尺寸坐标
        screen = QGuiApplication.primaryScreen().geometry()

        # 获取主窗口坐标
        size = self.geometry()

        Left = (screen.width() - size.width()) / 2
        Right = (screen.height() - size.height()) / 2

        # 将主窗口移动到中心位置
        self.move(Left, Right)


def myfun():
    app = QApplication()

    icon = QIcon(r'box-color.ico')
    # 设置主窗口的图标
    app.setWindowIcon(icon)

    MainWindow = LearnQLabel()

    MainWindow.show()
    while app.exec():
        pass
    # sys.exit(app.exec())


if __name__ == '__main__':
    myfun()
