Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  MPU6050 x 1

Example

**Introduction**

This example will demonstrate getting the raw data from MPU6050.

**Procedure**

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the
diagram below.

|image1|

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”->
“MPU6050_raw”.

|A screenshot of a computer Description automatically generated|

Compile and run the example. In the Serial Monitor, you should be able
to see the raw data from MPU6050.

|image2|

If you see that the values are all 0, press reset until you can get
values from MPU6050. If the first initialisation is done properly, the
values will be sent continuously over the I2C interface and will not
cause any hanging issues.

You may choose to uncomment #define OUTPUT_BINARY_ACCELGYRO and comment
#define OUTPUT_READABLE_ACCELGYRO to transmit the raw data faster.

|A screenshot of a computer program Description automatically generated|

Code Reference

[1] MPU6050 library and examples by ElectronicCats:

https://github.com/ElectronicCats/mpu6050

.. |image1| image:: ../../_static/Example_Guides/I2C_-_MPU6050_Raw_Data/I2C_-_MPU6050_Raw_Data_images/image01.png
   :width: 5.15925in
   :height: 3.74074in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_Raw_Data/I2C_-_MPU6050_Raw_Data_images/image02.png
   :width: 5.9114in
   :height: 6.03976in
.. |image2| image:: ../../_static/Example_Guides/I2C_-_MPU6050_Raw_Data/I2C_-_MPU6050_Raw_Data_images/image03.png
   :width: 3.04687in
   :height: 2.12377in
.. |A screenshot of a computer program Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_Raw_Data/I2C_-_MPU6050_Raw_Data_images/image04.png
   :width: 6.26806in
   :height: 2.01806in
