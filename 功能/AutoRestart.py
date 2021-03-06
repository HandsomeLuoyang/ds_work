#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年3月31日
@author: Irony."[讽刺]
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: AutoRestart
@description: 
'''

#系统自动重启功能

from optparse import OptionParser
import os
import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout


canRestart = True


def restart(twice):
    os.execl(sys.executable, sys.executable, *[sys.argv[0], "-t", twice])


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(400, 400)
        layout = QHBoxLayout(self)

        self.buttonRestart = QPushButton(
            "app start...%s...twice\napp pid: %s\n点击按钮重启...\n" %
            (options.twice, os.getpid()), self)
        self.buttonRestart.clicked.connect(self.close)

        self.buttonExit = QPushButton('退出', self, clicked=self.doExit)

        layout.addWidget(self.buttonRestart)
        layout.addWidget(self.buttonExit)

    def doExit(self):
        global canRestart
        canRestart = False
        self.close()


if __name__ == "__main__":
    parser = OptionParser(usage="usage:%prog [optinos] filepath")
    parser.add_option("-t", "--twice", type="int",
                      dest="twice", default=1, help="运行次数")
    options, _ = parser.parse_args()
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
    if canRestart:
        restart(str(options.twice + 1))
