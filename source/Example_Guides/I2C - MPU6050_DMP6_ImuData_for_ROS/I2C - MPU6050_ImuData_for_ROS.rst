Materials

AmebaPro2 [AMB82 MINI] x 1

MPU6050 x 1

Example

Introduction

This example will demonstrate getting the data from MPU6050 with DMP6.
MPU6050 is equipped with a Digital Motion Processor (DMP) to handle the
calculations of motion algorithms such as conversion to 3-axis
yaw/pitch/roll of planes, conversion to quaternion, or conversion to
Euler angle. In addition, this example will calculate world-frame
acceleration, adjusted to remove gravity, and rotated based on known
orientation from quaternion.

Procedure

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the
diagram below.

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”->
“MPU6050_DMP6_ImuData_for_ROS.ino”.

Compile and run the example. In the Serial Monitor, you should be able
to see the output of quaternion, world-frame acceleration, world-frame
gyro values and yaw/pitch/roll values.

Code Reference

[1] MPU6050 library and examples by ElectronicCats:

https://github.com/ElectronicCats/mpu6050

|image01.png| |image02.png| |image03.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_I2C%20-%20MPU6050_DMP6_ImuData_for_ROS/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_I2C%20-%20MPU6050_DMP6_ImuData_for_ROS/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_I2C%20-%20MPU6050_DMP6_ImuData_for_ROS/image03.png
