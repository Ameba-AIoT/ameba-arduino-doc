Class USBHIDMouse
=================

.. contents::
  :local:
  :depth: 2

**USBHIDMouse Class**
---------------------

**Description**
~~~~~~~~~~~~~~~

A class used for creating and managing a USB HID Mouse.

**Syntax**
~~~~~~~~~~

.. code:: c++

    class USBHIDMouse

**Members**
~~~~~~~~~~~

**Public Constructors**

+--------------------------------+-------------------------------------+
| USBHIDMouse::USBHIDMouse       | Constructs a USBHIDMouse object     |
+--------------------------------+-------------------------------------+

**Public Methods**

+------------------------------------+---------------------------------+
| USBHIDMouse::setReportID           | Set HID report ID for the HID   |
|                                    | Mouse                           |
+------------------------------------+---------------------------------+
| USBHIDMouse::mouseReport           | Send a HID Mouse report         |
+------------------------------------+---------------------------------+
| USBHIDMouse::mousePress            | Send a HID Mouse report         |
|                                    | indicating buttons pressed      |
+------------------------------------+---------------------------------+
| USBHIDMouse::mouseRelease          | Send a HID Mouse report         |
|                                    | indicating buttons released     |
+------------------------------------+---------------------------------+
| USBHIDMouse::mouseReleaseAll       | Send a HID Mouse report         |
|                                    | indicating no buttons pressed   |
+------------------------------------+---------------------------------+
| USBHIDMouse::mouseMove             | Send a HID Mouse report         |
|                                    | indicating mouse movement       |
+------------------------------------+---------------------------------+
| USBHIDMouse::mouseScroll           | Send a HID Mouse report         |
|                                    | indicating mouse scroll wheel   |
|                                    | movement                        |
+------------------------------------+---------------------------------+

-------------------------------

**USBHIDMouse::USBHIDMouse**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a USBHIDMouse object.

**Syntax**
~~~~~~~~~~

.. code:: c++

    USBHIDMouse(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDMouse <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDMouse/USBHIDMouse.ino>`_

.. note :: “USBHIDMouse.h” must be included to use the class function.

--------------------------

**USBHIDMouse::setReportID**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set HID report ID for the HID Mouse.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setReportID(uint8_t reportID);

**Parameters**
~~~~~~~~~~~~~~

``reportID``: The report ID for the HID mouse device, corresponding to the HID report descriptor.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBHIDMouse.h” must be included to use the class function.

-----------------------------

**USBHIDMouse::mouseReport**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Mouse report.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void mouseReport (hid_mouse_report_t* report);

.. code:: c++

    void mouseReport (uint8_t buttons, int8_t x, int8_t y, int8_t scroll);

**Parameters**
~~~~~~~~~~~~~~

``report``: pointer to mouse report structure containing data on mouse inputs

``buttons``: bitmap indicating state of each button. 1 = pressed, 0 = released.

``x``: mouse x-axis movement. Integer value from -127 to 127.

``y``: mouse y-axis movement. Integer value from -127 to 127.

``scroll``: mouse scroll wheel movement. Integer value from -127 to 127.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBHIDMouse.h” must be included to use the class function.

---------------------------

**USBHIDMouse::mousePress**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Mouse report indicating buttons pressed.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void mousePress(uint8_t buttons);

**Parameters**
~~~~~~~~~~~~~~

``buttons``: bitmap indicating buttons pressed. 1 = pressed.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDMouse <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDMouse/USBHIDMouse.ino>`_

.. note :: “USBHIDMouse.h” must be included to use the class function.

---------------------------

**USBHIDMouse::mouseRelease**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Mouse report indicating buttons released.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void mouseRelease(uint8_t buttons);

**Parameters**
~~~~~~~~~~~~~~

``buttons``: bitmap indicating buttons released. 1 = released.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDMouse <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDMouse/USBHIDMouse.ino>`_

.. note :: “USBHIDMouse.h” must be included to use the class function.

------------------------------

**USBHIDMouse::mouseReleaseAll**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Mouse report indicating no buttons pressed.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void mouseReleaseAll(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBHIDMouse.h” must be included to use the class function.

-----------------------------

**USBHIDMouse::mouseMove**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Mouse report indicating mouse movement.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void mouseMove (int8_t x, int8_t y);

**Parameters**
~~~~~~~~~~~~~~

``x``: mouse x-axis movement. Integer value from -127 to 127.

``y``: mouse y-axis movement. Integer value from -127 to 127.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDMouse <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDMouse/USBHIDMouse.ino>`_

.. note :: “USBHIDMouse.h” must be included to use the class function.

----------------------------

**USBHIDMouse::mouseScroll**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID Mouse report indicating mouse scroll wheel movement.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void mouseScroll(int8_t scroll);

**Parameters**
~~~~~~~~~~~~~~

``scroll``: mouse scroll wheel movement. Integer value from -127 to 127.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDMouse <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDMouse/USBHIDMouse.ino>`_

.. note :: “USBHIDMouse.h” must be included to use the class function.
