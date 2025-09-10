#!/usr/bin/env 

from time import time
from pathlib import Path
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
from sensor_msgs.msg import FluidPressure
from sensor_msgs.msg import RelativeHumidity

def  save_read(readings: str, file_name = 'weather.txt'):
      home_dir = Path.home()
      info_path = home_dir / "ros2_ws" / file_name

      info_file = info_path.open("a")
      info_file.write(readings + '\n')
      info_file.close()
      
   

class Monitor(Node):
    def __init__(self):
        super().__init__('monitor_node')
        self.temp_val = 0
        self.temp_var = 0
        self.hum_val = 0
        self.hum_var = 0
        self.pressure_val = 0
        self.pressure_var = 0

        self.tempe = self.create_subscription(
            Temperature,
            '/temparature',
            self.temperature_callback,
            10)
        
        self.hum = self.create_subscription(
            RelativeHumidity,
            '/humidity',
            self.humidity_callback,
            10)
        
        self.pressure = self.create_subscription(
            FluidPressure,
            '/pressure',
            self.pressure_callback,
            10)
        
        self.timer = self.create_timer(1, self.publish_combined_data)

    def temperature_callback(self, msg:Temperature):
         self.temp_val = msg.temperature
         self.temp_var = msg.variance

    def humidity_callback(self, msg:RelativeHumidity):
         self.hum_val = msg.relative_humidity
         self.hum_var = msg.variance     
    
    def pressure_callback(self, msg:FluidPressure):
         self.pressure_val = msg.fluid_pressure
         self.pressure_var = msg.variance

    def publish_combined_data(self):
         readings_val = f'({time()}) Temp = {self.temp_val} ◦ C, Humidity = {self.hum_val * 100} %, Pressure = {self.pressure_val / 1000} hPa.'
         self.get_logger().info(f' Temp = {self.temp_val} ◦ C, Humidity = {self.hum_val * 100} %, Pressure = {self.pressure_val / 1000} hPa.')
         save_read(readings_val , "weather.txt")

def main():
    rclpy.init()
    node = Monitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()