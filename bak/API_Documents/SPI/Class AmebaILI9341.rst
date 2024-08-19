**AmebaILI9341 Class**

| **Description**
| A class to use ILI9341 TFT SPI display driver on Ameba.

| **Syntax**
| class AmebaILI9341

**Members**

+--------------------------+-------------------------------------------+
| **Public Constructors**  |                                           |
+==========================+===========================================+
| `A                       | Constructs an AmebaILI9341 object         |
| mebaILI9341::AmebaILI934 |                                           |
| 1 <https://www.amebaiot. |                                           |
| com/en/rtl8722dm-arduino |                                           |
| -api-amebaili9341/#Ameba |                                           |
| ILI9341_AmebaILI9341>`__ |                                           |
+--------------------------+-------------------------------------------+
| **Public Methods**       |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI93              | Initialize SPI, pin mapping and screen    |
| 41::begin <https://www.a | configuration                             |
| mebaiot.com/en/rtl8722dm |                                           |
| -arduino-api-amebaili934 |                                           |
| 1/#AmebaILI9341begin>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::setAddr   | Initialize image size and position        |
| ess <https://www.amebaio |                                           |
| t.com/en/rtl8722dm-ardui |                                           |
| no-api-amebaili9341/#Ame |                                           |
| baILI9341_setAddress>`__ |                                           |
+--------------------------+-------------------------------------------+
| `A                       | SPI transfer a command                    |
| mebaILI9341::writecomman |                                           |
| d <https://www.amebaiot. |                                           |
| com/en/rtl8722dm-arduino |                                           |
| -api-amebaili9341/#Ameba |                                           |
| ILI9341_writecommand>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::write     | SPI transfer a piece of data              |
| data <https://www.amebai |                                           |
| ot.com/en/rtl8722dm-ardu |                                           |
| ino-api-amebaili9341/#Am |                                           |
| ebaILI9341_writedata>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::setRotati | Set screen orientation                    |
| on <https://www.amebaiot |                                           |
| .com/en/rtl8722dm-arduin |                                           |
| o-api-amebaili9341/#Ameb |                                           |
| aILI9341_setRotation>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::fillScr   | Fill the screen with a color              |
| een <https://www.amebaio |                                           |
| t.com/en/rtl8722dm-ardui |                                           |
| no-api-amebaili9341/#Ame |                                           |
| baILI9341_fillScreen>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaIL                 | Clear screen                              |
| I9341::clr <https://www. |                                           |
| amebaiot.com/en/rtl8722d |                                           |
| m-arduino-api-amebaili93 |                                           |
| 41/#AmebaILI9341_clr>`__ |                                           |
+--------------------------+-------------------------------------------+
| `Ame                     | Fill a rectangle shape with color and     |
| baILI9341::fillRectangle | display on the screen.                    |
|  <https://www.amebaiot.c |                                           |
| om/en/rtl8722dm-arduino- |                                           |
| api-amebaili9341/#AmebaI |                                           |
| LI9341_fillRectangle>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::drawP     | Draw a pixel by coordinates on the        |
| ixel <https://www.amebai | screen.                                   |
| ot.com/en/rtl8722dm-ardu |                                           |
| ino-api-amebaili9341/#Am |                                           |
| ebaILI9341_drawPixel>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::dra       | Draw a character in the frame buffer but  |
| wChar <https://www.ameba | does not refresh.                         |
| iot.com/en/rtl8722dm-ard |                                           |
| uino-api-amebaili9341/#A |                                           |
| mebaILI9341_drawChar>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::dra       | Draw a line and display on the screen     |
| wLine <https://www.ameba |                                           |
| iot.com/en/rtl8722dm-ard |                                           |
| uino-api-amebaili9341/#A |                                           |
| mebaILI9341_drawLine>`__ |                                           |
+--------------------------+-------------------------------------------+
| `Ame                     | Draw a rectangular shape and display on   |
| baILI9341::drawRectangle | the screen.                               |
|  <https://www.amebaiot.c |                                           |
| om/en/rtl8722dm-arduino- |                                           |
| api-amebaili9341/#AmebaI |                                           |
| LI9341_drawRectangle>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::drawCir   | Draw a circle shape and display on the    |
| cle <https://www.amebaio | screen.                                   |
| t.com/en/rtl8722dm-ardui |                                           |
| no-api-amebaili9341/#Ame |                                           |
| baILI9341_drawCircle>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI934             | Display a character and display on the    |
| 1::write <https://www.am | screen                                    |
| ebaiot.com/en/rtl8722dm- |                                           |
| arduino-api-amebaili9341 |                                           |
| /#AmebaILI9341_write>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::get       | Get the width of the image                |
| Width <https://www.ameba |                                           |
| iot.com/en/rtl8722dm-ard |                                           |
| uino-api-amebaili9341/#A |                                           |
| mebaILI9341_getWidth>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::getHe     | Get the height of the image               |
| ight <https://www.amebai |                                           |
| ot.com/en/rtl8722dm-ardu |                                           |
| ino-api-amebaili9341/#Am |                                           |
| ebaILI9341_getHeight>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::setCu     | Set the cursor to a specific position on  |
| rsor <https://www.amebai | the screen                                |
| ot.com/en/rtl8722dm-ardu |                                           |
| ino-api-amebaili9341/#Am |                                           |
| ebaILI9341_setCursor>`__ |                                           |
+--------------------------+-------------------------------------------+
| `Ame                     | Set foreground color                      |
| baILI9341::setForeground |                                           |
|  <https://www.amebaiot.c |                                           |
| om/en/rtl8722dm-arduino- |                                           |
| api-amebaili9341/#AmebaI |                                           |
| LI9341_setForeground>`__ |                                           |
+--------------------------+-------------------------------------------+
| `Ame                     | Set background color                      |
| baILI9341::setBackground |                                           |
|  <https://www.amebaiot.c |                                           |
| om/en/rtl8722dm-arduino- |                                           |
| api-amebaili9341/#AmebaI |                                           |
| LI9341_setBackground>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI9341::setFontSi | Set character font size                   |
| ze <https://www.amebaiot |                                           |
| .com/en/rtl8722dm-arduin |                                           |
| o-api-amebaili9341/#Ameb |                                           |
| aILI9341_setFontSize>`__ |                                           |
+--------------------------+-------------------------------------------+
| `AmebaILI934             | Reset the module                          |
| 1::reset <https://www.am |                                           |
| ebaiot.com/en/rtl8722dm- |                                           |
| arduino-api-amebaili9341 |                                           |
| /#AmebaILI9341_reset>`__ |                                           |
+--------------------------+-------------------------------------------+


