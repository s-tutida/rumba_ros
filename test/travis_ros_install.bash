#! /bin/bash -xve

#required packages
pip install catkin_pkg
pip install empy
pip install pyyaml
pip install rospkg

#ros install
cd ..
git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server.git
cd ./ros_setup_scripts_Ubuntu14.04_server
bash ./step0.bash
bash ./step1.bash

#catkin setup
mkdir -p ~/ros_test/src
cd ~/ros_test/src
source /opt/ros/indigo/setup.bash
catkin_init_workspace
cd ~/ros_test
catkin_make
