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
| **Public Constructors**            |                                  |
+====================================+==================================+
| FlashMemoryClass::FlashMemoryClass | Constructs a FlashMemoryClass    |
|                                    | object                           |
+------------------------------------+----------------------------------+
| **Public Methods**                 |                                  |
+------------------------------------+----------------------------------+
| FlashMemoryClass::begin            | Initialize/Re-initialize the     |
|                                    | base address and size            |
+------------------------------------+----------------------------------+
| FlashMemoryClass::end              | Free the buf set by begin,       |
|                                    | deinit flash memory process      |
+------------------------------------+----------------------------------+
| FlashMemoryClass::read             | Read content (stream of word)    |
|                                    | from flash memory to buffer.     |
|                                    | Able to set address with         |
|                                    | specific offset.                 |
+------------------------------------+----------------------------------+
| FlashMemoryClass::write            | Write the content in the buffer  |
|                                    | back to the flash memory. Able   |
|                                    | to set address with specific     |
|                                    | offset.                          |
+------------------------------------+----------------------------------+
| FlashMemoryClass::readWord         | Read word (4 bytes) from flash   |
|                                    | memory based on the new base     |
|                                    | address with specific offset.    |
+------------------------------------+----------------------------------+
| FlashMemoryClass::writeWord        | Write word to flash memory based |
|                                    | on the new base address with     |
|                                    | specific offset.                 |
+------------------------------------+----------------------------------+
| FlashMemoryClass::eraseSector      | Erase flash memory by sector (4K |
|                                    | bytes)                           |
+------------------------------------+----------------------------------+
| FlashMemoryClass::eraseWord        | Erase flash memory by word       |
+------------------------------------+----------------------------------+
| FlashMemoryClass::buf_size         | The buf size regarded as work    |
|                                    | size                             |
+------------------------------------+----------------------------------+
| FlashMemoryClass::buf              | The buf to be operated           |
+------------------------------------+----------------------------------+

**FlashMemoryClass::FlashMemoryClass**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a FlashMemoryClass object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    FlashMemoryClass(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteWord <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteWord/ReadWriteWord.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::begin**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize/Re-initialize the base address and size. The default usable flash memory size is 0x3000.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(unsigned int flash_base_address, unsigned int flash_buf_size);

**Parameters**
~~~~~~~~~~~~~~

flash_base_address: The starting location/position of the flash memory.

flash_buf_size: The desired buffer size.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteWord <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteWord/ReadWriteWord.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::end**

**Description**
~~~~~~~~~~~~~~~

Free the buf set by begin, deinit flash memory process.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

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

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::read**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Read from the flash memory and copy into a buffer. All modification of the contents will be done in the buffer before updating the flash memory. The default length of the buf is buf_size with 0x3000. Update buf and buf_size by function “begin()”. Indicate the starting address by “offset”.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void read(unsigned int offset = 0);

**Parameters**
~~~~~~~~~~~~~~

offset: offset to the base address.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteStream/ReadWriteStream.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::write**

**Description**
~~~~~~~~~~~~~~~

Write buf back to flash memory. Indicate the starting address by “offset”. The default length of the buf is buf_size with 0x3000. Update buf and buf_size by function “begin()”

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void write(unsigned int offset = 0);

**Parameters**
~~~~~~~~~~~~~~

offset: offset to the base address.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteStream/ReadWriteStream.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

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

offset: offset to the base address.

**Returns**
~~~~~~~~~~~

This function returns the 4 bytes read data. The return type is “unsigned int”.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteWord <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteWord/ReadWriteWord.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::writeWord**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Write 4 bytes data (a word) to a flash address, based on the new base address with specific offset. Then read data from the address and compare with the original data. If there is difference. Buffer a flash sector from the new base address, then erase the sector from the flash. Replace the correct data back into buffer. Then rewrite the buffer into the flash.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void writeWord(unsigned int offset, unsigned int data);

**Parameters**
~~~~~~~~~~~~~~

offset: offset to the base address.

data: The data to be written (4 bytes / a word)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteWord <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteWord/ReadWriteWord.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::eraseSector**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Erase flash memory by sector (4K bytes). The erase size should be the multiples of sector size.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void eraseSector(unsigned int sector_offset);

**Parameters**
~~~~~~~~~~~~~~

offset: offset to the base address.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::eraseWord**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Erase flash memory by word (4 bytes). The offset according to base address.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void eraseWord(unsigned int offset);

**Parameters**
~~~~~~~~~~~~~~

offset: offset to the base address.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::buf_size**
------------------------------

**Description**
~~~~~~~~~~~~~~~

The buf size regarded as work size. Maximum size is MAX_FLASH_MEMORY_APP_SIZE that is 0x3000.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    unsigned int buf_size;

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteWord <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteWord/ReadWriteWord.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.

**FlashMemoryClass::buf**
-------------------------

**Description**
~~~~~~~~~~~~~~~

The buf to be operated. Modify buf won't change the content of buf. It needs update to write back to flash memory.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    unsigned char *buf;

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadWriteWord <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/FlashMemory/examples/ReadWriteWord/ReadWriteWord.ino>`_

.. note :: “FlashMemory.h” must be included to use the class function.
