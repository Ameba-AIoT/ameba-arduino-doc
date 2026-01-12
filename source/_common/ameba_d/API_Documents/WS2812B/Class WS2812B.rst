Class WS2812B
=============

**WS2812B Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

A class for using WS2812B LED with AmebaD.

**Syntax**
~~~~~~~~~~

.. code:: c++

    class WS2812B

**Members**
~~~~~~~~~~~

+-------------------------------------------+--------------------------+
| **Public Methods**                                                   |
+===========================================+==========================+
| WS2812B::WS2812B                          | Constructs a WS2812B     |
|                                           | object                   |
+-------------------------------------------+--------------------------+
| **Public Methods**                                                   |
+-------------------------------------------+--------------------------+
| WS2812B::begin                            | Check for correct pin    |
|                                           | settings and prepare to  |
|                                           | drive the WS2812B        |
+-------------------------------------------+--------------------------+
| WS2812B::show                             | Pushes the color data    |
|                                           | out to the LEDs          |
+-------------------------------------------+--------------------------+
| WS2812B::clear                            | Clear the memory         |
+-------------------------------------------+--------------------------+
| WS2812B::setLEDCount                      | Set total number of LED  |
|                                           | that will be used and    |
|                                           | allocate memory for      |
|                                           | all the LEDs             |
+-------------------------------------------+--------------------------+
| WS2812B::setPixelColor                    | Set the color of a LED   |
+-------------------------------------------+--------------------------+
| WS2812B::fill                             | Set multiple LEDs with   |
|                                           | the same color           |
+-------------------------------------------+--------------------------+
| WS2812B::colorHSV                         | Convert to RGB values    |
|                                           | from HSV                 |
+-------------------------------------------+--------------------------+
| WS2812B::rainbow                          | Fill all the LEDs with   |
|                                           | one or more cycle of     |
|                                           | hues                     |
+-------------------------------------------+--------------------------+

----------------------

**WS2812B::WS2812B**
--------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WS2812B object

**Syntax**
~~~~~~~~~~

.. code:: c++

    WS2812B(uint8_t input_pin, uint16_t num_leds);

**Parameters**
~~~~~~~~~~~~~~

``input_pin`` : The MOSI pin that is connected to the WS2812B LED.

``num_leds`` : The number of LEDs that needs to be light up

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Basics <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Basics/WS2812B_Basics.ino>`_

.. important :: Only SPI MOSI pin is valid for driving WS2812B LEDs.

.. note :: "WS2812B.h" must be included to use the class function.

------------------------

**WS2812B::begin**
------------------

**Description**
~~~~~~~~~~~~~~~

Check for correct pin settings and prepare to drive the WS2812B

**Syntax**
~~~~~~~~~~

.. code:: c++

    void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Basics <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Basics/WS2812B_Basics.ino>`_

.. important :: Only SPI MOSI pin is valid for driving WS2812B LEDs.

.. note :: "WS2812B.h" must be included to use the class function.

--------------------

**WS2812B::show**
-----------------

**Description**
~~~~~~~~~~~~~~~

