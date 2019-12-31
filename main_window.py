from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from main import Ui_Form
import sys
import os
from web import get_shortest_panel
from visiualGo_window import Visiual_Window



class Main_window(QMainWindow, Ui_Form):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)

        self.browser = QWebEngineView()
        # self.showMaximized()
        self.browser.load(QUrl("file:///map.html"))
        self.verticalLayout.addWidget(self.browser)

        # 主菜单栏
        self.bar = self.menuBar()
        self.f1 = self.bar.addMenu("功能1")
        self.f2 = self.bar.addMenu("功能2")
        self.f3 = self.bar.addMenu("功能3")
        self.f4 = self.bar.addMenu("算法分析")
        self.f5 = self.bar.addMenu("地图主题选择")
        self.setStyleSheet("#bar{background-color:red;}")

        #  bar.triggered()

        fun1 = QAction("&显示最短路径", self)
        fun1.setShortcut("Ctrl+S")
        fun1.setStatusTip("最短路径")
        fun1.triggered.connect(self.accident_appear)

        # 卫星地图
        mapStyle_1 = QAction("&卫星地图", self)
        mapStyle_1.triggered.connect(self.weixinMap)

        # 标准地图
        mapStyle_base = QAction("&标准地图", self)
        mapStyle_base.triggered.connect(self.baseMap)

        # 实时路况
        trafficLayer = self.f5.addMenu("实时路况")
        # 实时路况显示
        trafficLayer_show = QAction("&显示路况", self)
        trafficLayer.addAction(trafficLayer_show)
        trafficLayer_show.triggered.connect(self.trafficLayer_show1)

        trafficLayer_hide = QAction("&隐藏路况", self)
        trafficLayer.addAction(trafficLayer_hide)
        trafficLayer_hide.triggered.connect(self.trafficLayer_hide1)

        # 迪杰斯特拉算法演示
        dijkstra = QAction("&Dijkstra算法及优化版时间分析", self)
        dijkstra.triggered.connect(self.dijkstra_show)
        dijkstra_tu = QAction("&Dijkstra算法动态图演示", self)
        dijkstra_tu.triggered.connect(self.dijkstra_tu_show)

        self.f1.addAction(fun1)

        self.f2.addAction("temp")

        self.f3.addAction("temp")

        self.f4.addAction(dijkstra)
        self.f4.addAction(dijkstra_tu)

        self.f5.addAction(mapStyle_1)
        self.f5.addAction(mapStyle_base)
        self.show()

    def accident_appear(self):
        """
        Get a accident position from file random.
        And draw the shortest panel on the map.
        """
        # Pass in the accident point.
        shortest_panel = get_shortest_panel()
        self.browser.page().runJavaScript(
            """var panel_x = {0};
var panel_y = {1};
var accident_point_x = {2};
var accident_point_y = {3};
draw_panel(panel_x, panel_y, accident_point_x, accident_point_y);
        """.format(
                shortest_panel[0], shortest_panel[1],
                shortest_panel[2], shortest_panel[3]
            )
        )

    def weixinMap(self):
        """
        -显示卫星地图
        :return:
        """
        self.browser.page().runJavaScript(
            """
                weixinMap();
                """
        )

    def trafficLayer_show1(self):
        self.browser.page().runJavaScript(
            """
            trafficLayer_show1();
            """
        )

    def trafficLayer_hide1(self):
        self.browser.page().runJavaScript(
            """
            trafficLayer_hide1();
            """
        )

    def baseMap(self):
        self.browser.page().runJavaScript(
            """
            baseMap();
            """
        )

    def dijkstra_show(self):
        path = "map.exe"
        os.system(path)

    def dijkstra_tu_show(self):
        self.visiual_window = Visiual_Window()
        self.visiual_window.show()


def main():
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
