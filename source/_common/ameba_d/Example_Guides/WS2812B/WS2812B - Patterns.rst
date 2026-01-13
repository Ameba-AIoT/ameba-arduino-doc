WS2812B - Patterns
==================

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 / AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1
- WS2812B LED Strip / Ring / Stick / Board x1

Example
-------

**Introduction**
~~~~~~~~~~~~~~~~

In this example, we will be using the AmebaD board to control the WS2812B RGB LED, using the SPI peripheral to create the waveform necessary for the LEDs.

WS2812B patterns controls LED (Strip / Ring / Stick / Board) with different colors with different LED patterns.

Procedure
-----------

Firstly, connect the WS2812B to the Ameba board as shown in the following diagrams.

.. only:: amb21

**AMB21 / AMB22** Wiring Diagram:

|image01|

.. only:: end amb21

.. only:: amb23

**AMB23** Wiring Diagram:

|image02|

.. only:: end amb23

.. only:: bw16-typeb

**BW16** Wiring Diagram:

|image03|

.. only:: end bw16-typeb

.. only:: bw16-typec

**BW16-TypeC** Wiring Diagram:

|image04|

.. only:: end bw16-typec

.. only:: aw-cu488

**AW-CU488 Thing Plus** Wiring Diagram:

|image05|

.. only:: end aw-cu488

.. only:: amb25

**AMB25** Wiring Diagram:

|image06|

.. only:: end amb25

.. only:: amb26

**AMB26** Wiring Diagram:

|image07|

.. only:: end amb26

To create different light patterns with many different colors, use**WS2812B_Patterns**.

Open the example in :guilabel:`File -> Example -> AmebaWS2812B -> WS2812B_Patterns`

|image08|

In the sample code, modify **TOTAL_NUM_OF_LEDS** to be the total number of LEDs on the WS2812B module, and modify **NUM_OF_LEDS** to be the number of LEDs that you have connected.

|image09|

Next compile and upload to Ameba, then press the reset button. You will see the WS2812B displaying a color wipe, theater chase, rainbow, and theater chase rainbow light patterns in loop.

|image10|

|image11|

|image12|

|image13|

Code Reference
--------------

[1] WS2812B Datasheet:

https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf

.. |image01| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image01.png
   :width: 1234
   :height: 747
   :scale: 70%
.. |image02| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image02.png
   :width: 1375
   :height: 724
   :scale: 60%
.. |image03| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image03.png
   :width: 1320
   :height: 685
   :scale: 60%
.. |image04| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image04.png
   :width: 1381
   :height: 684
   :scale: 60%
.. |image05| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image05.png
   :width: 957
   :height: 710
   :scale: 80%
.. |image06| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image06.png
   :width: 1287
   :height: 702
   :scale: 60%
.. |image07| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image07.png
   :width: 1437
   :height: 616
   :scale: 60%
.. |image08| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image08.png
   :width: 707
   :height: 1005
.. |image09| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image09.png
   :width: 620
   :height: 313
.. |image10| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image10.png
   :width: 3016
   :height: 544
   :scale: 20%
.. |image11| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image11.png
   :width: 2724
   :height: 536
   :scale: 30%
.. |image12| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image12.png
   :width: 2300
   :height: 528
   :scale: 30%
.. |image13| image:: ../../../../_static/amebad/Example_Guides/WS2812B/WS2812B_Patterns/image13.png
   :width: 2888
   :height: 592
   :scale: 30%
