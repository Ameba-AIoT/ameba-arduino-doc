I2C - Display Data on LCD Screen

Materials

-  AmebaPro2 [ `:mark:`AMB82
   Mini` <https://www.amebaiot.com/en/amebapro2-amb82-mini-arduino-getting-started/>`__]
   x 1

-  I2C 2×16 LCD

Example

**Introduction**
================

| Normally there are many pins on an LCD display, as shown below.
| |1|

An LCD display can be equipped with an additional processing chip to
process the data. The processing chip can connect to a microcontroller
using the I2C interface.

**Procedure**

**AMB82 Mini** wiring diagram:

|image1|

| Open the example in “File” -> “Examples” -> “AmebaWire” ->
  “LCD_HelloWorld”.
| Compile and upload to Ameba, then press the reset button.
| You can now see “Hello World” in the first line, and “Ameba” in the
  second line displayed on the LCD screen.

|3|

After 8 seconds, you can input to the Serial Monitor the string you
would like to display on the LCD.

|4|

For example, we enter “123456789” and press “Send”:

|5|

Code Reference

The required settings for each model of LCD might be different. The
constructor we use in this example is:

LiquidCrystal_I2C(uint8_t lcd_Addr, uint8_t En, uint8_t Rw, uint8_t Rs,

uint8_t d4, uint8_t d5, uint8_t d6, uint8_t d7,

uint8_t backlighPin, t_backlighPol pol);

And the setting parameters are as follows:

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); // Set
the LCD I2C address

The first parameter 0x27 is the address of I2C. Each of the following 8
parameters represents the meaning of each bit in a byte, i.e., En is bit
2, Rw is bit 1, Rs is bit 0, d4 is bit 4, and so forth.

| Call backlight() to light the screen.
| Call setCursor(0, 0) to set the position of the cursor.
| LCD inherits the Print class, so we can use lcd.print() to output
  string on the screen.

.. |1| image:: ../../_static/Example_Guides/I2C_-_Display_Data_on_I2C_Screen/I2C_Display_Data_on_LCD_Screen_images/image01.png
   :width: 6.26806in
   :height: 5.44583in
.. |image1| image:: ../../_static/Example_Guides/I2C_-_Display_Data_on_I2C_Screen/I2C_Display_Data_on_LCD_Screen_images/image02.png
   :width: 5.76806in
   :height: 3.58333in
.. |3| image:: ../../_static/Example_Guides/I2C_-_Display_Data_on_I2C_Screen/I2C_Display_Data_on_LCD_Screen_images/image3.jpeg
   :width: 5.27639in
   :height: 3.17847in
.. |4| image:: ../../_static/Example_Guides/I2C_-_Display_Data_on_I2C_Screen/I2C_Display_Data_on_LCD_Screen_images/image4.jpeg
   :width: 6.26806in
   :height: 3.73333in
.. |5| image:: ../../_static/Example_Guides/I2C_-_Display_Data_on_I2C_Screen/I2C_Display_Data_on_LCD_Screen_images/image5.jpeg
   :width: 6.26806in
   :height: 3.80764in
