**BLECharacteristic Class**

**Description**

A class used for creating and managing BLE GATT characteristics.

**Syntax**

class BLECharacteristic

**Members**

**Public Constructors**

+-------------------------------------+--------------------------------+
| B                                   | Constructs a BLECharacteristic |
| LECharacteristic::BLECharacteristic | object                         |
+=====================================+================================+
+-------------------------------------+--------------------------------+

**Public Methods**

+------------------------------------+---------------------------------+
| BLECharacteristic::setUUID         | Set the UUID of the             |
|                                    | characteristic.                 |
+====================================+=================================+
| BLECharacteristic::getUUID         | Get the UUID of the             |
|                                    | characteristic.                 |
+------------------------------------+---------------------------------+
| BLECharacteristic::setBufferLen    | Set the size of the internal    |
|                                    | data buffer                     |
+------------------------------------+---------------------------------+
| BLECharacteristic::getBufferLen    | Get the current size of the     |
|                                    | internal data buffer            |
+------------------------------------+---------------------------------+
| BLECharacteristic::setReadProperty | Set the Read property value     |
+------------------------------------+---------------------------------+
| B                                  | Set the Write property value    |
| LECharacteristic::setWriteProperty |                                 |
+------------------------------------+---------------------------------+
| BLE                                | Set the write without response  |
| Characteristic::setWriteNRProperty | property value                  |
+------------------------------------+---------------------------------+
| BL                                 | Set the Notify property value   |
| ECharacteristic::setNotifyProperty |                                 |
+------------------------------------+---------------------------------+
| BLEC                               | Set the Indicate property value |
| haracteristic::setIndicateProperty |                                 |
+------------------------------------+---------------------------------+
| BLECharacteristic::setProperties   | Set the characteristic          |
|                                    | properties                      |
+------------------------------------+---------------------------------+
| BLECharacteristic::getProperties   | Get the characteristic          |
|                                    | properties                      |
+------------------------------------+---------------------------------+
| BLE                                | Set the characteristic read     |
| Characteristic::setReadPermissions | permissions                     |
+------------------------------------+---------------------------------+
| BLEC                               | Set the characteristic write    |
| haracteristic::setWritePermissions | permissions                     |
+------------------------------------+---------------------------------+
| BLECharacteristic::setPermissions  | Set the characteristic          |
|                                    | permissions                     |
+------------------------------------+---------------------------------+
| BLECharacteristic::getPermissions  | Get the characteristic          |
|                                    | permissions                     |
+------------------------------------+---------------------------------+
| BLECharacteristic::readString      | Read the characteristic data    |
|                                    | buffer as a String object       |
+------------------------------------+---------------------------------+
| BLECharacteristic::readData8       | Read the characteristic data    |
|                                    | buffer as an unsigned 8-bit     |
|                                    | integer                         |
+------------------------------------+---------------------------------+
| BLECharacteristic::readData16      | Read the characteristic data    |
|                                    | buffer as an unsigned 16-bit    |
|                                    | integer                         |
+------------------------------------+---------------------------------+
| BLECharacteristic::readData32      | Read the characteristic data    |
|                                    | buffer as an unsigned 32-bit    |
|                                    | integer                         |
+------------------------------------+---------------------------------+
| BLECharacteristic::writeString     | Write data to the               |
|                                    | characteristic data buffer as a |
|                                    | String object or character      |
|                                    | array                           |
+------------------------------------+---------------------------------+
| BLECharacteristic::writeData8      | Write data to the               |
|                                    | characteristic data buffer as   |
|                                    | an unsigned 8-bit integer       |
+------------------------------------+---------------------------------+
| BLECharacteristic::writeData16     | Write data to the               |
|                                    | characteristic data buffer as   |
|                                    | an unsigned 16-bit integer      |
+------------------------------------+---------------------------------+
| BLECharacteristic::writeData32     | Write data to the               |
|                                    | characteristic data buffer as   |
|                                    | an unsigned 16-bit integer      |
+------------------------------------+---------------------------------+
| BLECharacteristic::setData         | Write data to the               |
|                                    | characteristic data buffer      |
+------------------------------------+---------------------------------+
| BLECharacteristic::getData         | Read data from the              |
|                                    | characteristic data buffer      |
+------------------------------------+---------------------------------+
| BLECharacteristic::getDataBuff     | Get a pointer to the            |
|                                    | characteristic data buffer      |
+------------------------------------+---------------------------------+
| BLECharacteristic::getDataLen      | Get the length of data (in      |
|                                    | bytes) in the characteristic    |
|                                    | data buffer.                    |
+------------------------------------+---------------------------------+
| BLECharacteristic::notify          | Send a notification to a        |
|                                    | connected device                |
+------------------------------------+---------------------------------+
| BLECharacteristic::indicate        | Send an indication to a         |
|                                    | connected device                |
+------------------------------------+---------------------------------+
| BL                                 | Add a user description          |
| ECharacteristic::setUserDescriptor | descriptor to characteristic    |
+------------------------------------+---------------------------------+
| BLEC                               | Add a data format descriptor to |
| haracteristic::setFormatDescriptor | characteristic                  |
+------------------------------------+---------------------------------+
| BLEChar                            | Add a report reference          |
| acteristic::setReportRefDescriptor | descriptor to a characteristic  |
+------------------------------------+---------------------------------+
| BLECharacteristic::getReportRefID  | Get the previously set report   |
|                                    | reference descriptor ID         |
+------------------------------------+---------------------------------+
| B                                  | Get the previously set report   |
| LECharacteristic::getReportRefType | reference descriptor type       |
+------------------------------------+---------------------------------+
| BLECharacteristic::setReadCallback | Set a user function as a read   |
|                                    | callback                        |
+------------------------------------+---------------------------------+
| B                                  | Set a user function as a write  |
| LECharacteristic::setWriteCallback | callback                        |
+------------------------------------+---------------------------------+
| BLECharacteristic::setCCCDCallback | Set a user function as a CCCD   |
|                                    | write callback                  |
+------------------------------------+---------------------------------+


