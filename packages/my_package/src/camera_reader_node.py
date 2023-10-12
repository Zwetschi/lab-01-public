import os
import rospy
from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage

import cv2
from cv_bridge import CvBridge


class CameraReaderNode(DTROS):
    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(CameraReaderNode, self).__init__(
            node_name=node_name, node_type=NodeType.VISUALIZATION
        )
        # static parameters
        self._vehicle_name = os.environ["VEHICLE_NAME"]
        # bridge between OpenCV and ROS
        self._bridge = CvBridge()
        # create window
        cv2.namedWindow("camera-reader", cv2.WINDOW_AUTOSIZE)
        # construct subscriber
        _camera_topic = r""  # suche knoten der das haben kann
        sub = rospy.Subscriber(_camera_topic, CompressedImage, self.callback)

    def callback(self, msg: CompressedImage):
        # msg = np.frombuffer(jpeg_data, np.uint8)# gehe mal davon aus dass das argument schon n array ist
        # image = cv2.imdecode(msg, cv2.IMREAD_COLOR)
        image = self._bridge.compressed_imgmsg_to_cv2(msg)  # wird das hier sein
        img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # NOTE ist im rgb?
        img_blur = cv2.GaussianBlur(img, (5, 5), 2)
        edges = cv2.Canny(img_blur, 100, 180)
        # anzeigen von mehreren bilder mit np.concatenate
        stacked_image = np.hstack((image1, image2))
        cv2.imshow("hfh", img1)
        cv2.waitKey(0)
        cv2.imshow("hfh", img2)
        cv2.waitKey(0)
        self.show(image)

    def show(self, img):
        if img is not None:
            cv2.imshow("gg", img)
            # cv2.waitKey(0) # warte unendlich lange auf tasteneingabe
            # warte x millisecunden auf tastatureingabe und gebe den wert zurück
            cv2.waitKey(1)
            # cv2.destroyAllWindows()


if __name__ == "__main__":
    # create the node
    node = CameraReaderNode(node_name="camera_reader_node")
    # keep spinning
    rospy.spin()
