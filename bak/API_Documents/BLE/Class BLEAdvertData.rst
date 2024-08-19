**BLEAdvertData Class**

**Description**

A class used for managing BLE advertising data.

**Syntax**

class BLEAdvertData

**Members**

**Public Constructors**

+---------------------------------+------------------------------------+
| BLEAdvertData::BLEAdvertData    | Constructs a BLEAdvertData object  |
+=================================+====================================+
+---------------------------------+------------------------------------+

**Public Methods**

+---------------------------------+------------------------------------+
| BLEAdvertData::clear            | Clear all advertising data.        |
+=================================+====================================+
| BLEAdvertData::addData          | Add binary data to advertising     |
|                                 | data packet.                       |
+---------------------------------+------------------------------------+
| BLEAdvertData::addFlags         | Add flags to advertising data      |
|                                 | packet.                            |
+---------------------------------+------------------------------------+
| BL                              | Add partial list of service UUIDs  |
| EAdvertData::addPartialServices | to advertising data packet.        |
+---------------------------------+------------------------------------+
| BLEAdvertData::                 | Add complete service UUIDs to      |
| addCompleteServices             | advertising data packet.           |
+---------------------------------+------------------------------------+
| BLEAdvertData::addAppearance    | Add device appearance to           |
|                                 | advertising data packet.           |
+---------------------------------+------------------------------------+
| BLEAdvertData::addShortName     | Add shortened device name to       |
|                                 | advertising data packet.           |
+---------------------------------+------------------------------------+
| BLEAdvertData::addCompleteName  | Add complete device name to        |
|                                 | advertising data packet.           |
+---------------------------------+------------------------------------+
| BLEAdvertData::parseScanInfo    | Parse advertising data packets     |
|                                 | received from a scan.              |
+---------------------------------+------------------------------------+
| BLEAdvertData::hasFlags         | Check if received data includes    |
|                                 | advertising flags.                 |
+---------------------------------+------------------------------------+
| BLEAdvertData::hasUUID          | Check if received data includes    |
|                                 | service UUIDs.                     |
+---------------------------------+------------------------------------+
| BLEAdvertData::hasName          | Check if received data includes    |
|                                 | device name.                       |
+---------------------------------+------------------------------------+
| BLEAdvertData::hasManufacturer  | Check if received data includes    |
|                                 | manufacturer data.                 |
+---------------------------------+------------------------------------+
| BLEAdvertData::getAdvType       | Get advertising type of received   |
|                                 | data.                              |
+---------------------------------+------------------------------------+
| BLEAdvertData::getAddrType      | Get Bluetooth address type of      |
|                                 | received data.                     |
+---------------------------------+------------------------------------+
| BLEAdvertData::getAddr          | Get Bluetooth address of received  |
|                                 | data.                              |
+---------------------------------+------------------------------------+
| BLEAdvertData::getRSSI          | Get received signal strength       |
|                                 | indicator (RSSI) of received data. |
+---------------------------------+------------------------------------+
| BLEAdvertData::getFlags         | Get advertising flags of received  |
|                                 | data                               |
+---------------------------------+------------------------------------+
| BLEAdvertData::getServiceCount  | Get the total number of advertised |
|                                 | services in the received data.     |
+---------------------------------+------------------------------------+
| BLEAdvertData::getServiceList   | Get a list of advertised service   |
|                                 | UUIDs in received data.            |
+---------------------------------+------------------------------------+
| BLEAdvertData::getName          | Get advertised device name in      |
|                                 | received data.                     |
+---------------------------------+------------------------------------+
| BLEAdvertData::getTxPower       | Get the advertised transmission    |
|                                 | power from received data.          |
+---------------------------------+------------------------------------+
| BLEAdvertData::getAppearance    | Get advertised device appearance   |
|                                 | in received data.                  |
+---------------------------------+------------------------------------+
| BLEAdvertData::getManufacturer  | Get advertised manufacturer in     |
|                                 | received data.                     |
+---------------------------------+------------------------------------+
| BLEAdvert                       | Get length of manufacturer data in |
| Data::getManufacturerDataLength | received data.                     |
+---------------------------------+------------------------------------+
| BLE                             | Get advertised manufacturer data   |
| AdvertData::getManufacturerData | in received data.                  |
+---------------------------------+------------------------------------+


**BLEAdvertData::BLEAdvertData**

**Description**

Constructs a BLEAdvertData object.

