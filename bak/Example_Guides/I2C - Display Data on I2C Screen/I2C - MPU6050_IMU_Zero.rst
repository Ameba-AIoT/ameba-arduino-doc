Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  MPU6050 x 1

Example

**Introduction**

This example will demonstrate how to do calibration for the MPU6050 IMU.

**Procedure**

Connect the MPU6050 to I2C_SDA and I2C_SCL of the board as shown in the
diagram below.

|image1|

Open the example in “File” -> “Examples” -> “AmebaWire” -> “MPU6050”->
“MPU6050_IMU_Zero”

|A screenshot of a computer Description automatically generated|

If an MPU6050

\* is an ideal member of its tribe,

\* is properly warmed up,

\* is at rest in a neutral position,

\* is in a location where the pull of gravity is exactly 1g, and

\* has been loaded with the best possible offsets,

then it will report 0 for all accelerations and displacements, except
for Z acceleration, for which it will report 16384 (that is, 2^14). Your
device probably won't do quite this well, but good offsets will all get
the baseline outputs close to these target values. Put the MPU6050 on a
flat and horizontal surface and leave it operating for 5-10 minutes so
its temperature gets stabilized.

| Compile and run this example. A "----- done -----" line will indicate
  that it has done its best. With the current accuracy-related constants
  (NFast = 1000, NSlow = 10000), it will take a few minutes to get
  there. Along the way, it will generate a dozen or so lines of output,
  showing that for each of the 6 desired offsets, it is
| \* first, trying to find two estimates, one too low and one too high,
  and
| \* then, closing in until the bracket can't be made smaller.

The line just above the "done" line will look something like [567,567]
--> [-1,2] [-2223,-2223] --> [0,1] [1131,1132] --> [16374,16404]
[155,156] --> [-1,1] [-25,-24] --> [0,3] [5,6] --> [0,4].

| As will have been shown in interspersed header lines, the six groups
  making up this
| line describe the optimum offsets for the X acceleration, Y
  acceleration, Z acceleration,
| X gyro, Y gyro, and Z gyro, respectively. In the sample shown just
  above, the trial showed
| that +567 was the best offset for the X acceleration, -2223 was best
  for Y acceleration,
| and so on.

Below shows the Serial Monitor output for running this example.

|A screen shot of a computer Description automatically generated|

|A black and white screen with white text Description automatically
generated with medium confidence|

Code Reference

[1] MPU6050 library and examples by ElectronicCats:

https://github.com/ElectronicCats/mpu6050

.. |image1| image:: ../../_static/Example_Guides/I2C_-_MPU6050_IMU_Zero/I2C_-_MPU6050_IMU_Zero_images/image01.png
   :width: 4.54167in
   :height: 3.29296in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_IMU_Zero/I2C_-_MPU6050_IMU_Zero_images/image02.png
   :width: 6.26806in
   :height: 4.85in
.. |A screen shot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_MPU6050_IMU_Zero/I2C_-_MPU6050_IMU_Zero_images/image03.png
   :width: 6.26806in
   :height: 2.68125in
.. |A black and white screen with white text Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/I2C_-_MPU6050_IMU_Zero/I2C_-_MPU6050_IMU_Zero_images/image04.png
   :width: 6.26806in
   :height: 2.44444in
