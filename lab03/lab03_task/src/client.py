#! /usr/bin/env python

import rospy
import numpy as np
import random
import time

#TODO: import the SRV file from its corresponding folder, as well as its Request
from lab03_task.srv import rotmat2quatRequest
from lab03_task.srv import rotmat2quat


def rot2quat_client():
    rospy.wait_for_service('rotmat2quat')

    while not rospy.is_shutdown():
        #TODO: Initialise the ROS service client. It takes two arguments: The name of the service, and the service definition.
        client = rospy.ServiceProxy('rotmat2quat', rotmat2quat )

        
        req = rotmat2quatRequest()
        req.R.data = []

        #TODO: create a random request matrix

        for i in range(9):
            req.R.data.append(random.uniform(-1, 1))



        res = client(req)

        print(res)

        time.sleep(3)


if __name__ == '__main__':
    try:
        rot2quat_client()
    except rospy.ROSInterruptException:
        pass
