Header OTA
==========

.. contents::
  :local:
  :depth: 2

**OTA Header**
--------------

**Description**
~~~~~~~~~~~~~~~

A header file for OTA API.

**Syntax**
~~~~~~~~~~

NA

**Members**
~~~~~~~~~~~

+-----------------------------------+----------------------------------+
| **Public Constructors**           |                                  |
+===================================+==================================+
| NA                                | NA                               |
|                                   |                                  |
|                                   |                                  |
+-----------------------------------+----------------------------------+
| **Public Methods**                |                                  |
+-----------------------------------+----------------------------------+
| start_OTA_threads                 | To begin threading tasks for OTA |
|                                   | firmware update.                 |
+-----------------------------------+----------------------------------+

**start_OTA_threads**
---------------------

**Description**
~~~~~~~~~~~~~~~

To begin threading tasks for OTA firmware update.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void start_OTA_threads();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `OTA <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/OTA/examples/OTA/OTA.ino>`_

.. note :: “ota_thread.h” must be included to use the function.