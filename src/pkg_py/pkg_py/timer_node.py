#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

class timer_node(Node):
    def __init__(self):
        super().__init__("timer_node")
        self.counter=10
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
        if self.counter > 0 : 
            self.get_logger().info(f"{self.counter}")
            self.counter-=1
        elif self.counter == 0 :
            self.get_logger().info("TIME is up!")
            self.counter-=1
            return 0

def main():
    rclpy.init()
    node = timer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()