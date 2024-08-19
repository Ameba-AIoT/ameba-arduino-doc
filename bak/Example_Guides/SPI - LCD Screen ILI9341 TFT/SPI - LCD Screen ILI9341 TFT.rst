If you are not familiar with SPI, please read `Introduction to
SPI <https://www.amebaiot.com/spi-intro/>`__ first.

 

Preparation

-  AmebaPro2 [AMB82 MINI] x 1

-  ILI9341 TFT LCD with SPI interface x 1

Example

We have tested the following two models of ILI9341 TFT LCD with SPI
interface:

-  Adafruit 2.8″ TFT LCD (with touch screen)

   -  https://www.adafruit.com/products/1651

   -  https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2?view=all

-  QVGA 2.2″ TFT LCD

   -  http://www.lcdwiki.com/2.2inch_SPI_Module_ILI9341_SKU:MSP2202

Common pins in ILI9341 TFT LCD with SPI interface:

-  MOSI: Standard SPI Pin

-  MISO: Standard SPI Pin

-  SLK: Standard SPI Pin

-  CS: Standard SPI Pin

-  RESET: Used to reboot LCD.

-  D/C: Data/Command. When it is at LOW, the signal transmitted are
   commands, otherwise the data transmitted are data.

-  LED (or BL): Adapt the screen backlight. Can be controlled by PWM or
   connected to VCC for 100% backlight.

-  VCC: Connected to 3V or 5V, depends on its spec.

-  GND: Connected to GND.

**:mark:`
`**

**AMB82 MINI and QVGA TFT LCD Wiring** **Diagram:**

|image1|

**AMB82 MINI and Adafruit 2.8” TFT LCD touch** **shield:**

|image2|

Please note that this shield model enables the backlight by default and
pin 8 is not for backlight, and the VCC should be connected to 5V.

Open the example, “File” -> “Examples”-> “AmebaSPI” ->
“LCD_Screen_ILI9341_TFT”

|Graphical user interface, application Description automatically
generated|

| Compile and upload to Ameba, then press the reset button.
| Then you can see some display tests appear on the LCD screen, such as
  displaying different colors, drawing vertical and horizontal lines,
  drawing circles, etc.…

|4|

:mark:`Besides, it can also display any user images based on the screen
size. Using the online Image converting tool
`here <http://www.rinkydinkelectronics.com/t_imageconverter565.php>`__
that supports input images in png, .jpg and .gif ad output as .c file.
Upon converting is done, place the .c file in our template Amebalogo.h
file and upload the code again.`

|A picture containing text, screenshot, graphic design Description
automatically generated|\ |image3| :mark:`u`

Code Reference

-  |  **RGB 16-bit**
   | ILI9341 uses RGB 16-bit to display colors. Different from RGB
     24-bit, it uses 5 bits for red, 6 bits for green, 5 bits for blue.
     For example, the RGB 24-bit representation of sky blue is 0x87CEFF,
     that is in binary:

   -  Red: 0x87 = B10000111

   -  Green: 0xCE = B11001110

   -  Blue: 0xFF = B11111111

..

   and converted to RGB 16-bit:

-  Red: B10000

-  Green: B110011

-  Blue: B11111

..

   Then concatenate them, which forms B1000011001111111 = 0x867F

-  **Drawing of ILI9341**

   -  First you must specify the range of the rectangle to draw, then
      pass the 2-byte RGB 16-bit color to ILI9341 corresponding to each
      pixel one by one, in this way ILI9341 fills each color to each
      pixel.

   -  You still must specify the drawing range even though the range
      covers only one pixel.

   -  From the rules we mentioned above, we can conclude that drawing
      vertical or horizontal lines are faster than diagonal lines.

-  **Printing text on ILI9341**

   -  In our API, each character is 5×7 but each character is printed to
      size 6×8 (its right side and below are left blank), so as to
      separate from next character. For example, the character “A”:|5|

   -  The font size represents the dot size. For example, if the font
      size is 2, each dot in the character is a 2×2 rectangle

-  **Screen rotation**

   -  ILI9341 provides 0, 90, 180, 270 degrees screen rotation.

   -  If the original width is 240 and original height is 320, when the
      screen rotates 90 degrees, the width becomes 320 and the height
      becomes 240.

.. |image1| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image01.png
   :width: 6.26806in
   :height: 3.64407in
.. |image2| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image02.png
   :width: 6.14998in
   :height: 4.12569in
.. |Graphical user interface, application Description automatically generated| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image03.png
   :width: 5.08696in
   :height: 5.93516in
.. |4| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image04.png
   :width: 6.26806in
   :height: 2.00972in
.. |A picture containing text, screenshot, graphic design Description automatically generated| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image5.jpeg
   :width: 2.79167in
   :height: 1.45787in
.. |image3| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image06.png
   :width: 2.88542in
   :height: 4.11875in
.. |5| image:: ../../_static/Example_Guides/SPI_-_LCD_Screen_ILI9341_TFT/SPI_-_LCD_Screen_ILI9341_TFT_images/image07.png
   :width: 2.06944in
   :height: 2.76736in