**BLECharacteristic::BLECharacteristic**

**Description**

Constructs a BLECharacteristic object.

**Syntax**

BLECharacteristic::BLECharacteristic(BLEUUID uuid);

BLECharacteristic::BLECharacteristic(const char\* uuid);

**Parameters**

uuid: characteristic UUID, expressed as a BLEUUID class object or a
character array

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.\ **

**BLECharacteristic::setUUID**

**Description**

Set the UUID of the characteristic.

**Syntax**

void setUUID(BLEUUID uuid);

**Parameters**

uuid: new UUID for the characteristic, expressed as a BLEUUID class
object.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getUUID**

**Description**

Get the UUID of the characteristic.

**Syntax**

BLEUUID getUUID(void);

**Parameters**

NA

**Returns**

The function returns the UUID of the characteristic in a BLEUUID class
object.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setBufferLen**

**Description**

Set the size of the internal data buffer of the characteristic.

**Syntax**

void setBufferLen(uint16_t max_len);

**Parameters**

max_len: the number of bytes that the internal buffer will be resized to

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

Characteristic data buffer has a default size of 20 bytes and can be
increased up to 230 bytes.

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getBufferLen**

**Description**

Get the current size of the internal data buffer of the characteristic.

**Syntax**

uint16_t getBufferLen(void);

**Parameters**

NA

**Returns**

The function returns the currently set internal buffer size.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setReadProperty**

**Description**

Set the Read property value of the characteristic.

**Syntax**

void setReadProperty(bool value);

**Parameters**

value: To allow connected devices to read characteristic’s data. Valid
values: true or false.

**Returns**

NA

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setWriteProperty**

**Description**

Set the Write property value of the characteristic.

