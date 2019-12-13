#! /usr/bin/env python
# ^_^ coding:utf-8 ^_^
# -*- coding: utf-8 -*-

'''
    【简介】
	QWebView打开网页例子

'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtWebChannel import *

class MainWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('缺德地图')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 1 加载html代码
        self.browser = QWebEngineView()
        self.browser.setHtml('''
		<!doctype html>
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
        resizeEnable:true,
        center: [106.550464,29.563761],//地图中心点
        zoom: 13 //地图显示的缩放级别
    });
    //构造路线导航类
    var driving = new AMap.Driving({
        map: map,
        panel: "panel"
    }); 
    // 根据起终点经纬度规划驾车导航路线
    driving.search(new AMap.LngLat(106.213213, 29.52132), new AMap.LngLat(106.12234, 29.21323), function(status, result) {
        // result 即是对应的驾车导航信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_DrivingResult
        if (status === 'complete') {
            log.success('救援路线绘制完成！')
        } else {
            log.error('救援路线绘制失败！：' + result)
        }
    });
</script>
</body>
</html>
		'''
                             )

       # self.browser1 = QWebEngineView()
#         self.browser1.setHtml(
#             """
# <!doctype html>
# <html>
# <head>
#     <meta charset="utf-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
#     <title>地点关键字 + 驾车路线规划</title>
#     <style type="text/css">
#     html,
#     body,
#     #container {
#       width: 100%;
#       height: 100%;
#     }
#     </style>
#     <style type="text/css">
#         #panel {
#             position: fixed;
#             background-color: white;
#             max-height: 90%;
#             overflow-y: auto;
#             top: 10px;
#             right: 10px;
#             width: 280px;
#         }
#         #panel .amap-call {
#             background-color: #009cf9;
#             border-top-left-radius: 4px;
#    	        border-top-right-radius: 4px;
#         }
#         #panel .amap-lib-driving {
# 	        border-bottom-left-radius: 4px;
#    	        border-bottom-right-radius: 4px;
#             overflow: hidden;
#         }
#     </style>
#     <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css" />
#     <script src="https://a.amap.com/jsapi_demos/static/demo-center/js/demoutils.js"></script>
#     <script type="text/javascript" src="https://webapi.amap.com/maps?v=1.4.15&key=您申请的key值&plugin=AMap.Driving"></script>
#     <script type="text/javascript" src="https://cache.amap.com/lbs/static/addToolbar.js"></script>
# </head>
# <body>
# <div id="container"></div>
# <div id="panel"></div>
# <script type="text/javascript">
#     //基本地图加载
#     var map = new AMap.Map("container", {
#         resizeEnable: true,
#         center: [116.397428, 39.90923],//地图中心点
#         zoom: 13 //地图显示的缩放级别
#     });
#     //构造路线导航类
#     var driving = new AMap.Driving({
#         map: map,
#         panel: "panel"
#     });
#     // 根据起终点名称规划驾车导航路线
#     driving.search([
#         {keyword: '北京市地震局(公交站)',city:'北京'},
#         {keyword: '亦庄文化园(地铁站)',city:'北京'}
#     ], function(status, result) {
#         // result 即是对应的驾车导航信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_DrivingResult
#         if (status === 'complete') {
#             log.success('绘制驾车路线完成')
#         } else {
#             log.error('获取驾车数据失败：' + result)
#         }
#     });
# </script>
# </body>
# </html>
#             """
#
#         )
      #  self.browser1.setUrl(QUrl('https://gaode.com/dir?from%5Bname%5D=%E5%8C%97%E4%BA%AC%E5%B8%82%E5%9C%B0%E9%9C%87%E5%B1%80(%E5%85%AC%E4%BA%A4%E7%AB%99)&from%5Blnglat%5D=116.30600700000002%2C39.979759&to%5Bname%5D=%E4%BA%A6%E5%BA%84%E6%96%87%E5%8C%96%E5%9B%AD(%E5%9C%B0%E9%93%81%E7%AB%99)&to%5Blnglat%5D=116.490632%2C39.80689&policy=1&type=car'))

        bar = self.menuBar()
        map = bar.addMenu("地图")
        map.addAction("两点间最短路径规划")
        map.addAction("重庆市高速路网图")
        map.addAction("功能C")

        accident=bar.addMenu("事故")
        accident.addAction("产生随机事故点")

        algorithm = bar.addMenu("算法分析")
        algorithm.addAction("Dijkstra算法")
        algorithm.addAction("改进的Dijkstra算法")

        layout = QHBoxLayout()
        self.items = QDockWidget("事故类型", self)
        self.listWidget = QListWidget()

        self.listWidget.addItem("事故类型A")
        self.listWidget.addItem("事故类型B")
        self.listWidget.addItem("事故类型C")
        self.listWidget.addItem("事故类型D")


        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setWindowTitle("缺德地图")

        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
