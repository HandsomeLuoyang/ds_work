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
        # self.browser.setUrl(QUrl("https://www.google.com/"))
        self.browser.setHtml(
            """<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <title>位置经纬度 + 驾车规划路线</title>
    <style type="text/css">
    html,
    body,
    #container {
      width: 100%;
      height: 100%;
    }
    </style>
    <style type="text/css">
        #panel {
            position: fixed;
            background-color: white;
            max-height: 90%;
            overflow-y: auto;
            top: 10px;
            right: 10px;
            width: 280px;
        }
        #panel .amap-call {
            background-color: #009cf9;
            border-top-left-radius: 4px;
   	        border-top-right-radius: 4px;
        }
        #panel .amap-lib-driving {
	        border-bottom-left-radius: 4px;
   	        border-bottom-right-radius: 4px;
            overflow: hidden;
        }
    </style>
    <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css" />
    <script src="https://a.amap.com/jsapi_demos/static/demo-center/js/demoutils.js"></script>
    <script type="text/javascript" src="https://webapi.amap.com/maps?v=1.4.15&key=47f6201d035967605a79f0032b5fc154&plugin=AMap.Driving"></script>
    <script type="text/javascript" src="https://cache.amap.com/lbs/static/addToolbar.js"></script>
</head>
<body>
<div id="container"></div>
<div id="panel"></div>
<script type="text/javascript">
    //基本地图加载
    var map = new AMap.Map("container", {
        resizeEnable: true,
        center: [106.550464,29.563761],//地图中心点
        zoom: 8,//地图显示的缩放级别
        viewMode: "3D"
    });
    
    var icon = new AMap.Icon({
        size: new AMap.Size(30, 37), //图标大小
        imageSize: new AMap.Size(30, 37)
        })
        
        var marker1 = new AMap.Marker({
        position: [106.738211,29.840777],

        offset: new AMap.Pixel(-13, -30)
        });
        var marker2 = new AMap.Marker({
        position: [106.351097,29.75598],

        offset: new AMap.Pixel(-13, -30)
        });
        var marker3 = new AMap.Marker({
        position: [106.711726,29.498983],

        offset: new AMap.Pixel(-13, -30)
        });
        var marker4 = new AMap.Marker({
        position: [106.288054,29.536045],
        offset: new AMap.Pixel(-13, -30)
        });
        var marker5 = new AMap.Marker({
        position: [106.444183,29.53087],
        offset: new AMap.Pixel(-13, -30)
        });
        var marker6 = new AMap.Marker({
        position: [106.586582,29.352452],
        offset: new AMap.Pixel(-13, -30)
        });
        var marker7 = new AMap.Marker({
        position: [106.478209,29.481837],
        offset: new AMap.Pixel(-13, -30)
        });
        var marker8 = new AMap.Marker({
        position: [106.456811,29.258333],
        offset: new AMap.Pixel(-13, -30)
        });

        var markerList = [marker1,marker2,marker3,marker4,marker5,marker6,marker7,marker8]
        
        marker1.setTitle('我是marker的title');
        marker1.setLabel({
        offset: new AMap.Pixel(20, 20),  //设置文本标注偏移量
        direction: 'right' //设置文本标注方位
         });

        map.add(markerList);
    
    //构造路线导航类
   function draw_panel(shortest_panel_x, shortest_panel_y)
  {
  	var driving = new AMap.Driving({
        map: map,
        panel: "panel"
    });
    // 根据起终点经纬度规划驾车导航路线
    driving.search(new AMap.LngLat(shortest_panel_x, shortest_panel_y), new AMap.LngLat(106.56566, 29.64543), function(status, result) {
        // result 即是对应的驾车导航信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_DrivingResult
        if (status === 'complete') {
            log.success('绘制救援路线完成')
        } else {
            log.error('获取救援路线失败：' + result)
        }
    });
  }

</script>
</body>
</html>"""
        )
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
