#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import RelativeHumidity
import random

class HumPublisher(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.publisher_ = self.create_publisher(RelativeHumidity, '/humidity', 10)
        self.create_timer(1,self.humidity_callback)
        self.num=None
        self.get_logger().info("humidity node started")

    def humidity_callback(self):
        self.num=random.uniform(0.0,1.0)

        msg=RelativeHumidity() 
        msg.relative_humidity=self.num 
        msg.variance = 0.01

        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = HumPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()