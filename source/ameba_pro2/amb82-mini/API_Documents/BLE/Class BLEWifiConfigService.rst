Class BLEWifiConfigService
==========================

**BLEWifiConfigService Class**
------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing a BLE WiFi configuration service running on
the device

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLEWifiConfigService

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| BLEWifiConfigService::             | Create an instance of the       |
| BLEWifiConfigService               | BLEWifiConfigService object     |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| BLEWifiConfigService::begin        | Start background thread to      |
|                                    | process WiFi configuration      |
|                                    | commands                        |
+------------------------------------+---------------------------------+
| BLEWifiConfigService::end          | Stop background thread          |
|                                    | processing WiFi configuration   |
|                                    | commands                        |
+------------------------------------+---------------------------------+
| BLEWifiConfigService::addService   | Add the service to the BLE stack|
+------------------------------------+---------------------------------+
| BLEWifiConfigService::advData      | Get advertising data correctly  |
|                                    | formatted for WiFi configuration|
|                                    | service                         |
+------------------------------------+---------------------------------+

**BLEWifiConfigService::BLEWifiConfigService**
----------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Create an instance of the BLEWifiConfigService object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void BLEWifiConfigService (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEWifiConfig <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino>`_

.. note :: Only one instance of this class / service should be created. "BLEWifiConfigService.h" must be included to use the class function.

**BLEWifiConfigService::begin**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Start background thread to process WiFi configuration commands.

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

Example: `BLEWifiConfig <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino>`_

.. note :: "BLEWifiConfigService.h" must be included to use the class function.

**BLEWifiConfigService::end**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Stop background thread processing WiFi configuration commands.

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

NA

.. note :: "BLEWifiConfigService.h" must be included to use the class function.

**BLEWifiConfigService::addService**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Add the WiFi configuration service to the BLE stack.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void addService(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEWifiConfig <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino>`_

.. note :: "BLEWifiConfigService.h" must be included to use the class function.

**BLEWifiConfigService::advData**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get advertising data correctly formatted for WiFi configuration service.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    BLEAdvertData advData(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns a BLEAdvertData object that contains the required advertising data fields for the WiFi configuration service to work.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEWifiConfig <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino>`_

.. note :: The advertisement data needs to be correctly formatted for the corresponding smartphone app to recognise the device. WiFi configuration service advertisement data requires the local BT address, and should be called only after peripheral mode is started and may also require stopping and restarting the advertising process. "BLEWifiConfigService.h" must be included to use the class function.
