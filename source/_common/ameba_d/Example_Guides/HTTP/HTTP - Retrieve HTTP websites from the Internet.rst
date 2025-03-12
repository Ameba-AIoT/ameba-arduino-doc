HTTP - Retrieve HTTP websites from the Internet
================================================

.. contents::
  :local:
  :depth: 2
  
Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 /  AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

Example
-------

In this example, the HttpClient library is used to retrieve a webpage using the HTTP protocol.

First, make sure that the correct Ameba development board is selected in “Tools” -> “Board”

Then open “File” -> “Examples” -> “AmebaHttp” -> “SimpleHttpExample”

|image01|

In the sample code, modify the highlighted section to enter the information required (ssid, password, key index) to connect to your WiFi network.

|image02|

Upload the code and press the reset button on Ameba once the upload is finished. Open the serial monitor in the Arduino IDE and you can see the information retrieved from the website.

|image03|

Code Reference
----------------

| Use WiFi.begin() to establish WiFi connection:
| https://www.arduino.cc/en/Reference/WiFiBegin
| To get the information of a WiFi connection:
| Use WiFi.SSID() to get SSID of the current connected network.
| https://www.arduino.cc/en/Reference/WiFiSSID
| Use WiFi.RSSI() to get the signal strength of the connection.
| https://www.arduino.cc/en/Reference/WiFiRSSI
| Use WiFi.localIP() to get the IP address of Ameba.
| https://www.arduino.cc/en/Reference/WiFiLocalIP
| Use WiFiClient to create a client to handle the WiFi connection.
| https://www.arduino.cc/en/Reference/WiFiClient
| Use HTTPClient to create a client to handle the HTTP connection.
| Use http.get() to send a GET request to the website.
 

.. |image01| image:: ../../../../_static/amebad/Example_Guides/HTTP/HTTP_Retrieve_HTTP_websites_from_the_Internet/image01.png
   :width:  511 px
   :height:  521 px
.. |image02| image:: ../../../../_static/amebad/Example_Guides/HTTP/HTTP_Retrieve_HTTP_websites_from_the_Internet/image02.png
   :width:  568 px
   :height:  565 px
.. |image03| image:: ../../../../_static/amebad/Example_Guides/HTTP/HTTP_Retrieve_HTTP_websites_from_the_Internet/image03.png
   :width:  940 px
   :height:  620 px
