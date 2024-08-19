**iBeacon Class**

**Description**

A class used for managing iBeacon BLE advertising data.

**Syntax**

class iBeacon

**Members**

**Public Constructors**

+--------------------------+-------------------------------------------+
| iBeacon::iBeacon         | Constructs an iBeacon object              |
+==========================+===========================================+
|                          |                                           |
+--------------------------+-------------------------------------------+

**Public Methods**

+--------------------------+-------------------------------------------+
| iB                       | Get current manufacturer ID value         |
| eacon::getManufacturerId |                                           |
+==========================+===========================================+
| iBeacon::getUUID         | Get current UUID value                    |
+--------------------------+-------------------------------------------+
| iBeacon::getMajor        | Get current Major value for customizing   |
|                          | beacons                                   |
+--------------------------+-------------------------------------------+
| iBeacon::getMinor        | Get current Minor value for customizing   |
|                          | beacons                                   |
+--------------------------+-------------------------------------------+
| iBeacon::getRSSI         | Get current received signal strength      |
|                          | indicator (RSSI) value                    |
+--------------------------+-------------------------------------------+
| iB                       | Set manufacturer ID value                 |
| eacon::setManufacturerId |                                           |
+--------------------------+-------------------------------------------+
| iBeacon::setUUID         | Set UUID value                            |
+--------------------------+-------------------------------------------+
| iBeacon::setMajor        | Set Major value for customizing beacons   |
+--------------------------+-------------------------------------------+
| iBeacon::setMinor        | Set Minor value for customizing beacons   |
+--------------------------+-------------------------------------------+
| iBeacon::setRSSI         | Set received signal strength indicator    |
|                          | (RSSI) value                              |
+--------------------------+-------------------------------------------+
| iBeacon::getAdvData      | Get current advertising data              |
+--------------------------+-------------------------------------------+
| iBeacon::getScanRsp      | Get current scan response data            |
+--------------------------+-------------------------------------------+

**altBeacon Class**

**Description**

A class used for managing altBeacon BLE advertising data.

**Syntax**

class altBeacon

**Members**

**Public Constructors**

+-------------------------------+--------------------------------------+
| altBeacon::altBeacon          | Constructs an altBeacon object       |
+===============================+======================================+
+-------------------------------+--------------------------------------+

**Public Methods**

+------------------------------+---------------------------------------+
| altBeacon::getManufacturerId | Get current manufacturer ID value     |
+==============================+=======================================+
| altBeacon::getUUID           | Get current UUID value                |
+------------------------------+---------------------------------------+
| altBeacon::getMajor          | Get current Major value for           |
|                              | customizing beacons                   |
+------------------------------+---------------------------------------+
| altBeacon::getMinor          | Get current Minor value for           |
|                              | customizing beacons                   |
+------------------------------+---------------------------------------+
| altBeacon::getRSSI           | Get current received signal strength  |
|                              | indicator (RSSI) value                |
+------------------------------+---------------------------------------+
| altBeacon::getRSVD           | Get current Reserved value            |
+------------------------------+---------------------------------------+
| altBeacon::setManufacturerId | Set manufacturer ID value             |
+------------------------------+---------------------------------------+
| altBeacon::setUUID           | Set UUID value                        |
+------------------------------+---------------------------------------+
| altBeacon::setMajor          | Set Major value for customizing       |
|                              | beacons                               |
+------------------------------+---------------------------------------+
| altBeacon::setMinor          | Set Minor value for customizing       |
|                              | beacons                               |
+------------------------------+---------------------------------------+
| altBeacon::setRSSI           | Set received signal strength          |
|                              | indicator (RSSI) value                |
+------------------------------+---------------------------------------+
| altBeacon::setRSVD           | Set Reserved value                    |
+------------------------------+---------------------------------------+
| altBeacon::getAdvData        | Get current advertising data          |
+------------------------------+---------------------------------------+
| altBeacon::getScanRsp        | Get current scan response data        |
+------------------------------+---------------------------------------+


**iBeacon::iBeacon**

**Description**

Constructs an iBeacon object.

**Syntax**

