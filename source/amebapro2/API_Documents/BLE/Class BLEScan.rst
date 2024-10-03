Class BLEScan
=============

.. contents::
  :local:
  :depth: 2

**BLEScan Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing BLE scanning settings.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLEScan

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**            |                                 |
+====================================+=================================+
| No public constructor is available as this class is intended to be a |
| singleton class. You can get a pointer to this class using           |
| BLEDevice::configScan                                                |
+------------------------------------+---------------------------------+
| **Public Methods**                 |                                 |
+------------------------------------+---------------------------------+
| BLEScan::updateScanParams          | Update the lower Bluetooth      |
|                                    | stack with the current scan     |
|                                    | settings                        |
+------------------------------------+---------------------------------+
| BLEScan::startScan                 | Start a BLE scan                |
+------------------------------------+---------------------------------+
| BLEScan::stopScan                  | Stop a BLE scan                 |
+------------------------------------+---------------------------------+
| BLEScan::setScanMode               | Set the BLE scanning mode       |
+------------------------------------+---------------------------------+
| BLEScan::setScanInterval           | Set the BLE scanning interval   |
+------------------------------------+---------------------------------+
| BLEScan::setScanWindow             | Set the BLE scanning window     |
+------------------------------------+---------------------------------+
| BLEScan::setScanDuplicateFilter    | Set the BLE scan duplicate      |
|                                    | filter                          |
+------------------------------------+---------------------------------+
| BLEScan::scanInProgress            | Check if a scan is currently in |
|                                    | progress                        |
+------------------------------------+---------------------------------+
| BLEScan::printScanInfo             | Print out scanned information   |
+------------------------------------+---------------------------------+

**BLEScan::updateScanParams**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Update the lower Bluetooth stack with the current scan settings.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void updateScanParams(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_ 

.. note :: Stop any scans in progress first before using this 
    function. 
    
    “BLEScan.h” must be included to use the class function.

**BLEScan::startScan**
----------------------

**Description**
~~~~~~~~~~~~~~~

Start BLE scanning.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void startScan(void);

    void startScan(uint32_t scanDuration_ms);

**Parameters**
~~~~~~~~~~~~~~

scanDuration: BLE scan will stop after scanDuration milliseconds.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_ 

.. note :: Set the scan parameters first before starting a scan. BLE scans will
    occur continuously for the duration set with BLEDevice::setScanWindow()
    and will repeat with a time interval set with
    BLEDevice::setScanInterval(). Call this member function without an
    argument to start scanning until BLEDevice::stopScan() is called.

    “BLEScan.h” must be included to use the class function.

**BLEScan::stopScan**
---------------------

**Description**
~~~~~~~~~~~~~~~

Stop BLE scanning.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void stopScan(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “BLEScan.h” must be included to use the class function.

**BLEScan::setScanMode**
------------------------

**Description**
~~~~~~~~~~~~~~~

Set the BLE scanning mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setScanMode(uint8_t scanMode);

**Parameters**
~~~~~~~~~~~~~~

scanMode: GAP_SCAN_MODE_PASSIVE for passive scanning,
GAP_SCAN_MODE_ACTIVE for active scanning. 

Default value: GAP_SCAN_MODE_ACTIVE.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_ 

.. note :: Active scanning will request for scan response packets after discovering
        an advertising device. Passive scanning will only capture advertising data packets.
    
    “BLEScan.h” must be included to use the class function.

**BLEScan::setScanInterval**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set the BLE scanning interval.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setScanInterval(uint16_t scanInt_ms);

**Parameters**
~~~~~~~~~~~~~~

scanInt_ms: scan interval in milliseconds. Value range of 3 to 10240.

Default value of 40ms.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_ 

.. note :: A BLE scan will repeat with a time interval set with this member
    function. 

    “BLEScan.h” must be included to use the class function.

**BLEScan::setScanWindow**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Set the BLE scanning window.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setScanWindow(uint16_t scanWindow_ms);

**Parameters**
~~~~~~~~~~~~~~

scanWindow_ms: scan window in milliseconds. Value range of 3 to 10240.

Default value of 30ms.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_ 

.. note :: A BLE scan will scan continuously for a window duration set with this
    member function. The scan window should be less than or equal to the
    scan interval. 
    
    “BLEScan.h” must be included to use the class function.

**BLEScan::setScanDuplicateFilter**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the scan duplicate filter.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setScanDuplicateFilter(bool dupeFilter);

**Parameters**
~~~~~~~~~~~~~~

dupeFilter: TRUE to enable duplicate filtering. Enabled by default.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Enabling duplicate filters will ignore scan results for devices already
    discovered previously. 

    “BLEScan.h” must be included to use the class function.

**BLEScan::scanInProgress**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Check if scanning is currently in progress.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool scanInProgress(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns TRUE if BLE scanning is in progress.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “BLEScan.h” must be included to use the class function.

**BLEScan::printScanInfo**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Parse and print out scanned information.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void printScanInfo(T_LE_CB_DATA* p_data);

**Parameters**
~~~~~~~~~~~~~~

p_data: pointer to scan data of type T_LE_CB_DATA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEScan <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino>`_ 

.. note :: Use this member function to parse the various fields of received
    advertisement data packets and print the results out to the serial monitor. 
    
    “BLEScan.h” must be included to use the class function.