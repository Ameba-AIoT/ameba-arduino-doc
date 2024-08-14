BLERemoteCharacteristic Class

Description A class used for managing BLE GATT characteristics on
connected remote devices.

Syntax class BLERemoteCharacteristic

Members

BLERemoteCharacteristic::getDescriptor

Description Get a descriptor with the specified UUID on the remote
device.

Syntax BLERemoteDescriptor\* getDescriptor(const char\* uuid);
BLERemoteDescriptor\* getDescriptor(BLEUUID uuid);

Parameters uuid: the desired descriptor UUID, expressed as a character
array or a BLEUUID object

Returns This function returns the found descriptor as a
BLERemoteDescriptor object pointer, otherwise nullptr is returned if a
descriptor with the UUID is not found.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::getUUID

Description Get the characteristic UUID.

Syntax BLEUUID getUUID(void);

Parameters NA

Returns The function returns the characteristic UUID as a BLEUUID class
object.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::setBufferLen

Description Set the size of the internal data buffer of the
characteristic.

Syntax void setBufferLen(uint16_t max_len);

Parameters max_len: the size in bytes to resize the internal buffer to

Returns NA

Example Code Example: BLEUartClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartClient/BLEUartClient.ino)

Notes and Warnings Characteristic data buffer has a default size of 20
bytes and can be increased up to 230 bytes. “BLERemoteCharacteristic.h”
must be included to use the class function.

BLERemoteCharacteristic::getBufferLen

Description Get the current size of the characteristic internal buffer.

Syntax uint16_t getBufferLen(void);

Parameters NA

Returns This function returns the current internal buffer size that is
set.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::canRead

Description Determine if characteristic has read property enabled.

Syntax bool canRead(void);

Parameters NA

Returns This function returns TRUE if the read property for the
characteristic is enabled.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::canWrite

Description Determine if characteristic has write property enabled.

Syntax bool canWrite(void);

Parameters NA

Returns This function returns TRUE if the write property or the write no
response property for the characteristic is enabled.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::canNotify

Description Determine if characteristic has notify property enabled.

Syntax bool canNotify(void);

Parameters NA

Returns The function returns TRUE if the notify property for the
characteristic is enabled.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::canIndicate

Description Determine if characteristic has indicate property enabled.

Syntax bool canIndicate(void);

Parameters NA

Returns The function returns TRUE if the indicate property for the
characteristic is enabled.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::getProperties

Description Get the characteristic properties.

Syntax uint16_t getProperties(void);

Parameters NA

Returns The function returns the characteristic properties.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::readString

Description Request for characteristic data from the remote device and
read the data in the buffer, expressed as a String class object.

Syntax String readString(void);

Parameters NA

Returns The function returns the data in the characteristic data buffer
expressed as a String class object.

Example Code Example: BLEUartClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartClient/BLEUartClient.ino)

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::readData8

Description Request for characteristic data from the remote device and
read the data in the buffer, expressed as an unsigned 8-bit integer.

Syntax uint8_t readData8(void);

Parameters NA

Returns This function returns the data in the characteristic data buffer
expressed as a uint8_t value.

Example Code Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::readData16

Description Request for characteristic data from the remote device and
read the data in the buffer, expressed as an unsigned 16-bit integer.

Syntax uint16_t readData16(void);

Parameters NA

Returns This function returns the data in the characteristic data buffer
expressed as a uint16_t value.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::readData32

Description Request for characteristic data from the remote device and
read the data in the buffer, expressed as an unsigned 32-bit integer.

Syntax uint32_t readData32(void);

Parameters NA

Returns This function returns the data in the characteristic data buffer
expressed as a uint32_t value.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::writeString

Description Write data to the remote device characteristic as a String
object or character array.

Syntax bool writeString(String str); bool writeString(const char\* str);

Parameters str: the data to write to the remote characteristic,
expressed as a String class object or a char array.

Returns This function returns TRUE if writing data to the remote device
characteristic is successful.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::writeData8

Description Write data to the remote device characteristic as an
unsigned 8-bit integer.

Syntax bool writeData8(uint8_t num);

Parameters num: the data to write to the characteristic buffer expressed
as an unsigned 8-bit integer.

Returns This function returns TRUE if writing data to the remote device
characteristic is successful.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::writeData16

Description Write data to the remote device characteristic as an
unsigned 16-bit integer.

Syntax bool writeData16(uint16_t num);

Parameters num: the data to write to the characteristic buffer expressed
as an unsigned 16-bit integer.

Returns This function returns TRUE if writing data to the remote device
characteristic is successful.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::writeData32

Description Write data to the remote device characteristic as a 32-bit
integer.

Syntax bool writeData32(uint32_t num); bool writeData32(int num);

Parameters num: the data to write to the characteristic buffer expressed
as a 32-bit integer.

Returns This function returns TRUE if writing data to the remote device
characteristic is successful.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::setData

Description Write data to the remote device characteristic.

Syntax bool setData(uint8_t\* data, uint16_t datalen);

Parameters data: pointer to byte array containing desired data datalen:
number of bytes of data to write

Returns This function returns TRUE if writing data to the remote device
characteristic is successful.

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::getData

Description Get the characteristic data from the remote device and read
the data in the buffer.

Syntax uint16_t getData (uint8_t\* data, uint16_t datalen);

Parameters data: pointer to byte array to save data read from buffer
datalen: number of bytes of data to read

Returns This function returns the number of bytes read.

Example Code NA

Notes and Warnings If the data buffer contains less data than requested,
it will only read the available number of bytes of data.
“BLERemoteCharacteristic.h” must be included to use the class function.

BLERemoteCharacteristic::enableNotifyIndicate

Description Enable the remote device to send notifications or
indications for the characteristic.

Syntax void enableNotifyIndicate(bool notify);

Parameters notify: TRUE to enable notifications, FALSE to enable
indications. Default value: “1” – True.

Returns NA

Example Code Example: BLEUartClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartClient/BLEUartClient.ino)

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::disableNotifyIndicate

Description Disable receiving notifications and indications for the
characteristic from the remote device.

Syntax void disableNotifyIndicate(void);

Parameters

NA

Returns NA

Example Code NA

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.

BLERemoteCharacteristic::setNotifyCallback

Description Set a user function to be called when the characteristic
receives a notification from the remote device.

Syntax void setNotifyCallback(void (\*fCallback)
(BLERemoteCharacteristic\* chr, uint8_t\* data, uint16_t length));

Parameters fCallback: A user callback function that returns void and
takes three arguments. chr: pointer to BLERemoteCharacteristic object
associated with notification. data: pointer to byte array containing
notification data. length: number of bytes of notification data in
array.

Returns NA

Example Code Example: BLEUartClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartClient/BLEUartClient.ino)

Notes and Warnings “BLERemoteCharacteristic.h” must be included to use
the class function.
