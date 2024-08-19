**BLEHIDKeyboard Class**

**Description**

A class used for creating and managing a BLE HID Keyboard.

**Syntax**

class BLEHIDKeyboard

**Members**

**Public Constructors**

+------------------------------------+---------------------------------+
| BLEHIDKeyboard::BLEHIDKeyboard     | Constructs a BLEHIDKeyboard     |
|                                    | object                          |
+====================================+=================================+
+------------------------------------+---------------------------------+

**Public Methods**

+------------------------------------+---------------------------------+
| BLEHIDKeyboard::setReportID        | Set HID report ID for the HID   |
|                                    | Keyboard and HID consumer       |
|                                    | control                         |
+====================================+=================================+
| BLEHIDKeyboard::consumerReport     | Send a HID Consumer report      |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::keyboardReport     | Send a HID Keyboard report      |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::consumerPress      | Send a HID Consumer report      |
|                                    | indicating button pressed       |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::consumerRelease    | Send a HID Consumer report      |
|                                    | indicating button released      |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::keypress           | Send a HID Keyboard report      |
|                                    | indicating keys pressed         |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::keyRelease         | Send a HID Keyboard report      |
|                                    | indicating keys released        |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::keyReleaseAll      | Send a HID Keyboard report      |
|                                    | indicating no keys pressed      |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::keyCharPress       | Send a HID Keyboard report      |
|                                    | indicating keys pressed to      |
|                                    | output an ASCII character       |
+------------------------------------+---------------------------------+
| BLEHIDKeyboard::keySequence        | Send a HID Keyboard report      |
|                                    | indicating keys pressed to      |
|                                    | output an ASCII string          |
+------------------------------------+---------------------------------+


**BLEHIDKeyboard::BLEHIDKeyboard**

**Description**

Constructs a BLEHIDKeyboard object.

**Syntax**

BLEHIDKeyboard(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEHIDKeyboard
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDKeyboard/BLEHIDKeyboard.ino)

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.\ **

**BLEHIDKeyboard::setReportID**

**Description**

Set HID report ID for the HID Keyboard and HID consumer control.

**Syntax**

void setReportID (uint8_t reportIDKeyboard, uint8_t reportIDConsumer);

**Parameters**

reportIDKeyboard: The report ID for the HID keyboard device,
corresponding to the HID report descriptor.

reportIDConsumer: The report ID for the HID consumer control device,
corresponding to the HID report descriptor.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::consumerReport**

**Description**

Send a HID Consumer report.

**Syntax**

void consumerReport (uint16_t usage_code);

**Parameters**

usage_code: HID consumer control usage code for the button pressed.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::keyboardReport**

**Description**

Send a HID Keyboard report.

**Syntax**

void keyboardReport (void);

void keyboardReport (uint8_t modifiers, uint8_t keycode[6]);

**Parameters**

modifiers: bitmap indicating key modifiers pressed (CTRL, ALT, SHIFT).

keycode: byte array indicating keys pressed.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::consumerPress**

**Description**

Send a HID Consumer report indicating button pressed.

**Syntax**

void consumerPress (uint16_t usage_code);

**Parameters**

usage_code: HID consumer control usage code for the button pressed.

**Returns**

NA

**Example Code**

Example: BLEHIDKeyboard
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDKeyboard/BLEHIDKeyboard.ino)

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::consumerRelease**

**Description**

Send a HID Consumer report indicating button released.

**Syntax**

void consumerRelease (void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEHIDKeyboard
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDKeyboard/BLEHIDKeyboard.ino)

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::keypress**

**Description**

Send a HID Keyboard report indicating keys pressed.

**Syntax**

void keyPress (uint16_t key);

**Parameters**

key: HID keycode for key pressed, value ranges from 0x00 to 0xE7.

**Returns**

NA

**Example Code**

Example: BLEHIDKeyboard
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDKeyboard/BLEHIDKeyboard.ino)

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::keyRelease**

**Description**

Send a HID Keyboard report indicating keys released.

**Syntax**

void keyRelease (uint16_t key);

**Parameters**

key: HID keycode for key pressed, value ranges from 0x00 to 0xE7.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::keyReleaseAll**

**Description**

Send a HID Keyboard report indicating no keys pressed.

**Syntax**

void keyReleaseAll (void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEHIDKeyboard
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDKeyboard/BLEHIDKeyboard.ino)

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::keyCharPress**

**Description**

Send a HID Keyboard report indicating keys pressed to output a specific
ASCII character.

**Syntax**

void keyCharPress (char ch);

**Parameters**

ch: ASCII character to output.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.

**BLEHIDKeyboard::keySequence**

**Description**

Send a HID Keyboard report indicating keys pressed to output an ASCII
string.

**Syntax**

void keySequence (const char\* str, uint16_t delayTime);

void keySequence (String str, uint16_t delayTime);

**Parameters**

str: character string to output, expressed as a pointer to a character
array or a String class object

delayTime: time delay between key press and release, in milliseconds.
Default value of 5.

**Returns**

NA

**Example Code**

Example: BLEHIDKeyboard
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDKeyboard/BLEHIDKeyboard.ino)

**Notes and Warnings**

“BLEHIDKeyboard.h” must be included to use the class function.
