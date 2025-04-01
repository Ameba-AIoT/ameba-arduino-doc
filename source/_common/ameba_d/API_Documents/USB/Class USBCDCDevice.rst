Class USBCDCDevice
==================

.. contents::
  :local:
  :depth: 2

**USBCDCDevice Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class for managing, transmitting, and receiving data using USB CDC ACM
device class.

**Syntax**
~~~~~~~~~~

.. code:: c++

    class USBCDCDevice

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| The public constructor should not be used as this class is intended  |
| to be a singleton class. Access member functions using the object    |
| instance named ``SerialUSB``.                                        |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| USBCDCDevice::setVID               | Set USB vendor ID value         |
+------------------------------------+---------------------------------+
| USBCDCDevice::setPID               | Set USB product ID value        |
+------------------------------------+---------------------------------+
| U                                  | Set USB manufacturer string     |
| SBCDCDevice::setManufacturerString |                                 |
+------------------------------------+---------------------------------+
| USBCDCDevice::setModelString       | Set USB product model string    |
+------------------------------------+---------------------------------+
| USBCDCDevice::setSerialString      | Set USB product serial number   |
|                                    | string                          |
+------------------------------------+---------------------------------+
| USBCDCDevice::USBconnected         | Check if the USB port is        |
|                                    | connected to a host             |
+------------------------------------+---------------------------------+
| USBCDCDevice::connected            | Check if the USB CDC serial     |
|                                    | terminal is ready on the host   |
+------------------------------------+---------------------------------+
| USBCDCDevice::dtr                  | Check DTR signal state          |
+------------------------------------+---------------------------------+
| USBCDCDevice::rts                  | Check RTS signal state          |
+------------------------------------+---------------------------------+
| USBCDCDevice::begin                | Start serial communication      |
|                                    | using USB CDC                   |
+------------------------------------+---------------------------------+
| USBCDCDevice::end                  | Stop serial communication using |
|                                    | USB CDC                         |
+------------------------------------+---------------------------------+
| USBCDCDevice::available            | Get the number of bytes         |
|                                    | (characters) available for      |
|                                    | reading from the USB serial     |
|                                    | port                            |
+------------------------------------+---------------------------------+
| USBCDCDevice::peek                 | Returns the next byte           |
|                                    | (character) of incoming serial  |
|                                    | data without removing it from   |
|                                    | the internal buffer             |
+------------------------------------+---------------------------------+
| USBCDCDevice::read                 | Reads incoming serial data      |
+------------------------------------+---------------------------------+
| USBCDCDevice::flush                | Waits for the transmission of   |
|                                    | outgoing serial data to         |
|                                    | complete                        |
+------------------------------------+---------------------------------+
| USBCDCDevice::write                | Writes binary data to the       |
|                                    | serial port                     |
+------------------------------------+---------------------------------+

-----------------------------

**USBCDCDevice::setVID**
------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB vendor ID value.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setVID (uint16_t VID);

**Parameters**
~~~~~~~~~~~~~~

``VID``: vendor ID

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The VID should be configured before USBCDCDevice::begin() function is called.

.. note :: “USBCDCDevice.h” must be included to use the class function.

-------------------------

**USBCDCDevice::setPID**
------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB product ID value.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setPID (uint16_t PID);

**Parameters**
~~~~~~~~~~~~~~

``PID``: product ID

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The PID should be configured before USBCDCDevice::begin() function is called. 

.. note :: “USBCDCDevice.h” must be included to use the class function.

---------------------------------------

**USBCDCDevice::setManufacturerString**
---------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB manufacturer string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setManufacturerString (const char* manufacturer);

**Parameters**
~~~~~~~~~~~~~~

``manufacturer``: Character string containing manufacturer name

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The manufacturer string should be configured before USBCDCDevice::begin() function is called. 

.. note :: “USBCDCDevice.h” must be included to use the class function.

-----------------------------

