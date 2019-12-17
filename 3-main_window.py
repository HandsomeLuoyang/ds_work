import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from main import Ui_Form
import sys
from webAPI_And_JsAPI.web import get_shortest_panel


class Main_window(QMainWindow, Ui_Form):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)

        self.statusBar().showMessage("Map have ready!")

        self.browser = QWebEngineView()
        self.browser.load(QUrl("file:///map.html"))
        self.verticalLayout.addWidget(self.browser)

        bar = self.menuBar()

        #  bar.triggered()

        fun1 = QAction("&显示最短路径", self)
        fun1.setShortcut("Ctrl+S")
        fun1.setStatusTip("最短路径")
        fun1.triggered.connect(self.find_shortest_way)

        f1 = bar.addMenu("功能1")
        f2 = bar.addMenu("功能2")
        f3 = bar.addMenu("功能3")
        f4 = bar.addMenu("功能4")
        f5 = bar.addMenu("功能5")

        f1.addAction(fun1)
        f1.addAction("temp")
        f1.addAction("temp")
        f1.addAction("temp")

        f2.addAction("temp")
        f2.addAction("temp")
        f2.addAction("temp")
        f2.addAction("temp")
        f2.addAction("temp")

        f3.addAction("temp")
        f3.addAction("temp")
        f3.addAction("temp")
        f3.addAction("temp")
        f3.addAction("temp")

        self.show()

    def find_shortest_way(self):
        shortest_panel = get_shortest_panel()
        self.browser.page().runJavaScript(
            """var panel_x = {0};
var panel_y = {1};
draw_panel(panel_x, panel_y);""".format(
                shortest_panel[0], shortest_panel[1]
            )
        )


#         print(
#             """var panel_x = {0};
# var panel_y = {1};
# draw_panel(panel_x, panel_y);""".format(
#                 shortest_panel[0], shortest_panel[1]
#             )
#         )


def main():
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
