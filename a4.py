from PyQt6.QtWidgets import QApplication, QMainWindow,QLabel
import sys
from PyQt6.QtGui import QIcon, QFont, QGuiApplication,QPalette
from PyQt6.QtCore import Qt



class LearnQLabel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.center()

    def initUI(self):
        self.resize(640, 480)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color = yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.window,Qt.blue)

    def center(self):
        # 获取屏幕尺寸
        screen = QGuiApplication.primaryScreen().geometry()

        # 获取主窗口的尺寸
        MainUiSize = self.geometry()

        NewLeft = screen.width() / 2 - MainUiSize.width() / 2
        NewRight = screen.height() / 2 - MainUiSize.height() / 2

        self.move(int(NewLeft), int(NewRight))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))

    MainUi = LearnQLabel()

    MainUi.show()
    sys.exit(app.exec())
