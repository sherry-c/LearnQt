"""
注意设置主窗口位置两种设置方法的区别

1.移动的基准是窗口的左上角
QMainWindow().resize(weigh,height)
QMainWindow().move(x,y)


2.setGeometry设置的位置基准是窗口内可以放控件的区域的左上角（不是以左上方的工具栏的位置）
QMainWindow().setGeometry(x, y, weigh, height)


"""

import time
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6.QtGui import QIcon, QGuiApplication
from multiprocessing import Process, Manager,Lock



class IconForm1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMainWindowUI()

    def initMainWindowUI(self):
        # 设置主窗口大小
        self.resize(400, 500)
        # 设置窗口位置和大小 self.setGeometry(x,y,weigh,height)

        # 主窗口居中
        screen = QGuiApplication.primaryScreen().geometry()
        centerLeft = int((screen.width() - self.width()) / 2)
        centerRight = int((screen.height() - self.height()) / 2)

        self.move(centerLeft, centerRight)
        # 移动的基准是窗口的左上角

        self.setWindowTitle('第一个窗口')

        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)
        print('第一个窗口的位置', self.x(), self.y())


class IconForm2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMainWindowUI()

    def initMainWindowUI(self):
        # 设置主窗口大小
        # self.resize(400, 500)
        # 设置窗口位置和大小 self.setGeometry(x,y,weigh,height)

        # 主窗口居中
        screen = QGuiApplication.primaryScreen().geometry()
        centerLeft = int((screen.width() - self.width()) / 2)
        centerRight = int((screen.height() - self.height()) / 2)

        self.move(centerLeft, centerRight)
        self.setGeometry(568, 182, 400, 500)
        # setGeometry设置的位置基准是窗口内可以放控件的区域的左上角（不是以左上方的工具栏的位置）

        self.setWindowTitle('第二个窗口')

        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)
        print(self.x(), self.y())


def f1():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))
    MainWindow = IconForm1()
    MainWindow.show()
    sys.exit(app.exec())


def f2():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))
    MainWindow = IconForm2()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    p1 = Process(target=f1)
    p1.start()
    # p2 = Process(target=f2)
    # p2.start()

