#!/usr/bin/env python3

#Im just gonna add more commenting after Git commit cuz i was lazy :o
#All using Docker!!!!
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):
    def __init__(self):
        super().__init__('merge_arrays_node')

        # Gets the 2 arrays subscribes
        self.array1_sub = self.create_subscription(
            Int32MultiArray, '/input/array1', self.array1_callback, 10)
        self.array2_sub = self.create_subscription(
            Int32MultiArray, '/input/array2', self.array2_callback, 10)

        # publishes merged array into that node
        self.merged_array_pub = self.create_publisher(
            Int32MultiArray, '/output/array', 10)

        # Initialize arrays to store the incoming data
        self.array1 = []
        self.array2 = []

    # Callback for /input/array1
    def array1_callback(self, msg):
        self.array1 = msg.data
        self.get_logger().info(f'Received array 1: {self.array1}')
        self.merge_and_publish()

    # Callback for /input/array2
    def array2_callback(self, msg):
        self.array2 = msg.data
        self.get_logger().info(f'Received array 2: {self.array2}')
        self.merge_and_publish()

    # Method to merge arrays and publish
    def merge_and_publish(self):
    if self.array1 and self.array2:
        merged_array = sorted(self.array1 + self.array2)
        msg = Int32MultiArray()
        msg.data = merged_array

        self.merged_array_pub.publish(msg)
        self.get_logger().info(f'Merged Array: {merged_array}')
    else:
        self.get_logger().info('Waiting for both arrays to be received.')

#just initializes args and gets the job done
def main(args=None):
    rclpy.init(args=args)
    node = MergeArraysNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
