source /opt/ros/humble/setup.bash

check_urdf /home/lenovo2204/Documents/AGV/src/agv_control/urdf/agv.urdf
colcon build

source install/setup.bash
ros2 launch agv_control agv_launch.py


export TURTLEBOT3_MODEL=burger  # or waffle
ls /opt/ros/humble/share/turtlebot3_gazebo/launch
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
