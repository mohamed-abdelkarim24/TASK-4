#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import keyboard  

class turtle_node(Node):
    def __init__(self):
        super().__init__('turtle_node')
        
        self.lin_vel = 2.0
        self.ang_vel = 2.0
        self.turtle_1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.turtle_2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
       
        self.timer = self.create_timer(0.1, self.pressOnkeyboard)

    def pressOnkeyboard(self):
        msg1 = Twist()  
        msg2 = Twist()  
        
        if keyboard.is_pressed('up'):
            msg1.linear.x = self.lin_vel
        elif keyboard.is_pressed('down'):
            msg1.linear.x = -self.lin_vel
        elif keyboard.is_pressed('right'):
            msg1.angular.z = -self.ang_vel
        elif keyboard.is_pressed('left'):
            msg1.angular.z = self.ang_vel
        
        if keyboard.is_pressed('w'):
            msg2.linear.x = self.lin_vel
        elif keyboard.is_pressed('s'):
            msg2.linear.x = -self.lin_vel
        elif keyboard.is_pressed('a'):
            msg2.angular.z = self.ang_vel
        elif keyboard.is_pressed('d'):
            msg2.angular.z = -self.ang_vel
        
        self.turtle_1.publish(msg1)
        self.turtle_2.publish(msg2)
    
def main():
    rclpy.init()
    node = turtle_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()