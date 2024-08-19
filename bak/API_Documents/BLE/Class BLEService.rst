**BLEService Class**

**Description**

A class used for creating and managing BLE GATT services.

**Syntax**

class BLEService

**Members**

**Public Constructors**

+------------------------------+---------------------------------------+
| BLEService::BLEService       | Constructs a BLEService object        |
+==============================+=======================================+
+------------------------------+---------------------------------------+

**Public Methods**

+------------------------------------+---------------------------------+
| BLEService::setUUID                | Set service UUID                |
+====================================+=================================+
| BLEService::getUUID                | Get service UUID                |
+------------------------------------+---------------------------------+
| BLEService::addCharacteristic      | Add a characteristic to service |
+------------------------------------+---------------------------------+
| BLEService::getCharacteristic      | Get a previously added          |
|                                    | characteristic                  |
+------------------------------------+---------------------------------+


**BLEService::BLEService**

**Description**

Constructs a BLEService object.

**Syntax**

BLEService(BLEUUID uuid);

BLEService(const char\* uuid);

**Parameters**

uuid: service UUID, expressed as a BLEUUID class object or a character
array

**Returns**

NA

**Example Code**

Example: BLEUartService

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLEService.h” must be included to use the class function.

**BLEService::setUUID**

**Description**

Set the service UUID.

**Syntax**

void setUUID(BLEUUID uuid);

**Parameters**

uuid: service UUID, expressed as a BLEUUID class object.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEService.h” must be included to use the class function.

**BLEService::getUUID**

**Description**

Get the service UUID.

**Syntax**

BLEUUID getUUID(void);

**Parameters**

NA

**Returns**

This function returns the service UUID in a BLEUUID class object.

**Example Code**

NA

**Notes and Warnings**

“BLEService.h” must be included to use the class function.

**BLE::addCharacteristic**

**Description**

Add a characteristic to the service.

**Syntax**

void addCharacteristic(BLECharacteristic& newChar);

**Parameters**

newChar: the BLECharacteristic to add to the service.

**Returns**

NA

**Example Code**

Example: BLEUartService

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEUartService/BLEUartService.ino)

**Notes and Warnings**

“BLEService.h” must be included to use the class function.

**BLE::getCharacteristic**

**Description**

Get a previously added characteristic.

**Syntax**

BLECharacteristic\* getCharacteristic(uint8_t charIndex);

**Parameters**

charIndex: position index of characteristic.

**Returns**

This function returns a pointer to the BLECharacteristic at the
requested position index else return NULL.

**Example Code**

NA

**Notes and Warnings**

“BLEService.h” must be included to use the class function.