**AmebaILI9341::AmebaILI9341**

**Description**

The main class constructor when using AmebaILI9341 SPI display modules.

**Syntax**

AmebaILI9341::AmebaILI9341(int csPin, int dcPin, int resetPin)

**Parameters**

| csPin: the Chip Select pin in AmebaD development board
| dcPin: the Data Command pin in AmebaD development board
| resetPin: the Reset pin in AmebaD development board

**Returns**

NA

**Example Code**

Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

**Notes and Warnings**

“AmebaILI9341.h” must be included to use the class function.


**AmebaILI**\ **9341::begin**

| **Description**
| Initialize hardware SPI, configure SPI DC and Reset pin mapping and
  SPI screen hardware module configuration including power control,
  memory access control, etc.

| **Syntax**
| void begin(void);

| **Parameters**
| NA

| **Returns**
| NA

**Example Code**

Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

**Notes and Warnings**

| “AmebaILI9341.h” must be included to use the class function.
| This method is required to run first before other operations on the
  display.


**AmebaILI9341::setAddress**

| **Description**
| Initialize image size and positioning on the display

| **Syntax**
| void setAddress(uint16_t x0, uint16_t y0, uint16_t x1, uint16_t y1);

| **Parameters**
| x0: leftmost coordinate of the image
| y0: top coordinate of the image
| x1: rightmost coordinate of the image
| y1: bottom coordinate of the image

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Do not use this to set the cursor, use “setCursor” method instead.
  “AmebaILI9341.h” must be included to use the class function.


