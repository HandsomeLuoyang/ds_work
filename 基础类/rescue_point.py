#! /usr/bin/env python
# ^_^ coding:utf-8 ^_^

class rescue_point(object):
    """救援点初始化"""
    def __init__(self,name='xxx救援',point='106.754991,29.838469',police=5,tow_truck=2,ambulance=3):
        self.name = name
        self.point = point
        self.police = police
        self.tow_truck = tow_truck
        self.ambulance = ambulance

    def get_point(self):
        return self.point
