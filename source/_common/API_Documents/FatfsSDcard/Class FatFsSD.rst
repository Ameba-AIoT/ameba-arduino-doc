Class FatFsSD
=============

.. contents::
  :local:
  :depth: 2

**FatFsSD Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

Defines a class of SD FAT File system.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class FatFsSD

**Members**
~~~~~~~~~~~

+-------------------------+-------------------------------------------+
|**Public Constructors**                                              |
+=========================+===========================================+
|FatFsSD::FatFsSD         |  Constructs a FatFsSD object              |
+-------------------------+-------------------------------------------+
|FatFsSD::~FatFsSD        |  Destructs a FatFsSD object               |
+-------------------------+-------------------------------------------+
|**Public Methods**                                                   |
+-------------------------+-------------------------------------------+
| FatFsSD::begin          | Initialize SD FAT File System             |
+-------------------------+-------------------------------------------+
| FatFsSD::end            | Deinitialize SD FAT File System           |
+-------------------------+-------------------------------------------+
| FatFsSD::\*getRootPath  | Get the root path of the SD FAT File      |
|                         | System                                    |
+-------------------------+-------------------------------------------+
| FatFsSD::readDir        | List items under a specific folder        |
+-------------------------+-------------------------------------------+
| FatFsSD::mkdir          | Create folder                             |
+-------------------------+-------------------------------------------+
| FatFsSD::rm             | Remove folder or file                     |
+-------------------------+-------------------------------------------+
| FatFsSD::isDir          | Check if a specific path is a directory   |
+-------------------------+-------------------------------------------+
| FatFsSD::isFile         | Check if a specific path is a file        |
+-------------------------+-------------------------------------------+
| FatFsSD::getLastModTime | Get the last modified time for a file or  |
|                         | directory                                 |
+-------------------------+-------------------------------------------+
| FatFsSD::setLastModTime | Set the last modified time for a file or  |
|                         | directory                                 |
+-------------------------+-------------------------------------------+
| FatFsSD::status         | Return the current status of SD           |
+-------------------------+-------------------------------------------+
| FatFsSD::open           | Open a file                               |
+-------------------------+-------------------------------------------+

**FatFsSD::begin**
------------------

**Description**
~~~~~~~~~~~~~~~

Initialize SD FAT File System.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

Returns **0** if success, else returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::end**
----------------

**Description**
~~~~~~~~~~~~~~~

De-initialize SD FAT File System.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int end(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

Returns “0” if success, else returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::*getRootPath**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the root path of the SD FAT File System. The logical volume character is starting from '0', so the root path would like “0:/”.

**Syntax**
~~~~~~~~~~

.. code:: c++

  char *getRootPath(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the root path.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::readDir**
--------------------

**Description**
~~~~~~~~~~~~~~~

List items under a specific folder. List items under a specific folder
and store the result in the buffer that user specified. Each item is
separated by '\0'.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int readDir(char *path, char *result_buf, unsigned int bufsize);

**Parameters**
~~~~~~~~~~~~~~

``path``: The absolute directory path to be listed.

``result_buf`` : The buffer to be stored results.

``bufsize`` : The size of result_buf. If results exceed this size, then the results larger than this size would be discarded.

**Returns**
~~~~~~~~~~~

Returns ``0`` if success, else returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `get_file_attribute <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/get_file_attribute/get_file_attribute.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::mkdir**
------------------

**Description**
~~~~~~~~~~~~~~~

Create folder.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int mkdir(char *absolute_path);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path`` : The absolute directory path to be created

**Returns**
~~~~~~~~~~~

Returns ``0`` if success, else returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::rm**
---------------

**Description**
~~~~~~~~~~~~~~~

Remove folder or file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int rm(char *absolute_path);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path`` : The absolute directory or file path to be deleted

**Returns**
~~~~~~~~~~~

Returns ``0`` if success, else returns a negative value.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::isDir**
------------------

**Description**
~~~~~~~~~~~~~~~

Check if a specific path is a directory.

**Syntax**
~~~~~~~~~~

.. code:: c++

  unsigned char isDir(char *absolute_path);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path``: The absolute path to be queried

**Returns**
~~~~~~~~~~~

The function returns ``1`` if it is a directory, else returns ``0``.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `get_file_attribute <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/get_file_attribute/get_file_attribute.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::isFile**
-------------------

**Description**
~~~~~~~~~~~~~~~

Check if a specific path is a file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  unsigned char isFile(char *absolute_path);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path`` : The absolute path to be queried

**Returns**
~~~~~~~~~~~

The function returns “1” if it is a directory, else returns “0”.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `get_file_attribute <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/get_file_attribute/get_file_attribute.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::getLastModTime**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get the last modified time for a file or directory.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int getLastModTime(char *absolute_path, uint16_t *year, uint16_t *month, uint16_t *date, uint16_t *hour, uint16_t *minute, uint16_t *second);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path``: The absolute path to be queried.

``year``: The value of the year.

``month``: The value of the month.

``date``: The value of the date.

``hour``: The value of an hour.

``minute``: The value of a minute.

``second``: field “second” contains no valid information in the current version.

**Returns**
~~~~~~~~~~~

The function returns “0” if success, otherwise returns a negative value for failure.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `last_modified_time <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/last_modified_time/last_modified_time.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::setLastModTime**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Set the last modified time for a file or directory. Ameba doesn't have built-in RTC. So we manually change file/directory last modified time.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int setLastModTime(char *absolute_path, uint16_t year,uint16_t month, uint16_t date, uint16_t hour, uint16_t minute, uint16_t second);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path``: The absolute path to be queried.

``year``: The value of the year.

``month``: The value of the month.

``date``: The value of the date.

``hour``: The value of an hour.

``minute``: The value of a minute.

``second``: field “second” contains no valid information in the current version.

**Returns**
~~~~~~~~~~~

The function returns “0” if success, otherwise returns a negative value for failure.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `last_modified_time <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/last_modified_time/last_modified_time.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::status**
-------------------

**Description**
~~~~~~~~~~~~~~~

Return the current status of SD.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int status(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

Function returns “1” if ready to use, else return “0” if the status is inactivating or abnormal.

**Example Code**
~~~~~~~~~~~~~~~~

NA.

.. note :: “FatFs_SD.h” must be included to use the class function.

**FatFsSD::open**
-----------------

**Description**
~~~~~~~~~~~~~~~

Open a file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  SdFatFile open(char *absolute_path);

**Parameters**
~~~~~~~~~~~~~~

``absolute_path``: The path to a file.

**Returns**
~~~~~~~~~~~

The file object is an instance of SdFatFile.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `create_folder <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/FatfsSDIO/examples/create_folder/create_folder.ino>`_

.. note :: “FatFs_SD.h” must be included to use the class function.
