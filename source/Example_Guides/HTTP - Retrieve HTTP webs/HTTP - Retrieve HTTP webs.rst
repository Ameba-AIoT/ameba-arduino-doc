Materials

AmebaPro2 [AMB82 MINI] x 1

Example

In this example, the HttpClient library is used to retrieve a webpage
using the HTTP protocol. First, make sure that the correct Ameba
development board is selected in “Tools” -> “Board”

Then open “File” -> “Examples” -> “AmebaHttp” -> “RetrieveHttpWebs”

In the sample code, modify the highlighted section to enter the
information required (ssid, password, key index) to connect to your WiFi
network.

Upload the code and press the reset button on Ameba once the upload is
finished. Open the serial monitor in the Arduino IDE and you can see the
information retrieved from the website.

 

 

Code Reference

Use WiFi.begin() to establish WiFi connection:
https://www.arduino.cc/en/Reference/WiFiBegin To get the information of
a WiFi connection: Use WiFi.SSID() to get SSID of the current connected
network. https://www.arduino.cc/en/Reference/WiFiSSID Use WiFi.RSSI() to
get the signal strength of the connection.
https://www.arduino.cc/en/Reference/WiFiRSSI Use WiFi.localIP() to get
the IP address of Ameba. https://www.arduino.cc/en/Reference/WiFiLocalIP
Use WiFiClient to create a client to handle the WiFi connection.
https://www.arduino.cc/en/Reference/WiFiClient Use HTTPClient to create
a client to handle the HTTP connection.

Use http.get() to send a GET request to the website.

 

|image01.png| |image02.png| |image03.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Retrieve%20HTTP%20webs/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Retrieve%20HTTP%20webs/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Retrieve%20HTTP%20webs/image03.png
