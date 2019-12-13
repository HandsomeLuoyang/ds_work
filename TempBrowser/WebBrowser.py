from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtWebChannel import *
import time


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  # init the MainWindow

        self.setGeometry(200, 50, 1560, 960)  # Set the Geometry
        self.setWindowTitle("WebBrowser")  # Set WindowTitle
        self.browser = QWebEngineView()  # Create a browser
        self.setCentralWidget(self.browser)  # Set the browser on the MainWindow
        self.main_index = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
    <style type="text/css">
      body,html,#container{
        width: 100%;
        height: 100%;
        margin: 0px
      }
    </style>
    <title>API加载</title>
  </head>
  <body>
    <div id="container" tabindex="0"></div>
    <script type="text/javascript">
        window.init = function(){
            var map = new AMap.Map('container', {
               resizeEnable: true,
               center:[106.550464,29.563761],
               zoom:11
            });
            if (location.href.indexOf('guide=1') !== -1) {
                map.setStatus({scrollWheel: false});
                map.plugin(["AMap.ToolBar"], function() {
                  map.addControl(new AMap.ToolBar({liteStyle:true}))
                });
            }
          }
    </script>
    <script src="https://webapi.amap.com/maps?v=1.4.15&key=47f6201d035967605a79f0032b5fc154&callback=init"></script>
  </body>
</html>"""
        self.browser.setHtml(self.main_index)
        # self.browser.load(QUrl("https://www.google.com/"))
        self.show()  # Show window

    def print_new_url(self):
        print(self.browser.url())

    def find_shortest_way_window_show(self):
        from_position = "106.22343, 29.12334"
        to_position = "106.56566, 29.64543"
        html = """<!doctype html>
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
                zoom: 13//地图显示的缩放级别
            });
            //构造路线导航类
            var driving = new AMap.Driving({
                map: map,
                panel: "panel"
            }); 
            // 根据起终点经纬度规划驾车导航路线
            driving.search(new AMap.LngLat(""" + from_position + """), new AMap.LngLat(""" + to_position + """), function(status, result) {
                // result 即是对应的驾车导航信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_DrivingResult
                if (status === 'complete') {
                    log.success('救援路线绘制完成！')
                } else {
                    log.error('救援路线绘制失败！：' + result)
                }
            });
        </script>
        </body>
        </html>"""
        self.browser.setHtml(html)
        self.browser.reload()
        self.browser.urlChanged.connect(self.print_new_url)  # Tell me the url when it changed.


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
