import rospy
from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String


class MySubscriberNode(DTROS):
    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MySubscriberNode, self).__init__(
            node_name=node_name, node_type=NodeType.GENERIC
        )
        # construct subscriber
        # im sub kann nur eine funktion als callback angebeen werden
        rospy.Subscriber("chatter", String, self.callback)
        # sub.unregister(): keine weiteren nachrichten
        # sub.register(callback): register mir angeba von callback func
        # sub.get_num_connections(): anzahl verbindungen topic
        # sub.get_num_publishers(): anzahl pubs topic
        # sub.get_topic(): topic auf dem nachrichtem empfangen werden
        # sub.get_stats()

        # rospy.init_node('listener', anonymous=True)
        # denke hier nicht nötik da vererbung von DTROS

        # log level kann man angeben log_level=rospy.DEBUG

    def callback(self, data):
        rospy.loginfo("I heard '%s'", data.data)


if __name__ == "__main__":
    # create the node
    node = MySubscriberNode(node_name="my_subscriber_node")
    # keep spinning
    # das objet wird nicht immer neu erzeugt, auch wenn ich irgenwo gelesen habe das das skript immer neu ausgeführt wird
    # der thread bzw die Q oder der Sub wartet lediglich auf eine eintreffende nachricht
    # das heist mit der erzeugung der instanz wird auch die callback funktion immer wieder aufgerufen
    rospy.spin()
