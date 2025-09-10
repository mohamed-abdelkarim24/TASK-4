#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
import random

class tempPublisher(Node):
    def __init__(self):
        super().__init__('temperature_node')
        self.publisher_ = self.create_publisher(Temperature, '/temparature', 10)
        self.create_timer(1,self.temperature_callback)
        self.num=None
        self.get_logger().info("Temprature node started")

    def temperature_callback(self):
        self.num=random.uniform(15,40)

        msg=Temperature() 
        msg.temperature=self.num
        msg.variance = 0.05 

        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = tempPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()