
# Created by Anna Madlener on 2019/03/04.
# Subscriber for ROS node between Arduino and Raspberry Pi for data logging on RbPi.
# Initialising the "rosduck" node, subscribing to topic "duckchatter", to which Arduino publishes.
# When testing, this script should be run automatically when booting the RbPi.


#!/usr/bin/env python

#import roslib; roslib.load_manifest('numpy_tutorials') #not sure why I need this it was here: https://answers.ros.org/question/159276/read-data-from-serial-port-and-publish-over-a-topic/
import rospy
import serial
from nmea_msgs import Sentences

#define serial port to listen to
ser = serial.Serial('/dev/ttyACM0', 115200)

#read NMEA messages received from arduino
def duckpiTalker():
    pub = rospy.Publisher('duckChatter', Sentences, queue_size=10)
    rospy.init_node('duckpiTalker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        nmeamessage = ser.read(2) #not sure what this number means yet or what it should be
        #rospy.loginfo(nmeamessage)
        pub.publish(nmeamessage)
        #rate.sleep()

if __name__=='__main__':
    try:
        duckpiTalker();
    except rospy.ROSInterruptException:
        pass



#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def talker():
 while not rospy.is_shutdown():
   data= ser.read(2) # I have "hi" coming from the arduino as a test run over the serial port
   rospy.loginfo(data)
   pub.publish(String(data))
   rospy.sleep(1.0)


if __name__ == '__main__':
  try:
    pub = rospy.Publisher('chatter', String)
    rospy.init_node('talker')
    talker()
  except rospy.ROSInterruptException:
    pass
