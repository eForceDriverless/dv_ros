from enum import Enum

#: Delay in seconds before the state can
#: change to AS.AS_DRIVING
GO_SIGNAL_DELAY = 5

class SubSystem(Enum):
    """Enum describing the state of car subsystems e.g. EBS, TS, ..

    """
    ON = 0
    OFF = 1
    AVAILABLE = 2
    UNAVAILABLE = 3
    ARMED = 4
    ACTIVATED = 5
    ENGAGED = 6
    X = 7


class AS(Enum):
    """Enum describing the Autonomous state

    """
    AS_OFF = 0
    AS_READY = 1
    AS_DRIVING = 2
    AS_FINISHED = 3
    AS_EMERGENCY = 4
    MANUAL_DRIVING = 5


class Mission(Enum):
    """Enum describing the current mission

    """
    NOT_SELECTED = 0
    ACCELERATION = 1
    SKIDPAD = 2
    AUTOCROSS = 3
    TRACKDRIVE = 4
    EBS_TEST = 5
    INSPECTION = 6
    MANUAL_DRIVING = 7


class MissionStatus(Enum):
    """Enum describing the status of the current mission

    """
    UNAVAILABLE = 0 #: test
    ONGOING = 1 #: test
    FINISHED = 2
