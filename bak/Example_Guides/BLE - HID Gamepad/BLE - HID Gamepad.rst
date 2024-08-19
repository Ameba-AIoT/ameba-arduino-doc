Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  BLE capable host device [Windows / Linux / MacOS / Android]

Example

Introduction
============

In this example, the AmebaPro2 board emulates a HID gamepad connected
using BLE.

Procedure
=========

Open the example, "Files" -> "Examples" -> “AmebaBLE” ->
“BLEHIDGamepad”.

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
to send gamepad input to the host device. Connect digital pin 8 to 3.3V
to start sending input, and connect to GND to stop.

To view the input, open a browser window and go to
https://gamepad-tester.com/. The connected gamepad device should show up
here, and some of the buttons and axes should show changing values.

|A screenshot of a computer Description automatically generated|

On Windows, gamepad input can also be viewed by going to “Control Panel”
-> “Devices and Printers” -> “AMEBA_BLE_HID” -> “Game Controller
Settings” -> “Properties”. The buttons and axes should also show
changing values here.

|Graphical user interface, website Description automatically generated|

|Graphical user interface Description automatically generated|

On Android, gamepad testing apps such as
https://play.google.com/store/apps/details?id=com.chimera.saturday.evogamepadtester
can also be used to view the gamepad input.

|Calendar Description automatically generated with low confidence|

Code Reference

By default, the board emulates a gamepad with an 8-direction hat switch
(d-pad), 6 analog axes and 16 buttons. How the inputs are interpreted is
dependent on the host device, and the button ordering may differ between
devices. Also, some axes or buttons may be disabled or missing on
certain host devices.

.. |image1| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image01.png
   :width: 3.27539in
   :height: 4.57561in
.. |A screenshot of a computer Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image02.png
   :width: 4.61458in
   :height: 2.51435in
.. |Graphical user interface, text Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image03.png
   :width: 1.57292in
   :height: 3.14583in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image04.png
   :width: 3.70833in
   :height: 2.15696in
.. |Graphical user interface, website Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image05.png
   :width: 2.95122in
   :height: 2.04167in
.. |Graphical user interface Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image06.png
   :width: 2.96875in
   :height: 2.05379in
.. |Calendar Description automatically generated with low confidence| image:: ../../_static/Example_Guides/BLE_-_HID_Gamepad/BLE_-_HID_Gamepad_images/image07.png
   :width: 3.42708in
   :height: 1.71354in
