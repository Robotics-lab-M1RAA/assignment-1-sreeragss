#!/usr/bin/python3  #Shebang

import rospy
from std_msgs.msg import String

def callback(msg2):
    rospy.loginfo(f"reciveed : {msg2.data}")


def listener():
    rospy.init_node("CET")
    rospy.Subscriber("hello_college",String,callback)
    rospy.spin()

if __name__ == "__main__" :
    listener()