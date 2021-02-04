from setuptools import setup, find_packages

package_name = 'map2gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'nav_msgs'],
    zip_safe=True,
    maintainer='Moritz Willmann',
    maintainer_email='moritz.willmann@uni-ulm.de',
    description='The map2gazebo package for ros2',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'src.map2gazebo:main'
        ],
    },
)
