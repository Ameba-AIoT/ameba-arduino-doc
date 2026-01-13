USB - CDC Serial Port
=======================

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23] x 1

- USB host device [Windows / Linux / MacOS]

- USB cable x 2

Example
--------

In this example, the RTL8722 board emulates a CDC ACM virtual COM-port connected using USB.

**USB connection**

Two USB ports will be used simultaneously, thus two USB cables are required for this example. In addition to the regular USB port used for uploading code, the second USB cable should be connected to the USB OTG port as shown below.

For AMB23, connect the second USB cable to the USB port in the red box.

|image01|

Open the example, :guilabel:`Files -> Examples -> AmebaUSB -> USBCDCSerial`

|image05|

Upload the code and press the reset button once the upload is finished. Open the Arduino serial monitor.

Immediately after reset, a second COM port should become available. On your host device, open a terminal application (e.g., Teraterm) and connect to this new COM port.

Any message sent on the Arduino serial monitor should appear on the terminal application. Similarly, any message sent on the terminal application should appear in Arduino serial monitor.

|image06|

|image07|

Code Reference
----------------

The SerialUSB class can be used in the same way as the familiar Serial class, and supports all the same print features.

.. |image01| image:: ../../../../_static/amebad/Example_Guides/USB/USB_CDC_Serial_Port/image01.png
   :width: 2190
   :height: 3532
   :scale: 20%

.. |image05| image:: ../../../../_static/amebad/Example_Guides/USB/USB_CDC_Serial_Port/image05.png
   :width: 640
   :height: 950

.. |image06| image:: ../../../../_static/amebad/Example_Guides/USB/USB_CDC_Serial_Port/image06.png
   :width: 671
   :height: 357

.. |image07| image:: ../../../../_static/amebad/Example_Guides/USB/USB_CDC_Serial_Port/image07.png
   :width: 671
   :height: 357
