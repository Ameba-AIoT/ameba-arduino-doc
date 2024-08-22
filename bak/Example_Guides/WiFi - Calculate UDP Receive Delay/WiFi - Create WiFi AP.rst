In AP mode, Ameba can accept at most 3 station connections, and can be
set to open mode or WPA2 mode.

Preparation

-  AmebaPro2 [AMB82 MINI] x 1

Example

In this example, we turn on the AP mode of Ameba and connect station to
Ameba.

:mark:`Open example, “File” -> “Examples” -> “WiFi” -> “CreateWiFiAP”`

|Graphical user interface, text, application, email Description
automatically generated|

In the highlighted code snippet, fill in your SSID, PASSWORD and
CHANNEL.

:mark:`If you prefer to enter your SSID & password in the Serial monitor
while the program is running, uncomment #define MANUAL_INPUT at the top
of the file.`

|image1|

:mark:`Note: If you enabled MANUAL_INPUT, after uploading the sample
code and pressing the reset button on Ameba, input your SSID in the
Serial monitor and press enter. Next, input your password and press
enter. AP mode should start after that.`

|image2|

The code highlighted is the API we used to turn on the AP mode in
security mode.

If you want to turn on the AP mode in open mode, please modify the code
to status = WiFi.apbegin(ssid, channel);

Then upload the sample code and press reset, and you can see related
information shown in serial monitor.

|image3|

In the figure below, we show the messages shown in serial monitor when
two stations connect to Ameba AP in open mode:

|image4|

In the figure below, we show the messages shown in serial monitor when a
station connects to Ameba AP in security mode:

|Graphical user interface, text, application Description automatically
generated|

.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Create_WiFi_AP/WiFi_-_Create_WiFi_AP_images/image01.png
   :width: 6.26806in
   :height: 6.75625in
.. |image1| image:: ../../_static/Example_Guides/WiFi_-_Create_WiFi_AP/WiFi_-_Create_WiFi_AP_images/image02.png
   :width: 6.26806in
   :height: 6.76667in
.. |image2| image:: ../../_static/Example_Guides/WiFi_-_Create_WiFi_AP/WiFi_-_Create_WiFi_AP_images/image03.png
   :width: 6.26806in
   :height: 7.56597in
.. |image3| image:: ../../_static/Example_Guides/WiFi_-_Create_WiFi_AP/WiFi_-_Create_WiFi_AP_images/image04.png
   :width: 6.26806in
   :height: 7.32708in
.. |image4| image:: ../../_static/Example_Guides/WiFi_-_Create_WiFi_AP/WiFi_-_Create_WiFi_AP_images/image05.png
   :width: 4.97917in
   :height: 5.83333in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Create_WiFi_AP/WiFi_-_Create_WiFi_AP_images/image06.png
   :width: 5.84375in
   :height: 7.41667in
