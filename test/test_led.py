#!/usr/bin/env python
import rospy,unittest,rostest
import rosnode
import time
from std_msgs.msg import UInt16
import actionlib
from rumba_ros.msg import MusicAction,MusicResult,MusicFeedback,MusicGoal

class ledTest(unittest.TestCase):
	def setUp(self):
		self.client = actionlib.SimpleActionClient("music",MusicAction)
		self.device_values = []

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
			self.assertEqual(data,"1234\n","value does not written to rtbuzzer0")

	def test_music(self):
		goal = MusicGoal()
		goal.freqs = [100,200,300,0]
		goal.durations = [2,2,2,2]

		self.client.wait_for_server()
		self.client.send_goal(goal,feedback_cb = self.feedback_cb)
		self.client.wait_for_result()

		self.assertTrue(self.client.get_result(),"invalid result")
		self.assertEqual(gola.freqs,self.device_values,"invalid feedback:" + ",".join([str(e) for e in self.device_values]) )

		self.device_values = []
		self.client.send_goal(goal,feedback_cb = self.feedback_cb)
		self.client.wait_for_result(rospy.Duration.from_sec(0.5))
		
		self.assertFalse(self.client.get_result(),"stop is requested but return true")
		self.assertFalse(gola.freqs==self.device_values,"not stopped" )
		
		

	def feedback_cb(self,feedback):
		with open("/dev/rtbuzzer0","r") as f:
			data = f.readline()
			self.device_values.append(int(data.rstrip()))

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('led_test_node')
	rostest.rosrun('rumba_ros','led_test_node',ledTest)
