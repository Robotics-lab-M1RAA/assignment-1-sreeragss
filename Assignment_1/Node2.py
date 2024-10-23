#!/usr/bin/python3  #Shebang

import rospy   
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"reciveed : {msg.data}")


def publisher1():

    rospy.init_node('M1RAA_24_26',anonymous=True)
    pub1 = rospy.Publisher("welcome", String, queue_size=10)
    pub2 = rospy.Publisher("hello_college", String, queue_size=10)
    rospy.Subscriber("hello_class",String,callback)
    
    rate = rospy.Rate(10)  
    rospy.loginfo('publishing test') 

    while not rospy.is_shutdown():

        msg1 = String()
        msg1.data = "Hello Sreerag Welcome!"
        pub1.publish(msg1)

        msg2 = String()
        msg2.data = "Hello CET!"
        pub2.publish(msg2)
        #rospy.loginfo(msg)
        rate.sleep()

if __name__=='__main__':
    try:
        publisher1()
    except rospy.ROSInterruptException:
        pass