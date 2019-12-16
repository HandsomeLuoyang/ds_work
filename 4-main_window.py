from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from 基础类.rescue_point import rescue_point
from main import Ui_Form
import sys


class Main_window(QMainWindow, Ui_Form):
    def __init__(self):

        super(QWidget, self).__init__()

        #救援点初始化
        re_point = []
        r1 = rescue_point(name="渝北救援点",point='106.738211,29.840777')
        r2 = rescue_point(name="北碚救援点", point='106.351097,29.75598')
        r3 = rescue_point(name="南岸救援点", point='106.711726,29.498983')
        r4 = rescue_point(name="九龙坡救援点", point='106.288054,29.536045')
        r5 = rescue_point(name="沙坪坝救援点", point='106.444183,29.53087')
        r6 = rescue_point(name="巴南救援点", point='106.586582,29.352452')
        r7 = rescue_point(name="大渡口救援点", point='106.478209,29.481837')
        r8 = rescue_point(name="江津救援点", point='106.456811,29.258333')
        re_point.append(r1)
        re_point.append(r2)
        re_point.append(r3)
        re_point.append(r4)
        re_point.append(r5)
        re_point.append(r6)
        re_point.append(r7)
        re_point.append(r8)



        self.setupUi(self)

        self.show()



def main():
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
