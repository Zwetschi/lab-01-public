#!/usr/bin/env python3

import os
import rospy
from std_msgs.msg import String
from duckietown.dtros import DTROS, NodeType


class MyPublisherNode(DTROS):
    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyPublisherNode, self).__init__(
            node_name=node_name, node_type=NodeType.GENERIC
        )
        # static parameters
        self._vehicle_name = os.environ["VEHICLE_NAME"]
        # construct publisher
        topic_name = "chatter"
        # queue size ist wie in queu modul in pyhon, wenn voll dann alte nachrichten raus LIFI FIFO
        self.pub = rospy.Publisher(topic_name, String, queue_size=5)

    def run(self):
        # publish message every 1 second (1 Hz)
        rate = rospy.Rate(1)
        message = f"Hello from {self._vehicle_name}!"
        while not rospy.is_shutdown():
            rospy.loginfo("Publishing log message: '%s'" % message)
            # implizit vom typ string publishen
            self.pub.publish(message)  # sync
            # synchronous FRAGE: wenn n sub abkratz dann führt das allgemein zu fehlern auch wenns nur ein bei einem subscriber nicht klappt?
            # pub.publish(std_msgs.msg.String("hello world")) explizit
            # std_msgs.msg.String hat n attribut data so:  pub.publish(data="hello world") is ok too
            # std_msgs.msg.ColorRGBA has four fields (r, g, b, a), so we could call:
            # pub.publish(255.0, 255.0, 255.0, 128.0)
            rate.sleep()


if __name__ == "__main__":
    # create the node
    node = MyPublisherNode(node_name="my_publisher_node")
    # run node
    node.run()
    # keep the process from terminating
    rospy.spin()
