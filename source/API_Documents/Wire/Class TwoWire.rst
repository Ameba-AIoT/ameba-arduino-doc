Class TwoWire
=============

.. contents::
  :local:
  :depth: 2

**TwoWire Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

A class of I2C API.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class TwoWire

**Members**
~~~~~~~~~~~

+----------------------------+----------------------------------------+
| **Public Constructors**                                             |
+============================+========================================+
| TwoWire::TwoWire           | Constructs a TwoWire object            |
+----------------------------+----------------------------------------+
| **Public Methods**                                                  |
+----------------------------+----------------------------------------+
| TwoWire::begin             | Initialize I2C master/slave            |
+----------------------------+----------------------------------------+
| TwoWire::end               | Deinitialize I2C master/slave          |
+----------------------------+----------------------------------------+
| TwoWire::setClock          | Set I2C clock frequency                |
+----------------------------+----------------------------------------+
| TwoWire::beginTransmission | Begin I2C transmission                 |
+----------------------------+----------------------------------------+
| TwoWire::endTransmission   | Stop I2C transmission                  |
+----------------------------+----------------------------------------+
| TwoWire::requestFrom       | Set I2C requestFrom                    |
+----------------------------+----------------------------------------+
| TwoWire::write             | Write data to I2C                      |
+----------------------------+----------------------------------------+
| TwoWire::available         | Check if I2C is available              |
+----------------------------+----------------------------------------+
| TwoWire::read              | Read data from I2C                     |
+----------------------------+----------------------------------------+
| TwoWire::peek              | Read peek from I2C                     |
+----------------------------+----------------------------------------+
| TwoWire::flush             | Do nothing, use, and transmission(..)  |
|                            | to force data transfer                 |
+----------------------------+----------------------------------------+
| TwoWire::onReceive         | Callback function when I2C on receive  |
+----------------------------+----------------------------------------+
| TwoWire::onRequest         | Callback function when I2C on request  |
+----------------------------+----------------------------------------+
| TwoWire::slaveWrite        | Send data as a slave device            |
+----------------------------+----------------------------------------+

**TwoWire::TwoWire**
--------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a TwoWire object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    TwoWire(void *pWireObj, uint32_t dwSDAPin, uint32_t dwSCLPin);

**Parameters**
~~~~~~~~~~~~~~

pWireObj: Pointer to the Wire object.

dwSDAPin: Pin name (from pinmap) to be set as SDA pin.

dwSCLPin: Pin name (from pinmap) to be set as SCL pin.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::begin**
------------------

**Description**
~~~~~~~~~~~~~~~

Initialize I2C master/slave. To use in I2C master, no argument should be passed in, otherwise I2C will be in slave mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin (void);
    void begin (uint8_t address = 0);
    void begin (int address);

**Parameters**
~~~~~~~~~~~~~~

address: Set the I2C slave address value.

- 0 - 127

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function. When configured as I2C slave, begin() will also configure and enable I2C interrupt and attach user callback to be used in the I2C interrupt service routine.

**TwoWire::end**
----------------

**Description**
~~~~~~~~~~~~~~~

