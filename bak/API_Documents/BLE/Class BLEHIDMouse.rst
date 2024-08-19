**BLEHIDMouse Class**

**Description**

A class used for creating and managing a BLE HID Mouse.

| **Syntax**
| class BLEHIDMouse

**Members**

+----------------------------+-----------------------------------------+
| **Public Constructors**    |                                         |
+============================+=========================================+
| `BLEHIDMouse:              | Constructs a BLEHIDMouse object         |
| :BLEHIDMouse <https://www. |                                         |
| amebaiot.com/en/rtl8722dm- |                                         |
| arduino-api-blehidmouse/#B |                                         |
| LEHIDMouse_BLEHIDMouse>`__ |                                         |
+----------------------------+-----------------------------------------+
| **Public Methods**         |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMouse:              | Set HID report ID for the HID Mouse     |
| :setReportID <https://www. |                                         |
| amebaiot.com/en/rtl8722dm- |                                         |
| arduino-api-blehidmouse/#B |                                         |
| LEHIDMouse_setReportID>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMouse:              | Send a HID Mouse report                 |
| :mouseReport <https://www. |                                         |
| amebaiot.com/en/rtl8722dm- |                                         |
| arduino-api-blehidmouse/#B |                                         |
| LEHIDMouse_mouseReport>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMous                | Send a HID Mouse report indicating      |
| e::mousePress <https://www | buttons pressed                         |
| .amebaiot.com/en/rtl8722dm |                                         |
| -arduino-api-blehidmouse/# |                                         |
| BLEHIDMouse_mousePress>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMouse::m            | Send a HID Mouse report indicating      |
| ouseRelease <https://www.a | buttons released                        |
| mebaiot.com/en/rtl8722dm-a |                                         |
| rduino-api-blehidmouse/#BL |                                         |
| EHIDMouse_mouseRelease>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMouse::mouseRe      | Send a HID Mouse report indicating no   |
| leaseAll <https://www.ameb | buttons pressed                         |
| aiot.com/en/rtl8722dm-ardu |                                         |
| ino-api-blehidmouse/#BLEHI |                                         |
| DMouse_mouseReleaseAll>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMo                  | Send a HID Mouse report indicating      |
| use::mouseMove <https://ww | mouse movement                          |
| w.amebaiot.com/en/rtl8722d |                                         |
| m-arduino-api-blehidmouse/ |                                         |
| #BLEHIDMouse_mouseMove>`__ |                                         |
+----------------------------+-----------------------------------------+
| `BLEHIDMouse:              | Send a HID Mouse report indicating      |
| :mouseScroll <https://www. | mouse scroll wheel movement             |
| amebaiot.com/en/rtl8722dm- |                                         |
| arduino-api-blehidmouse/#B |                                         |
| LEHIDMouse_mouseScroll>`__ |                                         |
+----------------------------+-----------------------------------------+


**BLEHIDMouse::BLEHIDMouse**

| **Description**
| Constructs a BLEHIDMouse object.

| **Syntax**
| BLEHIDMouse(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDMouse (
  https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::setReportID**

| **Description**
| Set HID report ID for the HID Mouse.

| **Syntax**
| void setReportID (uint8_t reportID);

| **Parameters**
| reportID: The report ID for the HID mouse device, corresponding to the
  HID report descriptor.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::mouseReport**

| **Description**
| Send a HID Mouse report.

| **Syntax**
| void mouseReport (hid_mouse_report_t\* report);
| void mouseReport (uint8_t buttons, int8_t x, int8_t y, int8_t scroll);

| **Parameters**
| report: pointer to mouse report structure containing data on mouse
  inputs
| buttons: bitmap indicating state of each button. 1 = pressed, 0 =
  released.
| x: mouse x-axis movement. Integer value from -127 to 127.
| y: mouse y-axis movement. Integer value from -127 to 127.
| scroll: mouse scroll wheel movement. Integer value from -127 to 127.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::mousePress**

| **Description**
| Send a HID Mouse report indicating buttons pressed.

| **Syntax**
| void mousePress (uint8_t buttons);

| **Parameters**
| buttons: bitmap indicating buttons pressed. 1 = pressed.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDMouse (
  https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::mouseRelease**

| **Description**
| Send a HID Mouse report indicating buttons released.

| **Syntax**
| void mouseRelease (uint8_t buttons);

| **Parameters**
| buttons: bitmap indicating buttons released. 1 = released.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDMouse (
  https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::mouseReleaseAll**

| **Description**
| Send a HID Mouse report indicating no buttons pressed.

| **Syntax**
| void mouseReleaseAll(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::mouseMove**

| **Description**
| Send a HID Mouse report indicating mouse movement.

| **Syntax**
| void mouseMove (int8_t x, int8_t y);

| **Parameters**
| x: mouse x-axis movement. Integer value from -127 to 127.
| y: mouse y-axis movement. Integer value from -127 to 127.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDMouse (
  https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.


**BLEHIDMouse::mouseScroll**

| **Description**
| Send a HID Mouse report indicating mouse scroll wheel movement.

| **Syntax**
| void mouseScroll (int8_t scroll);

| **Parameters**
| scroll: mouse scroll wheel movement. Integer value from -127 to 127.

| **Returns**
| NA

| **Example Code**
| Example: BLEHIDMouse (
  https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

| **Notes and Warnings**
| “BLEHIDMouse.h” must be included to use the class function.
