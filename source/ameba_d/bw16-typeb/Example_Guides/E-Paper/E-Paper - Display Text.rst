E-Paper - Display Text
=========================

.. contents::
  :local:
  :depth: 2

Materials
---------
- AmebaD [AMB21 / AMB22 / AMB23 / AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

- Waveshare E-Paper [2.9inch E-Paper HAT (D)/ 2.9inch E-Paper V2/ 2.9inch e-Paper Module (B)/ 4.2inch e-Paper Module/ 4.2inch v2 e-Paper Module/ 7.5-inch E-Ink display HAT] x1

Example
-------

In this example, AmebaD boards will be used to connect to a Waveshare e-Paper module (2.9inch/ 4.2inch/ 7.5inch) to display texts. The display uses the flexible substrate as base plate, with an interface and a reference system design. You may refer to the official datasheet to know more information about these modules.

**BW16 wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image03|

2.9inch E-Paper v2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image03v2| 

4.2inch e-Paper Module/ 4.2inch v2 e-Paper Module

|image10|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image17|

Download the Eink zip library, AmebaEink.zip, at https://github.com/Ameba-AIoT/ameba-arduino-d/tree/master/Arduino_zip_libraries. Then install the AmebaEink.zip by navigating to “Sketch” -> “Include Library” -> “Add .ZIP Library…”.

Eink examples are categorised based on the size and modules of the e-Paper display.

|image22|

Open one of the “EinkDisplayText” examples. For example, “File” → “Examples” → “AmebaEink” → “EPD_2in9v2” → “EinkDisplayText”:

|image23|

You may choose any GPIO pins for Busy, Reset and DC pin.

|image24|

Upload the code to the board and press the reset button after uploading is done. You will find these texts displayed on the boards:

The 2.9-inch e-Paper Module (B) supports three colours—red, black, and white. Therefore, it can display red on the e-Paper display shown on the most left.

|image25|

|image26|

|image27|

Code Reference
---------------

[1] We use Good Display GDEH029A1 2.9 Inch / 296x128 Resolution / Partial Refresh Arduino Sample Code to get the e-Paper successfully Display:
http://www.good-display.com/product/201.html

[2] EPD libraries can be obtained from:
https://github.com/waveshare/e-Paper

[3] Generate a QR code on the E-paper module:
https://eugeniopace.org/qrcode/arduino/eink/2019/07/01/qrcode-on-arduino.html

.. |image03| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image03.png
   :width:  945 px
   :height:  390 px

.. |image03v2| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image03v2.png
   :width:  889 px
   :height:  391 px

.. |image10| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image10.png
   :width:  678 px
   :height:  375 px

.. |image17| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image17.png
   :width:  544 px
   :height:  832 px

.. |image22| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image22.png
   :width:  726 px
   :height:  728 px

.. |image23| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image23.png
   :width:  726 px
   :height:  728 px

.. |image24| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image24.png
   :width:  726 px
   :height:  728 px

.. |image25| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image25.png
   :width:  832 px
   :height:  624 px

.. |image26| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image26.png
   :width:  956 px
   :height:  720 px

.. |image27| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image27.png
   :width:  708 px
   :height:  890 px