
# Created by Anna Madlener on 2019/03/04.
# Subscriber for ROS node between Arduino and Raspberry Pi for data logging on RbPi.
# Initialising the "rosduck" node, subscribing to topic "duckchatter", to which Arduino publishes.
# When testing, this script should be run automatically when booting the RbPi.


#!/usr/bin/env python

import rospy
from nmea_msgs import Sentences
from std_msgs import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.Sentences) # not sure if i need this
    # is this where the rosbag should be?

#define the subscriber
def duckpiSubscriber():
    rospy.init_node('duckpiSubscriber', anonymous=True)
    rospy.Subscriber('duckchatter',Sentences, callback)
    rospy.spin()

def duckpiLogger():


if __name__=='__main__':
    while not rospy.is_shutdown():
        duckpiSubscriber()
        duckpiLogger()
        rate.sleep()

'''
#!/usr/bin/env python
import rospy
from nmea_msgs import Sentences

def callback(nmea_msgs):
    rospy.loginfo(rospy.get_time(), nmea_msgs.Sentences)

def duckpiListener():

    rospy.init_node('duckpiListener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()'''
