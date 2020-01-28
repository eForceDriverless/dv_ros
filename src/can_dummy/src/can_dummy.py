#!/usr/bin/env python
from enum import Enum
import json
import rospy
from std_msgs.msg import String, Header
from common.constants import Mission
import asm
from asm.msg import CarState


def make_car_state():
    car_state = CarState()
    car_state.header = Header()
    car_state.mission = Mission.MANUAL_DRIVING.name
    car_state.TS = 'on'
    car_state.R2D = 'on'
    car_state.SA = 'available'
    car_state.SB = 'available'
    car_state.EBS = 'off'
    car_state.ASSI = 'off'
    car_state.ASMS = 'on'

    return car_state


class CANDummy(object):
    def __init__(self):
        self.car_state = make_car_state()
        self.car_state_publisher = rospy.Publisher('/car_state', CarState, queue_size=1)


    def publish(self):
        self.car_state_publisher.publish(self.car_state)


if __name__ == '__main__':
    rospy.init_node('CAN Dummy', log_level=rospy.DEBUG)
    can_dummy = CANDummy()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        can_dummy.publish()
        rate.sleep()