void iBeacon(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEBeacon.h” must be included to use the class function.\ **

**altBeacon::altBeacon**

**Description**

Constructs an altBeacon object

**Syntax**

void altBeacon(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEBeacon.h” must be included to use the class function.\ **

**iBeacon::getManufacturerId**

**altBeacon::getManufacturerId**

**Description**

Get current Manufacturer ID value.

**Syntax**

uint16_t getManufacturerId(void);

**Parameters**

NA

**Returns**

The function returns a 16-bit unsigned integer containing the current
Company ID.

**Example Code**

NA

**Notes and Warnings**

Refer to
https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers/
for the full list of assigned Bluetooth company identifiers.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::getUUID**

**altBeacon::getUUID**

**Description**

Get the current UUID value.

**Syntax**

void getUUID(uint8_t\* UUID);

**Parameters**

UUID: Provide a pointer to a 16 elements uint8_t array containing
current UUID.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

UUID is a 128-bit number used to uniquely identify a beacon. It is
commonly expressed as a 32-character hexadecimal string. UUIDs can be
generated at https://www.uuidgenerator.net/.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::getMajor**

**altBeacon::getMajor**

**Description**

Get current Major value for customizing beacons.

**Syntax**

uint16_t getMajor(void);

**Parameters**

NA

**Returns**

This function returns a 16-bit unsigned integer containing the current
major value.

**Example Code**

NA

**Notes and Warnings**

Major and Minor are values used for customizing beacons. These can be
set to any value. Refer to https://developer.apple.com/ibeacon/ or
https://altbeacon.org/ for more information.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::getMinor**

**altBeacon::getMinor**

**Description**

Get current Minor value for customizing beacons.

**Syntax**

uint16_t getMinor(void);

**Parameters**

NA

**Returns**

This function returns a 16-bit unsigned integer containing the current
minor value.

**Example Code**

NA

**Notes and Warnings**

Major and Minor are values used for customizing beacons. These can be
set to any value. Refer to https://developer.apple.com/ibeacon/ or
https://altbeacon.org/ for more information.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::getRSSI**

**altBeacon::getRSSI**

**Description**

Get the current received signal strength indicator (RSSI) value.

**Syntax**

int8_t getRSSI(void);

**Parameters**

NA

**Returns**

This function returns an 8-bit signed integer containing the currently
set RSSI value.

**Example Code**

NA

**Notes and Warnings**

The beacon RSSI value is the received signal strength at 1 meter. This
can be used to estimate the distance to the beacon. Refer to
https://developer.apple.com/ibeacon/ or https://altbeacon.org/ for more
information.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::setManufacturerId**

**altBeacon::setManufacturerId**

**Description**

Set Manufacturer ID value.

**Syntax**

void setManufacturerId(uint16_t id);

**Parameters**

id: desired Manufacturer ID

**Returns**

NA

**Example Code**

Example: BLEBeacon
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBeacon/BLEBeacon.ino)

**Notes and Warnings**

Refer to
https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers/
for the full list of assigned Bluetooth company identifiers.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::setUUID**

**altBeacon::setUUID**

**Description**

Set UUID value.

**Syntax**

void setUUID(uint8_t\* UUID);

void setUUID(const char\* UUID);

**Parameters**

uint8_t\* UUID: Provide pointer to a 16 element uint8_t array containing
the desired UUID

const char\* UUID: desired UUID expressed as a character string

**Returns**

NA

**Example Code**

Example: BLEBeacon
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBeacon/BLEBeacon.ino)

**Notes and Warnings**

UUID is a 128-bit number used to uniquely identify a beacon. It is
commonly expressed as a 32-character hexadecimal string. UUIDs can be
generated at https://www.uuidgenerator.net/.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::setMajor**

**altBeacon::setMajor**

**Description**

Set Major value for customizing beacons.

**Syntax**

void setMajor(uint16_t major);

**Parameters**

major: desired Major value

**Returns**

NA

**Example Code**

Example: BLEBeacon
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBeacon/BLEBeacon.ino)

**Notes and Warnings**

Major and Minor are values used for customizing beacons. These can be
set to any value. Refer to https://developer.apple.com/ibeacon/ or
https://altbeacon.org/ for more information.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::setMinor**

**altBeacon::setMinor**

**Description**

Set Minor value for customizing beacons.

**Syntax**

void setMinor(uint16_t minor);

**Parameters**

minor: desired Minor value

**Returns**

NA

**Example Code**

Example: BLEBeacon
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBeacon/BLEBeacon.ino)

**Notes and Warnings**

Major and Minor are values used for customizing beacons. These can be
set to any value. Refer to https://developer.apple.com/ibeacon/ or
https://altbeacon.org/ for more information.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::setRSSI**

**altBeacon::setRSSI**

**Description**

Set RSSI value.

**Syntax**

void setRSSI(int8_t RSSI);

**Parameters**

RSSI: desired RSSI value

**Returns**

NA

**Example Code**

Example: BLEBeacon
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBeacon/BLEBeacon.ino)

**Notes and Warnings**

The beacon RSSI value is the received signal strength at 1 meter. This
can be used to estimate the distance to the beacon. Refer to
https://developer.apple.com/ibeacon/ or https://altbeacon.org/ for more
information.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::getAdvData**

**altBeacon::getAdvData**

**Description**

Get current beacon advertising data.

**Syntax**

uint8_t\* getAdvData(void);

**Parameters**

NA

**Returns**

This function returns a uint8_t pointer to the structure containing
beacon advertising data.

**Example Code**

NA

**Notes and Warnings**

Avoid changing the beacon data through the returned pointer, use the
member functions instead.

“BLEBeacon.h” must be included to use the class function.

**iBeacon::getScanRsp**

**altBeacon::getScanRsp**

**Description**

Get current beacon advertising scan response data.

**Syntax**

uint8_t\* getScanRsp(void);

**Parameters**

NA

**Returns**

This function returns a uint8_t pointer to the structure containing
beacon advertising scan response data.

**Example Code**

NA

**Notes and Warnings**

Avoid changing the beacon data through the returned pointer, use the
member functions instead.

“BLEBeacon.h” must be included to use the class function.

**altBeacon::getRSVD**

**Description**

Get current Reserved value.

**Syntax**

uint8_t getRSVD(void);

**Parameters**

NA

**Returns**

This function returns an 8-bit unsigned integer containing the current
Reserved value.

**Example Code**

NA

**Notes and Warnings**

Reserved for use by the manufacturer to implement special features. The
interpretation of this value is to be defined by the manufacturer and is
to be evaluated based on the MFG ID value. Refer to
https://altbeacon.org/ for more information.

“BLEBeacon.h” must be included to use the class function.

**altBeacon::setRSVD**

**Description**

Set Reserved value.

**Syntax**

void setRSVD(uint8_t rsvd);

**Parameters**

rsvd: desired Reserved value

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Reserved for use by the manufacturer to implement special features. The
interpretation of this value is to be defined by the manufacturer and is
to be evaluated based on the MFG ID value. Refer to
https://altbeacon.org/ for more information.

“BLEBeacon.h” must be included to use the class function.
