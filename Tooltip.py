from PyQt6.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton, QLineEdit, QWidget
import sys
from PyQt6.QtGui import QIcon, QFont,QGuiApplication


class TooltipMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.center()

    def initUI(self):
        self.resize(640, 480)

        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是星期五')
        self.setWindowTitle('第一个窗口')

        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)

        # 创建一个按钮，创建一个窗口
        self.button1 = QPushButton(self)
        self.button1.setText('calculate')
        self.button1.move(200, 300)
        self.button1.setToolTip('计算结果')

        self.line1 = QLineEdit(self)
        self.line1.move(100, 100)
    def center(self):
        screen = QGuiApplication.primaryScreen().geometry()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\15516\Desktop\testui/box-color.ico'))

    MainUi = TooltipMainWin()

    MainUi.show()
    sys.exit(app.exec())
