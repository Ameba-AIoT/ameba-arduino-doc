BMI270 Calibration NVM
======================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

- `SparkFun 6oF IMU Breakout - BMI270 <https://www.sparkfun.com/sparkfun-6dof-imu-breakout-bmi270-qwiic.html>`__ x 1

Example
-------

Introduction
~~~~~~~~~~~~

This example does some basic calibration of the BMI270 and then allows you to write those calibrations to non volatile memory.

Procedure
~~~~~~~~~

Connect the AMB82-mini to I2C_SDA and I2C_SCL of the sensor as shown in the diagram below.

|image01|

Open the example in :guilabel:`File -> Examples -> AmebaWire -> BMI270 -> CalibrationNVM`

|image02|

Compile and run the example.

|image03|

.. warning:: This chip only allows a total of 14 writes. Be mindful of this limit when recalibrating.

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Calibration_NVM/image01.png
    :width: 916 px
    :height: 724 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Calibration_NVM/image02.png
    :width: 874 px
    :height: 1010 px
    :scale: 80%
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/I2C/BMI270_Calibration_NVM/image03.png
    :width: 1074 px
    :height: 344 px
    :scale: 80%
