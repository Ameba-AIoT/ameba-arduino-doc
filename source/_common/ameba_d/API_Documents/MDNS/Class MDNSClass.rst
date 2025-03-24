Class MDNS
==========

.. contents::
  :local:
  :depth: 2

**MDNS Class**
--------------

**Description**
~~~~~~~~~~~~~~~

A class used for registering and removing MDNS service records.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class MDNSClass

**Members**
~~~~~~~~~~~

+-------------------------------+-------------------------------------+
| **Public Constructors**       |                                     |
+===============================+=====================================+
| The public constructor should not be used as this class is          |
| intended to be a singleton class. Access member functions using     |
| the object instance named MDNS.                                     |
+-------------------------------+-------------------------------------+
| **Public Methods**                                                  |   
+-------------------------------+-------------------------------------+
| MDNSClass::begin              | Start MDNS operations               |
+-------------------------------+-------------------------------------+
| MDNSClass::end                | Stop MDNS operations                |
+-------------------------------+-------------------------------------+
| MDNSClass::registerService    | Add a service record                |
+-------------------------------+-------------------------------------+
| MDNSClass::deregisterService  | Remove service record               |
+-------------------------------+-------------------------------------+
| MDNSClass::updateService      | Update service record               |
+-------------------------------+-------------------------------------+

------------------------

**MDNSClass::begin**
--------------------

**Description**
~~~~~~~~~~~~~~~

Start MDNS operations to begin responding to MDNS queries.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `mDNS_On_Arduino_IDE <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/MDNS/examples/mDNS_On_Arduino_IDE/mDNS_On_Arduino_IDE.ino>`_

.. note :: “AmebaMDNS.h” must be included to use the class function.

----------------------------------------------------------

**MDNSClass::end**
------------------

**Description**
~~~~~~~~~~~~~~~

Stop MDNS operations and stop responding to MDNS queries.

**Syntax**
~~~~~~~~~~

.. code:: c++

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

.. note :: “AmebaMDNS.h” must be included to use the class function.

------------------------------------------------------------

**MDNSClass::registerService**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Add a service record to be included in MDNS responses.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void registerService(MDNSService service);

**Parameters**
~~~~~~~~~~~~~~

``service``: MDNSService class object with required MDNS service data

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `mDNS_On_Arduino_IDE <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/MDNS/examples/mDNS_On_Arduino_IDE/mDNS_On_Arduino_IDE.ino>`_

.. note :: “AmebaMDNS.h” must be included to use the class function.

--------------------------------------------------------------------------------

**MDNSClass::deregisterService**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Remove a service record from MDNS responses.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void deregisterService(MDNSService service);

**Parameters**
~~~~~~~~~~~~~~

``service`` : MDNSService class object to be removed

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `mDNS_On_Arduino_IDE <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/MDNS/examples/mDNS_On_Arduino_IDE/mDNS_On_Arduino_IDE.ino>`_

.. note :: “AmebaMDNS.h” must be included to use the class function.

-------------------------------------------------------------


**MDNSClass::updateService**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Update a service record.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void updateService(MDNSService service, unsigned int ttl);

**Parameters**
~~~~~~~~~~~~~~

``service``: MDNSService class object to be updated

``ttl``: time-to-live(TTL) for service

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AmebaMDNS.h” must be included to use the class function.
