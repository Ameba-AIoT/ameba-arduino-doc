WiFi - Set up UDP Server to Communicate
========================================

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 / AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

Example
--------

In this example, we connect Ameba to WiFi and use Ameba to be an UDP server. When Ameba receives a message from UDP client, it replies "acknowledged" message to client.

Open the WiFi Web Server example. :guilabel:`File -> Examples -> WiFi -> WiFiUdpSendReceiveString`

|image01|

Modify the highlighted code section (ssid, password, keyindex) to connect to your WiFi network.

|image02|

Compile the code and upload it to Ameba. After pressing the Reset button, Ameba connects to WiFi and starts the UDP server with port 2390. After the UDP server starts service, Ameba prints the "Starting connection to server" message and waits for client connection.

|image03|

As to the UDP client, we use "sokit" program in the computer to connect to UDP server.

Choose client mode and fill in the IP of UDP server (which is the IP of Ameba) and port 2390, then click "UDP Connect".

After the connection is established, fill in "Hello World" in the Buf 0 field in sokit and click "Send". Then you can see the Ameba UDP server replies "acknowledged".

|image04|

Code Reference
---------------

| Refer to the Arduino tutorial for detailed information about this example.
| https://www.arduino.cc/en/Tutorial/WiFiSendReceiveUDPString

| First, use begin() to open an UDP port on Ameba.
| https://www.arduino.cc/en/Reference/WiFiUDPBegin

| Use parsePacket() to wait for data from client.
| https://www.arduino.cc/en/Reference/WiFiUDPParsePacket

| When a connection is established, use remoteIP() and remotePort() to get the IP and port of the client.
| https://www.arduino.cc/en/Reference/WiFiUDPRemoteIP

| Then use read() to read the data sent by client.
| https://www.arduino.cc/en/Reference/WiFiUDPRead

| To send reply, use beginPacket(), write(), end().
| https://www.arduino.cc/en/Reference/WiFiUDPBeginPacket
| https://www.arduino.cc/en/Reference/WiFiUDPWrite
| https://www.arduino.cc/en/Reference/WiFiUDPEndPacket

.. |image01| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Set_up_UDP_Server_to_Communicate/image01.png
   :width:  898 px
   :height:  961 px
.. |image02| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Set_up_UDP_Server_to_Communicate/image02.png
   :width:  945 px
   :height:  994 px
.. |image03| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Set_up_UDP_Server_to_Communicate/image03.png
   :width:  938 px
   :height:  422 px
.. |image04| image:: ../../../../_static/amebad/Example_Guides/WiFi/WiFi_Set_up_UDP_Server_to_Communicate/image04.png
   :width:  798 px
   :height:  579 px

