# -*- coding: utf-8 -*-

"""
Module implementing Web2PyQt5.
"""
import sys
from PyQt5.QtCore import pyqtSlot, Qt, QUrl, QFileInfo
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from Ui_main import Ui_Form
from shared import Myshared

class Web2PyQt5(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Web2PyQt5, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 7)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        vLayout = QVBoxLayout()
        vLayout.setContentsMargins(0, 0, -1, -1)
        url = QUrl(QFileInfo("./webchannel.html").absoluteFilePath())
        self.view = QWebEngineView(self.widget)
        vLayout.addWidget(self.view)
        self.widget.setLayout(vLayout)
        self.view.load(url)

    @pyqtSlot()
    def on_pb_submit_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.lineEdit_username.text() == "":
            QMessageBox.warning(self, "警告", "用户名没有输入")
            self.lineEdit_username.setFocus()
        elif self.lineEdit_pwd.text() == "":
            QMessageBox.warning(self, "警告", "密码没有输入")
            self.lineEdit_pwd.setFocus()
        else:
            name = self.lineEdit_username.text()
            pwd = self.lineEdit_pwd.text()
            jscode = "PyQt52WebValue('{}','{}');".format(name, pwd)
            self.view.page().runJavaScript(jscode)

    @pyqtSlot()
    def on_pb_reset_clicked(self):
        """
        PyQt5的输入栏内容清空
        """
        self.lineEdit_username.setText("")
        self.lineEdit_pwd.setText("")

    def setLineEdit(self, list):
        self.lineEdit_username.setText(list[0])
        self.lineEdit_pwd.setText(list[1])

    def __del__(self):
        self.view.deleteLater()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    web_pyqt = Web2PyQt5()
    web_pyqt.show()
    channel = QWebChannel()
    shared = Myshared()
    channel.registerObject("connection", shared)
    web_pyqt.view.page().setWebChannel(channel)
    shared.finish[list].connect(web_pyqt.setLineEdit)
    sys.exit(app.exec_())