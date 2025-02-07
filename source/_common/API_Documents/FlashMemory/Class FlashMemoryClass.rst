Class FlashMemory
=================

.. contents::
  :local:
  :depth: 2

**FlashMemoryClass Class**
--------------------------

**Description**
~~~~~~~~~~~~~~~

A class for Flash memory API.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class FlashMemoryClass

**Members**
~~~~~~~~~~~

+------------------------------------+----------------------------------+
| **Public Constructors**                                               |
+====================================+==================================+
| FlashMemoryClass::FlashMemoryClass | Constructs a FlashMemoryClass    |
|                                    | object                           |
+------------------------------------+----------------------------------+
| **Public Methods**                                                    |
+------------------------------------+----------------------------------+
| FlashMemoryClass::begin            | Initialize/Re-initialize the     |
|                                    | base address and size            |
+------------------------------------+----------------------------------+
| FlashMemoryClass::read             | Read content from flash memory   |
|                                    | to buffer                        |
+------------------------------------+----------------------------------+
| FlashMemoryClass::update           | Write the content in the buffer  |
|                                    | back to the flash memory         |
+------------------------------------+----------------------------------+
| FlashMemoryClass::readWord         | Read 4 bytes from flash          |
|                                    | memory based on the new base     |
|                                    | address with specific offset.    |
+------------------------------------+----------------------------------+
| FlashMemoryClass::writeWord        | Write word to flash memory       |
+------------------------------------+----------------------------------+

**FlashMemoryClass::FlashMemoryClass**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a FlashMemoryClass object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    FlashMemoryClass(unsigned int _base_address, unsigned int _buf_size);

**Parameters**
~~~~~~~~~~~~~~

``_base_address``: The starting location/position of the flash memory area
``_buf_size``: The buf size for mirroring a copy to reduce flash memory operation

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FleshMemory_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/FlashMemory_Basic/FlashMemory_Basic.ino>`_

.. note :: "FlashMemory.h" must be included to use the class function.

**FlashMemoryClass::begin**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize/Re-initialize the base address and size. The default usable flash memory size is 0x1000.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(unsigned int _base_address, unsigned int _buf_size);

**Parameters**
~~~~~~~~~~~~~~

``_base_address``: The starting location/position of the flash memory area
``_buf_size``: The desired buffer size

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FleshMemory_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/FlashMemory_Basic/FlashMemory_Basic.ino>`_

.. note :: "FlashMemory.h" must be included to use the class function.

**FlashMemoryClass::read**
--------------------------

**Description**
~~~~~~~~~~~~~~~

When read() is called, contents will be read from the flash memory and copy into a buffer. All modification of the contents will be done in the buffer before updating the flash memory. The default length of the data to read is 0x1000 (flash sector size).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void read(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FleshMemory_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/FlashMemory_Basic/FlashMemory_Basic.ino>`_

.. note :: "FlashMemory.h" must be included to use the class function.

**FlashMemoryClass::update**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Write the content of the buffer into the flash memory. The default length of the data is 0x1000 (flash sector size).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void update(bool erase = true);

**Parameters**
~~~~~~~~~~~~~~

erase: It is set to true by default and erases flash memory before writing.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FleshMemory_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/FlashMemory_Basic/FlashMemory_Basic.ino>`_

.. note :: "FlashMemory.h" must be included to use the class function.

**FlashMemoryClass::readWord**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Read 4 bytes data (a word) from a flash address, based on the new base address with specific offset.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    unsigned int readWord(unsigned int offset);

**Parameters**
~~~~~~~~~~~~~~

``offset``: offset to the base address.

**Returns**
~~~~~~~~~~~

This function returns the 4 bytes read data.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteOneWord <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteOneWord/ReadWriteOneWord.ino>`_

.. note :: "FlashMemory.h" must be included to use the class function.

**FlashMemoryClass::writeWord**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Write 4 bytes data (a word) to a flash address, based on the new base address with specific offset. Then read data from the address and compare with the original data. If there is difference. Buffer a flash sector from the new base address, then erase the sector from the flash. Replace the correct data back into buffer. Then rewrite the buffer in to the flash.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void writeWord(unsigned int offset, unsigned int data);

**Parameters**
~~~~~~~~~~~~~~

``offset``: offset to the base address.

``data``: The data to be written (4 bytes / a word)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteOneWord <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteOneWord/ReadWriteOneWord.ino>`_

.. note :: "FlashMemory.h" must be included to use the class function.
