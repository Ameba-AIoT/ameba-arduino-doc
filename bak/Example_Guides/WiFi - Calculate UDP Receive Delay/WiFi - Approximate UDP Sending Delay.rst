Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Computer that connected to same network

Example

This example uses Ameba to send UDP packets to a computer and calculates
the UDP sending delay.

**Computer Side**

-  Connect the computer to the network.

-  Download the “SendDelay_win.exe” from
   https://github.com/ambiot/ambpro2_arduino
   “Ameba_misc/Example_Tools/UDP_Calculate”.

-  Open terminal.

-  Run command “ipconfig”. Record the IPv4 address as the client IP
   address.

-  Run command “./SendDelay_win.exe”. The computer begins to listen for
   packets from Ameba.

|A screenshot of a computer Description automatically generated|

**Ameba Side**

-  Open the example in “File” -> “Examples” -> “WiFi” -> ”
   UDPCalculation ” -> “SendDelay”.

-  Modify the ssid, password and key index (optional). Compile and
   upload the code from the Arduino IDE to Ameba and press the reset
   button when the upload is complete. Ameba should connect to the same
   network as the computer.

-  Enter the recorded client IP address into serial monitor.

|A screenshot of a computer program Description automatically generated
with medium confidence|

-  The Ameba will begin to send UDP packets to the computer. Once 1000
   packets have been received, the computer will calculate the average
   delay and print out the result.

..

   |image1|

.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/WiFi_-_Calculate_UDP_Sending_Delay/WiFi_-_Approximate_UDP_Sending_Delay_images/image01.png
   :width: 6.26806in
   :height: 3.79931in
.. |A screenshot of a computer program Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/WiFi_-_Calculate_UDP_Sending_Delay/WiFi_-_Approximate_UDP_Sending_Delay_images/image02.png
   :width: 5.83056in
   :height: 3.24149in
.. |image1| image:: ../../_static/Example_Guides/WiFi_-_Calculate_UDP_Sending_Delay/WiFi_-_Approximate_UDP_Sending_Delay_images/image03.png
   :width: 6.26806in
   :height: 3.60833in
