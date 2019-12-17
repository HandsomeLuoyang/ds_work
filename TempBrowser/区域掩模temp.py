#! /usr/bin/env python
# ^_^ coding:utf-8 ^_^


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setWindowTitle("区域掩模及自定义地图的使用")
        self.brower = QWebEngineView()
        self.brower.setHtml(
            """
<!DOCTYPE HTML>
<html>
<head>
<meta name="viewport" content="width=device-width initial-scale=1.0 maximum-scale=1.0 user-scalable=0">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>区域掩模</title>
<style>
body,html,#container{ margin:0;width: 100%;height: 100%}
</style>
</head>
<body>
<div id="container"></div>
<script language="javascript" src="https://webapi.amap.com/maps?v=1.4.15&key=8d9498bee9fb7089b0c69b8636ca6acf&plugin=Map3D,AMap.DistrictSearch"></script> 

<script language="javascript">

    var opts = {
        subdistrict: 0,
        extensions: 'all',
        level: 'city'
    };
    //利用行政区查询获取边界构建mask路径
    //也可以直接通过经纬度构建mask路径
    var district = new AMap.DistrictSearch(opts);
    district.search('重庆市', function(status, result) {
        var bounds = result.districtList[0].boundaries;
        var mask = []
        for(var i =0;i<bounds.length;i+=1){
            mask.push([bounds[i]])
        }
        var map = new AMap.Map('container', {
            mask:mask,
            center:[106.550464,29.563761],
            mapStyle:'amap://styles/680fb9a12e9f180db2779ac6d9fb1d09',
            disableSocket:true,
            viewMode:'3D',
            showLabel:false,
            labelzIndex:130,
            pitch:40,
            zoom:8,
            layers:[
                new AMap.TileLayer.RoadNet({
                    //rejectMapMask:true
                }),
                new AMap.TileLayer.Satellite()
            ]
        });
        var maskerIn = new AMap.Marker({
            position:[106.550464,29.563761],
            map:map
        })
        var maskerOut = new AMap.Marker({//区域外的不会显示
            position:[106.550464,29.563761],
            map:map
        })
        //添加高度面
        var object3Dlayer = new AMap.Object3DLayer({zIndex:1});
        map.add(object3Dlayer)
        var height = -8000;
        var color = '#0088ffcc';//rgba
        var wall = new AMap.Object3D.Wall({
            path:bounds,
            height:height,
            color:color
        });
        wall.transparent = true
        object3Dlayer.add(wall)
        //添加描边
        for(var i =0;i<bounds.length;i+=1){
            new AMap.Polyline({
                path:bounds[i],
                strokeColor:'#99ffff',
                strokeWeight:4,
                map:map
            })
        }
    });
    </script>
</body>
</html>
            """
        )
    def main(self):
        self.setCentralWidget(self.brower)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()
    Main.main()
    sys.exit(app.exec())