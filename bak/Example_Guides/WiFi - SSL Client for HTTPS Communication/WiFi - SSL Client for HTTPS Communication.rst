Materials

-  AmebaPro2 [AMB82 MINI] x 1

Example

This example uses Ameba to securely retrieve information from the
internet using SSL. SSL is an acronym for Secure Sockets Layer. It is a
cryptographic protocol designed to provide communications security over
a computer network, by encrypting the messages passed between server and
client.

Open the “WiFiSSLClient” example in “File” -> “Examples” -> “WiFi” -> ”
SSLClient “.

|image1|

In the sample code, modify the highlighted snippet to reflect your WiFi
network settings.

|image2|

Upload the code and press the reset button on Ameba once the upload is
finished.

Open the serial monitor in the Arduino IDE and observe as Ameba
retrieves a text file from os.mbed.com.

|4-2|

| Code Reference
| Use “WiFiSSLClient client;” to create a client that uses SSL. After
  creation, the client can be used in the same way as a regular client.

.. |image1| image:: ../../_static/Example_Guides/WiFi_-_SSL_Client_for_HTTPS_Communication/WiFi_-_SSL_Client_for_HTTPS_Communication_images/image01.png
   :width: 3.77806in
   :height: 4.55619in
.. |image2| image:: ../../_static/Example_Guides/WiFi_-_SSL_Client_for_HTTPS_Communication/WiFi_-_SSL_Client_for_HTTPS_Communication_images/image02.png
   :width: 3.89918in
   :height: 4.70226in
.. |4-2| image:: ../../_static/Example_Guides/WiFi_-_SSL_Client_for_HTTPS_Communication/WiFi_-_SSL_Client_for_HTTPS_Communication_images/image03.png
   :width: 6.26806in
   :height: 2.71736in
