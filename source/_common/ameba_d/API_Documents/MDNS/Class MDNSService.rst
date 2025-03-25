Class MDNSService
=================

.. contents::
  :local:
  :depth: 2

**MDNSService Class**
---------------------

**Description**
~~~~~~~~~~~~~~~

A class used for creating MDNS service records.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class MDNSService

**Members**
~~~~~~~~~~~

+---------------------------+---------------------------------+
| **Public Constructors**   |                                 |  
+===========================+=================================+
| MDNSService::MDNSService  | Create a MDNS service record    |
+---------------------------+---------------------------------+
| **Public Methods**        |                                 |  
+---------------------------+---------------------------------+
| MDNSService::addTxtRecord | Add text to MDNS service record |
+---------------------------+---------------------------------+

-----------------------------------------------------------

**MDNSService::MDNSService**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Create a MDNS service record.

**Syntax**
~~~~~~~~~~

.. code:: c++

  MDNSService(char* name, char* service_type, char* domain, unsigned short port, int bufsize);

**Parameters**
~~~~~~~~~~~~~~

``name``: device name

``service_type``: MDNS service type

``domain``: host domain

``port``: network port

``bufsize`` : size of buffer for MDNS text record

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `mDNS_On_Arduino_IDE <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/MDNS/examples/mDNS_On_Arduino_IDE/mDNS_On_Arduino_IDE.ino>`_

.. note :: “AmebaMDNS.h” must be included to use the class function.

-------------------------------------------

**MDNSService::addTxtRecord**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Add text to MDNS service record.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int addTextRecord(char* key, int value_len, char* value);

**Parameters**
~~~~~~~~~~~~~~

``key``: item key name expressed as character string. 

``value_len``: length of value string

``value``: new value of the key expressed as character string

**Returns**
~~~~~~~~~~~

This function returns 0 if the text record is added to the MDNS service record successfully.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `mDNS_On_Arduino_IDE <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/MDNS/examples/mDNS_On_Arduino_IDE/mDNS_On_Arduino_IDE.ino>`_

.. note :: “AmebaMDNS.h” must be included to use the class function.