**AmebaILI9341::writecommand**

**Description**

Write a SPI command to the hardware peripheral

| **Syntax**
| void writecommand(uint8_t command);

| **Parameters**
| command: SPI command in 8-bit

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “AmebaILI9341.h” must be included to use the class function.\ **

**AmebaILI9341::writedata**

**Description**

Write a SPI data to the hardware peripheral

| **Syntax**
| void writedata(uint8_t data);

| **Parameters**
| data: SPI data in 8-bit

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Only use this method to write 1 byte at a time. “AmebaILI9341.h” must
  be included to use the class function.


**AmebaILI9341::setRotation**

| **Description**
| Setting screen orientation, “0” for no rotation, “1” for 90 degrees
  rotation, “2” for 180 degrees rotation, “3” for 270 degrees rotation.

| **Syntax**
| void setRotation(uint8_t m);

| **Parameters**
| m: select desired screen orientation, expressing it as an integer.
  (Defualt: 0)

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

**Notes and Warnings**

Although “0” for no rotation, “1” for 90 degrees rotation, “2” for 180
degrees rotation, “3” for 270 degrees rotation, if m is more than 3, for
example, m = 4: there will be no rotation, m= 5: 90 degrees rotation and
so on.

“AmebaILI9341.h” must be included to use the class function.


**AmebaILI9341::fillScreen**

| **Description**
| Fill the entire screen with a single color

| **Syntax**
| void fillScreen(uint16_t color);

| **Parameters**
| color: a 16-bit color, color definition (RGB565) can be found in
  AmebaILI9341.h

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Refer to AmebaILI9341.h for available colors. “AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::clr**

| **Description**
| Clear the screen.

