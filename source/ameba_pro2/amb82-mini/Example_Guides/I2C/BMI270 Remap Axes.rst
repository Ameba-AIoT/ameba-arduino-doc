BMI270 Remap Axes
=================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

- `SparkFun 6oF IMU Breakout - BMI270 <https://www.sparkfun.com/sparkfun-6dof-imu-breakout-bmi270-qwiic.html>`__ x 1

Example
-------

Introduction
~~~~~~~~~~~~

This example shows how to remap IMU axis directions.

Procedure
~~~~~~~~~

Connect the AMB82-mini to I2C_SDA and I2C_SCL of the sensor as shown in the diagram below.

|image01|

Open the example in "File" -> "Examples" -> "AmebaWire" -> "BMI270" -> "RemapAxes".

|image02|

Compile and run the example.

The remapped axes measurements from the sensor will be printed out at 20ms interval.

|image03|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Remap_Axes/image01.png
    :width: 916 px
    :height: 724 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Remap_Axes/image02.png
    :width: 785 px
    :height: 1008 px
    :scale: 80%
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Remap_Axes/image03.png
    :width: 1090 px
    :height: 615 px
    :scale: 80%