**Syntax**

void setWriteProperty(bool value);

**Parameters**

value: To allow connected devices to write characteristic data. Valid
values: true or false.

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setWriteNRProperty**

**Description**

Set the write without response property value of the characteristic.

**Syntax**

void setWriteNRProperty(bool value);

**Parameters**

value: To allow connected devices to write characteristic data with no
response. Valid values: true or false.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.\ **

**BLECharacteristic::setNotifyProperty**

**Description**

Set the Notify property of the characteristic.

**Syntax**

void setNotifyProperty(bool value);

**Parameters**

value: To allow connected devices to receive characteristic data
notification messages. Valid values: true or false.

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

Enabling this property will add a CCCD descriptor to the characteristic.

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setIndicateProperty**

**Description**

Set the Indicate property value of characteristic.

**Syntax**

void setIndicateProperty(bool value);

**Parameters**

value: To allow connected devices to receive characteristic data
indication messages. Valid values: true or false.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Enabling this property will add a CCCD descriptor to the characteristic.

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setProperties**

**Description**

Set the characteristic properties.

**Syntax**

void setProperties(uint8_t value);

**Parameters**

value: desired characteristic properties. Default value: 0x00 (no
properties)

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getProperties**

**Description**

Get characteristic properties that is currently set.

**Syntax**

uint8_t getProperties(void);

**Parameters**

NA

**Returns**

This function returns the currently set characteristic properties
expressed as an unsigned 8-bit integer.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setReadPermissions**

**Description**

Set the characteristic read permissions.

**Syntax**

void setReadPermissions(uint32_t value);

**Parameters**

value: desired characteristic read permissions. Valid values:

-  GATT_PERM_READ

-  GATT_PERM_READ_AUTHEN_REQ

-  GATT_PREM_READ_AUTHOR_REQ

-  GATT_PERM_READ_ENCRYPTED_REQ

-  GATT_PERM_READ_AUTHEN_SC_REQ

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

If no permissions are set, the default permission is GATT_PERM_NONE

“BLECharacteristic.h” must be included to use the class function.\ **

**BLECharacteristic::setWritePermissions**

**Description**

Set the characteristic write permissions.

**Syntax**

void setWritePermissions(uint32_t value);

**Parameters**

value: desired characteristic write permissions. Valid values:

-  GATT_PERM_WRITE

-  GATT_PERM_WRITE_AUTHEN_REQ

-  GATT_PREM_WRITE_AUTHOR_REQ

-  GATT_PERM_WRITE_ENCRYPTED_REQ

-  GATT_PERM_WRITE_AUTHEN_SC_REQ

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

If no permissions are set, the default permission is GATT_PERM_NONE

“BLECharacteristic.h” must be included to use the class function.\ **

**BLECharacteristic::setPermissions**

**Description**

Set the characteristic permissions.

**Syntax**

void setPermissions(uint32_t value);

**Parameters**

value: desired characteristic permissions. Valid values:

-  GATT_PERM_READ

-  GATT_PERM_READ_AUTHEN_REQ

-  GATT_PREM_READ_AUTHOR_REQ

-  GATT_PERM_READ_ENCRYPTED_REQ

-  GATT_PERM_READ_AUTHEN_SC_REQ

-  GATT_PERM_WRITE

-  GATT_PERM_WRITE_AUTHEN_REQ

-  GATT_PREM_WRITE_AUTHOR_REQ

-  GATT_PERM_WRITE_ENCRYPTED_REQ

-  GATT_PERM_WRITE_AUTHEN_SC_REQ

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

If no permissions are set, the default permission is GATT_PERM_NONE

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getPermissions**

**Description**

Get the characteristic permissions.

**Syntax**

uint32_t getPermissions(void);

**Parameters**

NA

**Returns**

This function returns the characteristic permissions that are previously
set using the setReadPermissions, setWritePermissions and setPermissions
functions.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.


