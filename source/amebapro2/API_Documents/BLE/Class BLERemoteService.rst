Class BLERemoteService
======================

.. contents::
  :local:
  :depth: 2

**BLERemoteService Class**
--------------------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing BLE GATT services on connected remote devices.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLERemoteService

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**            |                                 |
+====================================+=================================+
| No public constructor is available for this class. You can get a     |
| pointer to an instance of this class using BLEClient::getService().  |
+------------------------------------+---------------------------------+
| **Public Methods**                 |                                 |
+------------------------------------+---------------------------------+
| BLERemoteService::getUUID          | Get the service UUID            |
+------------------------------------+---------------------------------+
| BLERemoteService::getCharacteristic| Get a specific characteristic   |
|                                    | on the remote device            |
+------------------------------------+---------------------------------+

**BLERemoteService::getUUID**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the service UUID.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    BLEUUID getUUID(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the service UUID as a BLEUUID class object.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “BLERemoteService.h” must be included to use the class function.

**BLERemoteService::getCharacteristic**
---------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get a characteristic with the specified UUID on the remote device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    BLERemoteCharacteristic* getCharacteristic (const char* uuid);

    BLERemoteCharacteristic* getCharacteristic (BLEUUID uuid);

**Parameters**
~~~~~~~~~~~~~~

uuid: the desired characteristic UUID, expressed as a character array or a BLEUUID class object.

**Returns**
~~~~~~~~~~~

The function returns the found characteristic as a
BLERemoteCharacteristic object pointer, otherwise nullptr is returned if
a characteristic with the UUID is not found.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEUartClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartClient/BLEUartClient.ino>`_ 

.. note :: BLERemoteService.h” must be included to use the class function.