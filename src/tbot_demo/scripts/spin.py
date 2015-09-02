#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def spin():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('spin', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.angular.z = rospy.get_param('~spin_rate')
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        spin()
    except rospy.ROSInterruptException:
        pass
