#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def slow_and_steady():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('slow_and_teady', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.25
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        slow_and_steady()
    except rospy.ROSInterruptException:
        pass
