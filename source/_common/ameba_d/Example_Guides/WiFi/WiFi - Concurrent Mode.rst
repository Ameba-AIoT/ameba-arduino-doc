WiFi - Concurrent Mode
=======================

.. contents::
  :local:
  :depth: 2

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 / AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

Example
---------

WiFi concurrent mode, also known as AP + Station mode, is a feature that allows devices to operate simultaneously as an Access point and a Station. In this example, the Ameba board can connect to an existing wireless network while providing wireless connectivity to other devices.

First, open the example in “File” -> “Examples” -> “WiFi” -> “ConcurrentMode”.

In the sample code, fill in your SSID, PASSWORD, AP SSID, AP PASSWORD and CHANNEL.

|image01|

If you prefer to enter all the information in the Serial monitor while the program is running, uncomment #define MANUAL_INPUT

Note: If you enabled MANUAL_INPUT, after uploading the sample code and pressing the reset button on Ameba, input your SSID, Password, AP SSID, AP Password and channel. The AP mode should start first.

For Ameba boards, there is a limitation that the AP mode must be the same channel as the WiFi station mode. To see the channel, you may download NetSpot software : https://www.netspotapp.com/download-win.html

Next upload the sample code and press the reset button on Ameba. You will be able to see AP mode start first.

The code by default turn on the AP mode in security mode. If you want to turn on the AP mode in open mode, please modify the code to status = WiFi.apbegin(ssid, channel);

|image02|

Next, you will see the information of the AP mode shown, and after that you will see a message “Connected to the network”, and the information of this WiFi connection is printed in the serial monitor every 10 seconds.

|image03|

In the figure below, this message will appear in the serial monitor when a device is connected to the AP:

|image04|

Comparison with Arduino
------------------------
In the Arduino platform, we need to add an extra WiFi shield to be the WiFi module to realize the WiFi connection. And we must #include to use SPI to communicate with WiFi module.

However, Ameba is already equipped with WiFi module. Therefore, #include is not needed.


.. |image01| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Concurrent_Mode/image01.png
   :width:  509 px
   :height:  119 px
.. |image02| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Concurrent_Mode/image02.png
   :width:  1013 px
   :height:  224 px
.. |image03| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Concurrent_Mode/image03.png
   :width:  1017 px
   :height:  223 px
.. |image04| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Concurrent_Mode/image04.png
   :width:  1013 px
   :height:  366 px
   