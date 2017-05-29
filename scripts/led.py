#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
import RPi.GPIO as GPIO
import time

def write_light(hz=0):
#def write_light(mode=1):
#	GPIO.setmode(GPIO.BCM)
#	GPIO.setup(18,GPIO.OUT)
#	GPIO.output(18,int(mode))
#	time.sleep(1)
#	GPIO.output(18,1-int(mode))
#	GPIO.cleanup()
#	rospy.loginfo(mode)
        gpiofile = "/dev/rtbuzzer0"
	try:
		with open(gpiofile,"w") as f:
			f.write(str(hz) + "\n" )
			rospy.loginfo(data.data)
	except IOError:
		rospy.logerr("cant't write to" + gpiofile)

def recv_light(data):
	write_light(data.data)
	
if __name__ == '__main__':
	rospy.init_node('led_node')
        #when recieve messege from other node, call method of third option 
	rospy.Subscriber("led_node", UInt16, recv_light)
	rospy.spin()

