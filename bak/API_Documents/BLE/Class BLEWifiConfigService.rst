**BLEWifiConfigService Class**

**Description**

A class used for managing a BLE WiFi configuration service running on
the device

**Syntax**

class BLEWifiConfigService

**Members**

**Public Constructors**

+----------------------------------------+-----------------------------+
| BLEW                                   | Create an instance of the   |
| ifiConfigService::BLEWifiConfigService | BLEWifiConfigService object |
+========================================+=============================+
+----------------------------------------+-----------------------------+

**Public Methods**

+----------------------------------+-----------------------------------+
| BLEWifiConfigService::begin      | Start background thread to        |
|                                  | process WiFi configuration        |
|                                  | commands                          |
+==================================+===================================+
| BLEWifiConfigService::end        | Stop background thread processing |
|                                  | WiFi configuration commands       |
+----------------------------------+-----------------------------------+
| BLEWifiConfigService::addService | Add the service to the BLE stack  |
+----------------------------------+-----------------------------------+
| BLEWifiConfigService::advData    | Get advertising data correctly    |
|                                  | formatted for WiFi configuration  |
|                                  | service                           |
+----------------------------------+-----------------------------------+


**BLEWifiConfigService::BLEWifiConfigService**

**Description**

Create an instance of the BLEWifiConfigService object.

**Syntax**

void BLEWifiConfigService (void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

Only one instance of this class / service should be created.
“BLEWifiConfigService.h” must be included to use the class function.\ **

**BLEWifiConfigService::begin**

**Description**

Start background thread to process WiFi configuration commands.

**Syntax**

void begin(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

“BLEWifiConfigService.h” must be included to use the class function.\ **

**BLEWifiConfigService::end**

**Description**

Stop background thread processing WiFi configuration commands.

**Syntax**

void end(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEWifiConfigService.h” must be included to use the class function.\ **

**BLEWifiConfigService::addService**

**Description**

Add the WiFi configuration service to the BLE stack.

**Syntax**

void addService(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

“BLEWifiConfigService.h” must be included to use the class function.

**BLEWifiConfigService::advData**

**Description**

Get advertising data correctly formatted for WiFi configuration service.

**Syntax**

BLEAdvertData advData(void);

**Parameters**

NA

**Returns**

This function returns a BLEAdvertData object that contains the required
advertising data fields for the WiFi configuration service to work.

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

The advertisement data needs to be correctly formatted for the
corresponding smartphone app to recognise the device. WiFi configuration
service advertisement data requires the local BT address, and should be
called only after peripheral mode is started and may also require
stopping and restarting the advertising process.
“BLEWifiConfigService.h” must be included to use the class function.
