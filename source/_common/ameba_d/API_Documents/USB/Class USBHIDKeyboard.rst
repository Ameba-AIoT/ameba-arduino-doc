Class USBHIDKeyboard
====================

**USBHIDKeyboard Class**
------------------------

**Description**
~~~~~~~~~~~~~~~

A class used for creating and managing a USB HID Keyboard.

**Syntax**
~~~~~~~~~~

.. code:: c++

    class USBHIDKeyboard

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| USBHIDKeyboard::USBHIDKeyboard     | Constructs a USBHIDKeyboard     |
|                                    | object                          |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::setReportID        | Set HID report ID for the HID   |
|                                    | Keyboard and HID consumer       |
|                                    | control                         |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::consumerReport     | Send a HID Consumer report      |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::keyboardReport     | Send a HID Keyboard report      |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::consumerPress      | Send a HID Consumer report      |
|                                    | indicating button pressed       |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::consumerRelease    | Send a HID Consumer report      |
|                                    | indicating button released      |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::keyPress           | Send a HID Keyboard report      |
|                                    | indicating keys pressed         |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::keyRelease         | Send a HID Keyboard report      |
|                                    | indicating keys released        |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::keyReleaseAll      | Send a HID Keyboard report      |
|                                    | indicating no keys pressed      |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::keyCharPress       | Send a HID Keyboard report      |
|                                    | indicating keys pressed to      |
|                                    | output an ASCII character       |
+------------------------------------+---------------------------------+
| USBHIDKeyboard::keySequence        | Send a HID Keyboard report      |
|                                    | indicating keys pressed to      |
|                                    | output an ASCII string          |
+------------------------------------+---------------------------------+

---------------------------------

**USBHIDKeyboard::USBHIDKeyboard**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a USBHIDKeyboard object.

**Syntax**
~~~~~~~~~~

.. code:: c++

    USBHIDKeyboard(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDKeyboard <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDKeyboard/USBHIDKeyboard.ino>`_

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

-----------------------------

**USBHIDKeyboard::setReportID**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set HID report ID for the HID Keyboard and HID consumer control.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setReportID(uint8_t reportIDKeyboard, uint8_t reportIDConsumer);

**Parameters**
~~~~~~~~~~~~~~

``reportIDKeyboard``: The report ID for the HID keyboard device, corresponding to the HID report descriptor.

``reportIDConsumer``: The report ID for the HID consumer control device, corresponding to the HID report descriptor.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

--------------------------------

**USBHIDKeyboard::consumerReport**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Consumer report.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void consumerReport(uint16_t usage_code);

**Parameters**
~~~~~~~~~~~~~~

``usage_code``: HID consumer control usage code for the button pressed.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

-------------------------------------

**USBHIDKeyboard::keyboardReport**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Keyboard report.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void keyboardReport(void);

.. code:: c++

    void keyboardReport(uint8_t modifiers, uint8_t keycode[6]);

**Parameters**
~~~~~~~~~~~~~~

``modifiers``: bitmap indicating key modifiers pressed (CTRL, ALT, SHIFT).

``keycode``: byte array indicating keys pressed.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

------------------------------

**USBHIDKeyboard::consumerPress**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Consumer report indicating button pressed.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void consumerPress(uint16_t usage_code);

**Parameters**
~~~~~~~~~~~~~~

``usage_code``: HID consumer control usage code for the button pressed.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

----------------------------------------

**USBHIDKeyboard::consumerRelease**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Consumer report indicating button released.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void consumerRelease(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDKeyboard <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDKeyboard/USBHIDKeyboard.ino>`_

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

------------------------------------------

**USBHIDKeyboard::keyPress**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Keyboard report indicating keys pressed.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void keyPress(uint16_t key);

**Parameters**
~~~~~~~~~~~~~~

``key``: HID keycode for key pressed, value ranges from 0x00 to 0xE7.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDKeyboard <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDKeyboard/USBHIDKeyboard.ino>`_

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

------------------------------

**USBHIDKeyboard::keyRelease**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Keyboard report indicating keys released.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void keyRelease(uint16_t key);

**Parameters**
~~~~~~~~~~~~~~

``key``: HID keycode for key pressed, value ranges from 0x00 to 0xE7.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

-----------------------------------

**USBHIDKeyboard::keyReleaseAll**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Keyboard report indicating no keys pressed.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void keyReleaseAll(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDKeyboard <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDKeyboard/USBHIDKeyboard.ino>`_

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

---------------------------------------

**USBHIDKeyboard::keyCharPress**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Keyboard report indicating keys pressed to output an ASCII character.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void keyCharPress(char ch);

**Parameters**
~~~~~~~~~~~~~~

``ch``: ASCII character to output.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBHIDKeyboard.h" must be included to use the class function.

-----------------------------------

**USBHIDKeyboard::keySequence**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Keyboard report indicating keys pressed to output an ASCII string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void keySequence (const char* str, uint16_t delayTime);

.. code:: c++

    void keySequence (String str, uint16_t delayTime);

**Parameters**
~~~~~~~~~~~~~~

``str``: character string to output, expressed as a char array or a String class object

``delayTime``: time delay between key press and release, in milliseconds. Default value of 5.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDKeyboard <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDKeyboard/USBHIDKeyboard.ino>`_

.. note :: "USBHIDKeyboard.h" must be included to use the class function.
