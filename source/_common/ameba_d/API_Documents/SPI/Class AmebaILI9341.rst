Class AmebaILI9341
==================

**AmebaILI9341 Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class to use ILI9341 TFT SPI display driver on Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class AmebaILI9341

**Members**
~~~~~~~~~~~

+-------------------------------+-------------------------------------------+
| **Public Constructors**                                                   |
+===============================+===========================================+
| AmebaILI9341::AmebaILI934     | Constructs an AmebaILI9341 object         |
+-------------------------------+-------------------------------------------+
| **Public Methods**                                                        |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::begin           | Initialize SPI, pin mapping and screen    |
|                               | configuration                             |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::setAddress      | Initialize image size and position        |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::writecommand    | SPI transfer a command                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::writedata       | SPI transfer a piece of data              |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::setRotation     | Set screen orientation                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::fillScreen      | Fill the screen with a color              |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::clr             | Clear screen                              |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::fillScreen      | Fill a rectangle shape with color and     |
|                               | display on the screen.                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::drawPixel       | Draw a pixel by coordinates on the        |
|                               | screen                                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::drawChar        | Draw a character in the frame buffer but  |
|                               | does not refresh.                         |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::drawLine        | Draw a line and display on the screen     |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::drawRectangle   | Draw a rectangular shape and display on   |
|                               | the screen.                               |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::drawCircle      | Draw a circle shape and display on the    |
|                               | screen                                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::drawBitmap      | Draw an image in bitmap format on the     |
|                               | screen                                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::write           | Display a character and display on the    |
|                               | screen                                    |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::getWidth        | Get the width of the image                |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::getHeight       | Get the height of the image               |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::setCursor       | Set the cursor to a specific position on  |
|                               | the screen                                |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::setForeground   | Set foreground color                      |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::setBackground   | Set background color                      |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::setFontSize     | Set character font size                   |
+-------------------------------+-------------------------------------------+
| AmebaILI9341::reset           | Reset the module                          |
+-------------------------------+-------------------------------------------+

-------------------------------------------------

**AmebaILI9341::AmebaILI9341**
------------------------------

**Description**
~~~~~~~~~~~~~~~

The main class constructor when using AmebaILI9341 SPI display modules.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    AmebaILI9341(int csPin, int dcPin, int resetPin);

**Parameters**
~~~~~~~~~~~~~~

``csPin``: the Chip Select pin in AmebaD development board

``dcPin``: the Data Command pin in AmebaD development board

``resetPin``: the Reset pin in AmebaD development board

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::begin**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Initialize hardware SPI, configure SPI DC and Reset pin mapping and SPI screen hardware module configuration including power control, memory access control, etc.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. important :: This method is required to run first before other operations on the display.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::setAddress**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize image size and positioning on the display

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setAddress(uint16_t x0, uint16_t y0, uint16_t x1, uint16_t y1);

**Parameters**
~~~~~~~~~~~~~~

``x0``: leftmost coordinate of the image

``y0``: top coordinate of the image

``x1``: rightmost coordinate of the image

``y1``: bottom coordinate of the image

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. Caution :: Do not use this to set the cursor, use "setCursor" method instead.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::writecommand**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Write a SPI command to the hardware peripheral

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void writecommand(uint8_t command);

**Parameters**
~~~~~~~~~~~~~~

``command``: SPI command in 8-bit

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~
NA

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::writedata**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Write a SPI data to the hardware peripheral

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void writedata(uint8_t data);

**Parameters**
~~~~~~~~~~~~~~

``data``: SPI data in 8-bit

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: Only use this method to write 1 byte at a time.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::setRotation**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Setting screen orientation, "0" for no rotation, "1" for 90 degrees rotation, "2" for 180 degrees rotation, "3" for 270 degrees rotation.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  void setRotation(uint8_t m);

**Parameters**
~~~~~~~~~~~~~~

``m``: select desired screen orientation, expressing it as an integer. Default value is "0".

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. important :: Although "0" for no rotation, "1" for 90 degrees rotation, "2" for 180 degrees rotation, "3" for 270 degrees rotation, if m is more than 3, for example, m = 4 : there will be no rotation, m = 5 : 90 degrees rotation and so on.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::fillScreen**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Fill the entire screen with a single color

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void fillScreen(uint16_t color);

**Parameters**
~~~~~~~~~~~~~~

``color``: a 16-bit color, color definition (RGB565) can be found in AmebaILI9341.h

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. tip ：：Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::clr**
---------------------

**Description**
~~~~~~~~~~~~~~~

