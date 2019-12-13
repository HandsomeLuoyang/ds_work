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

        # 1 加载html代码
        self.browser = QWebEngineView()
        self.browser.setHtml('''
		<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css" />
    <style>
        html,
        body,
        #container {
            width: 100%;
            height: 100%;
        }
    </style>
    <title>地图加载完成</title>
</head>
<body>
<div id="container"></div>
<script src="https://webapi.amap.com/maps?v=1.4.13&key=47f6201d035967605a79f0032b5fc154"></script>
<script src="https://a.amap.com/jsapi_demos/static/demo-center/js/demoutils.js"></script>
<script>
    var map = map = new AMap.Map('container', {
        zoom:11,
        resizeEnable: true,
        viewMode:'3D',
        center:[106.30316,29.430904]
    });
    map.on("complete", function(){
        log.success("地图加载完成！");
    });
</script>
</body>

</html>
		'''
                             )

        # 路径规划
        self.routePlan = QWebEngineView()
        self.routePlan.setHtml(
            """
            <!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <title>使用数据自我展示</title>
    <link rel="stylesheet" href="https://cache.amap.com/lbs/static/AMap.DrivingRender1120.css"/>
    <style>
    html,
    body,
    #container {
        width: 100%;
        height: 100%;
    }
    #panel {
        position: fixed;
        background-color: white;
        max-height: 90%;
        overflow-y: auto;
        top: 10px;
        right: 10px;
        width: 280px;
    }
    #panel .amap-lib-driving {
   	    border-radius: 4px;
        overflow: hidden;
    }
    </style>
    <link rel="stylesheet" href="https://a.amap.com/jsapi_demos/static/demo-center/css/demo-center.css" />
    <script src="https://a.amap.com/jsapi_demos/static/demo-center/js/demoutils.js"></script>
    <script type="text/javascript" src="https://webapi.amap.com/maps?v=1.4.15&key=866f8338214aceb54845173751671bae&plugin=AMap.Driving"></script>
    <script type="text/javascript" src="https://cache.amap.com/lbs/static/DrivingRender1230.js"></script>
    <script type="text/javascript" src="https://cache.amap.com/lbs/static/addToolbar.js"></script>
</head>
<body>
<div id="container"></div>
<div id="panel"></div>
<script type="text/javascript">
    var map = new AMap.Map("container", {
        resizeEnable: true
    });
    //驾车导航，您如果想修改结果展现效果，请参考页面：https://lbs.amap.com/fn/css-style/
    var drivingOption = {
        policy:AMap.DrivingPolicy.LEAST_TIME
    };
    var driving = new AMap.Driving(drivingOption); //构造驾车导航类
    //根据起终点坐标规划驾车路线
    driving.search([{keyword:'北京市地震局(公交站)'},{keyword:'亦庄文化园(地铁站)'}], function(status, result){
		if(status === 'complete' && result.info === 'OK'){
			(new Lib.AMap.DrivingRender()).autoRender({
				data: result,
                map: map,
                panel: "panel"
            });
            
            log.success('绘制驾车路线完成')
		}else{
            log.error('获取驾车数据失败：' + result)
        }
	});
</script>
</body>
</html>
            """
        )

        bar = self.menuBar()
        map = bar.addMenu("地图")

        map.addAction("两点间最短路径规划")
        map.addAction("重庆市高速路网图")
        map.addAction("功能C")

        accident = bar.addMenu("事故")
        accident.addAction("产生随机事故点")

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
        # self.setCentralWidget(self.routePlan)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
