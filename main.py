# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1179, 814)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(1170, 420, 120, 80))
        self.widget.setObjectName("widget")
        self.widget.setWindowIcon(QIcon('icon/pictogram_din_e007_rescue_phone_16px_543296_easyicon.net.ico'))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1181, 821))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.statusBar().showMessage("Map have ready!")
        self.browser = QWebEngineView()
        # self.browser.setUrl(QUrl("https://www.google.com/"))
        self.browser.setHtml("""<!doctype html>
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
                viewMode:'3D',
                center: [106.550464,29.563761],//地图中心点
                zoom: 8 //地图显示的缩放级别
            });
        
        var icon = new AMap.Icon({
        image: 'icon\pictogram_din_e007_rescue_phone_256px_543296_easyicon.net.png',
        size: new AMap.Size(30, 37), //图标大小
        imageSize: new AMap.Size(30, 37)
        })
        
        var marker1 = new AMap.Marker({
        position: [106.738211,29.840777],
        icon:icon,
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
           function draw_panel()
          {
          	var driving = new AMap.Driving({
                map: map,
                panel: "panel"
            }); 
            // 根据起终点经纬度规划驾车导航路线
            driving.search(new AMap.LngLat(106.22343, 29.12334), new AMap.LngLat(106.56566, 29.64543), function(status, result) {
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
        </html>""")
        self.verticalLayout.addWidget(self.browser)
        bar = self.menuBar()
        #  bar.triggered()
        fun1 = QAction('&显示最短路径', self)
        fun1.setShortcut('Ctrl+S')
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




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def find_shortest_way(self):
        from_position = "106.22343, 29.12334"
        to_position = "106.56566, 29.64543"
        self.browser.page().runJavaScript("draw_panel()")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "主界面"))


