
# Created by Anna Madlener on 2019/03/04.
# Subscriber for ROS node between Arduino and Raspberry Pi for data logging on RbPi.
# Initialising the "rosduck" node, subscribing to topic "duckchatter", to which Arduino publishes.
# When testing, this script should be run automatically when booting the RbPi.


#!/usr/bin/env python

import rospy
import nmea_msgs

def callback(data):


if __name__=='__main__':
    //define the subscriber
    def duckSubscriber():
        rospy.init_node('duckpiNode', anonymous=True)
        rospy.Subscriber('duckchatter',nmea_msgs, callback)
        rospy.spin()

    while not rospy.is_shutdown():

    duckSubscriber()

***ROSBAG TO LOG DATA***
    rate.sleep()
