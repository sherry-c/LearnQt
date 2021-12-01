# QGuiApplication
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
import sys
from PyQt6.QtGui import QIcon, QGuiApplication
import time


# app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))
# 设置窗口图标

# QApplication 主要是做一些窗口控制相关的操作

# QMainWindow 主要是布置窗口的ui界面设计
# QMainWindow 可以在主窗口是创建：菜单栏、工具栏、状态栏、标题栏


class CenterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('第一个窗口')
        self.resize(640, 480)

        # 设置主窗口的状态栏消息
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)

        self.button1 = QPushButton('exit')

        # 将信号/signal和槽/slot相关联
        self.button1.clicked.connect(self.onClickButton)

        # 创建一个水平布局，将按钮添加上去
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        MainFram = QWidget()
        MainFram.setLayout(layout)

        self.setCentralWidget(MainFram)

    # 自定义的槽/slot
    # @staticmethod
    def onClickButton(self):
        print(self.button1.text())
        self.close()

    # 将主窗口移动到屏幕的中间
    def center(self):
        # 获取屏幕尺寸

        screen = QGuiApplication.primaryScreen().geometry()

        # 获取主窗口的尺寸
        MainUiSize = self.geometry()

        NewLeft = screen.width() / 2 - MainUiSize.width() / 2
        NewRight = screen.height() / 2 - MainUiSize.height() / 2

        self.move(int(NewLeft), int(NewRight))
        # print(screen.width(), screen.height())
        # print(self.geometry().width(), self.geometry().height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))
    MainUi = CenterForm()
    MainUi.show()
    MainUi.center()
    sys.exit(app.exec())
