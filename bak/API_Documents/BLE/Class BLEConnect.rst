**BLEConnect Class**

**Description**

A class used for managing BLE connection settings.

**Syntax**

class BLEConnect

**Members**

**Public Constructors**

No public constructor is available as this class is intended to be a
singleton class. You can get a pointer to this class using
BLEDevice::configConnection

**Public Methods**

+--------------------------------+-------------------------------------+
| BLEConnect::connect            | Scan and search for all accessible  |
|                                | BLE devices, then select and        |
|                                | connect to one of them              |
+================================+=====================================+
| BLEConnect::disconnect         | Disconnect from targeted BLE device |
+--------------------------------+-------------------------------------+
| BLEConnect::setScanInterval    | Set the scan interval when          |
|                                | searching for the targeted device   |
+--------------------------------+-------------------------------------+
| BLEConnect::setScanWindow      | Set the BLE scan window when        |
|                                | searching for the targeted device   |
|                                | to connect to                       |
+--------------------------------+-------------------------------------+
| BLEConnect::setConnInterval    | Set the BLE connection interval     |
|                                | duration                            |
+--------------------------------+-------------------------------------+
| BLEConnect::setConnLatency     | Set the BLE connection slave        |
|                                | latency value                       |
+--------------------------------+-------------------------------------+
| BLEConnect::setConnTimeout     | Set the BLE connection timeout      |
|                                | value                               |
+--------------------------------+-------------------------------------+
| BLEConnect::updateConnParams   | Update a connected device with new  |
|                                | connection parameters               |
+--------------------------------+-------------------------------------+
| BLEConnect::getConnInfo        | Get connection information          |
+--------------------------------+-------------------------------------+
| BLEConnect::getConnAddr        | Get the Bluetooth address for a     |
|                                | certain connection                  |
+--------------------------------+-------------------------------------+
| BLEConnect::getConnId          | Get the connection ID for a certain |
|                                | device                              |
+--------------------------------+-------------------------------------+


**BLEConnect::connect**

**Description**

This class function is used to scan and search for all accessible BLE
devices, then select and connect to one of them.

**Syntax**

bool connect(char\* btAddr, T_GAP_REMOTE_ADDR_TYPE destAddrType,
uint16_t scanTimeout);

bool connect(uint8_t (&btAddr)[6], T_GAP_REMOTE_ADDR_TYPE destAddrType,
uint16_t scanTimeout);

bool connect(BLEAdvertData targetDevice, uint16_t scanTimeout);

bool connect(BLEAddr destAddr, T_GAP_REMOTE_ADDR_TYPE destAddrType,
uint16_t scanTimeout);

**Parameters**

char\* btAddr: pointer to the targeted BLE device’s Bluetooth address
expressed as a character string.

uint8_t (&btAddr): targeted BLE device’s Bluetooth address contained in
a 6-byte array.

destAddr: targeted BLE device’s Bluetooth address contained in BLEAddr
class object.

targetDevice: advertising data packet scanned from targeted BLE device.

destAddrType: Bluetooth address type of targeted BLE device, Valid
values:

-  GAP_REMOTE_ADDR_LE_PUBLIC

-  GAP_REMOTE_ADDR_LE_RANDOM

scan timeout: duration in milliseconds for which to look for the
targeted BLE device before giving up.

**Returns**

This function returns true if the connection is successful, otherwise
false.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

“BLEConnect.h” must be included to use the class function.

**BLEConnect::disconnect**

**Description**

Disconnect from targeted BLE device.

**Syntax**

bool disconnect(uint8_t connId);

**Parameters**

connId: connection ID for target device. Default connection ID set to 0.

**Returns**

This function returns true if the operation is successful, otherwise
false.

**Example Code**

NA

**Notes and Warnings**

“BLEConnect.h” must be included to use the class function.

**BLEConnect::setScanInterval**

**Description**

Set the scan interval when searching for the targeted device.

**Syntax**

void setScanInterval(uint16_t scanInt_ms);

**Parameters**

scanInt_ms: scan interval in milliseconds. Valid value: 3 to 10240.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Scan interval defines how often the scanning process is started. The
value set for scanInt_ms must be equal or larger than the value set for
scanWindow_ms. scanInt_ms value is defined in units of 625 microseconds.

“BLEConnect.h” must be included to use the class function.

**BLEConnect::setScanWindow**

**Description**

Set the BLE scan window when searching for the targeted device to
connect to.

