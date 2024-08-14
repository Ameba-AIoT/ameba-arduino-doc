Materials

AmebaPro2 [AMB82 MINI] x 1

BLE capable host device [Windows / Linux / MacOS / Android]

Example

Introduction

In this example, the AmebaPro2 board emulates a HID gamepad connected
using BLE.

Procedure

Open the example, "Files" -> "Examples" -> “AmebaBLE” ->
“BLEHIDGamepad”.

Upload the code and press the reset button once the upload is finished.

Immediately after reset, the board will begin BLE advertising as
“AMEBA_BLE_HID”. On your host device, go to the Bluetooth settings menu,
scan, and connect to the board.

You should ensure that the connection process is completed before
proceeding.

On Windows, ensure that any driver installation is finished, and the
board shows up in the Bluetooth menu under the “Mouse, keyboard & pen”
category.

On Android, ensure that “Input device” is enabled for the board.

After the Bluetooth connection process is completed, the board is ready
to send gamepad input to the host device. Connect digital pin 8 to 3.3V
to start sending input, and connect to GND to stop.

To view the input, open a browser window and go to
https://gamepad-tester.com/. The connected gamepad device should show up
here, and some of the buttons and axes should show changing values.

On Windows, gamepad input can also be viewed by going to “Control Panel”
-> “Devices and Printers” -> “AMEBA_BLE_HID” -> “Game Controller
Settings” -> “Properties”. The buttons and axes should also show
changing values here.

On Android, gamepad testing apps such as
https://play.google.com/store/apps/details?id=com.chimera.saturday.evogamepadtester
can also be used to view the gamepad input.

Code Reference

By default, the board emulates a gamepad with an 8-direction hat switch
(d-pad), 6 analog axes and 16 buttons. How the inputs are interpreted is
dependent on the host device, and the button ordering may differ between
devices. Also, some axes or buttons may be disabled or missing on
certain host devices.

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.png|

.. |image01.png| image:: ../../../_static/_Other_Guides/image01.png
.. |image02.png| image:: ../../../_static/_Other_Guides/image02.png
.. |image03.png| image:: ../../../_static/_Other_Guides/image03.png
.. |image04.png| image:: ../../../_static/_Other_Guides/image04.png
.. |image05.png| image:: ../../../_static/_Other_Guides/image05.png
.. |image06.png| image:: ../../../_static/_Other_Guides/image06.png
.. |image07.png| image:: ../../../_static/_Other_Guides/image07.png
