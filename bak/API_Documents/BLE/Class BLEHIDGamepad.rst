**BLEHIDGamepad Class**

**Description**

A class used for creating and managing a BLE HID Gamepad.

| **Syntax**
| class BLEHIDGamepad

**Members**

+----------------------------+-----------------------------------------+
| **Public Constructors**    |                                         |
+============================+=========================================+
| `BLEHIDGamepad::BLEHIDG    | Constructs a BLEHIDGamepad object       |
| amepad <https://www.amebai |                                         |
| ot.com/en/rtl8722dm-arduin |                                         |
| o-api-blehidgamepad/#BLEHI |                                         |
| DGamepad_BLEHIDGamepad>`__ |                                         |
+----------------------------+-----------------------------------------+
| **Public Methods**         |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::set        | Set HID report ID for the HID Gamepad   |
| ReportID <https://www.ameb |                                         |
| aiot.com/en/rtl8722dm-ardu |                                         |
| ino-api-blehidgamepad/#BLE |                                         |
| HIDGamepad_setReportID>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::gamepad    | Send a HID Gamepad report               |
| Report <https://www.amebai |                                         |
| ot.com/en/rtl8722dm-arduin |                                         |
| o-api-blehidgamepad/#BLEHI |                                         |
| DGamepad_gamepadReport>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::but        | Send a HID Gamepad report indicating    |
| tonPress <https://www.ameb | buttons pressed                         |
| aiot.com/en/rtl8722dm-ardu |                                         |
| ino-api-blehidgamepad/#BLE |                                         |
| HIDGamepad_buttonPress>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::buttonR    | Send a HID Gamepad report indicating    |
| elease <https://www.amebai | buttons released                        |
| ot.com/en/rtl8722dm-arduin |                                         |
| o-api-blehidgamepad/#BLEHI |                                         |
| DGamepad_buttonRelease>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BL                        | Send a HID Gamepad report indicating no |
| EHIDGamepad::buttonRelease | buttons pressed                         |
| All <https://www.amebaiot. |                                         |
| com/en/rtl8722dm-arduino-a |                                         |
| pi-blehidgamepad/#BLEHIDGa |                                         |
| mepad_buttonReleaseAll>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGa                  | Send a HID Gamepad report indicating    |
| mepad::setHat <https://www | hat switch position                     |
| .amebaiot.com/en/rtl8722dm |                                         |
| -arduino-api-blehidgamepad |                                         |
| /#BLEHIDGamepad_setHat>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGame                | Send a HID Gamepad report indicating    |
| pad::setAxes <https://www. | position of all axes                    |
| amebaiot.com/en/rtl8722dm- |                                         |
| arduino-api-blehidgamepad/ |                                         |
| #BLEHIDGamepad_setAxes>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::setLe      | Send a HID Gamepad report indicating    |
| ftStick <https://www.ameba | position of axes corresponding to left  |
| iot.com/en/rtl8722dm-ardui | analog stick                            |
| no-api-blehidgamepad/#BLEH |                                         |
| IDGamepad_setLeftStick>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::setRigh    | Send a HID Gamepad report indicating    |
| tStick <https://www.amebai | position of axes corresponding to right |
| ot.com/en/rtl8722dm-arduin | analog stick                            |
| o-api-blehidgamepad/#BLEHI |                                         |
| DGamepad_setRightStick>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDGamepad::set        | Send a HID Gamepad report indicating    |
| Triggers <https://www.ameb | position of axes corresponding to       |
| aiot.com/en/rtl8722dm-ardu | triggers                                |
| ino-api-blehidgamepad/#BLE |                                         |
| HIDGamepad_setTriggers>`__ |                                         |
+----------------------------+-----------------------------------------+


**BLEHIDGamepad::BLEHIDGamepad**

| **Description**
| Constructs a BLEHIDGamepad object.

| **Syntax**
| BLEHIDGamepad(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDGamepad
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

| **Notes and Warnings**
| By default, the BLEHIDGamepad class assumes the HID report descriptor
  implements a gamepad device with 16 buttons, 6 16-bit axes and an
  8-direction hat switch. This class will not work if a different
  gamepad report descriptor is implemented. “BLEHIDGamepad.h” must be
  included to use the class function.


**BLEHIDGamepad::setReportID**

| **Description**
| Set HID report ID for the HID Gamepad.

| **Syntax**
| void setReportID (uint8_t reportID);

| **Parameters**
| reportID: The report ID for the gamepad device, corresponding to the
  HID report descriptor.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDGamepad
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

| **Notes and Warnings**
| HID report ID should start at 1. Some systems may consider a report ID
  of 0 as invalid. “BLEHIDGamepad.h” must be included to use the class
  function.


**BLEHIDGamepad::gamepadReport**

| **Description**
| Send a HID Gamepad report.

| **Syntax**
| void gamepadReport (hid_gamepad_report_t\* report);
| void gamepadReport (uint16_t buttons, uint8_t hat, int16_t x, int16_t
  y, int16_t z, int16_t Rz, int16_t Rx, int16_t Ry);

| **Parameters**
| report: pointer to gamepad report structure containing data on all
  inputs
| buttons: bitmap indicating state of each button. 1 = pressed, 0 =
  released.
| hat: position of hat switch. Valid values:
| – GAMEPAD_HAT_CENTERED = 0
| – GAMEPAD_HAT_UP = 1
| – GAMEPAD_HAT_UP_RIGHT = 2
| – GAMEPAD_HAT_RIGHT = 3
| – GAMEPAD_HAT_DOWN_RIGHT = 4
| – GAMEPAD_HAT_DOWN = 5
| – GAMEPAD_HAT_DOWN_LEFT = 6
| – GAMEPAD_HAT_LEFT = 7
| – GAMEPAD_HAT_UP_LEFT = 8
| x: position of x axis. Integer value from -32767 to 32767.
| y: position of y axis. Integer value from -32767 to 32767.
| z: position of z axis. Integer value from -32767 to 32767.
| Rz: position of Rz axis. Integer value from -32767 to 32767.
| Rx: position of Rx axis. Integer value from -32767 to 32767.
| Ry: position of Ry axis. Integer value from -32767 to 32767.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDGamepad
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::buttonPress**

| **Description**
| Send a HID Gamepad report indicating buttons pressed.

| **Syntax**
| void buttonPress (uint16_t buttons);

| **Parameters**
| buttons: bitmap indicating buttons pressed. 1 = pressed.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.\ **

**BLEHIDGamepad::buttonRelease**

| **Description**
| Send a HID Gamepad report indicating buttons released.

| **Syntax**
| void buttonRelease (uint16_t buttons);

| **Parameters**
| buttons: bitmap indicating buttons released. 1 = released.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::buttonReleaseAll**

| **Description**
| Send a HID Gamepad report indicating no buttons pressed.

| **Syntax**
| void buttonReleaseAll (void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDGamepad
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::setHat**

| **Description**
| Send a HID Gamepad report indicating hat switch position.

| **Syntax**
| void setHat (uint8_t hat);

| **Parameters**
| hat: position of hat switch. Valid values:
| – GAMEPAD_HAT_CENTERED = 0
| – GAMEPAD_HAT_UP = 1
| – GAMEPAD_HAT_UP_RIGHT = 2
| – GAMEPAD_HAT_RIGHT = 3
| – GAMEPAD_HAT_DOWN_RIGHT = 4
| – GAMEPAD_HAT_DOWN = 5
| – GAMEPAD_HAT_DOWN_LEFT = 6
| – GAMEPAD_HAT_LEFT = 7
| – GAMEPAD_HAT_UP_LEFT = 8

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::setAxes**

| **Description**
| Send a HID Gamepad report indicating position of all axes.

| **Syntax**
| void setAxes (int16_t x, int16_t y, int16_t z, int16_t Rz, int16_t Rx,
  int16_t Ry);

| **Parameters**
| x: position of x axis. Integer value from -32767 to 32767.
| y: position of y axis. Integer value from -32767 to 32767.
| z: position of z axis. Integer value from -32767 to 32767.
| Rz: position of Rz axis. Integer value from -32767 to 32767.
| Rx: position of Rx axis. Integer value from -32767 to 32767.
| Ry: position of Ry axis. Integer value from -32767 to 32767.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDGamepad
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::setLeftStick**

| **Description**
| Send a HID Gamepad report indicating position of axes corresponding to
  left analog stick.

| **Syntax**
| void setLeftStick (int16_t x, int16_t y);

| **Parameters**
| x: position of x axis. Integer value from -32767 to 32767.
| y: position of y axis. Integer value from -32767 to 32767.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::setRightStick**

| **Description**
| Send a HID Gamepad report indicating position of axes corresponding to
  right analog stick.

| **Syntax**
| void setLeftStick (int16_t z, int16_t Rz);

| **Parameters**
| z: position of z axis. Integer value from -32767 to 32767.
| Rz: position of Rz axis. Integer value from -32767 to 32767.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.


**BLEHIDGamepad::setTriggers**

| **Description**
| Send a HID Gamepad report indicating position of axes corresponding to
  triggers.

| **Syntax**
| void setTriggers (int16_t Rx, int16_t Ry);

| **Parameters**
| Rx: position of Rx axis. Integer value from -32767 to 32767.
| Ry: position of Ry axis. Integer value from -32767 to 32767.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDGamepad.h” must be included to use the class function.
