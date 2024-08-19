Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  MPU6050 x 1

Example

**Introduction**

This example will demonstrate getting the data from MPU6050 with DMP6.
MPU6050 is equipped with a Digital Motion Processor (DMP) to handle the
calculations of motion algorithms such as conversion to 3-axis
yaw/pitch/roll of planes, conversion to quaternion, or conversion to
Euler angle. In addition, this example will calculate world-frame
acceleration, adjusted to remove gravity, and rotated based on known
orientation from quaternion.

**Procedure**

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the
diagram below.

|image1|

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”->
“MPU6050_DMP6_ImuData_for_ROS.ino”.

|A screenshot of a computer Description automatically generated|

Compile and run the example. In the Serial Monitor, you should be able
to see the output of quaternion, world-frame acceleration, world-frame
gyro values and yaw/pitch/roll values.

|image2|

Code Reference

[1] MPU6050 library and examples by ElectronicCats:

https://github.com/ElectronicCats/mpu6050

.. |image1| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6_ImuData_for_ROS/I2C_-_MPU6050_ImuData_for_ROS_images/image01.png
   :width: 5.15925in
   :height: 3.74074in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6_ImuData_for_ROS/I2C_-_MPU6050_ImuData_for_ROS_images/image02.png
   :width: 6.26806in
   :height: 6.31597in
.. |image2| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6_ImuData_for_ROS/I2C_-_MPU6050_ImuData_for_ROS_images/image03.png
   :width: 5.70657in
   :height: 2.96836in
