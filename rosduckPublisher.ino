/*
Created by Anna Madlener on 2019/03/04.
Publisher for ROS node between Arduino and Raspberry Pi for data logging on RbPi.
Initialising the "arduNode" node, publishing on topic "duckchatter". The subscriber on RbPi
must subscribe to this topic, and logs all data receives on rosbags.
The Node must be initialized in the main.pde function.
*/


#include <ros.h>
#include <ros/time.h>
#include <nmea_msgs>
//to be completed

//initialize node
ros::NodeHandle arduNode;

//define message type, nmea?
ros::Publisher duckPublisher("/duckchatter", &nmea_msg);

//DEFINE THE DATA TO BE PUBLISHED
duck_msg = nmea_msg

void setup()
{
  arduNode.initNode();
  arduNode.advertise(duckchatter);
  Serial.begin(115000);//baudrate
}

void loop()
{
  nmea_msg.data = DATA;
  duckchatter.publish( &duck_msg):
  arduNode.spinOnce(); //find out
  ***DETERMINE PUBLISHING TIME ***
}
