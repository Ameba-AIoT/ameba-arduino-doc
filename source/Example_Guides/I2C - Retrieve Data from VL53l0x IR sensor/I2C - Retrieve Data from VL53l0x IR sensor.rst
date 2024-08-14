Materials

AmebaPro2 [AMB82 MINI] x 1

VL53l0x IR sensor x 1

Example

Introduction This example will illustrate how to retrieve the value of
VL53l0x IR sensor and pass it to the AMB82-Mini board. VL53L0X Distance
Sensor is a Time-of-Flight (ToF) ranging module based on the VL53L0X
from ST, with accurate ranging up to 2m, which can be controlled via I2C
interface and has pretty low power consumption.

This guide will be the same for these 2 examples:

1) Continuous.ino

2) Single.ino

Procedure

Connect the VL53l0x IR sensor to I2C_SDA and I2C_SCL of the board as
shown in the diagram below.

Open the example in “File” -> “Examples” -> “AmebaWire” -> “VL53L0x” ->
“Continuous” OR “Single”.

You will choose “Single” if you want to get single-shot range
measurements from the VL53L0X sensor. The sensor can be optionally be
configured with different ranging profiles to get better performance for
a certain application.

For both examples, the Serial Monitor will output the range measurements
as shown in the below image. It will output 8190 if there is no object
within 2m range.

Code Reference

[1] VL53l0x library and examples by Pololu:

https://github.com/pololu/vl53l0x-arduino

|image01.png| |image02.png| |image03.png|

.. |image01.png| image:: ../../../_static/_Other_Guides/image01.png
.. |image02.png| image:: ../../../_static/_Other_Guides/image02.png
.. |image03.png| image:: ../../../_static/_Other_Guides/image03.png
