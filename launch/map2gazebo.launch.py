from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

import os

def generate_launch_description():

    bringup_dir = get_package_share_directory('map2gazebo')
    launch_dir  = os.path.join(bringup_dir, 'launch')

    params_file = LaunchConfiguration('params_file')
    export_dir  = LaunchConfiguration('export_dir')

    return LaunchDescription([
        DeclareLaunchArgument(
            'params_file', 
            default_value=os.path.join(bringup_dir, 'config', 'defaults.yaml'),
            description='Full Path to ROS2 Parameters file'),
        
        DeclareLaunchArgument(
            'export_dir', 
            default_value=os.path.join(bringup_dir, 'models', 'map', 'meshes'),
            description='Full Path to export Directory'),

        Node(
            package='map2gazebo',
            executable='map2gazebo',
            output='screen',
            parameters=[params_file, {'export_dir': export_dir}],
        )
    ])
