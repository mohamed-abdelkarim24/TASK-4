#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure
import random

class PressurePublisher(Node):
    def __init__(self):
        super().__init__('pressure_node')
        self.publisher_ = self.create_publisher(FluidPressure, '/pressure', 10)
        self.create_timer(1,self.pressure_callback)
        self.num=None
        self.get_logger().info("pressure node started")

    def pressure_callback(self):
        self.num=random.uniform(900000,1100000)

        msg=FluidPressure() 
        msg.fluid_pressure=self.num
        msg.variance = 0.05 

        self.publisher_.publish(msg) 

def main():
    rclpy.init()
    node = PressurePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()