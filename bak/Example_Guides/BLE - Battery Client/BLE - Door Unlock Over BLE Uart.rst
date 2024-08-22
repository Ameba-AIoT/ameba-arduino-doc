Materials
=========

-  Ameba Pro2 [AMB82-Mini] x 1

-  SD card x 1

-  Button x 1

-  Green LED x 1

-  Red LED x 1

-  Servo (Ex. Tower Pro SG90) x 1

-  220 Ohm resistor x 2

-  10K Ohm resistor x 1

-  Android / iOS smartphone

Example 
========

Introduction
------------

In this example, we will be using Ameba Pro2 development board to create
a simple door access control system with BLE. Door can be unlocked
remotely through BLE UART service.

Procedure
---------

**AMB82 MINI** wiring diagram:

|image1|

Ensure that a compatible BLE UART app is installed on your smartphone,
it is available at:

– Google Play Store:

https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connecta>

https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal

– Apple App Store:

https://apps.apple.com/us/app/bluefruit-connect/id830125974

Open the BLE example in “File” -> “Examples” -> “AmebaBLE” ->
“DoorUnlockOverBLEUart”.

|image2|

In the highlighted code snippet, set your preferred BLE Device Name.

|image3|\ Compile the code and upload it to Ameba.

**Unlock door with BLE UART Service**

Open the Adafruit Bluefruit app on your smartphone, scan and connect to
the Ameba board shown as “AMEBA_BLE” or any BLE device name that has
been set. Then, choose UART function in the app.

|image4| |image5|

You should see the message “Door Bell Pressed” appearing in the UART
terminal section of the app when button is pressed. Enter “Open” message
and click send, this allows user to open the door and take a snapshot.
The image will be saved to SD card and named as Authorized{counter}.jpg.

|Shape, square Description automatically generated|

To take another snapshot, enter “Snapshot” message in the UART terminal
section after pressing the button. Image will be named as
SnapshotTaken{counter}.jpg and saved to SD card.

|image6|

.. |image1| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image01.png
   :width: 6.26111in
   :height: 2.73056in
.. |image2| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image02.png
   :width: 3.94583in
   :height: 4.51389in
.. |image3| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image03.png
   :width: 6.21875in
   :height: 5.10139in
.. |image4| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image4.jpeg
   :width: 2.87431in
   :height: 6.22153in
.. |image5| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image5.jpeg
   :width: 2.88194in
   :height: 6.23889in
.. |Shape, square Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image6.jpeg
   :width: 1.81944in
   :height: 3.93889in
.. |image6| image:: ../../_static/Example_Guides/BLE_-_Door_Unlock_Over_BLE_Uart/BLE_-_Door_Unlock_Over_BLE_Uart_images/image7.jpeg
   :width: 1.81944in
   :height: 3.93889in