**BLECharacteristic::readString**

**Description**

Read the characteristic data buffer as a String object.

**Syntax**

String readString(void);

**Parameters**

NA

**Returns**

The function returns the data in the characteristic internal buffer as a
String class object.

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

Non-ASCII data may result in unexpected characters in the string.

“BLECharacteristic.h” must be included to use the class function.


**BLECharacteristic::readData8**

**Description**

Read the data in the characteristic internal buffer, expressed as an
unsigned 8-bit integer.

**Syntax**

uint8_t readData8(void);

**Parameters**

NA

**Returns**

This function returns the data in the characteristic internal buffer
expressed as a uint8_t value.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::readData16**

**Description**

Read the data in the characteristic internal buffer, expressed as an
unsigned 16-bit integer.

**Syntax**

uint16_t readData16(void);

**Parameters**

NA

**Returns**

This function returns the data in the characteristic internal buffer
expressed as a uint16_t value.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::readData32**

**Description**

Read the data in the characteristic internal buffer, expressed as an
unsigned 32-bit integer.

**Syntax**

uint32_t readData32(void);

**Parameters**

NA

**Returns**

This function returns the data in the characteristic internal buffer
expressed as a uint32_t value.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::writeString**

**Description**

Write data to the characteristic data buffer as a String object or
character array.

**Syntax**

bool writeString(String str);

bool writeString(const char\* str);

**Parameters**

str: the data to write to the characteristic buffer, expressed as a
String class object or a char array.

**Returns**

This function returns TRUE if write data is successful.

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::writeData8**

**Description**

Write data to the characteristic data buffer as an unsigned 8-bit
integer.

**Syntax**

bool writeData8(uint8_t num);

**Parameters**

num: the data to write to the characteristic buffer expressed as an
unsigned 8-bit integer.

**Returns**

This function returns TRUE if write data is successful.

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::writeData16**

**Description**

Write data to the characteristic data buffer as an unsigned 16-bit
integer.

**Syntax**

bool writeData16(uint16_t num);

**Parameters**

num: the data to write to the characteristic buffer expressed as an
unsigned 16-bit integer.

**Returns**

This function returns TRUE if write data is successful.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::writeData32**

**Description**

Write data to the characteristic data buffer as an unsigned 32-bit
integer.

**Syntax**

bool writeData32(uint32_t num);

bool writeData32(int num);

**Parameters**

num: the data to write to the characteristic buffer expressed as a
signed or unsigned 32-bit integer.

**Returns**

This function returns TRUE if write data is successful.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setData**

**Description**

Write data to the characteristic data buffer.

**Syntax**

bool setData(uint8_t\* data, uint16_t datalen);

**Parameters**

data: pointer to byte array containing desired data

datalen: number of bytes of data to write

**Returns**

This function returns TRUE if write data is successful.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getData**

**Description**

Read data from the characteristic data buffer.

**Syntax**

uint16_t getData(uint8_t\* data, uint16_t datalen);

**Parameters**

data: pointer to byte array containing saved data from data buffer

datalen: number of bytes of data to be read

**Returns**

This function returns the number of bytes read.

**Example Code**

NA

**Notes and Warnings**

If the data buffer contains less data than requested, it will only read
the available number of bytes of data.

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getDataBuff**

**Description**

Get a pointer to the characteristic data buffer.

**Syntax**

uint8_t\* getDataBuff(void);

**Parameters**

NA

**Returns**

This function returns a pointer to the uint8_t array used as the
characteristic internal buffer.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::getDataLen**

**Description**

Get the length of data (in bytes) in the characteristic data buffer.

**Syntax**

uint16_t getDataLen(void);

**Parameters**

NA

**Returns**

This function returns the length of the last written data (in bytes) in
the internal data buffer.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::notify**

**Description**

Send a notification to a connected device.

**Syntax**

void notify(uint8_t conn_id);

**Parameters**

