from setuptools import setup

package_name = 'merge_arrays'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tanuj Karavadi',
    maintainer_email='karavadi@wisc.edu',
    description='A node to merge two sorted arrays in ROS2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'merge_arrays_node = merge_arrays.merge_arrays_node:main',
        ],
    },
)
