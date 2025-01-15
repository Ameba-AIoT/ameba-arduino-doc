Class BLERemoteDescriptor
=========================

.. contents::
  :local:
  :depth: 2

**BLERemoteDescriptor Class**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing BLE GATT descriptors on connected remote devices.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLERemoteDescriptor

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| No public constructor is available for this class. You can get a     |
| pointer to an instance of this class using                           |
| BLERemoteCharacteristic::getDescriptor()                             |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::getUUID       | Get the descriptor UUID         |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::setBufferLen  | Set the size of the internal    |
|                                    | data buffer                     |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::getBufferLen  | Get the current size of the     |
|                                    | internal data  buffer           |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::readString    | Read the descriptor data buffer |
|                                    | as a String object              |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::readData8     | Read the descriptor data buffer |
|                                    | as an unsigned 8-bit integer    |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::readData16    | Read the descriptor data buffer |
|                                    | as an unsigned 16-bit integer   |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::readData32    | Read the descriptor data buffer |
|                                    | as an unsigned 32-bit integer   |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::writeString   | Write data to the descriptor as |
|                                    | a String object or character    |
|                                    | array                           |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::writeData8    | Write data to the descriptor    |
|                                    | as an unsigned 8-bit integer    |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::writeData16   | Write data to the descriptor    |
|                                    | as an unsigned 16-bit integer   |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::writeData32   | Write data to the descriptor    |
|                                    | as an unsigned 32-bit integer   |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::setData       | Write data to the descriptor    |
+------------------------------------+---------------------------------+
| BLERemoteDescriptor::getData       | Get data from the descriptor    |
+------------------------------------+---------------------------------+

**BLERemoteDescriptor::getUUID**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the descriptor UUID.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    BLEUUID getUUID(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the descriptor UUID as a BLEUUID class object.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::setBufferLen**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the size of the internal data buffer of the descriptor.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBufferLen(uint16_t max_len);

**Parameters**
~~~~~~~~~~~~~~

max_len: the size in bytes to resize the internal buffer to.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Descriptor data buffer has a default size of 20 bytes and can be increased up to 230 bytes. "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::getBufferLen**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current size of the descriptor internal buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t getBufferLen(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current internal buffer size that is set.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::readString**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Request for descriptor data from the remote device and read the data in the buffer, expressed as a String class object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    String readString(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the data in the descriptor buffer expressed as a String class object.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::readData8**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Request for descriptor data from the remote device and read the data in the buffer, expressed as an unsigned 8-bit integer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t readData8(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the data in the descriptor buffer expressed as a uint8_t value.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::readData16**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Request for descriptor data from the remote device and read the data in the buffer, expressed as an unsigned 16-bit integer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t readData16(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the data in the descriptor buffer expressed as a uint16_t value.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::readData32**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Request for descriptor data from the remote device and read the data in the buffer, expressed as an unsigned 32-bit integer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t readData32(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the data in the descriptor buffer expressed as a uint32_t value.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::writeString**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Write data to the remote device descriptor as a String object or character array.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool writeString(String str);
    bool writeString(const char* str);

**Parameters**
~~~~~~~~~~~~~~

str: the data to write to the remote descriptor, expressed as a String class object or a char array.

**Returns**
~~~~~~~~~~~

This function returns TRUE if writing data to remote device descriptor is successful.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::writeData8**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Write data to the remote device descriptor as an unsigned 8-bit integer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool writeData8(uint8_t num);

**Parameters**
~~~~~~~~~~~~~~

num: the data to write to the descriptor buffer expressed as an unsigned 8-bit integer.

**Returns**
~~~~~~~~~~~

This function returns TRUE if writing data to remote device descriptor is successful.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::writeData16**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Write data to the remote device descriptor as an unsigned 16-bit integer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool writeData16(uint16_t num);

**Parameters**
~~~~~~~~~~~~~~

num: the data to write to the descriptor buffer expressed as an unsigned 16-bit integer.

**Returns**
~~~~~~~~~~~

This function returns TRUE if writing data to remote device descriptor is successful.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::writeData32**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Write data to the remote device descriptor as a 32-bit integer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool writeData32(uint32_t num);
    bool writeData32(int num);

**Parameters**
~~~~~~~~~~~~~~

num: the data to write to the descriptor buffer expressed as a 32-bit integer.

**Returns**
~~~~~~~~~~~

This function returns TRUE if writing data to remote device descriptor is successful.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::setData**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Write data to the descriptor.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool setData(uint8_t* data, uint16_t datalen);

**Parameters**
~~~~~~~~~~~~~~

data: pointer to byte array containing desired data to write.

datalen: number of bytes of data to write.

**Returns**
~~~~~~~~~~~

This function returns TRUE if writing data to remote device descriptor is successful.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLERemoteDescriptor.h" must be included to use the class function.

**BLERemoteDescriptor::getData**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the descriptor data from the remote device and read the data in the buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t getData(uint8_t* data, uint16_t datalen);

**Parameters**
~~~~~~~~~~~~~~

data: pointer to byte array to save data read from buffer.

datalen: number of bytes of data to read.

**Returns**
~~~~~~~~~~~

The function returns the number of bytes read.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: If the data buffer contains less data than requested, it will only read the available number of bytes of data. "BLERemoteDescriptor.h" must be included to use the class function.