conn_id: the connection ID for the device to send a notification to.

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::indicate**

Send an indication to a connected device.

**Syntax**

void indicate(uint8_t conn_id);

**Parameters**

conn_id: the connection ID for the device to send an indication to.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setUserDescriptor**

**Description**

Add a user description descriptor attribute (UUID 0x2901) to the
characteristic.

**Syntax**

void setUserDescriptor(const char\* description);

**Parameters**

description: the desired user description string expressed in a char
array.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setFormatDescriptor**

**Description**

Add a data format descriptor attribute (UUID 0x2904) to the
characteristic.

**Syntax**

void setFormatDescriptor(uint8_t format, uint8_t exponent, uint16_t
unit, uint16_t description);

**Parameters**

format: refer to
https://www.bluetooth.com/specifications/assigned-numbers/format-types/
for the valid values and associated format types.

exponent: base-10 exponent to be applied to characteristic data value

unit: refer to
https://btprodspecificationrefs.blob.core.windows.net/assigned-values/16-bit%20UUID%20Numbers%20Document.pdf
for the valid values and associated units.

description: refer to
https://www.bluetooth.com/specifications/assigned-numbers/gatt-namespace-descriptors/
for the valid values and associated descriptors.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setReportRefDescriptor**

**Description**

Add a HID report reference descriptor attribute (UUID 0x2908) to the
characteristic.

**Syntax**

void setReportRefDescriptor(uint8_t id, uint8_t type);

**Parameters**

id: HID report reference ID

type: HID report type. 0x01 for input report, 0x02 for output report,
0x03 for feature report.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

HID report reference ID should begin at 1. Some HID host systems may
consider an ID of 0 as invalid.

“BLECharacteristic.h” must be included to use the class function.


**BLECharacteristic::getReportRefID**

**Description**

Get the previously set HID report reference descriptor ID.

**Syntax**

uint8_t getReportRefID(void);

**Parameters**

NA

**Returns**

This function returns the report reference ID previously set using the
setReportRefDescriptor function.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.


**BLECharacteristic::getReportRefType**

**Description**

Get the previously set HID report reference descriptor type.

**Syntax**

uint8_t getReportRefType(void);

**Parameters**

NA

**Returns**

This function returns the report reference type previously set using the
setReportRefDescriptor function.

**Example Code**

NA

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.


**BLECharacteristic::setReadCallback**

**Description**

Set a user function to be called when the characteristic data is read by
a connected device.

**Syntax**

void setReadCallback(void (\*fCallback) (BLECharacteristic\* chr,
uint8_t conn_id));

**Parameters**

fCallback: A user callback function that returns void and takes two
arguments.

chr: pointer to BLECharacteristic object containing data read

conn_id: connection ID of connected device that read characteristic data

**Returns**

NA

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setWriteCallback**

**Description**

Set a user function to be called when the characteristic data is written
by a connected device.

**Syntax**

void setWriteCallback(void (\*fCallback) (BLECharacteristic\* chr,
uint8_t conn_id));

**Parameters**

fCallback: A user callback function that returns void and takes two
arguments.

chr: pointer to BLECharacteristic object containing written data.

conn_id: connection ID of connected device that wrote characteristic
data.

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.

**BLECharacteristic::setCCCDCallback**

**Description**

Set a user function to be called when a connected device modifies the
characteristic CCCD to enable or disable notifications or indications.

**Syntax**

void setCCCDCallback(void (\*fCallback) (BLECharacteristic\* chr,
uint8_t conn_id, uint16_t ccc_bits));

**Parameters**

fCallback: A user callback function that returns void and takes two
arguments.

chr: pointer to BLECharacteristic object containing written data.

conn_id: connection ID of connected device that wrote characteristic
data.

ccc_bits: the new CCCD data bits after modification by the connected
device

**Returns**

NA

**Example Code**

Example: BLEUartService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLECharacteristic.h” must be included to use the class function.
