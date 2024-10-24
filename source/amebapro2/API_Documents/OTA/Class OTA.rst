Class OTA
==========

.. contents::
  :local:
  :depth: 2

**OTA Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used for updating firmware Over the Air (OTA) in local area network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++
  
  class OTA

**Members**
~~~~~~~~~~~

+----------------------------------------------+--------------------------------------------+
| **Public Constructors**                                                                   |
+==============================================+============================================+
| A public constructor should not be used as this class is intended to be a singleton class.|
| Access member functions using the object instance named OTA.                              |                                  
+----------------------------------------------+--------------------------------------------+
| **Public Methods**                                                                        |
+----------------------------------------------+--------------------------------------------+
| OTA::start_OTA_threads                       | To begin threading tasks for OTA           |
|                                              | firmware update.                           |
+----------------------------------------------+--------------------------------------------+

**OTA::start_OTA_threads**
--------------------------

**Description**
~~~~~~~~~~~~~~~

To begin threading tasks for OTA firmware update.

**Syntax**
~~~~~~~~~~

.. code-block:: c++
  
  void start_OTA_threads(int port, char* server);

**Parameters**
~~~~~~~~~~~~~~

port: port number for the OTA HTTP server IP address

\*server: pointer for OTA HTTP server IP address

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `OTA <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/OTA/examples/OTA/OTA.ino>`_

.. note :: “OTA.h” must be included to use the function.
