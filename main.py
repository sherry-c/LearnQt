from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from PySide6.QtGui import QIcon


# QApplication 主要是做一些窗口控制相关的操作
# QMainWindow 主要是布置窗口的ui界面设计

# QMainWindow 可以在主窗口是创建：菜单栏、工具栏、状态栏、标题栏

# QWidget
# Dialog


class FirstMainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('第一个窗口')
        self.resize(640, 480)

        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))

    MainUi = FirstMainWin()

    MainUi.show()
    sys.exit(app.exec())
