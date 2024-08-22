Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Any I2C device x 1

Example

**Introduction**

The example will scan the I2C bus for devices that is connected to
Ameba. When a device is found, it will be shown on the serial monitor
with the address of the device.

**Procedure**

Connect any I2C device to I2C_SDA and I2C_SCL of the board.

Open the example in “File” -> “Examples” -> “AmebaWire” ->
“I2C_Scanner”.

|image1|

When the I2C bus detect any I2C device, the serial monitor will show the
address of the I2C device as shown below:

|A screen shot of a computer Description automatically generated|

When there is no I2C device connected to the board, the Arduino IDE
serial monitor will show the message below:

|A screenshot of a computer program Description automatically generated|

Code Reference

You can find detailed information of this example in the documentation
of Arduino:

https://playground.arduino.cc/Main/I2cScanner/

.. |image1| image:: ../../_static/Example_Guides/I2C_-_Scan_I2C_devices/I2C_-_Scan_I2C_devices_images/image01.png
   :width: 6.26806in
   :height: 6.44931in
.. |A screen shot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_Scan_I2C_devices/I2C_-_Scan_I2C_devices_images/image02.png
   :width: 3.29213in
   :height: 7.92819in
.. |A screenshot of a computer program Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_Scan_I2C_devices/I2C_-_Scan_I2C_devices_images/image03.png
   :width: 3.77136in
   :height: 7.93861in
