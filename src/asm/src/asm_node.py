#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from common.constants import AS, Mission
from asm.msg import CarState


class ASM(object):
    def __init__(self):
        self.state = AS.AS_OFF
        self.mission = Mission.NOT_SELECTED
        self.car_state = CarState()

        self.as_publisher = rospy.Publisher('/as', String, queue_size=1)
        self.mission_publisher = rospy.Publisher('/mission', String, queue_size=1)

        rospy.Subscriber('/car_state', CarState, self.update_car_state)


    def update_car_state(self, car_state):
        # rospy.loginfo('car state {}'.format(car_state.data))
        self.car_state = car_state
        self.mission = Mission[self.car_state.mission]


    def publish(self):
        self.as_publisher.publish(self.state.name)
        self.mission_publisher.publish(self.mission.name)



    # def check_transitions(self):
    #     if self.state == AS.AS_OFF:
    #         self.car_state['']


if __name__ == '__main__':
    rospy.init_node('ASM', log_level=rospy.DEBUG)
    asm = ASM()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        asm.publish()
        rate.sleep()

        