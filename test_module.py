# from GPCAlgo.CAlgoAAMeasurement import CAlgoAAMeasurement
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, \
    QLCDNumber, QMessageBox, QFileDialog, QLabel, QGridLayout, QTabWidget,QHBoxLayout
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import Signal, QObject, QThread, QDateTime
import time
# from calculate_depth import *


class BackendThread(QThread):
    update_date = Signal(str)

    def run(self):
        while True:
            pass


class WorkThread(QThread):
    timer = Signal()  # 每隔1秒发送一次信号
    end = Signal()  # 计数完成后发送信号

    def run(self):
        while True:
            pass


class ThreadUpdateUI(QTabWidget):

    def __init__(self):
        super().__init__()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabdesk = QWidget()

        self.addTab(self.tabdesk, "desk")

        self.desk_pic = QLabel(self.tabdesk)
        self.desk_pic.setPixmap(QPixmap(r't1.png'))
        self.desk_pic.move((self.tabdesk.width()-self.desk_pic.width())/2,(self.tabdesk.height()-self.desk_pic.height())/2)
        # self.layout3 = QHBoxLayout()
        # self.layout3.addWidget(self.desk_pic)
        # self.tabdesk.setLayout(self.layout3)

        self.addTab(self.tab1, 'tab1:手动调焦上位机')

        self.layout1 = QGridLayout(self.tab1)
        self.layout2 = QGridLayout(self.tab2)

        self.input1 = QLineEdit(self.tab1)
        self.input2 = QLineEdit(self.tab2)

        self.btn1 = QPushButton("关闭程序 1", self.tab1)
        self.btn2 = QPushButton("打开文件 2", self.tab1)

        self.label1 = QLabel(self.tab1)
        self.label2 = QLabel(self.tab1)
        self.label3 = QLabel(self.tab1)
        self.label4 = QLabel(self.tab1)
        self.label5 = QLabel(self.tab1)

        self.addTab(self.tab2, 'tab2:计算距离标定')
        self.backend = BackendThread()
        self.workThread = WorkThread()

        self.btn3 = QPushButton("关闭程序 3", self.tab2)
        self.btn4 = QPushButton("打开文件 4", self.tab2)

        self.initUI()

    def initUI(self):
        self.resize(1000, 700)
        self.setWindowTitle("测试上位机")

        # self.label1.resize(320, 240)
        # self.pic = QPixmap(r'D:\testsdk\AA_measurement\result_AA_measurement\1111_C.png')
        # self.label1.setPixmap(self.pic.scaled(320, 240))

        self.label1.setPixmap(QPixmap(r'D:\testsdk\AA_measurement\result_AA_measurement\1111_C.png').scaled(320, 240))
        self.label2.setPixmap(QPixmap(r'D:\testsdk\AA_measurement\result_AA_measurement\1111_DL.png').scaled(320, 240))
        self.label3.setPixmap(QPixmap(r'D:\testsdk\AA_measurement\result_AA_measurement\1111_DR.png').scaled(320, 240))
        self.label4.setPixmap(QPixmap(r'D:\testsdk\AA_measurement\result_AA_measurement\1111_UL.png').scaled(320, 240))
        self.label5.setPixmap(QPixmap(r'D:\testsdk\AA_measurement\result_AA_measurement\1111_UR.png').scaled(320, 240))

        self.layout1.addWidget(self.btn1, 0, 3)
        self.layout1.addWidget(self.btn2, 1, 3)
        self.layout1.addWidget(self.input1, 2, 3)

        self.layout1.addWidget(self.label1, 0, 0)
        self.layout1.addWidget(self.label2, 0, 2)
        self.layout1.addWidget(self.label3, 1, 1)
        self.layout1.addWidget(self.label4, 2, 0)
        self.layout1.addWidget(self.label5, 2, 2)

        self.btn1.clicked.connect(self.btnClicked)
        self.btn2.clicked.connect(self.openfile1)

        self.layout2.addWidget(self.btn3, 0, 3)
        self.layout2.addWidget(self.btn4, 1, 3)
        self.layout2.addWidget(self.input2, 1, 2)
        self.btn3.clicked.connect(self.btnClicked)
        self.btn4.clicked.connect(self.btn4Clicked)

    def btn4Clicked(self):
        path = QFileDialog.getExistingDirectory()
        print(path)
        pic_dirs_path = path
        depth_calibration_result_path = r'C:\Users\user\Desktop\temp\depth_calibration_result.txt'
        print('正在计算************')
        cal_depth_result(pic_dirs_path, depth_calibration_result_path)
        print('计算完成*********************')
        self.input2.setText('计算完成')

    def btnClicked(self):
        self.close()

    def openfile1(self):
        print('path')
        path = QFileDialog.getExistingDirectory()
        self.input1.setText(path)


if __name__ == '__main__':
    app = QApplication([])
    MainWindow = ThreadUpdateUI()
    app.setWindowIcon(QIcon(r'box-color.ico'))
    MainWindow.show()

    # 调焦算法接口
    # config_file_folder = "AA_measurement_calgo_config.json"
    # result = {}
    # a = CAlgoAAMeasurement(config_file_folder, result)
    #
    # data_result_folder = r"D:\testsdk\AA_measurement"
    # result = a.is_success(data_result_folder)
    # print(result)

    while app.exec():
        pass
