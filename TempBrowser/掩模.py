from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtWebChannel import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  # init the MainWindow

        self.setGeometry(200, 50, 1560, 960)  # Set the Geometry
        self.setWindowTitle("WebBrowser")  # Set WindowTitle

        self.browser = QWebEngineView()  # Create a browser
        self.setCentralWidget(self.browser)  # Set the browser on the MainWindow
        # self.browser.load(QUrl("https://www.bing.com/"))  # Load Google
        self.browser.setHtml("""<!DOCTYPE HTML>
<html>
<head>
<meta name="viewport" content="width=device-width initial-scale=1.0 maximum-scale=1.0 user-scalable=0">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>3D地图</title>
<style>
body,html{ margin:0;padding:0;font:12px/16px Verdana,Helvetica,Arial,sans-serif;width: 100%;height: 100%}
.container{
  height: 100%
}
</style>
<script language="javascript" src="//webapi.amap.com/maps?v=1.4.15&key=您申请的key值&plugin=AMap.ControlBar"></script>
</head>
<body >
<div id="container" style="width:100%; height:100%;resize:both;"></div>
<script language="javascript">
var map;
function mapInit(){
  map = new AMap.Map('container', {
    resizeEnable: true,
    rotateEnable:true,
    pitchEnable:true,
    zoom: 17,
    pitch:80,
    rotation:-15,
    viewMode:'3D',//开启3D视图,默认为关闭
    buildingAnimation:true,//楼块出现是否带动画
    
    expandZoomRange:true,
    zooms:[3,20],
    center:[116.333926,39.997245]
  });
  
  map.addControl(new AMap.ControlBar({
    showZoomBar:false,
    showControlButton:true,
    position:{
      right:'10px',
      top:'10px'
    }
  }))
}
mapInit()
</script>
</body>
</html>""")
        self.browser.urlChanged.connect(self.print_new_url)  # Tell me the url when it changed.
        self.show()  # Show window

    def print_new_url(self):
        print(self.browser.url())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
