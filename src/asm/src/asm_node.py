#!/usr/bin/env python
import time
from threading import Lock
import rospy
from std_msgs.msg import String, Bool
from common.constants import AS, Mission, SubSystem, GO_SIGNAL_DELAY, MissionStatus
from asm.msg import CarState


class ASM(object):
    def __init__(self):
        self.state = AS.AS_OFF
        self.mission = Mission.NOT_SELECTED
        self.mission_status = MissionStatus.UNAVAILABLE
        self.car_state = CarState()
        self.go_signal_received = -1

        self.as_publisher = rospy.Publisher('/as', String, queue_size=1)
        self.mission_publisher = rospy.Publisher('/mission', String, queue_size=1)

        self.update_lock = Lock()

        rospy.Subscriber('/car_state', CarState, self.update_car_state)
        rospy.Subscriber('/go_signal', Bool, self.update_car_state)
        rospy.Subscriber('/mission_status', String, self.update_car_state)



    def receive_mission_status(self, status):
        self.update_lock.acquire()
        self.mission_status = MissionStatus[status.data]
        self.update_as_state()
        self.update_lock.release()


    def receive_go_signal(self, _):
        self.update_lock.acquire()
        self.go_signal_received = time.time()
        self.update_as_state()
        self.update_lock.release()


    def update_car_state(self, car_state):
        self.update_lock.acquire()
        self.car_state = car_state
        self.mission = Mission[self.car_state.mission]
        self.update_as_state()
        self.update_lock.release()


    def publish(self):
        self.as_publisher.publish(self.state.name)
        self.mission_publisher.publish(self.mission.name)


    def update_as_state(self):
        if self.state == AS.AS_OFF:
            self.handle_as_off()
        elif self.state == AS.MANUAL_DRIVING:
            self.handle_manual_driving()
        elif self.state == AS.AS_READY:
            self.handle_as_ready()
        #TODO finish the state machine


    def handle_as_off(self):
        if self.mission = Mission.MANUAL_DRIVING and self.car_state.EBS = SubSystem.UNAVAILABLE and
            self.car_state.ASMS = SubSystem.OFF and self.car_state.TS = SubSystem.ON:

            self.state = AS.MANUAL_DRIVING

        elif self.mission != Mission.MANUAL_DRIVING and self.mission != Mission.NOT_SELECTED and
            self.car_state.EBS = SubSystem.ARMED and self.car_state.ASMS = SubSystem.ON and
            self.car_state.TS = SubSystem.ON

            self.state = AS.AS_READY
            self.go_signal_received = -1


    def handle_manual_driving(self):
        if self.car_state.TS = SubSystem.OFF:
            self.state = AS.AS_OFF


    def handle_as_ready(self):
        curr_time = time.time()
        if self.go_signal_received != -1 and (curr_time - self.go_signal_received) >= GO_SIGNAL_DELAY:
            self.state = AS.AS_DRIVING

        elif self.car_state.ASMS = SubSystem.OFF and self.car_state.EBS = SubSystem.X:
            self.state = AS.AS_OFF

        elif self.car_state.EBS = SubSystem.ACTIVATED:
            self.state = AS.AS_EMERGENCY



if __name__ == '__main__':
    rospy.init_node('ASM', log_level=rospy.DEBUG)
    asm = ASM()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        asm.publish()
        rate.sleep()

        