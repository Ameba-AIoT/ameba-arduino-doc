Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  BLE capable host device [Windows / Linux / MacOS / Android]

Example

Introduction
============

In this example, the AmebaPro2 board emulates a HID mouse connected
using BLE.

Procedure
=========

Open the example, "Files" -> "Examples" -> “AmebaBLE” -> “BLEHIDMouse”.

|image1|

Upload the code and press the reset button once the upload is finished.

Immediately after reset, the board will begin BLE advertising as
“AMEBA_BLE_HID”. On your host device, go to the Bluetooth settings menu,
scan, and connect to the board.

You should ensure that the connection process is completed before
proceeding.

On Windows, ensure that any driver installation is finished, and the
board shows up in the Bluetooth menu under the “Mouse, keyboard & pen”
category.

|A screenshot of a computer Description automatically generated with
medium confidence|

On Android, ensure that “Input device” is enabled for the board.

|Graphical user interface, text Description automatically generated|

After the Bluetooth connection process is completed, the board is ready
to send mouse input to the host device. Connect digital pin 8 to 3.3V to
start sending input, connect to GND to stop.

You should see the mouse cursor move around four points in a square,
performing right and left clicks, and scrolling up and down

Code Reference

How the mouse input is interpreted is dependent on the host system. Some
systems, such as mobile operating systems, may not support all mouse
button input functions.

.. |image1| image:: ../../_static/Example_Guides/BLE_-_HID_Mouse/BLE_-_HID_Mouse_images/image01.png
   :width: 3.29484in
   :height: 4.63891in
.. |A screenshot of a computer Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/BLE_-_HID_Mouse/BLE_-_HID_Mouse_images/image02.png
   :width: 3.86458in
   :height: 2.10869in
.. |Graphical user interface, text Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Mouse/BLE_-_HID_Mouse_images/image03.png
   :width: 1.57292in
   :height: 3.14583in
