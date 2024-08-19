Materials

-  AmebaPro2 [AMB82 MINI] x 1

Procedure

WiFi concurrent mode, also known as AP + Station mode, is a feature that
allows devices to operate simultaneously as an Access point and a
Station. In this example, the Ameba board can connect to an existing
wireless network while providing wireless connectivity to other devices.

First, open the example in “File” → “Examples” → “WiFi” →
“ConcurrentMode” .

|Graphical user interface, application Description automatically
generated|

In the sample code, fill in your SSID, PASSWORD, AP SSID, AP PASSWORD
and CHANNEL.

|image1|

If you prefer to enter all the information in the Serial monitor while
the program is running, uncomment #define MANUAL_INPUT

Note: If you enabled MANUAL_INPUT, after uploading the sample code and
pressing the reset button on Ameba, input your SSID, Password, AP SSID,
AP Password and channel. The AP mode should start first.

For Ameba boards, there is a limitation that the AP mode must be the
same channel as the WiFi station mode. To see the channel, you may
download NetSpot software : https://www.netspotapp.com/download-win.html

|image2|

Next upload the sample code and press the reset button on Ameba. You
will be able to see AP mode start first.

|image3|

The code by default turn on the AP mode in security mode. If you want to
turn on the AP mode in open mode, please modify the code to status =
WiFi.apbegin(ssid, channel);

|Graphical user interface, text, application Description automatically
generated|

Next, you will see the information of the AP mode shown, and after that
you will see a message “Connected to the network”, and the information
of this WiFi connection is printed in the serial monitor every 10
seconds.

In the figure below, this message will appear in the serial monitor when
a device is connected to the AP:

|Graphical user interface, text, application, email Description
automatically generated|

Comparison with Arduino

| In the Arduino platform, we need to add an extra WiFi shield to be the
  WiFi module to realize the WiFi connection. And we must #include to
  use SPI to communicate with WiFi module.
| However, Ameba is already equipped with WiFi module. Therefore,
  #include is not needed.

.. |Graphical user interface, application Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Concurrent_Mode/WiFi_-_Concurrent_Mode_images/image01.png
   :width: 6.26806in
   :height: 5.58542in
.. |image1| image:: ../../_static/Example_Guides/WiFi_-_Concurrent_Mode/WiFi_-_Concurrent_Mode_images/image02.png
   :width: 6.17075in
   :height: 3.5in
.. |image2| image:: ../../_static/Example_Guides/WiFi_-_Concurrent_Mode/WiFi_-_Concurrent_Mode_images/image03.png
   :width: 6.65071in
   :height: 0.96968in
.. |image3| image:: ../../_static/Example_Guides/WiFi_-_Concurrent_Mode/WiFi_-_Concurrent_Mode_images/image04.png
   :width: 6.26806in
   :height: 2.07431in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Concurrent_Mode/WiFi_-_Concurrent_Mode_images/image5.PNG
   :width: 6.26806in
   :height: 2.77639in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Concurrent_Mode/WiFi_-_Concurrent_Mode_images/image06.png
   :width: 6.26806in
   :height: 2.49444in
