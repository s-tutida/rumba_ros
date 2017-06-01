#!/usr/bin/env python
import rospy,actionlib
from std_msgs.msg import UInt16
from rumba_ros.msg import MusicAction,MusicResult,MusicFeedback

def write_freq(hz=0):
        gpiofile = "/dev/rtbuzzer0"
	try:
		with open(gpiofile,"w") as f:
			f.write(str(hz) + "\n" )
	except IOError:
		rospy.logerr("cant't write to" + gpiofile)

def exec_music(goal):
	r= MusicResult()
	fb= MusicFeedback()

	for i,f in enumerate(goal.freqs):
		fb.remaining_steps= len(goal.freqs) - i
		music.publish_feedback(fb)

		if music.is_preempt_requested():
			write_freq(0)
			r.finished = False
			music.set_preempted(r)
			return
		write_freq(f)
		rospy.sleep(1.0 if i >= len(goal.durations) else goal.durations[i])

	r.finished = True
	music.set_succeeded(r)

def recv_light(data):
	write_freq(data.data)

if __name__ == '__main__':
	rospy.init_node('led_node')
        #when recieve messege from other node, call method of third option 
	rospy.Subscriber("led_node", UInt16, recv_light)
	music = actionlib.SimpleActionServer('music',MusicAction,exec_music,False)
	music.start()
	rospy.on_shutdown(write_freq)
	rospy.spin()

