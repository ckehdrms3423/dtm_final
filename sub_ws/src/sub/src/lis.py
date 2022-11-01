#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix,Image
from ublox_msgs.msg import NavPVT
from darknet_ros_msgs.msg import BoundingBoxes
import message_filters
import nextcloud_client
import requests
import os
from datetime import datetime

nc=nextcloud_client.Client('http://61.252.59.34:31014')
nc.login('root','root')
lat=0
lng=0
obj_name=""
o_obj=""
bridge=CvBridge()
def callback(data):
    global lat
    global lng
    lat=data.latitude
    lng=data.longitude
#    print("lat:{}, lon:{}".format(lat,lng))
    

def callback2(data):
#    print("receive image")
    try:
        cv2_img=bridge.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError,e:
        print(e)
    else:
        if(o_obj!=obj_name):
            time=data.header.stamp
            t_s=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            img_name="{}.png".format(time)
            cv2.imwrite(img_name,cv2_img)
            nc.put_file('test/test{}.png'.format(time),img_name)
            os.remove(img_name)
            link_info=nc.share_file_with_link('test/test{}.png'.format(time)).get_link()+"preview"
            URL='http://103.218.163.29:3500/nodelinkapi/event?eventtype=etc&eventdetailtype='+obj_name+'&lat='+str(lat)+'&lng='+str(lng)+'&vehicle_id=31&image_path='+link_info+'&start_time='+str(t_s)
            response=requests.get(URL)
            print('send')
        else:
            print('skip')


def callback3(data):
    global obj_name
    global o_obj
    for i in data.bounding_boxes:
        obj_name+=str(i.id)
#    print("{}".format(obj_name))
    o_obj=obj_name
    obj_name=''

def callback4(data):
    head=data.heading/100000
    print("lat:{}, lon:{}".format(lat,lng))
    head_URL='http://103.218.163.29:3500/nodelinkapi/vehicle?vehicle_id=31&lat='+str(lat)+'&lng='+str(lng)+'&heading='+str(head)
    response=requests.get(head_URL)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('ublox_gps/fix', NavSatFix, callback)
    rospy.Subscriber('darknet_ros/bounding_boxes',BoundingBoxes,callback3)
    rospy.Subscriber('darknet_ros/detection_image',Image,callback2)
    rospy.Subscriber('ublox_gps/navpvt',NavPVT,callback4)
    rospy.spin()


if __name__ == '__main__':
    listener()
