from std_msgs.msg import Header
from geometry_msgs.msg import Vector3
from common.msg import Vector3Array


def make_vector3_array(arr):
    msg = Vector3Array()
    msg.header = Header()

    vectors = []
    for x, y, z in arr:
        vectors.append(Vector3(x, y, z))

    msg.vectors = vectors
    return msg