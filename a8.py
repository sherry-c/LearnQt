#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2021/12/3 9:54
import sys
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLCDNumber, QPushButton, QMessageBox

sec = 0


class WorkThread(QThread):
    timer = Signal()
    end1 = Signal()

    def run(self):
        while True:
            self.sleep(1)
            self.timer.emit()
            if sec == 5:
                self.end1.emit()


class LearnQThred(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240)
        self.btn = QPushButton('open')
        self.btn1 = QPushButton('close thread')
        self.label = QLabel(self)

        self.lcdnum = QLCDNumber(self)
        layout = QGridLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lcdnum)
        layout.addWidget(self.btn)
        layout.addWidget(self.btn1)

        self.setLayout(layout)
        self.label.setAlignment(Qt.AlignCenter)
        self.work = WorkThread()
        self.btn.clicked.connect(self.Work)
        self.btn1.clicked.connect(self.EndThred)
        self.work.timer.connect(self.countTime)
        self.work.end1.connect(self.end)

    def EndThred(self):
        self.work.terminate()

    def countTime(self):
        global sec
        sec += 1
        self.label.setText(str(sec))
        self.lcdnum.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    def Work(self):
        self.work.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = LearnQThred()
    wid.show()
    sys.exit(app.exec())