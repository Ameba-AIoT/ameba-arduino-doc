Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  BLE capable host device [Windows / Linux / MacOS / Android]

Example

Introduction
============

In this example, the AMB82 MINI board emulates a HID keyboard connected
using BLE.

Procedure
=========

Open the example, "Files" -> "Examples" -> “AmebaBLE” ->
“BLEHIDKeyboard”.

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
to send keyboard input to the host device. Select a text input field,
such as in the Serial Monitor or a text document. Connect digital pin 8
to 3.3V to start sending keystrokes, connect to GND to stop.

You should see the text “Hello World !” typed out and deleted
repeatedly.

|Graphical user interface, text, application Description automatically
generated|

.. |image1| image:: ../../_static/Example_Guides/BLE_-_HID_Keyboard/BLE_-_HID_Keyboard_images/image01.png
   :width: 3.5821in
   :height: 4.937in
.. |A screenshot of a computer Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/BLE_-_HID_Keyboard/BLE_-_HID_Keyboard_images/image02.png
   :width: 4in
   :height: 2.18258in
.. |Graphical user interface, text Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Keyboard/BLE_-_HID_Keyboard_images/image03.png
   :width: 1.57292in
   :height: 3.14583in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_HID_Keyboard/BLE_-_HID_Keyboard_images/image04.png
   :width: 2.51042in
   :height: 1.98958in
