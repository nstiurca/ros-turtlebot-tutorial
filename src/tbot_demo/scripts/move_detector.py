#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

class MoveDetector(object):
  def __init__(self):
    rospy.init_node('move_detector', anonymous=True)
    rospy.Subscriber('odom', Odometry, self.odom_callback)
    rospy.loginfo("Initialized MoveDetector")

    self.moving = False
    self.spinning = False

  def odom_callback(self, msg):
    vx = msg.twist.twist.linear.x
    wz = msg.twist.twist.angular.z
    moving = abs(vx) > 0.01
    spinning = abs(wz) > 0.05

    if moving and not self.moving:
      rospy.loginfo("Started moving with vel %f m/s"%vx)
    elif not moving and self.moving:
      rospy.loginfo("Stopped moving")

    if spinning and not self.spinning:
      rospy.loginfo("Started spinning with rotational vel %f rad/s"%wz)
    elif not spinning and self.spinning:
      rospy.loginfo("Stopped spinning")

    self.moving = moving
    self.spinning = spinning

if __name__ == '__main__':
  move_detector = MoveDetector()
  rospy.spin()
