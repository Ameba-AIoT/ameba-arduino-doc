Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Waveshare E-Paper [2.9inch E-Paper HAT (D)/ 2.9inch E-Paper V2/
   2.9inch e-Paper Module (B)/ 4.2inch e-Paper Module/ 7.5-inch E-Ink
   display HAT] x1

Example

Introduction
============

In this example, Ameba Pro2 board will be used to connect to a Waveshare
e-Paper module (2.9inch/ 4.2inch/ 7.5inch) to display texts. The display
uses the flexible substrate as base plate, with an interface and a
reference system design. You may refer to the
official `datasheet <https://www.waveshare.net/w/upload/b/b5/2.9inch_e-Paper_(D)_Specification.pdf>`__ to
know more information about these modules.

Procedure
=========

**AMB82-Mini wiring diagram:**

*2.9inch HAT (D) e-Paper Module*

|A picture containing text, rectangle, screenshot, design Description
automatically generated|

*2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)*

|A picture containing text, screenshot, rectangle Description
automatically generated|

*4.2inch e-Paper Module*

|A picture containing electronics, text, circuit, electronic component
Description automatically generated|

*7.5-inch e-Paper Module*

Do note that Display Config should be set to B and Interface Config
should be set to 0.

|A picture containing text, screenshot, electronic engineering,
electronics Description automatically generated|

| Next, download the Eink zip library, AmebaEink.zip,
  at https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_zip_libraries
| Then install the AmebaEink.zip by navigating to “Sketch” -> “Include
  Library” -> “Add .ZIP Library…”.

Eink examples are categorised based on the size and modules of the
e-Paper display.

|A screenshot of a computer Description automatically generated|

Open one of the “EinkDisplayText” examples. For example, “File” →
“Examples” → “AmebaEink” → “EPD_2in9v2”-> “EinkDisplayText”:

|image1|

You may choose any GPIO pins for Busy, Reset and DC pin. You can refer
to
https://www.amebaiot.com/en/amebapro2-amb82-mini-arduino-getting-started/
for AMB82-Mini’s pinmap.

|image2|

Upload the code to the board and press the reset button after uploading
is done. You will find these texts displayed on the boards:

The 2.9-inch e-Paper Module (B) supports three colours—red, black, and
white. Therefore, it can display red on the e-Paper display shown on the
most left.

|image3|

|image4|

|image5|

Code Reference

| [1] We use Good Display GDEH029A1 2.9 Inch / 296×128 Resolution /
  Partial Refresh Arduino Sample Code to get the e-Paper successfully
  Display:
| http://www.good-display.com/product/201.html

[2] EPD libraries can be obtained from:
https://github.com/waveshare/e-Paper

.. |A picture containing text, rectangle, screenshot, design Description automatically generated| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image01.png
   :width: 4.99828in
   :height: 2.48in
.. |A picture containing text, screenshot, rectangle Description automatically generated| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image02.png
   :width: 5.112in
   :height: 2.3361in
.. |A picture containing electronics, text, circuit, electronic component Description automatically generated| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image03.png
   :width: 4.64935in
   :height: 2.68645in
.. |A picture containing text, screenshot, electronic engineering, electronics Description automatically generated| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image04.png
   :width: 4.53247in
   :height: 3.07025in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image05.png
   :width: 3.76736in
   :height: 4.24392in
.. |image1| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image06.png
   :width: 4.14334in
   :height: 4.38679in
.. |image2| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image07.png
   :width: 4.03641in
   :height: 4.27358in
.. |image3| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image8.jpeg
   :width: 2.80117in
   :height: 3.73779in
.. |image4| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image9.jpeg
   :width: 2.97575in
   :height: 3.97075in
.. |image5| image:: ../../_static/Example_Guides/E-paper_-_Display_Text/E-paper_-_Display_Text_images/image10.jpeg
   :width: 3.96626in
   :height: 5.29245in
