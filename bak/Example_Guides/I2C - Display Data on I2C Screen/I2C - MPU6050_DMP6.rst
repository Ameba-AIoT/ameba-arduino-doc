Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  MPU6050 x 1

Example

**Introduction**

This example will demonstrate getting the data from MPU6050 with DMP6.
MPU6050 is equipped with a Digital Motion Processor (DMP) to handle the
calculations of motion algorithms such as conversion to 3-axis
yaw/pitch/roll of planes, conversion to quaternion, or conversion to
Euler angle.

| This guide will be the same for these 2 examples:
| 1) MPU6050_DMP6.ino
| 2) MPU6050_DMP6_using_DMP_V6v12.ino

The difference between these two examples is the DMP library being used.
For MPU6050_DMP6.ino, the DMP library version is 2.0. For
MPU6050_DMP6_using_DMP_V6v12.ino, the DMP library version is 6.12.

**Procedure**

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the
diagram below.

|image1|

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”->
“MPU6050_DMP6” **OR** “MPU6050_DMP6_using_DMP_V6v12”

|A screenshot of a computer Description automatically generated|

Compile and run the example. In the Serial Monitor, you should be able
to see the prompt to begin DMP programming. Key in any character on the
serial monitor and press ‘Enter’.

|A screenshot of a computer program Description automatically generated|

You should be able to see the output values calculated by the DMP.

|image2|

You can choose to uncomment either one of the options to see the type of
data to be printed out. The options are OUTPUT_READABLE_QUATERNION,
OUTPUT_READABLE_EULER, OUTPUT_READABLE_YAWPITCHROLL,
OUTPUT_READABLE_REALACCEL, OUTPUT_READABLE_WORLDACCEL and OUTPUT_TEAPOT.
In this example, the option used is OUTPUT_READABLE_YAWPITCHROLL.

The original example by ElectronicCats uses interrupt pin. Using
Interrupt pin will cause MPU6050 to hang, so this example can only work
reliably if no interrupt pin is used.

Code Reference

[1] MPU6050 library and examples by ElectronicCats:

https://github.com/ElectronicCats/mpu6050

.. |image1| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6/I2C_-_MPU6050_DMP6_images/image01.png
   :width: 4.54167in
   :height: 3.29296in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6/I2C_-_MPU6050_DMP6_images/image02.png
   :width: 6.26806in
   :height: 5.63403in
.. |A screenshot of a computer program Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6/I2C_-_MPU6050_DMP6_images/image03.png
   :width: 3.86883in
   :height: 2.55502in
.. |image2| image:: ../../_static/Example_Guides/I2C_-_MPU6050_DMP6/I2C_-_MPU6050_DMP6_images/image04.png
   :width: 6.26806in
   :height: 2.55208in
