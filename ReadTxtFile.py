import argparse
from ctypes import sizeof
import os
import pandas as pd
import numpy as np
import sensor_msgs.point_cloud2 as pc_utils
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import PointStamped
import rospy
import numpy as npcel
from rosbag import Bag
import json

if __name__ == "__main__":
    counter_frame = 0
    counter_obstacle = 0

    with open('/home/project/foresight/example.json') as f:
        data = json.load(f)
    while(1):   
        Frames = (data["Frames"][counter_frame])
        Obstacles = (Frames["Obstacles"])
        if(Obstacles == []):
            print("No object detected : ", Obstacles)

        else:
            for i in range(len(Obstacles)):
                BoundBox = (data["Frames"][counter_frame]["Obstacles"][counter_obstacle]["BoundBox"])
                print(BoundBox)
                counter_obstacle = counter_obstacle + 1

        counter_obstacle = 0                     #Reset the conteur of the object detected
        counter_frame = counter_frame+1          #Incremente the counter of the frame 

    
"""
from rospy_message_converter import json_message_converter
from std_msgs.msg import String

rospy.init_node("Json", anonymous=True)
json_str = '{"data": "Hello"}'         
message = json_message_converter.convert_json_to_ros_message('std_msgs/String', json_str)
publisher = rospy.Publisher("/Json/topic", String, queue_size=1)
while(1):
    publisher.publish(message)
print(type(message))
"""