This function is used to de-initialise the I2C device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void end (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::setClock**
---------------------

**Description**
~~~~~~~~~~~~~~~

Set I2C clock frequency.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setClock(uint32_t frequency);

**Parameters**
~~~~~~~~~~~~~~

frequency: Set user defined I2C clock frequency (Hz). Default value is 100000.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::beginTransmission**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Begin I2C transmission to device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void beginTransmission (uint8_t address);
    void beginTransmission (int address);

**Parameters**
~~~~~~~~~~~~~~

address: The transmission address.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::endTransmission**
----------------------------

**Description**
~~~~~~~~~~~~~~~

This function ends a transmission to a peripheral device that was begun by beginTransmission() and transmits the bytes that were queued by write().

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t endTransmission (uint8_t sendStop);
    uint8_t endTransmission (void);

**Parameters**
~~~~~~~~~~~~~~

sendStop: Set to True to end transmission after data is transferred from master to slave, and releasing the I2C bus. Set to False will send a restart keeping the connection active.

- true  (Default value)

- false

**Returns**
~~~~~~~~~~~

This function returns 0 if successful, else returns 1 indicating error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: Originally, ‘endTransmission’ was an f(void) function. It has been modified to take one parameter indicating whether a STOP should be performed on the bus. Calling endTransmission(false) allows a sketch to perform a repeated start. If the input parameter is void, this provides backward compatibility with the original definition, and expected behavior, of endTransmission. “Wire.h” must be included to use the class function.

.. warning:: Nothing in the library keeps track of whether the bus tenure has been properly ended with a STOP. It is very possible to leave the bus in a hung state if no call to endTransmission(true) is made. Some I2C devices will behave oddly if they do not see a STOP.

**TwoWire::requestFrom**
------------------------

**Description**
~~~~~~~~~~~~~~~

I2C master request data sending from I2C slave device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t requestFrom (uint8_t address, uint8_t quantity, uint8_t sendStop);
    uint8_t requestFrom (uint8_t address, uint8_t quantity);
    uint8_t requestFrom(int address, int quantity);
    uint8_t requestFrom (int address, int quantity, int sendStop);

**Parameters**
~~~~~~~~~~~~~~

address: The I2C slave address of the device to request bytes from.

quantity: The number of data (in byte) that to be received from I2C slave device.

sendStop: Set to True to end transmission after data is transferred from master to slave, and releasing the I2C bus. Set to False will send a restart keeping the connection active.

- true  (Default value)

- false

**Returns**
~~~~~~~~~~~

This function returns the length of data received as an int if successful, else returns error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterReader <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterReader/MasterReader.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::write**
------------------

**Description**
~~~~~~~~~~~~~~~

Write data to I2C master transmission buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    size_t write (uint8_t data);
    size_t write (const uint8_t *data, size_t quantity);

**Parameters**
~~~~~~~~~~~~~~

data: The data in 8-bit is to be transmitted from I2C master to slave.

quantity: The number of data in 8-bit to be transmitted.

**Returns**
~~~~~~~~~~~

.. code-block:: c++

    size_t write (uint8_t data);

Returns 1 if successful, else returns 0.

.. code-block:: c++

    size_t write (const uint8_t *data, size_t quantity);

Returns the number of bytes to be transmitted. (Reading this number is optional)

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterWriter/MasterWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::available**
----------------------

**Description**
~~~~~~~~~~~~~~~

This function returns the number of bytes available for retrieval with read().

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the number of bytes available for reading.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterReader <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterReader/MasterReader.ino>`_

.. note :: This function should be called on a controller device after a call to requestFrom() or on a peripheral inside the onReceive() handler. available() inherits from the Stream utility class. “Wire.h” must be included to use the class function.

**TwoWire::read**
-----------------

**Description**
~~~~~~~~~~~~~~~

This function reads a byte that was transmitted from a peripheral device to a controller device after a call to requestFrom() or was transmitted from a controller device to a peripheral device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int read(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next data in byte read from receiver buffer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterReader <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterReader/MasterReader.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::peek**
-----------------

**Description**
~~~~~~~~~~~~~~~

This function reads a byte that currently transmitted from a peripheral device to a controller device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current data read from receiver buffer. Otherwise, “-1”.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MasterReader <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/MasterReader/MasterReader.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::flush**
------------------

**Description**
~~~~~~~~~~~~~~~

An empty API that does nothing, use endTransmission() to force data transfer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual void flush(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::onReceive**
----------------------

**Description**
~~~~~~~~~~~~~~~

This function registers a function to be called when a peripheral device receives a transmission from a controller device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void TwoWire::onReceive (void(*function)(int));

**Parameters**
~~~~~~~~~~~~~~

function: The callback function to be called when the peripheral device receives data; this should take a single int parameter (the number of bytes read from the controller device) and return nothing.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SlaveReader <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/SlaveReader/SlaveReader.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::onRequest**
----------------------

**Description**
~~~~~~~~~~~~~~~

This function registers a function to be called when a controller device requests data from a peripheral device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void onRequest (void(*function)(void));

**Parameters**
~~~~~~~~~~~~~~

function: the function to be called, takes no parameters and returns nothing.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SlaveWriter <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Wire/examples/SlaveWriter/SlaveWriter.ino>`_

.. note :: “Wire.h” must be included to use the class function.

**TwoWire::slaveWrite**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Send data as a slave device, note that this API only work when device is configured as I2C slave (see begin()).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    size_t slaveWrite(int buffer);
    size_t slaveWrite(char *buffer);
    size_t slaveWrite(uint8_t *buffer, size_t len);

**Parameters**
~~~~~~~~~~~~~~

buffer: Data container that can be an integer or a character pointer.

Len: The length of the data buffer.

**Returns**
~~~~~~~~~~~

This function returns true if successful, else returns false.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Wire.h” must be included to use the class function. This function can only be called if the device is in slave mode and after user has registered a requestEvent using onRequest().
