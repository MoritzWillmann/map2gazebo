from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'map2gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'models', 'map'), ['models/map/model.config', 'models/map/model.sdf']),
        (os.path.join('share', package_name, 'models', 'map', 'meshes'), ['models/map/meshes/map.stl']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Moritz Willmann',
    maintainer_email='moritz.willmann@uni-ulm.de',
    description='The map2gazebo package for ros2',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'map2gazebo = map2gazebo.map2gazebo:main'
        ],
    },
)
