from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtWebChannel import *
import time


class Visiual_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  # init the MainWindow

        self.setGeometry(200, 50, 1560, 960)  # Set the Geometry
        self.setWindowTitle("WebBrowser")  # Set WindowTitle
        self.browser = QWebEngineView()  # Create a browser
        self.browser.load(QUrl("https://visualgo.net/en/sssp"))
        self.setCentralWidget(self.browser)  # Set the browser on the MainWindow
        # self.browser.urlChanged.connect(self.print_new_url)  # Tell me the url when it changed.


def main():
    app = QApplication(sys.argv)
    window = Visiual_Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
