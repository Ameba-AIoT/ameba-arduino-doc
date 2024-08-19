Materials

-  AmebaPro2 [AMB82 MINI] x 1

Example

| In this example, we use Ameba to be a web client to retrieve
  information from the Internet.
| First, make sure the correct Ameba development board is selected in
  “Tools” -> “Board”

Then open “File” -> “Examples” -> “WiFi” -> “SimpleHttpRequest”

|Graphical user interface, application Description automatically
generated|

In the sample code, modify the highlighted snippet and enter the
required information (ssid, password, key index) required to connect to
your WiFi network.

|Graphical user interface, text, application Description automatically
generated|

Upload the code and press the reset button on Ameba. Then you can see
the information retrieved from Google is shown in the Arduino serial
monitor.

|4-3|

Code Reference

| https://www.arduino.cc/en/Reference/WiFiBegin
| To get the information of a WiFi connection: Use WiFi.SSID() to get
  SSID of the current connected network.
| https://www.arduino.cc/en/Reference/WiFiSSID
| Use WiFi.RSSI() to get the signal strength of the connection.
| https://www.arduino.cc/en/Reference/WiFiRSSI
| Use WiFi.localIP() to get the IP address of Ameba.
| https://www.arduino.cc/en/Reference/WiFiLocalIP
| Use WiFiClient() to create a client.
| https://www.arduino.cc/en/Reference/WiFiClient
| Use client.connect() to connect to the IP address and port specified.
| https://www.arduino.cc/en/Reference/WiFiClientConnect
| Use client.println() to print data followed by a carriage return and
  newline.
| https://www.arduino.cc/en/Reference/WiFiClientPrintln
| Use client.available() to return the number of bytes available for
  reading.
| https://www.arduino.cc/en/Reference/WiFiClientAvailable
| Use client.read() to read the next byte received from the server the
  client is connected to.
| https://www.arduino.cc/en/Reference/WiFiClientRead
| Use client.stop() to disconnect from the server the client is
  connected to.
| https://www.arduino.cc/en/Reference/WiFIClientStop

.. |Graphical user interface, application Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Simple_Http_Request_to_Retrieve_Webs/WiFi_-_Simple_Http_Request_to_Retrieve_Webs_images/image01.png
   :width: 3.95213in
   :height: 4.73021in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Simple_Http_Request_to_Retrieve_Webs/WiFi_-_Simple_Http_Request_to_Retrieve_Webs_images/image02.png
   :width: 6.26806in
   :height: 7.50208in
.. |4-3| image:: ../../_static/Example_Guides/WiFi_-_Simple_Http_Request_to_Retrieve_Webs/WiFi_-_Simple_Http_Request_to_Retrieve_Webs_images/image03.png
   :width: 6.26806in
   :height: 4.68194in