**Syntax**

void setScanWindow(uint16_t scanWindow_ms);

**Parameters**

scanWindow_ms: scan window in milliseconds. Valid value: 3 to 10240.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

BLE scan window defines how long each interval should be scanned for.
The value set for scanWindow_ms set must be equal or smaller than the
value set for scanInt_ms. scanWindow_ms value is defined in units of 625
microseconds.

“BLEConnect.h” must be included to use the class function.

**BLEConnect::setConnInterval**

**Description**

Set the BLE connection interval duration.

**Syntax**

void setConnInterval(uint16_t min_ms, uint16_t max_ms);

**Parameters**

min_ms: minimum acceptable connection interval in milliseconds. Valid
value: 8 to 4000.

max_ms: maximum acceptable connection interval in milliseconds. Valid
value: 8 to 4000.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

The BLE connection interval defines the period between successive
connection events between a connected central and peripheral device.
Even if there is no data to exchange, a connection event is required to
maintain the connection. max_ms should be larger than or equal to
min_ms.

“BLEConnect.h” must be included to use the class function.

**BLEConnect::setConnLatency**

**Description**

Set the BLE connection slave latency value.

**Syntax**

void setConnLatency(uint16_t latency);

**Parameters**

latency: Connection slave latency value. Valid value: 0 to 499.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

The BLE connection slave latency defines the number of successive
connection events a connected peripheral device can ignore without being
considered as disconnected by the central device.

“BLEConnect.h” must be included to use the class function.

**BLEConnect::setConnTimeout**

**Description**

Set the BLE connection timeout value.

**Syntax**

void setConnTimeout(uint16_t timeout_ms);

**Parameters**

timeout_ms: connection timeout in milliseconds.

Valid value: 100 to 32000.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

The BLE connection timeout defines the duration a peripheral or central
device must wait after a failed connection event to consider the
connection broken.

“BLEConnect.h” must be included to use the class function.

**BLEConnect::updateConnParams**

**Description**

Update a connected device with new connection parameters.

**Syntax**

void updateConnParams(uint8_t conn_id);

**Parameters**

conn_id: connection ID of targeted device to update connection
parameters.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Update the connected device with new connection parameters such as
connection interval, slave latency and timeout values. The connected
device may reject the new values if it is unable to conform to them.

“BLEConnect.h” must be included to use the class function.

**BLEConnect::getConnInfo**

**Description**

Get connection information.

**Syntax**

bool getConnInfo(uint8_t connId, T_GAP_CONN_INFO \*pConnInfo);

**Parameters**

connId: connection ID to device get connection information from

pConnInfo: pointer to T_GAP_CONN_INFO structure to store obtained
connection information

**Returns**

This function returns true if the connection information is successfully
obtained. Otherwise, false.

**Example Code**

NA

**Notes and Warnings**

“BLEConnect.h” must be included to use the class function.

**BLEConnect::getConnAddr**

**Description**

Get the Bluetooth address for a certain connection.

**Syntax**

bool getConnAddr(uint8_t connId, uint8_t\* addr, uint8_t\* addrType);

**Parameters**

connId: connection ID of device to get Bluetooth address of

addr: pointer to 6 byte array to store retrieved Bluetooth address

addrType: pointer to uint8_t variable to store retrieved Bluetooth
address type

**Returns**

This function returns true if the connection address information is
successfully obtained. Otherwise, false.

**Example Code**

NA

**Notes and Warnings**

“BLEConnect.h” must be included to use the class function.

**BLEConnect::getConnId**

**Description**

Get the connection ID for a certain device.

**Syntax**

int8_t getConnId(char\* btAddr, uint8_t addrType);

int8_t getConnId(uint8_t\* btAddr, uint8_t addrType);

int8_t getConnId(BLEAdvertData targetDevice);

**Parameters**

char\* btAddr: targeted device Bluetooth address expressed as a
character string.

uint8_t\* btAddr: pointer to a 6-byte array containing targeted device
Bluetooth address.

targetDevice: advertising data packet scanned from targeted device.

addrType: Bluetooth address type of targeted device. Valid values:

-  GAP_REMOTE_ADDR_LE_PUBLIC

-  GAP_REMOTE_ADDR_LE_RANDOM

**Returns**

This function returns the requested connection ID. Else, returns -1 if
failed to obtain connection ID.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

“BLEConnect.h” must be included to use the class function.
