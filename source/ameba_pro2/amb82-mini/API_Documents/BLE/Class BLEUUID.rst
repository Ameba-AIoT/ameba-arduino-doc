Class BLEUUID
=============

**BLEUUID Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

A class used for creating and managing UUIDs.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLEUUID

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| BLEUUID::BLEUUID                   | Create a BLEUUID object         |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| BLEUUID::str                       | Get the character string        |
|                                    | representation of UUID          |
+------------------------------------+---------------------------------+
| BLEUUID::data                      | Get the binary representation of|
|                                    | UUID, with the UUID MSB in array|
|                                    | index [0]                       |
+------------------------------------+---------------------------------+
| BLEUUID::dataNative                | Get the binary representation of|
|                                    | UUID, with the UUID LSB in array|
|                                    | index [0]                       |
+------------------------------------+---------------------------------+
| BLEUUID::length                    | Get the length of UUID          |
+------------------------------------+---------------------------------+

**BLEUUID::BLEUUID**
--------------------

**Description**
~~~~~~~~~~~~~~~

Create a BLEUUID object from a UUID character string.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    BLEUUID(void);
    BLEUUID(const char* str);
    BLEUUID(uint8_t* data, uint8_t length);

**Parameters**
~~~~~~~~~~~~~~

str: UUID as character string used to create object

data: pointer to byte array containing the desired UUID

length: number of bytes in array containing the desired UUID.

- 2, 4 or 16.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLEUUID.h" must be included to use the class function.

**BLEUUID::str**
----------------

**Description**
~~~~~~~~~~~~~~~

Get the character string representation of UUID.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    const char* str(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to the UUID represented as a character string.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLEUUID.h" must be included to use the class function.

**BLEUUID::data**
-----------------

**Description**
~~~~~~~~~~~~~~~

Get the binary representation of UUID, with the UUID MSB in array index[0].

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    const uint8_t* data(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to an unsigned 8-bit integer array containing the UUID expressed in binary form.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Returned pointer is of const uint8_t* type and will not allow changing of the data. "BLEUUID.h" must be included to use the class function.

**BLEUUID::dataNative**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Get the binary representation of UUID, with the UUID LSB in array index [0].

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    const uint8_t* dataNative(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to an unsigned 8-bit integer array containing the UUID expressed in binary form.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Returned pointer is of const uint8_t* type and will not allow changing of the data. "BLEUUID.h" must be included to use the class function.

**BLEUUID::length**
-------------------

**Description**
~~~~~~~~~~~~~~~

Get the length of UUID.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t length(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the length of the UUID, in units of bytes.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: A 4-character UUID will be 16 bits / 2 bytes long. A 8-character UUID will be 32 bits / 4 bytes long. A 32-character UUID will be 128 bits / 16 bytes long. "BLEUUID.h" must be included to use the class function.
