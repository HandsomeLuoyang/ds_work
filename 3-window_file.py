from login import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QMouseEvent, QPixmap
from PyQt5 import Qt
import sys


class Main(Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        self.qwidget = QWidget()
        self.setupUi(self.qwidget)
        self.qwidget.setWindowTitle("欢迎")

    def show(self):
        self.qwidget.show()


def main():
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