**USBCDCDevice::setModelString**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB product model string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setModelString (const char* model);

**Parameters**
~~~~~~~~~~~~~~

``model``: Character string containing model name. Default “Realtek USB VCP”.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The model string should be configured before USBCDCDevice::begin() function is called. 

.. note :: “USBCDCDevice.h” must be included to use the class function.

---------------------------------------------

**USBCDCDevice::setSerialString**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Set USB product serial number string.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setSerialString (const char* serial);

**Parameters**
~~~~~~~~~~~~~~

``serial``: Character string containing serial number. Default “0123456789”.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The serial string should be configured before USBCDCDevice::begin() function is called. 

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------------

**USBCDCDevice::USBconnected**
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

The function returns TRUE if the USB port is connected to a host, FALSE if it is not connected.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------------

**USBCDCDevice::connected**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Check if the USB CDC serial terminal is ready on the host.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint8_t connected(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns TRUE if the USB port is connected to a host and the DTR and RTS signals are set, else returns FALSE.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------

USBCDCDevice::dtr

**Description**
~~~~~~~~~~~~~~~

Check DTR signal state.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint8_t dtr(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the state of the DTR signal line.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------

**USBCDCDevice::rts**
---------------------

**Description**
~~~~~~~~~~~~~~~

Check RTS signal state.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint8_t rts(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the state of the RTS signal line.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------

**USBCDCDevice::begin**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Start serial communication using USB CDC.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void begin(uint32_t baud);

**Parameters**
~~~~~~~~~~~~~~

``baud``: baud rate

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBCDCSerial <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBCDCSerial/USBCDCSerial.ino>`_

.. important :: The baud rate parameter has no significance in the context of a USB CDC serial port and can be left empty. 

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------

**USBCDCDevice::end**
---------------------

**Description**
~~~~~~~~~~~~~~~

Stop serial communication using USB CDC.

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

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------

**USBCDCDevice::available**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get the number of bytes (characters) available for reading from the USB serial port.

**Syntax**
~~~~~~~~~~

.. code:: c++

    int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the number of bytes received in the buffer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBCDCSerial <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBCDCSerial/USBCDCSerial.ino>`_

.. note :: “USBCDCDevice.h” must be included to use the class function.

------------------------

**USBCDCDevice::peek**
----------------------

**Description**
~~~~~~~~~~~~~~~

Get the next byte (character) of incoming serial data without removing it from the internal buffer.

**Syntax**
~~~~~~~~~~

.. code:: c++

    int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next byte of received serial data without removing it from the internal buffer else returns error(-1).

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBCDCDevice.h” must be included to use the class function.

-----------------------

**USBCDCDevice::read**
----------------------

**Description**
~~~~~~~~~~~~~~~

Reads incoming serial data.

**Syntax**
~~~~~~~~~~

.. code:: c++

    int read(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next byte of received serial data, else returns error(-1).

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBCDCSerial <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBCDCSerial/USBCDCSerial.ino>`_

.. note :: “USBCDCDevice.h” must be included to use the class function.

-----------------------

**USBCDCDevice::flush**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Waits for the transmission of outgoing serial data to complete.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void flush(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “USBCDCDevice.h” must be included to use the class function.

---------------------------

**USBCDCDevice::write**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Writes binary data to the serial port.

**Syntax**
~~~~~~~~~~

.. code:: c++

    size_t write(uint8_t data);

.. code:: c++

    size_t write(const uint8_t* buffer, size_t size);

**Parameters**
~~~~~~~~~~~~~~

``data``: 1 byte of data to write to serial port

``buffer``: pointer to buffer containing data to write to serial port

``size``: number of bytes of data in buffer to write to serial port

**Returns**
~~~~~~~~~~~

This function returns the number of bytes written to serial port.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USBCDCSerial <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/USBCDCSerial/USBCDCSerial.ino>`_

.. note :: “USBCDCDevice.h” must be included to use the class function.
    