**BLERemoteDescriptor Class**

**Description**

A class used for managing BLE GATT descriptors on connected remote
devices.

**Syntax**

class BLERemoteDescriptor

**Members**

**Public Constructors**

No public constructor is available for this class. You can get a pointer
to an instance of this class using
BLERemoteCharacteristic::getDescriptor().

**Public Methods**

+-------------------------+--------------------------------------------+
| BLERe                   | Get the descriptor UUID                    |
| moteDescriptor::getUUID |                                            |
+=========================+============================================+
| BLERemoteD              | Set the size of the internal data buffer   |
| escriptor::setBufferLen |                                            |
+-------------------------+--------------------------------------------+
| BLERemoteD              | Get the current size of the internal data  |
| escriptor::getBufferLen | buffer                                     |
+-------------------------+--------------------------------------------+
| BLERemot                | Read the descriptor data buffer as a       |
| eDescriptor::readString | String object                              |
+-------------------------+--------------------------------------------+
| BLERemo                 | Read the descriptor data buffer as an      |
| teDescriptor::readData8 | unsigned 8-bit integer                     |
+-------------------------+--------------------------------------------+
| BLERemot                | Read the descriptor data buffer as an      |
| eDescriptor::readData16 | unsigned 16-bit integer                    |
+-------------------------+--------------------------------------------+
| BLERemot                | Read the descriptor data buffer as an      |
| eDescriptor::readData32 | unsigned 32-bit integer                    |
+-------------------------+--------------------------------------------+
| BLERemote               | Write data to the descriptor as a String   |
| Descriptor::writeString | object or character array                  |
+-------------------------+--------------------------------------------+
| BLERemot                | Write data to the descriptor as an         |
| eDescriptor::writeData8 | unsigned 8-bit integer                     |
+-------------------------+--------------------------------------------+
| BLERemote               | Write data to the descriptor as an         |
| Descriptor::writeData16 | unsigned 16-bit integer                    |
+-------------------------+--------------------------------------------+
| BLERemote               | Write data to the descriptor as an         |
| Descriptor::writeData32 | unsigned 32-bit integer                    |
+-------------------------+--------------------------------------------+
| BLERe                   | Write data to the descriptor.              |
| moteDescriptor::setData |                                            |
+-------------------------+--------------------------------------------+
| BLERe                   | Get data from the descriptor               |
| moteDescriptor::getData |                                            |
+-------------------------+--------------------------------------------+


**BLERemoteDescriptor::getUUID**

**Description**

Get the descriptor UUID.

**Syntax**

BLEUUID getUUID(void);

**Parameters**

NA

**Returns**

This function returns the descriptor UUID as a BLEUUID class object.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::setBufferLen**

**Description**

Set the size of the internal data buffer of the descriptor.

**Syntax**

void setBufferLen(uint16_t max_len);

**Parameters**

max_len: the size in bytes to resize the internal buffer to

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Descriptor data buffer has a default size of 20 bytes and can be
increased up to 230 bytes. “BLERemoteDescriptor.h” must be included to
use the class function.

**BLERemoteDescriptor::getBufferLen**

**Description**

Get the current size of the descriptor internal buffer.

**Syntax**

uint16_t getBufferLen(void);

**Parameters**

NA

**Returns**

This function returns the current internal buffer size that is set.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::readString**

**Description**

Request for descriptor data from the remote device and read the data in
the buffer, expressed as a String class object.

**Syntax**

String readString(void);

**Parameters**

NA

**Returns**

The function returns the data in the descriptor buffer expressed as a
String class object.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::readData8**

**Description**

Request for descriptor data from the remote device and read the data in
the buffer, expressed as an unsigned 8-bit integer.

**Syntax**

uint8_t readData8(void);

**Parameters**

NA

**Returns**

The function returns the data in the descriptor buffer expressed as a
uint8_t value.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::readData16**

**Description**

Request for descriptor data from the remote device and read the data in
the buffer, expressed as an unsigned 16-bit integer.

**Syntax**

uint16_t readData16(void);

**Parameters**

NA

**Returns**

The function returns the data in the descriptor buffer expressed as a
uint16_t value.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::readData32**

**Description**

Request for descriptor data from the remote device and read the data in
the buffer, expressed as an unsigned 32-bit integer.

**Syntax**

uint32_t readData32(void);

**Parameters**

NA

**Returns**

The function returns the data in the descriptor buffer expressed as a
uint32_t value.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::writeString**

**Description**

Write data to the remote device descriptor as a String object or
character array.

**Syntax**

bool writeString(String str);

bool writeString(const char\* str);

**Parameters**

str: the data to write to the remote descriptor, expressed as a String
class object or a char array.

**Returns**

This function returns TRUE if writing data to remote device descriptor
is successful.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::writeData8**

**Description**

Write data to the remote device descriptor as an unsigned 8-bit integer.

**Syntax**

bool writeData8(uint8_t num);

**Parameters**

num: the data to write to the descriptor buffer expressed as an unsigned
8-bit integer.

**Returns**

This function returns TRUE if writing data to remote device descriptor
is successful.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::writeData16**

**Description**

Write data to the remote device descriptor as an unsigned 16-bit
integer.

**Syntax**

bool writeData16(uint16_t num);

**Parameters**

num: the data to write to the descriptor buffer expressed as an unsigned
16-bit integer.

**Returns**

This function returns TRUE if writing data to remote device descriptor
is successful.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::writeData32**

**Description**

Write data to the remote device descriptor as a 32-bit integer.

**Syntax**

bool writeData32(uint32_t num);

bool writeData32(int num);

**Parameters**

num: the data to write to the descriptor buffer expressed as a 32-bit
integer.

**Returns**

This function returns TRUE if writing data to remote device descriptor
is successful.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::setData**

**Description**

Write data to the descriptor.

**Syntax**

bool setData(uint8_t\* data, uint16_t datalen);

**Parameters**

data: pointer to byte array containing desired data to write

datalen: number of bytes of data to write

**Returns**

This function returns TRUE if writing data to remote device descriptor
is successful.

**Example Code**

NA

**Notes and Warnings**

“BLERemoteDescriptor.h” must be included to use the class function.

**BLERemoteDescriptor::getData**

**Description**

Get the descriptor data from the remote device and read the data in the
buffer.

**Syntax**

uint16_t getData(uint8_t\* data, uint16_t datalen);

**Parameters**

data: pointer to byte array to save data read from buffer

datalen: number of bytes of data to read

**Returns**

The function returns the number of bytes read.

**Example Code**

NA

**Notes and Warnings**

If the data buffer contains less data than requested, it will only read
the available number of bytes of data. “BLERemoteDescriptor.h” must be
included to use the class function.
