#!/usr/bin/env python
import rospy,unittest,rostest
import rosnode
import time

class ledTest(unittest.TestCase):
	def test_node_exist(self):
		nodes = rosnode.get_node_names()
		self.assertIn('/led_node',nodes,"node doesnt exist")

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('led_test_node')
	rostest.rosrun('rumba_ros','led_test_node',ledTest)
