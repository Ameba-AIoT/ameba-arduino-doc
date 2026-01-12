Class Httpfs
============

**Httpfs Class**
-----------------

**Description**
~~~~~~~~~~~~~~~~~

A class used HTTP File Server.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class Httpfs

**Members**
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **Public Constructors**           |                                   |
+===================================+===================================+
| Httpfs::Httpfs                    | Constructs a Httpfs object.       |
+-----------------------------------+-----------------------------------+
| **Public Methods**                                                    |
+-----------------------------------+-----------------------------------+
| Httpfs::begin                     | Initializes the HTTP file server, |
|                                   | set parameter, response callback  |
|                                   | function of the file server.      |
+-----------------------------------+-----------------------------------+
| Httpfs::mp4DirectoryInit          | Initializes the directory to save |
|                                   | MP4 recordings on SD card.        |
+-----------------------------------+-----------------------------------+
| Httpfs::end                       | Deinitializes the HTTP file       |
|                                   | server.                           |
+-----------------------------------+-----------------------------------+

**Httpfs::begin**
-----------------

**Description**
~~~~~~~~~~~~~~~

Initializes the HTTP file server, set parameter, response callback function of the file server.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Httpfs_mp4 <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Http/examples/Httpfs_mp4/Httpfs_mp4.ino>`_

**Httpfs::mp4DirectoryInit**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Initializes the directory to save MP4 recordings on SD card.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void mp4DirectoryInit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Httpfs_mp4 <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Http/examples/Httpfs_mp4/Httpfs_mp4.ino>`_

**Httpfs::end**
---------------

**Description**
~~~~~~~~~~~~~~~

Deinitializes the HTTP file server.

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

Example: `Httpfs_mp4 <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Http/examples/Httpfs_mp4/Httpfs_mp4.ino>`_

