import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    urdf_path = '/home/lenovo2204/Documents/AGV/AgvControl/src/urdf/agv.urdf'
    print(f"Path:{urdf_path}")
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='/usr/bin/gzserver',
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='/usr/bin/gzclient',
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',  # Add this line to spawn the AGV
            name='spawn_agv',
            output='screen',
            arguments=[
                '-entity', 'simple_agv',
                '-file', urdf_path,
                '-x', '0', '-y', '0', '-z', '0'
            ],
            parameters=[{
                'robot_description': open('/home/lenovo2204/Documents/AGV/AgvControl/src/urdf/agv.urdf').read()  # Adjust this path
            }]
        ),
        Node(
            package='agv_control',
            executable='controller_node',
            output='screen'
        )
    ])
