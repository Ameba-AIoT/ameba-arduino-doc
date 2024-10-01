Calculate UDP Receive Delay
===========================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  Computer that connected to same network

Example
-------

This example uses Ameba to receive UDP packets from a computer and
calculates the UDP receive delay.

**Ameba Side**

-  Open the example in "File" -> "Examples" -> "WiFi" -> "UDPCalculation" -> "ReceiveDelay".

-  Modify the ssid, password and key index (optional). Compile and
   upload the code from the Arduino IDE to Ameba and press the reset
   button when the upload is complete. Ameba should connect to the same
   network as the computer.

-  Open the serial monitor in Arduino IDE and record the IP address
   assigned to Ameba as the client IP address.

**Computer Side**

-  Connect the computer to the network.

-  Download the "ReceiveDelay_win.exe" from https://github.com/ambiot/ambpro2_arduino
   "Ameba_misc/Example_Tools/UDP_Calculate".

-  Open terminal.

-  Run command "./ReceiveDelay_win.exe <the client IP address>".

|image01|

-  The computer begins to send packets to Ameba. Once 10000 packets have
   been received, Ameba will calculate the average delay and print out
   the result to the serial monitor. It may take up to a few minutes for
   10000 packets to be sent.

|image02|

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/WiFi/Calculate_UDP_Receive_Delay/image01.png
   :width: 902 px
   :height: 518 px
.. |image02| image:: ../../../_static/amebapro2/Example_Guides/WiFi/Calculate_UDP_Receive_Delay/image02.png
   :width: 1025 px
   :height: 148 px
   :scale: 80%
