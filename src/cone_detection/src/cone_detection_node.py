#!/usr/bin/env python
import time
import numpy as np
import rospy
from std_msgs.msg import String
from common.util import make_vector3_array
from common.msg import Vector3Array
from common.constants import AS, Mission, SubSystem, MissionStatus


class Detector(object):
    def __init__(self):
        self.state = AS.AS_OFF
        self.mission = Mission.NOT_SELECTED
        self.mission_status = MissionStatus.UNAVAILABLE

        self.cone_publisher = rospy.Publisher('/cones', Vector3Array, queue_size=1)

        rospy.Subscriber('/as', String, self.receive_as)
        rospy.Subscriber('/mission', String, self.receive_mission)


    def publish(self):
        cones = np.random.rand(2, 3)
        cones_msg = make_vector3_array(cones)
        self.cone_publisher.publish(cones_msg)


    def receive_as(self, state):
        self.state = AS[state.data]


    def receive_mission(self, mission):
        self.mission = Mission[mission.data]


if __name__ == '__main__':
    rospy.init_node('Detector', log_level=rospy.DEBUG)
    detector = Detector()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        detector.publish()
        rate.sleep()
