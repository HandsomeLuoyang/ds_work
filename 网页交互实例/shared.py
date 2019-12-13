from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtProperty, pyqtSignal

class Myshared(QWidget):

    finish = pyqtSignal(list)

    def __init__(self):
        super().__init__()
    
    def PyQt52WebValue(self):
        return "666"
    
    def Web2PyQt5Value(self, str):
        info = str.split()
        fullinfo = "用户名：{}，密码：{}".format(info[0], info[1])
        QMessageBox.information(self, "从Web页面传值到PyQt5", fullinfo)
        self.finish.emit(info)

    value = pyqtProperty(str, fget=PyQt52WebValue, fset=Web2PyQt5Value)