Materials

AmebaPro2 [AMB82 MINI] x 1

MPU6050 x 1

Example

Introduction

This example will demonstrate getting the raw data from MPU6050.

Procedure

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the
diagram below.

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”->
“MPU6050_raw”.

Compile and run the example. In the Serial Monitor, you should be able
to see the raw data from MPU6050.

If you see that the values are all 0, press reset until you can get
values from MPU6050. If the first initialisation is done properly, the
values will be sent continuously over the I2C interface and will not
cause any hanging issues.

You may choose to uncomment #define OUTPUT_BINARY_ACCELGYRO and comment
#define OUTPUT_READABLE_ACCELGYRO to transmit the raw data faster.

Code Reference

[1] MPU6050 library and examples by ElectronicCats:

https://github.com/ElectronicCats/mpu6050

|image01.png| |image02.png| |image03.png| |image04.png|

.. |image01.png| image:: ../../../_static/_Other_Guides/image01.png
.. |image02.png| image:: ../../../_static/_Other_Guides/image02.png
.. |image03.png| image:: ../../../_static/_Other_Guides/image03.png
.. |image04.png| image:: ../../../_static/_Other_Guides/image04.png