| **Syntax**
| void clr (void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| Background color can be changed by calling setBackground(). Refer to
  AmebaILI9341.h for available colors of setBackground() function input
  parameter. ”AmebaILI9341.h” must be included to use the class
  function.


**AmebaILI9341::fillRectangle**

**Description**

Fill a rectangle shape with color and display on the screen.

| **Syntax**
| void fillRectangle(int16_t x, int16_t y, int16_t w, int16_t h,
  uint16_t color);

| **Parameters**
| x: leftmost coordinate of the rectangle shape
| y: top coordinate of the rectangle shape
| w: width of the rectangle shape
| h: height of the rectangle shape
| color: the color of the rectangle shape

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

**Notes and Warnings**

Refer to AmebaILI9341.h for available colors. ”AmebaILI9341.h” must be
included to use the class function.


**AmebaILI9341::drawPixel**

**Description**

Draw a single pixel by coordinates on the screen.

| **Syntax**
| void drawPixel(int16_t x, int16_t y, uint16_t color);

| **Parameters**
| x: leftmost coordinate of the pixel
| y: top coordinate of the pixel
| color: the color of the pixel

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Refer to AmebaILI9341.h for available colors. ”AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::drawChar**

| **Description**
| Draw a character in the frame buffer but does not refresh.

| **Syntax**
| void AmebaILI9341::drawChar(unsigned char c)
| void AmebaILI9341::drawChar(int16_t x, int16_t y, unsigned char c,
  uint16_t \_fontcolor, uint16_t \_background, uint8_t \_fontsize)

| **Parameters**
| x: leftmost coordinate of the character
| y: top coordinate of the character
| c: a character
| \_fontcolor: character font color
| \_background: character background color
| \_fontsize: character font size

| **Returns**
| NA

| **Example Code**
| NA

**Notes and Warnings**

This method only stores the string of character in a buffer frame. The
Print/Println method have to be called in order to display a string of
character on the serial monitor. Refer to AmebaILI9341.h for available
colors. ”AmebaILI9341.h” must be included to use the class function.


**AmebaILI9341::drawLine**

| **Description**
| Draw a line and display on the screen.

| **Syntax**
| void drawLine(int16_t x0, int16_t y0, int16_t x1, int16_t y1, uint16_t
  color);

void drawLine(int16_t x0, int16_t y0, int16_t x1, int16_t y1);

| **Parameters**
| x0: leftmost coordinate of the line
| y0: top coordinate of the line
| x1: leftmost coordinate of the line
| y1: top coordinate of the line
| color: the color of the line

| **Returns**
| NA

| **Example Code**
| NA

**Notes and Warnings**

Refer to AmebaILI9341.h for available colors. ”AmebaILI9341.h” must be
included to use the class function.


**AmebaILI9341::drawRectangle**

**Description**

Draw a rectangular shape and display on the screen.

| **Syntax**
| void drawRectangle(int16_t x, int16_t y, int16_t w, int16_t h,
  uint16_t color);

void drawRectangle(int16_t x, int16_t y, int16_t w, int16_t h);

| **Parameters**
| x: leftmost coordinate of the rectangular shape
| y: top coordinate of the rectangular shape
| w: width of the rectangular shape
| h: height of the rectangular shape
| color: the color of the rectangular shape outline

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Refer to AmebaILI9341.h for available colors. ”AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::drawCircle**

**Description**

Draw a circle shape and display on the screen.

| **Syntax**
| void drawCircle(int16_t x0, int16_t y0, int16_t r, uint16_t color);

void drawCircle(int16_t x0, int16_t y0, int16_t r);

| **Parameters**
| x0: leftmost coordinate of the circle shape
| y0: top coordinate of the circle shape
| r: radius of the circle shape
| color: the color of the circle shape outline

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Refer to AmebaILI9341.h for available colors. ”AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::write**

| **Description**
| Display a character and display on the screen.

| **Syntax**
| virtual size_t write(uint8_t);

| **Parameters**
| c: a character to be written on the screen

| **Returns**
| This function returns the number of bytes written.

| **Example Code**
| NA

| **Notes and Warnings**
| This an inherited method from Print class and is seldom used.
  ”AmebaILI9341.h” must be included to use the class function.


**AmebaILI9341::getWidth**

| **Description**
| Get the width of the image.

| **Syntax**
| int16_t getWidth(void);

| **Parameters**
| NA

| **Returns**
| This function returns the width of the image.

| **Example Code**
| NA

| **Notes and Warnings**
| The width is defined in” AmebaILI9341.h”. ” AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::getHeight**

| **Description**
| Get the height of the image.

| **Syntax**
| int16_t getHeight(void);

| **Parameters**
| NA

| **Returns**
| This function returns the height of the image.

| **Example Code**
| NA

| **Notes and Warnings**
| The height is defined in” AmebaILI9341.h”. ”AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::setCursor**

| **Description**
| Set the cursor to a specific position on the screen.

| **Syntax**
| void setCursor(int16_t x, int16_t y);

| **Parameters**
| x: coordinate on the x-axis
| y: coordinate on the y-axis

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| ”AmebaILI9341.h” must be included to use the class function.


**AmebaILI9341::setForeground**

| **Description**
| Set foreground color.

| **Syntax**
| void setForeground(uint16_t color);

| **Parameters**
| color: desired colors for foreground

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5 testText() function, to set foreground
  colors for different font sizes.

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| Refer to AmebaILI9341.h for available colors. “AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::setBackground**

| **Description**
| Set background color.

| **Syntax**
| void setBackground(uint16_t color);

| **Parameters**
| \_background: desired background color

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| Refer to AmebaILI9341.h for available colors. “AmebaILI9341.h” must be
  included to use the class function.


**AmebaILI9341::setFontSize**

| **Description**
| Set the font size of the characters to be printed on the screen.

| **Syntax**
| void AmebaILI9341::setFontSize(uint8_t size)

| **Parameters**
| size: desired font size. (Default values:1 to 5). Smaller value is
  indicating smaller font size.

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| “AmebaILI9341.h” must be included to use the class function.


**AmebaILI9341::reset**

**Description**

Reset the SPI display module using the Reset pin.

| **Syntax**
| void reset(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “AmebaILI9341.h” must be included to use the class function.
