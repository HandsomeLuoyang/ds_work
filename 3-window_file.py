from login import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QMouseEvent, QPixmap
import sys


class Main(Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        self.qwidget = QWidget()
        self.setupUi(self.qwidget)
        self.qwidget.setWindowTitle("欢迎")

    def show(self):
        self.qwidget.show()


# class Wind(QWidget, Ui_Form):
#     def __init__(self):
#         QWidget.__init__(self)
#         Ui_Form.__init__(self)
#         # super(Wind, self).__init__()  # 这个初始化有问题
#         self.setupUi(self)
#         # self.setWindowFlag(Qt.Qt.FramelessWindowHint)


def main():
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
