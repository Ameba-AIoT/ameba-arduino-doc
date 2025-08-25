IPv6 - Ameba as IPv6 Server/Client over UDP
===========================================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

Example
-------

Introduction
~~~~~~~~~~~~~

This example shows how Ameba can communicate on the local network using Internet Protocol version 6 over UDP.

.. note ::  This example only works after you have set up the server and then configure the client accordingly.

Procedure
~~~~~~~~~~

Step 1. IPv6UDPServer

Open the example, “Files” → “Examples” → “WiFi” → “IPv6UDPServer”.

|image01|

In the sample code, modify this section to enter the information required (ssid, password) to connect to your WiFi network.

|image02|

Upload the code, then reset the Ameba by pressing its reset button.

Open Serial Monitor and copy the IPv6 address of the Server for later use,

|image03|

Step 2. IPv6UDPClient

Now take the second AMB82 Mini and open another example, “Files” → “Examples” → “WiFi” → “IPv6UDPClient”.
    
|image04|

In the sample code, modify and enter the information required (ssid, password) to connect to your WiFi network.

|image05|

From the previous step, we obtained the server's IPv6 address. Now, copy this address into the “IPv6UDPClient” example.

|image06|

Upload the code, then reset the Ameba by pressing its reset button.

Open Serial Monitor on the port to the second AMB82 Mini, you should see server and client are sending text message to each other at the same time.

|image07|

|image08|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image01.png
   :width: 753
   :height: 969
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image02.png
   :width: 715
   :height: 434
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image03.png
   :width: 535
   :height: 163
.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image04.png
   :width: 860
   :height: 1040
   :scale: 90%
.. |image05| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image05.png
   :width: 753
   :height: 291
.. |image06| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image06.png
   :width: 819
   :height: 446
.. |image07| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image07.png
   :width: 429
   :height: 478
.. |image08| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/IPv6_Ameba_as_IPv6_Server_Client_over_UDP/image08.png
   :width: 478
   :height: 580
