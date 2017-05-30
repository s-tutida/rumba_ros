#!/usr/bin/env python
import rospy,unittest,rostest
import rosnode
import time
from rumba_ros.msg import GpioValue

class ledTest(unittest.TestCase):
	def setUp(self):
		self.count = 0
		rospy.Subscriber('/led_pub_node',GpioValue,self.callback)
		self.values = GpioValue()

	def callback(self,data):
		self.count += 1
		self.values = data

	def check_values(self,lf,ls,rf):
		vs = self.values
		self.assertEqual(vs.left_forward, lf , "different value: left_forward")
		self.assertEqual(vs.left_side, ls , "different value: left_side")
		self.assertEqual(vs.right_forward, rf , "different value: right_forward")
		self.assertEqual(vs.right_side, rs , "different value: right_side")
		self.assertEqual(vs.sum_all, lf+ls+rf+rs , "different value: sum_all")
		self.assertEqual(vs.sum_forward, lf+rf , "different value: sum_forward")
	
	def test_node_exist(self):
		nodes = rosnode.get_node_names()
		self.assertIn('/led_pub_node',nodes,"node doesnt exist")
	
	def test_get_value(self):
		rospy.set_param('led_pub_freq',10)
		time.sleep(2)
		with open("/dev/rtlightsensor0","w") as f:
			f.write("-1 0 123 4321\n")

		time.sleep(3)
		self.assertFalse(self.count == 0,"cannot subscribe the topic")
		self.check_values(4321,123,0,-1)
	
	def test_change_paramater(self):
		rospy.set_param('led_pub_freq',1)
		time.sleep(2)
		c_prev = self.count
		time.sleep(3)

		self.assertTrue(self.count < c_prev + 4,"freq does not change")
		self.assertFalse(self.count == c_prev,"Subscriber is stopped")

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('led_test_node')
	rostest.rosrun('rumba_ros','led_test_node',ledTest)
