E-Paper - Display Text
=========================

Materials
---------
- AmebaD [AMB21 / AMB22 / AMB23 / AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

- Waveshare E-Paper [2.9inch E-Paper HAT (D)/ 2.9inch E-Paper V2/ 2.9inch e-Paper Module (B)/ 4.2inch e-Paper Module/ 4.2inch V2 e-Paper Module/ 7.5-inch E-Ink display HAT] x1

.. note:: The ``Universal E-Paper Driver HAT`` using for all E-Papers is compatible with version V2.1 only.

Example
-------

In this example, AmebaD boards will be used to connect to a Waveshare e-Paper module (2.9inch/ 4.2inch/ 7.5inch) to display texts. The display uses the flexible substrate as base plate, with an interface and a reference system design. You may refer to the official datasheet to know more information about these modules.

.. only:: amb21

**AMB21/22 wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image01|

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image01v2|

4.2inch e-Paper Module/ 4.2inch V2 e-Paper Module

|image08|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image15|

.. only:: end amb21

.. only:: amb25

**AMB25 wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image06|

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image06v2|

4.2inch e-Paper Module/ 4.2inch V2 e-Paper Module

|image13|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image20|

.. only:: end amb25

.. only:: amb26

**AMB26 wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image07|

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image07v2|

4.2inch e-Paper Module/ 4.2inch v2 e-Paper Module

|image14|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image21|

.. only:: end amb26

.. only:: aw-cu488

**AW-CU488 Thing Plus wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image05|

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image05v2|

4.2inch e-Paper Module/ 4.2inch v2 e-Paper Module

|image12|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image19|

.. only:: end aw-cu488

.. only:: bw16-typeb

**BW16 wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image03|

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image03v2|

4.2inch e-Paper Module/ 4.2inch v2 e-Paper Module

|image10|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image17|

.. only:: end bw16-typeb

.. only:: bw16-typec

**BW16 wiring diagrams:**

2.9inch HAT (D) e-Paper Module

|image04|

2.9inch E-Paper V2 e-Paper Module/ 2.9inch e-Paper Module (B)

|image04v2|

4.2inch e-Paper Module/ 4.2inch v2 e-Paper Module

|image11|

7.5-inch e-Paper Module
Do note that Display Config should be set to B and Interface Config should be set to 0.

|image18|

.. only:: end bw16-typec

Download the Eink zip library, `AmebaEink.zip <https://github.com/Ameba-AIoT/ameba-arduino-d/tree/master/Arduino_zip_libraries>`__ Then install the AmebaEink.zip by navigating to :guilabel:`Sketch -> Include Library -> Add .ZIP Library…`

Eink examples are categorised based on the size and modules of the e-Paper display.

|image22|

Open one of the "EinkDisplayText" examples. For example, :guilabel:`File -> Examples -> AmebaEink -> EPD_2in9v2 -> EinkDisplayText`

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

.. only:: amb21

.. |image01| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image01.png
   :width:  823 px
   :height:  459 px

.. |image01v2| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image01v2.png
   :width:  800 px
   :height:  452 px

.. |image08| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image08.png
   :width:  868 px
   :height:  431 px

.. |image15| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image15.png
   :width:  554 px
   :height:  777 px

.. only:: end amb21

.. only:: amb25

.. |image06| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image06.png
   :width:  833 px
   :height:  421 px

.. |image06v2| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image06v2.png
   :width:  682 px
   :height:  373 px

.. |image13| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image13.png
   :width:  769 px
   :height:  392 px

.. |image20| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image20.png
   :width:  470 px
   :height:  830 px

.. only:: end amb25

.. only:: amb26

.. |image07| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image07.png
   :width:  844 px
   :height:  432 px

.. |image07v2| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image07v2.png
   :width:  896 px
   :height:  432 px

.. |image14| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image14.png
   :width:  732 px
   :height:  362 px

.. |image21| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image21.png
   :width:  601 px
   :height:  803 px

.. only:: end amb26

.. only:: aw-cu488

.. |image05| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image05.png
   :width:  893 px
   :height:  738 px

.. |image05v2| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image05v2.png
   :width:  935 px
   :height:  634 px

.. |image12| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image12.png
   :width:  905 px
   :height:  575 px

.. |image19| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image19.png
   :width:  863 px
   :height:  655 px

.. only:: end aw-cu488

.. only:: bw16-typeb

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

.. only:: end bw16-typeb

.. only:: bw16-typec

.. |image04| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image04.png
   :width:  817 px
   :height:  387 px

.. |image04v2| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image04v2.png
   :width:  789 px
   :height:  372 px

.. |image11| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image11.png
   :width:  672 px
   :height:  368 px

.. |image18| image:: ../../../../_static/amebad/Example_Guides/E-Paper/Epaper_Display_Text/image18.png
   :width:  580 px
   :height:  806 px

.. only:: end bw16-typec

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
