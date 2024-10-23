#!/usr/bin/python3  #Shebang

import rospy   
from std_msgs.msg import String

def callback(msg2):
    rospy.loginfo(f"reciveed : {msg2.data}")

def publisher1():

    rospy.init_node('sreerag',anonymous=True)
    pub1 = rospy.Publisher("hello_class", String, queue_size=10)
    rospy.Subscriber("welcome",String,callback)
    
    rate = rospy.Rate(10)  
    rospy.loginfo('publishing test') 

    while not rospy.is_shutdown():

        msg = String()
        msg.data = "Hello RAA24_26!"
        pub1.publish(msg)
        #rospy.loginfo(msg)
        rate.sleep()

if __name__=='__main__':
    try:
        publisher1()
    except rospy.ROSInterruptException:
        pass