from enum import Enum

class AS(Enum):
    AS_OFF = 1
    AS_READY = 2
    AS_DRIVING = 3
    AS_FINISHED = 4
    AS_EMERGENCY = 5
    MANUAL_DRIVING = 6


class Mission(Enum):
    NOT_SELECTED = 0
    ACCELERATION = 1
    SKIDPAD = 2
    AUTOCROSS = 3
    TRACKDRIVE = 4
    EBS_TEST = 5
    INSPECTION = 6
    MANUAL_DRIVING = 7