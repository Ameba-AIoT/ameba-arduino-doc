Materials

-  AmebaPro2 [AMB82 MINI] x 1

Procedure

There three common encryption type in WiFi connection. The first one is
“OPEN”, which means there is no password needed to connect to this
network. The second type of encryption is WPA, which requires the
correct password to access. The third type is WEP, which requires a
hexadecimal password and a keyindex.

In the following, we will give a brief introduction on how to establish
WiFi connection with these three types of encryptions on Ameba.

First, make sure the correct Ameba development board is selected in
“Tools” -> “Board”.

-  Open (WiFi connection without password)

Open example in “File” -> “Examples” -> “WiFi” -> “ConnectToWiFi” ->
“NoEncryption”

|Text Description automatically generated|

In the sample code, modify “ssid” to be the same as the WiFi SSID to be
connected to.

Next, upload the sample code, and press the reset button on Ameba. Then
you will see a message “You’re connected to the networkSSID: XXXXX”, and
the information of this WiFi connection is printed in the serial monitor
every 10 seconds.

|Graphical user interface, text, application, email Description
automatically generated|

-  **WiFi connection with WPA encryption**

Open example in “File” -> “Examples” -> “WiFi” -> “ConnectToWiFi” ->
“WPA_Security”

|Graphical user interface, text, email Description automatically
generated|

In the sample code, modify “ssid” to the WiFi SSID to be connected to
and “pass” to the network password.

If you prefer to enter your SSID & password in the Serial monitor while
the program is running, uncomment #define MANUAL_INPUT at the top of the
file.

|image1|

Next, upload the sample code, and press the reset button on Ameba. Then
you will see a message “You’re connected to the networkSSID: XXXXX”, and
the information of this WiFi connection is printed in the serial monitor
every 10 seconds.

Note: If you enabled MANUAL_INPUT, after uploading the sample code and
pressing the reset button on Ameba, input your SSID in the Serial
monitor and press enter. Next, input your password, and press enter.
Then you will see a message “You’re connected to the networkSSID:
XXXXX”, and the information of this WiFi connection is printed in the
serial monitor every 10 seconds.

|image2|

-  **WiFi connection with WEP encryption**

Open example in “File” -> “Examples” -> “WiFi” -> “ConnectToWiFi” ->
“WEP_Security”

|image3|

In the sample code, modify “ssid” to the SSID to be connected, “key” to
the hexadecimal password, “keyIndex” to your key index number.

If you prefer to enter your SSID & password in the Serial monitor while
the program is running, uncomment #define MANUAL_INPUT at the top of the
file.

|image4|

Next, upload the sample code, and press the reset button on Ameba. Then
you will see a message “You’re connected to the networkSSID: XXXXX”, and
the information of this WiFi connection is printed in the IDE every 10
seconds.

Note: If you enabled MANUAL_INPUT, after uploading the sample code and
pressing the reset button on Ameba, input your SSID in the Serial
monitor and press enter. Next, input your key and press enter. Finally
enter your password and press enter. Then you will see a message “You’re
connected to the networkSSID: XXXXX”, and the information of this WiFi
connection is printed in the serial monitor every 10 seconds.

|Graphical user interface, text, application Description automatically
generated|

Code Reference

| https://www.arduino.cc/en/Reference/WiFiBegin
| To get the information of a WiFi connection:
| Use WiFi.SSID() to get SSID of the current connected network.
| https://www.arduino.cc/en/Reference/WiFiSSID
| Use WiFi.RSSI() to get the signal strength of the connection.
| https://www.arduino.cc/en/Reference/WiFiRSSI
| Use WiFi.encryptionType() to get the encryption type of the WiFi
  connection.
| https://www.arduino.cc/en/Reference/WiFiEncryptionType
| Use WiFi.BSSID() to get the MAC address of the router you are
  connected to.
| https://www.arduino.cc/en/Reference/WiFiBSSID
| To get the information of Ameba:
| Use WiFi.macAddress() to get the MAC address of Ameba.
| https://www.arduino.cc/en/Reference/WiFiMACAddress
| Use WiFi.localIP() to get the IP address of Ameba.
| https://www.arduino.cc/en/Reference/WiFiLocalIP
| Use WiFi.subnetMask() to get the subnet mask.
| https://www.arduino.cc/en/Reference/WiFiSubnetMask
| Use WiFi.gatewayIP() to get the WiFi shield’s gateway IP address.
| https://www.arduino.cc/en/Reference/WiFiGatewayIP

Comparison with Arduino

| In the Arduino platform, we need to add an extra WiFi shield to be the
  WiFi module to realize the WiFi connection. And we must #include to
  use SPI to communicate with WiFi module.
| However, Ameba is already equipped with WiFi module. Therefore,
  #include is not needed.

.. |Text Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image01.png
   :width: 6.26806in
   :height: 7.2625in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image02.png
   :width: 6.26806in
   :height: 7.30486in
.. |Graphical user interface, text, email Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image03.png
   :width: 6.26806in
   :height: 6.29167in
.. |image1| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image04.png
   :width: 6.26806in
   :height: 5.45278in
.. |image2| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image05.png
   :width: 6.26806in
   :height: 7.67986in
.. |image3| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image06.png
   :width: 6.26875in
   :height: 6.82083in
.. |image4| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image07.png
   :width: 6.26806in
   :height: 6.16458in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Connect_to_WiFi/WiFi_-_Connect_to_WiFi_images/image08.png
   :width: 6.26806in
   :height: 5.31042in
