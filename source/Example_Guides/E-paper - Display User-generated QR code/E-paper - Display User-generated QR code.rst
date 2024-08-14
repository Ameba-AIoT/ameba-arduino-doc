Materials

AmebaPro2 [AMB82 MINI] x 1

Waveshare E-Paper [2.9inch E-Paper HAT (D)/ 2.9inch E-Paper V2/ 2.9inch
e-Paper Module (B)/ 4.2inch e-Paper Module/ 7.5-inch E-Ink display HAT]
x1

Example

Introduction

In this example, Ameba Pro2 board will be used to connect to a Waveshare
e-Paper module (2.9inch/ 4.2inch/ 7.5inch) to display texts. The display
uses the flexible substrate as base plate, with an interface and a
reference system design. You may refer to the official datasheet to know
more information about these modules.

Procedure

AMB82-Mini wiring diagram:

2.9inch HAT (D) e-Paper Module

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

4.2inch e-Paper Module

7.5-inch e-Paper Module

Do note that Display Config should be set to B and Interface Config
should be set to 0.

Next, download the Eink zip library, AmebaEink.zip,
at https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_zip_libraries
Then install the AmebaEink.zip by navigating to “Sketch” -> “Include
Library” -> “Add .ZIP Library…”.

Eink examples are categorised based on the size and modules of the
e-Paper display.

Open one of the “EinkDisplayQR” examples. For example, “File” →
“Examples” → “AmebaEink” → “EPD_2in9v2”-> “EinkDisplayQR”:

You may choose any GPIO pins for Busy, Reset and DC pin. You can refer
to
https://www.amebaiot.com/en/amebapro2-amb82-mini-arduino-getting-started/
for AMB82-Mini’s pinmap.

Modify the URL in the loop() section highlighted in yellow for your QR
code, then upload the code to the Ameba board. Upload the code to the
board and press the reset button after uploading is done.

A QR code generated based on the input URL will be shown on the E-paper
module. In the example, the QR code links to Ameba IoT official website.

Upload the code to the board and press the reset button after uploading
is done. Wait for around 1-2 seconds for the e-Paper module to refresh
its screen.

Code Reference

[1] We use Good Display GDEH029A1 2.9 Inch / 296×128 Resolution /
Partial Refresh Arduino Sample Code to get the e-Paper successfully
Display: http://www.good-display.com/product/201.html

[2] EPD libraries can be obtained from:
https://github.com/waveshare/e-Paper

[3] Provide the link to how to generate a QR code on the E-paper module:
https://eugeniopace.org/qrcode/arduino/eink/2019/07/01/qrcode-on-arduino.html

[4] A simple library for generating QR codes in C, optimized for
processing and memory-constrained systems:
https://github.com/ricmoo/QRCode#data-capacities

|image01.png| |image02.png| |image03.png| |image04.jpeg| |image05.png|
|image06.png| |image07.png| |image08.png| |image09.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image03.png
.. |image04.jpeg| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image04.jpeg
.. |image05.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image05.png
.. |image06.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image06.png
.. |image07.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image07.png
.. |image08.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image08.png
.. |image09.png| image:: ../../../_static/_Example_Guides/_E-paper%20-%20Display%20User-generated%20QR%20code/image09.png
