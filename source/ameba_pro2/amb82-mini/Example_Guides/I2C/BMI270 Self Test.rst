BMI270 Self Test
================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

- `SparkFun 6oF IMU Breakout - BMI270 <https://www.sparkfun.com/sparkfun-6dof-imu-breakout-bmi270-qwiic.html>`__ x 1

Example
-------

Introduction
~~~~~~~~~~~~

This example will run the sensor's self test feature. This will return an error code to indicate whether the test was successful.

Procedure
~~~~~~~~~

Connect the AMB82-mini to I2C_SDA and I2C_SCL of the sensor as shown in the diagram below.

|image01|

Open the example in "File" -> "Examples" -> "AmebaWire" -> "BMI270" -> "SelfTest".

|image02|

Compile and run the example.

The error code will be printed out if the test was unsuccessful.

|image03|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Self_Test/image01.png
    :width: 916 px
    :height: 724 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Self_Test/image02.png
    :width: 794 px
    :height: 1002 px
    :scale: 80%
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Self_Test/image03.png
    :width: 334 px
    :height: 78 px
