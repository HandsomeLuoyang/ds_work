from login import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QMouseEvent, QPixmap
from PyQt5 import Qt
import sys
from Crypto.Cipher import AES


class Main(Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        self.qwidget = QWidget()
        self.setupUi(self.qwidget)
        self.qwidget.setWindowTitle("欢迎")
        self.Button_login.clicked.connect(self.login)

    def show(self):
        self.qwidget.show()

    def login(self):
        userName = self.Username.text()
        passWord = self.Password.text()
        if not userName or not passWord:
            QMessageBox.warning(self.qwidget, "温馨提示！", "请输入账户名和密码！")
            self.Username.setFocus()
            return
        else:
            main_window.main()


def main():
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
