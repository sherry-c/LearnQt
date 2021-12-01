"""
P105 信号与槽的基础  button被点击，链接到相应的槽函数



"""

from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton
from PySide6.QtCore import QRect
import sys
import image_rc


class LearnSignalSlot(QWidget):
    def __init__(self, parent=None):
        super(LearnSignalSlot, self).__init__(parent)
        self.btn1 = QPushButton('anni', self)
        self.initUI()

    def initUI(self):
        self.resize(640, 480)
        groupbox = QGroupBox(self)
        groupbox.setGeometry(QRect(1, 1, 200, 200))
        groupbox.setStyleSheet(u"background-image: url(:/image/a.png);")
        self.btn1.move(300, 300)
        self.btn1.clicked.connect(self.OnClicked)

    def OnClicked(self):
        self.btn1.setText('aaa')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = LearnSignalSlot()
    widget.show()
    while app.exec():
        pass
