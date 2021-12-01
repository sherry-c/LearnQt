"""
使用QtDesigner设计Ui并且生成py程序，主程序的逻辑写法，
1.创建窗口控制基类
    app = QApplication(sys.argv)
2.创建主窗口
    MainWindow = QMainWindow()
3.创建QtDesigner设计出来的Ui类，将Ui类设置到主窗口当中
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
4.显示主窗口
    MainWindow.show()
5.设置系统结束
    sys.exit(app.exec())

"""

from PySide6.QtWidgets import QApplication,QMainWindow
import test
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


