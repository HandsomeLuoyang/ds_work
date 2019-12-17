# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


import ds_work_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1071, 543)
        Form.setStyleSheet(
            "#Form\n" "{\n" "    background-image: url(:/frame_bgimg.jpg);\n" "}\n" ""
        )
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(370, 50, 351, 401))
        self.frame.setStyleSheet(
            "#frame\n"
            "{\n"
            "    background-color:rgba(255,255,255,0.15);\n"
            "    border-radius:20px;\n"
            "    border:3px solid black;\n"
            "}\n"
            "#frame:hover\n"
            "{\n"
            "    background-color:rgba(255,255,255,0.3);\n"
            "    border:2px solid black;\n"
            "}"
        )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Login_font = QtWidgets.QLabel(self.frame)
        self.Login_font.setGeometry(QtCore.QRect(80, 0, 201, 101))
        self.Login_font.setText("")
        self.Login_font.setPixmap(QtGui.QPixmap(":/login_font.png"))
        self.Login_font.setObjectName("Login_font")
        self.Username = QtWidgets.QLineEdit(self.frame)
        self.Username.setGeometry(QtCore.QRect(30, 140, 291, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.Username.setFont(font)
        self.Username.setStyleSheet(
            "#Username\n"
            "{\n"
            "    background-color:rgba(255,255,255,0.4);\n"
            "    border-radius:10px;\n"
            "    border:2px solid black;\n"
            "}\n"
            "#Username:hover\n"
            "{\n"
            "    background-color:rgba(255,255,255,0.6);\n"
            "    border:1px solid black;\n"
            "}"
        )
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.frame)
        self.Password.setGeometry(QtCore.QRect(30, 230, 291, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setStyleSheet(
            "#Password\n"
            "{\n"
            "    background-color:rgba(255,255,255,0.4);\n"
            "    border-radius:10px;\n"
            "    border:2px solid black;\n"
            "}\n"
            "#Password:hover\n"
            "{\n"
            "    background-color:rgba(255,255,255,0.6);\n"
            "    border:1px solid black;\n"
            "}"
        )
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Button_login = QtWidgets.QPushButton(self.frame)
        self.Button_login.setGeometry(QtCore.QRect(30, 310, 291, 51))
        self.Button_login.setStyleSheet(
            "#Button_login\n"
            "{\n"
            "    border-radius:16px;\n"
            "    background-color:#134857;\n"
            "    font-size:18px;\n"
            "    font-family:Microsoft Yahei;\n"
            "    color:white;\n"
            "}\n"
            "#Button_login:hover\n"
            "{\n"
            "    background-color:#145060;\n"
            "}\n"
            "#Button_login:pressed\n"
            "{\n"
            "    background-color:#175565;\n"
            "    padding-left:3px;\n"
            "    padding-top:3px;\n"
            "}"
        )
        self.Button_login.setObjectName("Button_login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Username.setPlaceholderText(_translate("Form", "Username:"))
        self.Password.setPlaceholderText(_translate("Form", "Password:"))
        self.Button_login.setText(_translate("Form", "Login"))
