Class SdFatFile
===============

.. contents::
  :local:
  :depth: 2

**SdFatFile Class**
-------------------

**Description**
~~~~~~~~~~~~~~~

Defines a class of SD FAT File.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class SdFatFile

**Members**
~~~~~~~~~~~

+-----------------------+-------------------------------------------+
|**Public Constructors**                                            |
+=======================+===========================================+
|SdFatFile::SdFatFile   | Constructs a SdFatFile object             |
+-----------------------+-------------------------------------------+
|SdFatFile::~SdFatFile  | Destructs a SdFatFile object              |
+-----------------------+-------------------------------------------+
|**Public Methods**                                                 |
+-----------------------+-------------------------------------------+     
|SdFatFile::write       | Write content  1 byte/bytes to file       |
+-----------------------+-------------------------------------------+
|SdFatFile::read        | Read content (1 byte or bytes) from       |
|                       | the file                                  |
+-----------------------+-------------------------------------------+
|SdFatFile::peek        | Read 1 byte from file without move curser |
+-----------------------+-------------------------------------------+
|SdFatFile::available   | Check if the cursor is at EOF             |
|                       | (End-Of-File)                             |
+-----------------------+-------------------------------------------+
|SdFatFile::seek        | Change cursor to a specific position      |
+-----------------------+-------------------------------------------+
|SdFatFile::close       | Close file                                |
+-----------------------+-------------------------------------------+
|SdFatFile::cursor_pos  | Indicate the current cursor position      |
+-----------------------+-------------------------------------------+
|SdFatFile::file_size   | Output the size of file (DWORDs)          |
+-----------------------+-------------------------------------------+

**SdFatFile::write**
--------------------

**Description**
~~~~~~~~~~~~~~~

Write 1 byte or bytes to the file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual size_t write(uint8_t c);
  virtual size_t write(const uint8_t *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

``c`` : The character to be written.

``buf`` : The buffer to be written.

``size`` : The length of buffer to be written.

**Returns**
~~~~~~~~~~~

The function returns the number of byte count that has been successfully written to the file.

**Example Code**
~~~~~~~~~~~~~~~~

NA.

.. note :: “SdFatFile.h” must be included to use the class function.

**SdFatFile::read**
-------------------

**Description**
~~~~~~~~~~~~~~~

Read 1 byte or bytes from the file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual int read(void);
  int read(void *buf, uint16_t nbyte);

**Parameters**
~~~~~~~~~~~~~~

``buf``: The buffer to store the content.

``nbyte``: The buffer size. (Or can be regarded as the desired length to read).

**Returns**
~~~~~~~~~~~

The function returns a read character or the read size of the buffer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “SdFatFile.h” must be included to use the class function.

**SdFatFile::peek**
-------------------

**Description**
~~~~~~~~~~~~~~~

Read one byte from the file without moving the cursor.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the read character as an integer number.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “SdFatFile.h” must be included to use the class function.

**SdFatFile::available**
------------------------

**Description**
~~~~~~~~~~~~~~~

Check if the cursor is at EOF.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns ``0`` if the cursor is at EOF, else returns “1”.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “SdFatFile.h” must be included to use the class function.

**SdFatFile::seek**
-------------------

**Description**
~~~~~~~~~~~~~~~

Change cursor to a specific position.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int seek(uint32_t pos);

**Parameters**
~~~~~~~~~~~~~~

``pos``:  The desired position.

**Returns**
~~~~~~~~~~~

This function returns 0 if the cursor is set a specific position successfully otherwise returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “SdFatFile.h” must be included to use the class function.

**SdFatFile::close**
--------------------

**Description**
~~~~~~~~~~~~~~~

Close file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int close(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns 0 if runs successfully otherwise it returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “SdFatFile.h” in order to use the class function.

**SdFatFile::cursor_pos**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Indicate the current cursor position. It is a file read/write pointer (Zeroed on file open).

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t cursor_pos (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a file read/write pointer. “0” on file open.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “SdFatFile.h” in order to use the class function.

**SdFatFile::file_size**
------------------------

**Description**
~~~~~~~~~~~~~~~

Output the size of file (DWORDs).

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t file_size (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a DWORD value as the file size.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “SdFatFile.h” in order to use the class function.
