from login import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QMouseEvent, QPixmap
from PyQt5 import Qt
import sys
from Crypto.Cipher import AES
from main_window import Main_window
from 功能.jiami import PrpCrypt


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

        with open("account.txt", "r") as rf:
            account_list = rf.readlines()
        user_index = -1
        for i in range(0, len(account_list), 2):
            if userName == account_list[i][9:].rstrip():
                user_index = i
                break
        if user_index == -1:
            QMessageBox.warning(self.qwidget, "提示", "账户名或密码错误！")
            self.Password.setText("")
            return False
        real_pwd = account_list[user_index+1][9:].rstrip()
        pc = PrpCrypt()
        pwd = pc.encrypt(passWord).decode("utf-8")
        if real_pwd != pwd:
            QMessageBox.warning(self.qwidget, "提示", "账户名或密码错误！")
            self.Password.setText("")
            return False

        self.main_window = Main_window()
        self.main_window.show()
        self.qwidget.hide()


def main():
    app = QApplication(sys.argv)

    w = Main()
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
