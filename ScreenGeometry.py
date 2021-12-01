"""
主屏幕坐标系 创建主屏幕对象
screen = QGuiApplication.primaryScreen().geometry()

控件的尺寸
object.width()
object.height()

控件的位置
object.x()
object.y()

控件的几何尺寸 widget能布局其它控件的区域的大小
object.geometry().width()
object.geometry().height()

控件的几何位置
object.geometry().x()
object.geometry().y()


"""


import sys
from pprint import pprint

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


def ClickedButton():
    pprint('1')
    pprint(f"widget.x()= {widget.x()}")
    pprint('widget.y() = %d' % widget.y())
    pprint('widget.width() ={a}'.format(a=widget.width()))
    pprint('widget.height() ={a}'.format(a=widget.height()))

    pprint('2')
    pprint(f"widget.geometry().x()= {widget.geometry().x()}")
    pprint('widget.geometry().y() = %d' % widget.geometry().y())
    pprint('widget.geometry().width() ={a}'.format(a=widget.geometry().width()))
    pprint('widget.geometry().height() ={a}'.format(a=widget.geometry().height()))

    print('3')
    print(f'button1.x() = {btn.x()}')
    print(f'button1.y() = {btn.y()}')
    print(f'button1.width()) = {btn.width()}')
    print(f'button1.height() = {btn.height()}')

    print('4')
    print(f'button1.geometry().x() = {btn.geometry().x()}')
    print(f'button1.geometry().y() = {btn.y()}')
    print(f'button1.geometry().width()) = {btn.width()}')
    print(f'button1.geometry().height() = {btn.height()}')


app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle('设置屏幕坐标系')
widget.resize(400, 500)
# widget.move(200, 300)
screen = QGuiApplication.primaryScreen().geometry()
screen1 = QGuiApplication.primaryScreen().geometry()
pprint(screen1)
WidgetUiSize = widget.geometry()
NewLeft = screen.width() / 2 - WidgetUiSize.width() / 2
NewRight = screen.height() / 2 - WidgetUiSize.height() / 2
widget.move(int(NewLeft), int(NewRight))


btn = QPushButton(widget)
#button 继承 窗口控件
btn.setText('按钮')
btn.resize(100,50)
btn.clicked.connect(ClickedButton)
# btn.move(int((widget.width()-btn.width())/2), int(widget.height()/2-btn.height()/2))
btn.move(395,200)
widget.show()
sys.exit(app.exec())
