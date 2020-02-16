#!/usr/bin/env python
import time
import numpy as np
import rospy
from std_msgs.msg import String
from common.util import make_vector3_array
from common.msg import Vector3Array
from common.constants import AS, Mission, SubSystem, MissionStatus


class MotionPlanner(object):
    def __init__(self):
        self.state = AS.AS_OFF
        self.mission = Mission.NOT_SELECTED
        self.mission_status = MissionStatus.UNAVAILABLE

        # rospy.Subscriber('/path', Vector3Array, self.receive_as)
        rospy.Subscriber('/as', String, self.receive_as)
        rospy.Subscriber('/mission', String, self.receive_mission)


    def publish(self):
        pass


    def receive_as(self, state):
        self.state = AS[state.data]


    def receive_mission(self, mission):
        self.mission = Mission[mission.data]


if __name__ == '__main__':
    rospy.init_node('MotionPlanner', log_level=rospy.DEBUG)
    planner = MotionPlanner()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        planner.publish()
        rate.sleep()
