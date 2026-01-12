Class BLEAddr
=============

**BLEAddr Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing Bluetooth addresses.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLEAddr

**Members**
~~~~~~~~~~~

+------------------------------+--------------------------------------+
| **Public Constructors**                                             |
+==============================+======================================+
| BLEAddr::BLEAddr             | Constructs a BLEAddr object          |
+------------------------------+--------------------------------------+
| **Public Methods**                                                  |
+------------------------------+--------------------------------------+
| BLEAddr::str                 | Get the Bluetooth address            |
|                              | represented as a formatted string    |
+------------------------------+--------------------------------------+
| BLEAddr::data                | Get the Bluetooth address            |
|                              | represented as an integer array      |
+------------------------------+--------------------------------------+

**BLEAddr::BLEAddr**
--------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a BLEAddr object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    BLEAddr(void);
    BLEAddr(uint8_t (&addr)[6]);
    BLEAddr(const char * str);

**Parameters**
~~~~~~~~~~~~~~

addr: An array of 6 bytes containing the desired Bluetooth address.

str: desired Bluetooth address represented in character string.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: When expressing the Bluetooth address as a string, it should be written as 6 bytes in hexadecimal format. The bytes can be separated using a colon ":", for example – 00:11:22:33:EE:FF. "BLEAddr.h" must be included to use the class function.

**BLEAddr::str**
----------------

**Description**
~~~~~~~~~~~~~~~

Get the Bluetooth address represented as a formatted string.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    const char* str(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to the character string containing the hexadecimal representation of the Bluetooth address.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_

.. note :: When expressing the Bluetooth address as a string, it should be written as 6 bytes in hexadecimal format. The bytes can be separated using a colon ":", for example – 00:11:22:33:EE:FF. "BLEAddr.h" must be included to use the class function.

**BLEAddr::data**
-----------------

**Description**
~~~~~~~~~~~~~~~

Get the Bluetooth address represented as an integer array.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t* data(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to a 6-byte array containing the Bluetooth address.

**Example Code**

NA

.. note :: The MSB of Bluetooth address is stored at index 5 of the byte array. "BLEAddr.h" must be included to use the class function.