Clear the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void clr (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. important :: Background color can be changed by calling setBackground().

.. tip :: Refer to "AmebaILI9341.h" for available colors of setBackground() function input parameter.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::fillRectangle**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Fill a rectangle shape with color and display on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void fillRectangle(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);

**Parameters**
~~~~~~~~~~~~~~

``x``: leftmost coordinate of the rectangle shape

``y``: top coordinate of the rectangle shape

``w``: width of the rectangle shape

``h``: height of the rectangle shape

``color``: the color of the rectangle shape

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. tip :: Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::drawPixel**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a single pixel by coordinates on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawPixel(int16_t x, int16_t y, uint16_t color);

**Parameters**
~~~~~~~~~~~~~~

``x``: leftmost coordinate of the pixel

``y``: top coordinate of the pixel

``color``: the color of the pixel

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. tip :: Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::drawChar**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a character in the frame buffer but does not refresh.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AmebaILI9341::drawChar(unsigned char c);

.. code-block:: c++

    void AmebaILI9341::drawChar(int16_t x, int16_t y, unsigned char c, uint16_t _fontcolor, uint16_t _background, uint8_t _fontsize)

**Parameters**
~~~~~~~~~~~~~~

``x``: leftmost coordinate of the character

``y``: top coordinate of the character

``c``: a character

``_fontcolor``: character font color

``_background``: character background color

``_fontsize``: character font size

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: This method only stores the string of character in a buffer frame. The Print/Println method have to be called in order to display a string of character on the serial monitor.

.. tip :: Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::drawLine**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a line and display on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawLine(int16_t x0, int16_t y0, int16_t x1, int16_t y1, uint16_t color);

.. code-block:: c++

    void drawLine(int16_t x0, int16_t y0, int16_t x1, int16_t y1);

**Parameters**
~~~~~~~~~~~~~~

``x0``: leftmost coordinate of the line

``y0``: top coordinate of the line

``x1``: leftmost coordinate of the line

``y1``: top coordinate of the line

``color``: the color of the line

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. tip :: Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::drawRectangle**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a rectangular shape and display on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawRectangle(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);

.. code-block:: c++

    void drawRectangle(int16_t x, int16_t y, int16_t w, int16_t h);

**Parameters**
~~~~~~~~~~~~~~

``x``: leftmost coordinate of the rectangular shape

``y``: top coordinate of the rectangular shape

``w``: width of the rectangular shape

``h``: height of the rectangular shape

``color``: the color of the rectangular shape outline

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. tip :: Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::drawCircle**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a circle shape and display on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawCircle(int16_t x0, int16_t y0, int16_t r, uint16_t color);

.. code-block:: c++

    void drawCircle(int16_t x0, int16_t y0, int16_t r);

**Parameters**
~~~~~~~~~~~~~~

``x0``: leftmost coordinate of the circle shape

``y0``: top coordinate of the circle shape

``r``: radius of the circle shape

``color``: the color of the circle shape outline

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. tip :: Refer to "AmebaILI9341.h" for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::drawBitmap**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Draw an image in Bitmap format on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawBitmap(int16_t x, int16_t y, int16_t w, int16_t h, const unsigned short *color);

**Parameters**
~~~~~~~~~~~~~~

``x``: leftmost coordinate of the Bitmap image

``y``: top coordinate of the Bitmap image

``w``: width of the Bitmap image

``h``: height of the Bitmap image

``color``: the string name of the Bitmap image

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: Please convert the original image to Bitmap and save as "AmebaLogo.h". Last input parameter name should be same as the image name used in "AmebaLogo.h".

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::write**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Display a character and display on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual size_t write(uint8_t);

**Parameters**
~~~~~~~~~~~~~~

``c``: a character to be written on the screen

**Returns**
~~~~~~~~~~~

This function returns the number of bytes written.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: This an inherited method from Print class and is seldom used.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::getWidth**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Get the width of the image.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int16_t getWidth(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the width of the image.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: The width is defined in" AmebaILI9341.h". "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::getHeight**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get the height of the image.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int16_t getHeight(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the height of the image.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: The height is defined in" AmebaILI9341.h". "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::setCursor**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Set the cursor to a specific position on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setCursor(int16_t x, int16_t y);

**Parameters**
~~~~~~~~~~~~~~

``x``: coordinate on the x-axis

``y``: coordinate on the y-axis

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::setForeground**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set foreground color.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setForeground(uint16_t color);

**Parameters**
~~~~~~~~~~~~~~

``color``: desired colors for foreground

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. tip :: testText() function, to set foreground colors for different font sizes. Refer to AmebaILI9341.h for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::setBackground**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set background color.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBackground(uint16_t color);

**Parameters**
~~~~~~~~~~~~~~

``_background``: desired background color

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. tip :: Refer to AmebaILI9341.h for available colors.

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::setFontSize**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Set the font size of the characters to be printed on the screen.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AmebaILI9341::setFontSize(uint8_t size)

**Parameters**
~~~~~~~~~~~~~~

``size``: desired font size. (Default values:1 to 5). Smaller value is indicating smaller font size.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ILI9341_TFT_LCD_PM2.5 <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino>`_

.. note :: "AmebaILI9341.h" must be included to use the class function.

-------------------------------------------------

**AmebaILI9341::reset**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Reset the SPI display module using the Reset pin.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void reset(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaILI9341.h" must be included to use the class function.
