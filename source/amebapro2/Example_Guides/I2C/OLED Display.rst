OLED Display
============

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  0.96 inch OLED Display 128x64 (SSD1306) x 1

Example
-------

Introduction
~~~~~~~~~~~~

The example will showcase texts, shapes, and bitmap images on an OLED
display using the I2C communication protocol alongside Adafruit
libraries.

Procedure
~~~~~~~~~

Connect the 0.96-inch OLED display to I2C_SDA and I2C_SCL of the board.

|image01|

Open the example in "File" -> "Examples" -> "AmebaWire" -> "OLED_SSD1306".

|image02|

For this example, we will be using 0x3D as the address. 

|image03|

If the address doesn't work for you, you can run I2CScanner to find the
OLED address by navigating to "File" -> "Examples" -> "AmebaWire" ->
"I2CScanner".

|image04|

Compile and upload to Ameba, then press the reset button.

First, Realtek logo will be shown, followed by shapes, text, and
animations. Some examples are shown below.

|image05| 

|image06| 

|image07|

If you would like to change the Bitmap image shown on the OLED display,
you can prepare a picture/photo and resize the image based on the OLED
display that you are using. You can look for a photo resizing tool
online, for example, https://resizeimage.net/.

Next, you may use online tools such as https://javl.github.io/image2cpp/
to convert image into an array.

Code Reference
--------------

| [1] Adafruit_SSD1306 library and example obtained from:
| https://github.com/adafruit/Adafruit_SSD1306

| [2] Adafruit_GFX library obtained from:
| https://github.com/adafruit/Adafruit-GFX-Library/tree/master

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image01.png
   :width: 772 px
   :height: 562 px
.. |image02| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image02.png
   :width: 617 px
   :height: 944 px
   :scale: 80%
.. |image03| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image03.png
   :width: 878 px
   :height: 469 px
.. |image04| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image04.png
   :width: 453 px
   :height: 539 px
.. |image05| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image05.png
   :width: 2284 px
   :height: 1607 px
   :scale: 30%
.. |image06| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image06.png
   :width: 1582 px
   :height: 1336 px
   :scale: 40%
.. |image07| image:: ../../../_static/amebapro2/Example_Guides/I2C/OLED_Display/image07.png
   :width: 1718 px
   :height: 1498 px
   :scale: 40%
