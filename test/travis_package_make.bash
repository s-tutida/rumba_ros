#! /bin/bash -xve

#sync and make
rsync -av ./ ~/ros_test/src/rumba_ros/
cd ~/ros_test
catkin_make
