#! /usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os
import numpy as np
import sys,tty,termios,select
import rospkg
bridge=CvBridge()
rospack=rospkg.RosPack()
def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _=select.select([sys.stdin], [] ,[], 0.1)
    if rlist:
        key=sys.stdin.read(1)
    else:
        key=''
    termios.tcsetattr(sys.stdin,termios.TCSADRAIN,settings)
    return key

def talker():
    path=rospack.get_path('img_publisher')
    a=1
    b=1
    pub=rospy.Publisher('/darknet_ros/detection_image',Image,queue_size=10)
    rospy.init_node('img_node',anonymous=True)
    print("waitkey")
    while(1):
        key=getKey()
        if key=='1':
            path_1 = path + '/pothole/'+str(a)+'.jpeg'
            img = cv2.imread(path_1)
            a+=1
            image_message=bridge.cv2_to_imgmsg(img,encoding="passthrough")
            pub.publish(image_message)
            print('send1')
        if key=='2':
            path_2 = path + '/roadtripod/'+str(b)+'.jpeg'
            print(path_2)
            img = cv2.imread(path_2)
            b+=1
#            image_message=bridge.cv2_to_imgmsg(img,encoding="passthrough")
            image_message=bridge.cv2_to_imgmsg(img,'bgr8')
            pub.publish(image_message)
            print('send2')
        if key=='3':
            break

if __name__=='__main__':
    settings=termios.tcgetattr(sys.stdin)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
