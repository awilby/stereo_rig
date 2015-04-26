#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ "I got %f", data.data);


def listener():
    rospy.init_node('stereorig_web_reconfigure', anonymous=True)
    rospy.loginfo('Stereo Rig Web Reconfigure up and running')
    rospy.Subscriber("exposure",Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()