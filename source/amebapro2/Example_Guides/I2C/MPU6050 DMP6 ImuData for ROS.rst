MPU6050 DMP6 ImuData for ROS
============================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  MPU6050 x 1

Example
-------

Introduction
------------

This example will demonstrate getting the data from MPU6050 with DMP6.
MPU6050 is equipped with a Digital Motion Processor (DMP) to handle the
calculations of motion algorithms such as conversion to 3-axis
yaw/pitch/roll of planes, conversion to quaternion, or conversion to
Euler angle. In addition, this example will calculate world-frame
acceleration, adjusted to remove gravity, and rotated based on known
orientation from quaternion.

Procedure
---------

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the diagram below.

|image01|

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”-> “MPU6050_DMP6_ImuData_for_ROS.ino”.

|image02|

Compile and run the example. In the Serial Monitor, you should be able
to see the output of quaternion, world-frame acceleration, world-frame
gyro values and yaw/pitch/roll values.

|image03|

Code Reference
--------------

| [1] MPU6050 library and examples by ElectronicCats:
| https://github.com/ElectronicCats/mpu6050

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/I2C/MPU6050_DMP6_Imu_Data_for_ROS/image01.png
   :width: 1186 px
   :height: 860 px
   :scale: 70%
.. |image02| image:: ../../../_static/amebapro2/Example_Guides/I2C/MPU6050_DMP6_Imu_Data_for_ROS/image02.png
   :width: 602 px
   :height: 606 px
.. |image03| image:: ../../../_static/amebapro2/Example_Guides/I2C/MPU6050_DMP6_Imu_Data_for_ROS/image03.png
   :width: 546 px
   :height: 284 px