Pushes the color data out to the LEDs by initialising SPI pins and revert all the unnecessary SPI pins (MISO, DC and SS) to GPIO function first. Then allocate the RGB data to each LED.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void show(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Basics <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Basics/WS2812B_Basics.ino>`_

.. important :: The amount of time needed to push the color data will increase with more LEDs.

.. note :: "WS2812B.h" must be included to use the class function.

----------------------

**WS2812B::clear**
------------------

**Description**
~~~~~~~~~~~~~~~

Clear the memory

**Syntax**
~~~~~~~~~~

.. code:: c++

    void clear (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Patterns <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Patterns/WS2812B_Patterns.ino>`_

.. important :: This function only clears the color data from memory. To turn off the LED, please use WS2812B::show().

.. note :: "WS2812B.h" must be included to use the class function.

------------------------------

**WS2812B::setLEDCount**
------------------------

**Description**
~~~~~~~~~~~~~~~

Set the total number of LEDs to be used and allocate memory for all the LEDs.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setLEDCount(uint16_t num_leds);

**Parameters**
~~~~~~~~~~~~~~

``num_leds``: total number of LEDs to be used

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WS2812B.h" must be included to use the class function.

-----------------------------

**WS2812B::setPixelColor**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Verify that memory has been successfully allocated to the LED and set the color.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setPixelColor(uint16_t led_Number, uint8_t rColor, uint8_t gColor, uint8_t bColor);

**Parameters**
~~~~~~~~~~~~~~

``led_Number``: The LED number, with 0 being the LED closest to the data input pin

``rColor``: Red brightness level (Value available from 0-255, 0 indicates LED is off and 255 indicates LED is in the maximum brightness)

``gColor``: Green brightness level (Value available from 0-255)

``bColor``: Blue brightness level (Value available from 0-255)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Patterns <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Patterns/WS2812B_Patterns.ino>`_

.. note :: "WS2812B.h" must be included to use the class function.

---------------------------

**WS2812B::fill**
-----------------

**Description**
~~~~~~~~~~~~~~~

Set multiple LEDs with the same colors

**Syntax**
~~~~~~~~~~

.. code:: c++

    void fill(uint8_t rColor, uint8_t gColor, uint8_t bColor, uint16_t first, uint16_t count);

**Parameters**
~~~~~~~~~~~~~~

``rColor``: Red brightness level (Value available from 0-255)

``gColor``: Green brightness level (Value available from 0-255)

``bColor``: Blue brightness level (Value available from 0-255)

``first``: The index of the first LED to start filling with color (Default: 0)

``count``: Total number of LEDs to be set with the color (Default: 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Basics <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Basics/WS2812B_Basics.ino>`_

.. important :: If the input parameters "first" and "count" are not provided, the default behaviour would be to fill all the LEDs.

.. note :: "WS2812B.h" must be included to use the class function.

---------------------------

**WS2812B::colorHSV**
---------------------

**Description**
~~~~~~~~~~~~~~~

Convert to RGB values from HSV (Hue Saturation Value).

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint32_t colorHSV(uint16_t hue, uint8_t sat, uint8_t val);

**Parameters**
~~~~~~~~~~~~~~

``hue``: hue value in 16-bit. (Default: 0, acceptable range from: 0 - 65535, representing one full cycle of the color wheel. Starting from 0 for red, it increments first towards yellow, and on through green, cyan, blue, magenta, and black to red.)

``sat``: Intensity or purity of the color in 8-bit. (Acceptable range from: 0 - 255, you will get pastel color when value setting is adjusted to the middle)

``val``: Brightness of a color in 8-bit. (Value available from 0-255)

**Returns**
~~~~~~~~~~~

The function returns the RGB values converted from HSV.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Patterns <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Patterns/WS2812B_Patterns.ino>`_

.. note :: "WS2812B.h" must be included to use the class function.

----------------------

**WS2812B::rainbow**
--------------------

**Description**
~~~~~~~~~~~~~~~

Fill all the LEDs with one or more cycle of hues

**Syntax**
~~~~~~~~~~

.. code:: c++

    void rainbow(uint16_t first_hue, int8_t reps, uint8_t saturation, uint8_t brightness);

**Parameters**
~~~~~~~~~~~~~~

``first_hue``: hue of first LED (Default: 0, acceptable range from: 0 - 65535, representing one full cycle of the color wheel)

``reps``: number of cycles of the color wheel over the length of the strip. (Default: 1. Negative values can be used to reverse the hue order)

``saturation``: Intensity or purity of the color in 8-bit. (Default: 255. Acceptable range from: 0 - 255, you will get pastel color when value setting is adjusted to the middle)

``brightness``: Brightness of a color in 8-bit. (Default: 60. Acceptable range from 0-255)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WS2812B_Patterns <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WS2812B/examples/WS2812B_Patterns/WS2812B_Patterns.ino>`_

.. note :: "WS2812B.h" must be included to use the class function.
