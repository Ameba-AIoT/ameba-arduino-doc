Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  0.96 inch OLED Display 128x64 (SSD1306) x 1

Example

**Introduction**

The example will showcase texts, shapes, and bitmap images on an OLED
display using the I2C communication protocol alongside Adafruit
libraries.

**Procedure**

Connect the 0.96-inch OLED display to I2C_SDA and I2C_SCL of the board.

|image1|

Open the example in “File” -> “Examples” -> “AmebaWire” ->
“OLED_SSD1306”.

|A screenshot of a computer Description automatically generated|

For this example, we will be using 0x3D as the address. |A screenshot of
a computer program Description automatically generated|

If the address doesn’t work for you, you can run I2CScanner to find the
OLED address by navigating to “File” -> “Examples” -> “AmebaWire” ->
“I2CScanner”.

|image2|

Compile and upload to Ameba, then press the reset button.

First, Realtek logo will be shown, followed by shapes, text, and
animations. Some examples are shown below.

|image3| |A small blue rectangular device with wires Description
automatically generated| |image4|

If you would like to change the Bitmap image shown on the OLED display,
you can prepare a picture/photo and resize the image based on the OLED
display that you are using. You can look for a photo resizing tool
online, for example, https://resizeimage.net/.

Next, you may use online tools such as https://javl.github.io/image2cpp/
to convert image into an array.

Code Reference

[1] Adafruit_SSD1306 library and example obtained from:
https://github.com/adafruit/Adafruit_SSD1306

[2] Adafruit_GFX library obtained from:
https://github.com/adafruit/Adafruit-GFX-Library/tree/master

.. |image1| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image01.png
   :width: 5.224in
   :height: 3.80275in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image02.png
   :width: 4.10728in
   :height: 6.28379in
.. |A screenshot of a computer program Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image03.png
   :width: 5.12in
   :height: 2.73313in
.. |image2| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image04.png
   :width: 3.44in
   :height: 4.09288in
.. |image3| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image5.jpeg
   :width: 2.27347in
   :height: 1.6in
.. |A small blue rectangular device with wires Description automatically generated| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image6.jpeg
   :width: 1.888in
   :height: 1.59392in
.. |image4| image:: ../../_static/Example_Guides/I2C_-_OLED_Display/I2C_-_OLED_Display_images/image7.jpeg
   :width: 1.82639in
   :height: 1.59151in
