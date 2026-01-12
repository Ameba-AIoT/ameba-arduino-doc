BMI270 Filtering
================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

- `SparkFun 6oF IMU Breakout - BMI270 <https://www.sparkfun.com/sparkfun-6dof-imu-breakout-bmi270-qwiic.html>`__ x 1

Example
-------

Introduction
~~~~~~~~~~~~

This example shows how to configure the accelerometer and gyroscope with multiple settings to reduce the measurement noise.

Procedure
~~~~~~~~~

Connect the AMB82-mini to I2C_SDA and I2C_SCL of the sensor as shown in the diagram below.

|image01|

Open the example in "File" -> "Examples" -> "AmebaWire" -> "BMI270" -> "Filtering".

|image02|

Compile and run the example.

The measurements from the sensor will be printed at 20ms interval.

|image03|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Filtering/image01.png
    :width: 916 px
    :height: 724 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Filtering/image02.png
    :width: 778 px
    :height: 1013 px
    :scale: 80%
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Filtering/image03.png
    :width: 1074 px
    :height: 343 px
    :scale: 80%
