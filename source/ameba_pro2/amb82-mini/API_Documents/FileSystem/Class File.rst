Class File
==========

.. contents::
  :local:
  :depth: 2

**File Class**
--------------

**Description**
~~~~~~~~~~~~~~~

A class for data manipulation of files in a file system.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class File

**Members**
~~~~~~~~~~~

+---------------------------+------------------------------------------+
| **Public Constructors**                                              |
+===========================+==========================================+
| File::File                | Constructs a File object.                |
+---------------------------+------------------------------------------+
| **Public Methods**                                                   |
+---------------------------+------------------------------------------+
| File::open                | Open a file from the filesystem.         |
+---------------------------+------------------------------------------+
| File::close               | Close a previously opened file.          |
+---------------------------+------------------------------------------+
| File::write               | Write data to the currently open file.   |
+---------------------------+------------------------------------------+
| File::read                | Read data from the currently open file.  |
+---------------------------+------------------------------------------+
| File::peek                | Peek at the next data byte from the      |
|                           | currently open file.                     |
+---------------------------+------------------------------------------+
| File::available           | Check number of bytes remaining till end |
|                           | of file.                                 |
+---------------------------+------------------------------------------+
| File::flush               | Flush cached data.                       |
+---------------------------+------------------------------------------+
| File::seek                | Move read write pointer.                 |
+---------------------------+------------------------------------------+
| File::position            | Get current read write pointer.          |
+---------------------------+------------------------------------------+
| File::size                | Get file size.                           |
+---------------------------+------------------------------------------+
| File::isOpen              | Check if a file is currently open.       |
+---------------------------+------------------------------------------+
| File::name                | Get currently open file name.            |
+---------------------------+------------------------------------------+
| File::convertMp3ToArray   | Convert MP3 file to MP3data and MP3size. |
+---------------------------+------------------------------------------+
| File::setMp3DigitalVol    | Control the digital gain of DAC.         |
+---------------------------+------------------------------------------+
| File::playmp3             | Execute convertMp3TArray.                |
+---------------------------+------------------------------------------+
| File::readFile            | Read data according to opened file size  |
+---------------------------+------------------------------------------+

**File::File**
--------------

**Description**
~~~~~~~~~~~~~~~

Constructs a File object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    File::File(void);
    File::File(const char* filename);
    File::File(const char *filename, int fileType);

**Parameters**
~~~~~~~~~~~~~~

filename: pointer to a char array containing the path of the file to open.
fileType: The macro of the file type defined in AmebaFatFSFile.h to support different opening methods for different types of file.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `CreateFolder <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino>`_

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::open**
--------------

**Description**
~~~~~~~~~~~~~~~

Open a file from the file system.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool open(const char* filename);
    bool open(const char *filename, int fileType);

**Parameters**
~~~~~~~~~~~~~~

filename: pointer to a char array containing the path of the file to open.
fileType: The macro of the file type defined in AmebaFatFSFile.h to support different opening methods for different types of file.

**Returns**
~~~~~~~~~~~

This function returns true if the file is opened successfully, false otherwise.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::close**
---------------

**Description**
~~~~~~~~~~~~~~~

Close a previously opened file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void close(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `CreateFolder <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino>`_

.. note :: "AmebaFatFSFile.h" must be included to use the class function. Opened files need to be closed to ensure that any pending data is saved correctly.

**File::write**
---------------

**Description**
~~~~~~~~~~~~~~~

Write data to the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    size_t write(uint8_t c);
    size_t write(const uint8_t* buf, size_t size);
    size_t write(const char* str);
    size_t write(const char* buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

c: single data byte to write.

str: pointer to char array containing data to write, expressed as a null terminated string.

buf: pointer to array containing data to write.

size: number of bytes to write.

**Returns**
~~~~~~~~~~~

This function returns the number of data bytes written to file.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::read**
--------------

**Description**
~~~~~~~~~~~~~~~

Read data from the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int read(void);
    int read(void* buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: pointer to buffer to store read data.

size: number of data bytes to read.

**Returns**
~~~~~~~~~~~

When a buffer pointer is not used, this function returns the data byte read if successful, otherwise it returns "-1".

When a buffer pointer is used, this function returns the number of bytes read.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `CreateFolder <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino>`_

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::peek**
--------------

**Description**
~~~~~~~~~~~~~~~

Peek at the next data byte from the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next data byte if successful, otherwise it returns "-1".

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::available**
-------------------

**Description**
~~~~~~~~~~~~~~~

Check number of bytes remaining till end of file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the number of bytes available to read until the end of file.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ReadHTMLFile <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/FileSystem/examples/ReadHTMLFile/ReadHTMLFile.ino>`_

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::flush**
---------------

**Description**
~~~~~~~~~~~~~~~

Flush cached data.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void flush(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function flushes any cached data and writes all pending data into file.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::seek**
--------------

**Description**
~~~~~~~~~~~~~~~

Move the file read/write pointer of the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool seek(uint32_t pos);

**Parameters**
~~~~~~~~~~~~~~

pos: file position to move.

**Returns**
~~~~~~~~~~~

This function returns true if the file pointer is move successfully, false otherwise.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function. If the target position is larger than the size of the currently open file, the file size will be increased as required.

**File::position**
------------------

**Description**
~~~~~~~~~~~~~~~

Get the read/write pointer of the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t position(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current file read/write position.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::size**
--------------

**Description**
~~~~~~~~~~~~~~~

Get the size of the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t size(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the size of the currently open file.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::isOpen**
----------------

**Description**
~~~~~~~~~~~~~~~

Check if a file is currently open.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool isOpen(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if a file is currently open, false otherwise.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::name**
--------------

**Description**
~~~~~~~~~~~~~~~

Get the filename of the currently open file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    const char* name(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to a character array containing the filename of the currently open file. If no file is open, it returns NULL.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::convertMp3ToArray**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Convert MP3 file to MP3data and MP3size.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void convertMp3ToArray(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function convert MP3 file into character array containing the MP3data without the ID3 header. If no file is open for conversion, it will print out error message.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::setMp3DigitalVol**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Control the digital gain of DAC.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setMp3DigitalVol(uint8_t digitalVol);

**Parameters**
~~~~~~~~~~~~~~

digitalVol: output digital volume

.. note::
    Every Step is 0.375dB.
    
    | 0xAF: 0dB.
    | 0xAE: -0.375dB.
    | ...
    | 0x00: -65.625dB.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::playMp3**
-----------------

**Description**
~~~~~~~~~~~~~~~

Execute convertMp3TArray.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void playMp3(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.

**File::readFile**
------------------

**Description**
~~~~~~~~~~~~~~~

Read opened data file according to its file size, malloc is done within API, no pre-definition of fixed size buffer needed.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool readFile(unsigned char *file_data, uint32_t &file_size);

**Parameters**
~~~~~~~~~~~~~~

file_data: buffer pointer for the file to be read

file_size: the size of the file to be read

**Returns**
~~~~~~~~~~~

True if the file data is read successfully, false if failed to read file data.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "AmebaFatFSFile.h" must be included to use the class function.