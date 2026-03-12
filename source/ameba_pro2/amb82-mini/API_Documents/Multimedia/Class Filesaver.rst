Class Filesaver
===============

**Filesaver Class**
-------------------

**Description**
~~~~~~~~~~~~~~~

A class for file saving.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class Filesaver

**Members**
~~~~~~~~~~~

+------------------------------------------------+--------------------------------------------------------+
| **Public Constructors**                                                                                 |
+================================================+========================================================+
| Filesaver::Filesaver                           | Constructs a Filesaver object.                         |
+------------------------------------------------+--------------------------------------------------------+
| **Public Methods**                                                                                      |
+------------------------------------------------+--------------------------------------------------------+
| Filesaver::setFileName                         | Set the filename to be saved.                          |
+------------------------------------------------+--------------------------------------------------------+
| Filesaver::staticImgSaveCB                     | Static raw image saving callback function.             |
+------------------------------------------------+--------------------------------------------------------+
| Filesaver::rawImgSaveSDBegin                   | Save raw image into SD card.                           |
+------------------------------------------------+--------------------------------------------------------+
| Filesaver::rawImgSaveCB                        | Raw image saving callback function.                    |
+------------------------------------------------+--------------------------------------------------------+
| Filesaver::rawReform                           | Function to perform image raw reform.                  |
+------------------------------------------------+--------------------------------------------------------+

**Filesaver::setFileName**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Set the filename to be saved.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setFileName(char *filename);

**Parameters**
~~~~~~~~~~~~~~

filename: name of the file to be saved.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~~

Example: `SDCardSaveRaw <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureRaw/SDCardSaveRaw/SDCardSaveRaw.ino>`_

.. note :: "Filesaver.h" must be included to use the class function.

**Filesaver::staticImgSaveCB**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Static raw image saving callback function.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void staticImgSaveCB(char *file_path, uint32_t data_addr, uint32_t data_size);

**Parameters**
~~~~~~~~~~~~~~

file_path: file path of the image to be saved

data_addr: image data address

data_size: image data size

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SDCardSaveRaw <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureRaw/SDCardSaveRaw/SDCardSaveRaw.ino>`_

.. note :: "Filesaver.h" must be included to use the class function.

**Filesaver::rawImgSaveSDBegin**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Save raw image into SD card.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void rawImgSaveSDBegin();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SDCardSaveRaw <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureRaw/SDCardSaveRaw/SDCardSaveRaw.ino>`_

.. note :: "Filesaver.h" must be included to use the class function.

**Filesaver::rawImgSaveCB**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Raw image saving callback function.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void rawImgSaveCB(char *file_path, uint32_t data_addr, uint32_t data_size);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SDCardSaveRaw <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureRaw/SDCardSaveRaw/SDCardSaveRaw.ino>`_

.. note :: "Filesaver.h" must be included to use the class function.

**Filesaver::rawReform**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Function to perform image raw reform.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void rawReform(unsigned char *pData, int dataLen);

**Parameters**
~~~~~~~~~~~~~~

pData:  pointer to the image data address

dataLen: image data length


**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SDCardSaveRaw <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureRaw/SDCardSaveRaw/SDCardSaveRaw.ino>`_

.. note :: "Filesaver.h" must be included to use the class function.
