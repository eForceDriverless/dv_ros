from std_msgs.msg import Header
from geometry_msgs.msg import Vector3
from common.msg import Vector3Array

import common
print(common.__path__)



def make_vector3_array(arr):
    """test documentation
	test documentation
    """
    msg = Vector3Array()
    msg.header = Header()

    vectors = []
    for x, y, z in arr:
        vectors.append(Vector3(x, y, z))

    msg.vectors = vectors
    return msg
