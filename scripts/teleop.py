#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def teleop():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.init_node('teleop', anonymous=True)
    rospy.sleep(1.0)
    rate = rospy.Rate(10) #10hz

    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = 1.0
        vel.angular.z = 1.0
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass
