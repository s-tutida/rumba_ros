#!/usr/bin/env python
import rospy,unittest,rostest
import rosnode
import time
from std_msgs.msg import UInt16

class ledTest(unittest.TestCase):
	def test_node_exist(self):
		nodes = rosnode.get_node_names()
		self.assertIn('/led_node',nodes,"node doesnt exist")
	
	def test_put_value(self):
		pub = rospy.Publisher('/led_node',UInt16)
		for i in range(10):
			pub.publish(1234)
			time.sleep(0.1)
		with open("/dev/rtbuzzer0","r") as f:
			data = f.readline()
			self.assertEqual(data,"1235\n","value does not written to rtbuzzer0")


if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('led_test_node')
	rostest.rosrun('rumba_ros','led_test_node',ledTest)
