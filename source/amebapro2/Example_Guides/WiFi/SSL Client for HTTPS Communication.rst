SSL Client for HTTPS Communication
==================================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

Example
-------

This example uses Ameba to securely retrieve information from the
internet using SSL. SSL is an acronym for Secure Sockets Layer. It is a
cryptographic protocol designed to provide communications security over
a computer network, by encrypting the messages passed between server and
client.

Open the "WiFiSSLClient" example in "File" -> "Examples" -> "WiFi" -> "SSLClient".

|image01|

In the sample code, modify the highlighted snippet to reflect your WiFi
network settings.

|image02|

Upload the code and press the reset button on Ameba once the upload is
finished.

Open the serial monitor in the Arduino IDE and observe as Ameba
retrieves a text file from os.mbed.com.

|image03|

Code Reference
--------------

Use ``WiFiSSLClient client;`` to create a client that uses SSL. After creation, the client can be used in the same way as a regular client.

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/WiFi/SSL_Client_for_HTTPS_Communication/image01.png
   :width: 602 px
   :height: 726 px
.. |image02| image:: ../../../_static/amebapro2/Example_Guides/WiFi/SSL_Client_for_HTTPS_Communication/image02.png
   :width: 602 px
   :height: 726 px
.. |image03| image:: ../../../_static/amebapro2/Example_Guides/WiFi/SSL_Client_for_HTTPS_Communication/image03.png
   :width: 1164 px
   :height: 505 px
   :scale: 60%
