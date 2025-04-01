Class USBHIDDevice
==================

.. contents::
  :local:
  :depth: 2

**USBHIDDevice Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class used for creating and managing USB HID device class

**Syntax**
~~~~~~~~~~

.. code:: c++

    class USBHIDDevice

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| The public constructor should not be used as this class is intended  |
| to be a singleton class. Access member functions using the object    |
| instance named ``USBHIDDev``.                                        |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| USBHIDDevice::setReportDescriptor  | Configure the HID report        |
|                                    | descriptor                      |
+------------------------------------+---------------------------------+
| USBHIDDevice::setUSBEndpointMPS    | Configure USB endpoint maximum  |
|                                    | packet size                     |
+------------------------------------+---------------------------------+
| US                                 | Configure USB endpoint polling  |
| BHIDDevice::setUSBEndpointInterval | interval                        |
+------------------------------------+---------------------------------+
| USBHIDDevice::setVID               | Set USB vendor ID value         |
+------------------------------------+---------------------------------+
| USBHIDDevice::setPID               | Set USB product ID value        |
+------------------------------------+---------------------------------+
| U                                  | Set USB manufacturer string     |
| SBHIDDevice::setManufacturerString |                                 |
+------------------------------------+---------------------------------+
| USBHIDDevice::setModelString       | Set USB product model string    |
+------------------------------------+---------------------------------+
| USBHIDDevice::setSerialString      | Set USB product serial number   |
|                                    | string                          |
+------------------------------------+---------------------------------+
| USBHIDDevice::USBconnected         | Check if the USB port is        |
|                                    | connected to a host             |
+------------------------------------+---------------------------------+
| USBHIDDevice::begin                | Start USB HID device            |
+------------------------------------+---------------------------------+
| USBHIDDevice::end                  | Stop USB HID device             |
+------------------------------------+---------------------------------+
| USBHIDDevice::inputReport          | Send a HID input report         |
+------------------------------------+---------------------------------+

-------------------------------

**USBHIDDevice::setReportDescriptor**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure the HID report descriptor.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setReportDescriptor(uint8_t* report_desc, uint16_t len);

**Parameters**
~~~~~~~~~~~~~~

``report_desc``: pointer to buffer containing HID report descriptor

``len``: HID report descriptor length in number of bytes

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDGamepad <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDGamepad/USBHIDGamepad.ino>`_ 

.. important :: Default HID report descriptor is configured for mouse + keyboard + consumer control.

.. note :: “USBHIDDevice.h” must be included to use the class function.

-------------------------------

**USBHIDDevice::setUSBEndpointMPS**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure USB endpoint maximum packet size.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setUSBEndpointMPS(uint8_t max_packet_size);

**Parameters**
~~~~~~~~~~~~~~

``max_packet_size``: maximum HID report packet size in bytes

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDGamepad <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDGamepad/USBHIDGamepad.ino>`_

.. important :: The USB endpoint maximum packet size should correspond to the size of the largest HID report defined in the HID report descriptor.

.. note :: “USBHIDDevice.h” must be included to use the class function.

------------------------------------

**USBHIDDevice::setUSBEndpointInterval**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure USB endpoint polling interval.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setUSBEndpointInterval(uint8_t poll_interval);

**Parameters**
~~~~~~~~~~~~~~

``poll_interval``: polling interval for USB interrupt endpoint, expressed in milliseconds

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: Default polling interval is set at the minimum of 1 millisecond.

.. note :: “USBHIDDevice.h” must be included to use the class function.

--------------------------

**USBHIDDevice::setVID**
------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB vendor ID value.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setVID(uint16_t VID);

**Parameters**
~~~~~~~~~~~~~~

``VID``: vendor ID

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The VID should be configured before USBHIDDevice::begin() function is called.

.. note :: “USBHIDDevice.h” must be included to use the class function.

------------------------

**USBHIDDevice::setPID**
------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB product ID value.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setPID(uint16_t PID);

**Parameters**
~~~~~~~~~~~~~~

``PID``: product ID

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The PID should be configured before USBHIDDevice::begin() function is called. 

.. note :: “USBHIDDevice.h” must be included to use the class function.

----------------------------------------

**USBHIDDevice::setManufacturerString**
---------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB manufacturer string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setManufacturerString(const char* manufacturer);

**Parameters**
~~~~~~~~~~~~~~

``manufacturer``: Character string containing manufacturer name. Default “Realtek”.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The manufacturer string should be configured before USBHIDDevice::begin() function is called

.. note :: “USBHIDDevice.h” must be included to use the class function.

-----------------------------------

**USBHIDDevice::setModelString**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB product model string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setModelString(const char* model);

**Parameters**
~~~~~~~~~~~~~~

``model``: Character string containing model name. Default “Realtek USB HID”.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The model string should be configured before USBHIDDevice::begin() function is called. 

.. note :: “USBHIDDevice.h” must be included to use the class function.

----------------------------------

**USBHIDDevice::setSerialString**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB product serial number string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setSerialString(const char* serial);

**Parameters**
~~~~~~~~~~~~~~

``serial``: Character string containing serial number. Default “0123456789”.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The serial string should be configured before USBHIDDevice::begin() function is called. 

.. note :: “USBHIDDevice.h” must be included to use the class function.

----------------------------

**USBHIDDevice::USBconnected**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Check if the USB port is connected to a host.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint8_t USBconnected(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns TRUE as 1 if the USB port is connected to a host, FALSE as 0 if it is not connected.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBHIDGamepad <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDGamepad/USBHIDGamepad.ino>`_

.. note :: “USBHIDDevice.h” must be included to use the class function.

------------------------

**USBHIDDevice::begin**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Start USB HID device.

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

Example: `USBHIDGamepad <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBHIDGamepad/USBHIDGamepad.ino>`_

.. note :: “USBHIDDevice.h” must be included to use the class function.

---------------------

**USBHIDDevice::end**
---------------------

**Description**
~~~~~~~~~~~~~~~

Stop USB HID device.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void end(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBHIDDevice.h” must be included to use the class function.

-------------------------------

**USBHIDDevice::inputReport**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Send a HID input report.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void inputReport(uint8_t reportID, uint8_t* data, uint16_t len);

**Parameters**
~~~~~~~~~~~~~~

``reportID``: HID report ID of input report

``data``: pointer to HID input report data to send

``len``  length of HID input report data in bytes

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: A reportID value of 0 is not a valid report ID and will send an input report without the report ID field. 

.. note :: “USBHIDDevice.h” must be included to use the class function.
