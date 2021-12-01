import sys

from PySide6.QtCore import QDateTime, QTimer
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QGridLayout


class LearnQThread(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Learn QThread')
        self.resize(640, 480)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.btnStart = QPushButton('start')
        self.btnEnd = QPushButton('end')
        layout = QGridLayout()
        self.timer = QTimer()

        self.timer.timeout.connect(self.showtime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 0)
        layout.addWidget(self.btnEnd, 1, 1)

        self.btnStart.clicked.connect(self.StartTimer)
        self.btnEnd.clicked.connect(self.endTimer)
        self.setLayout(layout)

    """
    
    QTimer定时处理的任务
    
    """

    def showtime(self):
        # 获取当前时间
        time = QDateTime.currentDateTime()
        # 将当前时间转换成字符串类型
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')

        self.label.setText(timeDisplay)

    def StartTimer(self):
        # 开启定时器,执行时间/任务的频率是100ms
        self.timer.start(100)
        self.btnStart.setEnabled(False)
        self.btnEnd.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.label.clear()
        self.btnStart.setEnabled(True)
        self.btnEnd.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = LearnQThread()
    wid.show()
    sys.exit(app.exec())