**Syntax**

BLEAdvertData(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

This class is used for managing BLE advertising data for two primary
uses. First is to assemble advertising data for broadcasting as
advertising packets. Second is to process and split up the advertising
data received from a scan into separate types.

“BLEAdvertData.h” must be included to use the class function.


**BLEAdvertData::clear**

**Description**

Clear all advertising data.

**Syntax**

void clear(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::addData**

**Description**

Add binary data to advertising data packet.

**Syntax**

void addData(const uint8_t\* data, uint8_t size);

**Parameters**

data: pointer to array containing desired advertising data

size: number of bytes in the array

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

This function is provided for flexibility in adding BLE advertising
data. Other functions should be used for adding advertising data, if
possible, as this function does not perform any checks on the validity
of the data.

“BLEAdvertData.h” must be included to use the class function.


**BLEAdvertData::addFlags**

**Description**

Add flags to advertising data packet.

**Syntax**

uint8_t addFlags(uint8_t flags);

**Parameters**

flags: desired flags to add to advertising data. Default value:
(GAP_ADTYPE_FLAGS_LIMITED \| GAP_ADTYPE_FLAGS_BREDR_NOT_SUPPORTED)

Valid values:

-  GAP_ADTYPE_FLAGS_LIMITED: LE Limited Discoverable Mode.

-  GAP_ADTYPE_FLAGS_GENERAL: LE General Discoverable Mode.

-  GAP_ADTYPE_FLAGS_BREDR_NOT_SUPPORTED: BR/EDR Not Supported.

-  GAP_ADTYPE_FLAGS_SIMULTANEOUS_LE_BREDR_CONTROLLER: Simultaneous LE
   and BR/EDR Controller Supported.

-  GAP_ADTYPE_FLAGS_SIMULTANEOUS_LE_BREDR_HOST: Simultaneous LE and
   BR/EDR Host Supported.

**Returns**

This function returns the current total size of advertising data.

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::addPartialServices**

**Description**

Add partial list of service UUIDs to advertising data packet.

**Syntax**

uint8_t addPartialServices(BLEUUID uuid);

**Parameters**

uuid: the desired UUID contained in BLEUUID class object.

**Returns**

This function returns the current total size of the advertising data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.


**BLEAdvertData:: addCompleteServices**

**Description**

Add complete list of service UUIDs to advertising data packet.

**Syntax**

uint8_t addCompleteServices(BLEUUID uuid);

uint8_t addCompleteServices(uint8_t uuidBitLength);

**Parameters**

uuid: the desired UUID contained in BLEUUID class object.

uuidBitLength: UUID bit length for which a blank entry is to be added.
Valid values: 16, 32, 128.

**Returns**

This function returns the current total size of the advertising data.

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

uuidBitLength is used when a blank entry in the advertisement data is
required to be present. It is to indicate that no services with UUIDs of
a certain length are available.

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::addAppearance**

**Description**

Add device appearance to advertising data.

**Syntax**

uint8_t addAppearance(uint16_t appearance);

**Parameters**

appearance: the desired device appearance.

**Returns**

This function returns the current total size of the advertising data.

**Example Code**

Example: BLEHIDGamepad
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

**Notes and Warnings**

Refer to “gap_le_types.h” or Bluetooth specifications for a full list of
device appearance values.

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::addShortName**

**Description**

Add shortened device name to advertising data packet.

**Syntax**

uint8_t addShortName(const char\* str);

**Parameters**

str: character string containing desired short device name.

**Returns**

This function returns the current total size of the advertising data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::addCompleteName**

**Description**

Add complete device name to advertising data packet.

**Syntax**

uint8_t addCompleteName(const char\* str);

**Parameters**

str: character string containing desired device name.

**Returns**

This function returns the current total size of the advertising data.

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::parseScanInfo**

**Description**

Parse advertising data packets received from a scan.

**Syntax**

void parseScanInfo(T_LE_CB_DATA \*p_data);

**Parameters**

p_data: pointer to advertising data received from a Bluetooth scan.

**Returns**

NA

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

The information of the received data from advertising data can be
accessed using the member functions starting with “has” and “get”.

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::hasFlags**

**Description**

Check if received data includes advertising flags.

**Syntax**

bool hasFlags(void);

**Parameters**

NA

**Returns**

This function returns true if flags are present in received advertising
data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::hasUUID**

**Description**

Check if received data includes service UUIDs.

**Syntax**

bool hasUUID(void);

**Parameters**

NA

**Returns**

This function returns true if service UUIDs are present in received
advertising data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::hasName**

**Description**

Check if received data includes device name.

**Syntax**

bool hasName(void);

**Parameters**

NA

**Returns**

This function returns true if device name is present in received
advertising data.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::hasManufacturer**

**Description**

Check if received data includes manufacturer data.

**Syntax**

bool hasManufacturer(void);

**Parameters**

NA

**Returns**

This function returns true if manufacturer data is present in the
received advertising data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getAdvType**

**Description**

Get advertising type of received data.

**Syntax**

T_GAP_ADV_EVT_TYPE getAdvType(void);

**Parameters**

NA

**Returns**

This function returns the advertising type of received advertising data.

**Example Code**

NA

**Notes and Warnings**

Possible types:

-  GAP_ADV_EVT_TYPE_UNDIRECTED

-  GAP_ADV_EVT_TYPE_DIRECTED

-  GAP_ADV_EVT_TYPE_SCANNABLE

-  GAP_ADV_EVT_TYPE_NON_CONNECTABEL

-  GAP_ADV_EVT_TYPE_SCAN_RSP

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::getAddrType**

**Description**

Get Bluetooth address type of received data.

**Syntax**

T_GAP_REMOTE_ADDR_TYPE getAddrType(void);

**Parameters**

NA

**Returns**

This function returns the Bluetooth address type of received data.

**Example Code**

NA

**Notes and Warnings**

Possible types:

-  GAP_REMOTE_ADDR_LE_PUBLIC

-  GAP_REMOTE_ADDR_LE_RANDOM

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::getRSSI**

**Description**

Get received signal strength indicator (RSSI) of received data.

**Syntax**

Int8_t getRSSI(void);

**Parameters**

NA

**Returns**

This function returns the received signal strength.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getFlags**

**Description**

Get advertising flags of received data.

**Syntax**

uint8_t getFlags(void);

**Parameters**

NA

**Returns**

This function returns a single byte containing the advertising flags
found in received advertising data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getServiceCount**

**Description**

Get the total number of advertised services in the received data.

**Syntax**

uint8_t getServiceCount(void);

**Parameters**

NA

**Returns**

This function returns the number of advertised service UUIDs in received
data.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getServiceList**

**Description**

Get a list of advertised service UUIDs in received data.

**Syntax**

BLEUUID\* getServiceList(void);

**Parameters**

NA

**Returns**

This function returns a pointer to a BLEUUID array containing all
advertised service UUIDs.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getName**

**Description**

Get advertised device name in received data.

**Syntax**

String getName(void);

**Parameters**

NA

**Returns**

This function returns advertised device name contained in a String class
object

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getTxPower**

**Description**

Get the advertised transmission power of the received data.

**Syntax**

int8_t getTxPower(void);

**Parameters**

NA

**Returns**

This function returns advertised transmission power of the received
data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getAppearance**

**Description**

Get advertised device appearance in received data.

**Syntax**

uint16_t getAppearance(void);

**Parameters**

NA

**Returns**

This function returns advertised device appearance of the received data.

**Example Code**

NA

**Notes and Warnings**

Refer to “gap_le_types.h” or Bluetooth specifications for full list of
device appearance values.

“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::getManufacturer**

**Description**

Get advertised manufacturer in received data.

**Syntax**

uint16_t getManufacturer(void);

**Parameters**

NA

**Returns**

This function returns advertised manufacturer of the received data.

**Example Code**

NA

**Notes and Warnings**

Refer to Bluetooth specifications for full list of manufacturer codes.
“BLEAdvertData.h” must be included to use the class function.

**BLEAdvertData::getManufacturerDataLength**

**Description**

Get length of manufacturer data in received data.

**Syntax**

uint8_t getManufacturerDataLength(void);

**Parameters**

NA

**Returns**

This function returns the number of bytes of manufacturer data present
in received advertising data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.

[STRIKEOUT:
]

**BLEAdvertData::getManufacturerData**

**Description**

Get manufacturer data in received data.

**Syntax**

uint8_t\* getManufacturerData(void);

**Parameters**

NA

**Returns**

This function returns a pointer to an array containing manufacturer
data.

**Example Code**

NA

**Notes and Warnings**

“BLEAdvertData.h” must be included to use the class function.
