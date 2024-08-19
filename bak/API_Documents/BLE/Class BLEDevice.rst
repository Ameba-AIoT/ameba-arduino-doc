**BLEDevice Class**

**Description**

A class used for general control and management of BLE functions.

**Syntax**

class BLEDevice

**Members**

**Public Constructors**

The public constructor should not be used as this class is intended to
be a singleton class. Access member functions using the object instance
named BLE.

**Public Methods**

+------------------------------+---------------------------------------+
| BLEDevice:: init             | Initialize resources that are         |
|                              | required for BLE to function          |
+==============================+=======================================+
| BLEDevice::deinit            | Deinitialize all the operations for   |
|                              | BLE.                                  |
+------------------------------+---------------------------------------+
| BLEDevice::connected         | Check if a BLE device is connected    |
+------------------------------+---------------------------------------+
| BLEDevice::setDeviceName     | Set BLE Generic Access Profile (GAP)  |
|                              | device name                           |
+------------------------------+---------------------------------------+
| BL                           | Set BLE Generic Access Profile (GAP)  |
| EDevice::setDeviceAppearance | device appearance                     |
+------------------------------+---------------------------------------+
| BLEDevice::configAdvert      | Configure BLE advertising parameters  |
+------------------------------+---------------------------------------+
| BLEDevice::configScan        | Configure BLE scan parameters         |
+------------------------------+---------------------------------------+
| BLEDevice::configConnection  | Configure BLE connection parameters   |
+------------------------------+---------------------------------------+
| BLEDevice::configSecurity    | Configure BLE bonding security        |
|                              | parameters                            |
+------------------------------+---------------------------------------+
| BLEDevice::setScanCallback   | Set callback function for BLE scan    |
|                              | results                               |
+------------------------------+---------------------------------------+
| BLEDevice::beginCentral      | Start BLE stack to operate as a       |
|                              | central device.                       |
+------------------------------+---------------------------------------+
| BLEDevice::beginPeripheral   | Start BLE stack to operate as a       |
|                              | peripheral device.                    |
+------------------------------+---------------------------------------+
| BLEDevice::end               | Stop the operation of BLE stack as a  |
|                              | peripheral or central device.         |
+------------------------------+---------------------------------------+
| BLEDevice::configServer      | Configure BLE stack for services      |
+------------------------------+---------------------------------------+
| BLEDevice::addService        | Add a service to the BLE stack        |
+------------------------------+---------------------------------------+
| BLEDevice::configClient      | Configure BLE stack for clients       |
+------------------------------+---------------------------------------+
| BLEDevice::addClient         | Add a new client to the BLE stack     |
+------------------------------+---------------------------------------+
| BLEDevice::getLocalAddr      | Get local device Bluetooth address    |
+------------------------------+---------------------------------------+


**BLEDevice:: init**

**Description**

Initialize resources that are required for BLE to function.

**Syntax**

void init(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

Call this member function first before using any other member functions
in the BLEDevice class.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::deinit**

**Description**

Deinitialize all the operations for BLE.

**Syntax**

void deinit(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Call this member function last after all other BLE operations have been
terminated.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::connected**

**Description**

Check if a BLE device is connected.

**Syntax**

bool connected(uint8_t connId);

**Parameters**

connId: connection ID to check connection status.

**Returns**

This function returns TRUE if BLE device is connected, otherwise false.

**Example Code**

NA

**Notes and Warnings**

Peripheral mode should use connId = 0

“BLEDevice.h” must be included to use the class function.

**BLEDevice::setDeviceName**

**Description**

Set the BLE Generic Access Profile (GAP) device name which will be
visible after a connection is estabalished. The default device name is
set as “AMEBA_BLE_DEV”.

**Syntax**

void setDeviceName(String devName);

**Parameters**

devName: desired device name expressed as a character string.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

The GAP device name has a maximum length of 39 characters. Other devices
can see this name after a BLE connection is established. This name is
separate and different from the device name sent in a BLE advertisement,
the names should be the same but are not required.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::setDeviceAppearance**

**Description**

Set the BLE Generic Access Profile (GAP) device appearance.

**Syntax**

void setDeviceAppearance(uint16_t devAppearance);

**Parameters**

devAppearance: desired device appearance expressed as a 16-bit unsigned
integer.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Refer to Bluetooth SIG assigned device appearances at
https://www.bluetooth.com/specifications/gatt/characteristics/.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::configAdvert**

**Description**

Configure BLE advertising parameters.

**Syntax**

BLEAdvert\* configAdvert(void);

**Parameters**

NA

**Returns**

This function returns a pointer to a BLEAdvert class instance for
configuring BLE advertising parameters.

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

Use this member function instead of creating a BLEAdvert class instance
manually.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::configScan**

**Description**

Configure BLE scanning parameters.

**Syntax**

BLEScan\* configScan(void);

**Parameters**

NA

**Returns**

This function returns a pointer to a BLEScan class instance for
configuring BLE scanning parameters.

**Example Code**

Example: BLEScan
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino)

**Notes and Warnings**

Use this member function instead of creating a BLEScan class instance
manually.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::configConnection**

**Description**

Configure BLE connection parameters.

**Syntax**

BLEConnect\* configConnection(void);

**Parameters**

NA

**Returns**

This function returns a pointer to a BLEConnect class instance for
configuring BLE connection parameters.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

Use this member function instead of creating a BLEConnect class instance
manually.

“BLEDevice.h” must be included to use the class function.


**BLEDevice::configSecurity**

**Description**

Configure BLE bonding security parameters.

**Syntax**

BLESecurity\* configSecurity(void);

**Parameters**

NA

**Returns**

This function returns a pointer to a BLESecurity class instance for
configuring BLE bonding security parameters.

**Example Code**

Example: BLEHIDMouse
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

**Notes and Warnings**

Use this member function instead of creating a BLESecurity class
instance manually.

“BLEDevice.h” must be included to use the class function.


**BLEDevice::setScanCallback**

**Description**

Set a callback function for processing BLE scan results.

**Syntax**

void setScanCallback(void (\*scanCB)(T_LE_CB_DATA\*));

**Parameters**

scanCB: a function that returns nothing and takes in a scan data pointer
of type T_LE_CB_DATA\*

**Returns**

NA

**Example Code**

Example: BLEScan
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino)

**Notes and Warnings**

Use this member function to set a callback function that will be called
for each BLE device scan result found.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::beginCentral**

**Description**

Start the BLE stack to operate as a central device.

**Syntax**

void beginCentral(uint8_t connCount);

**Parameters**

connCount: maximum number of allowed connected devices. If no argument
is provided, default is maximum allowed connected devices for specific
board.

**Returns**

NA

**Example Code**

Example: BLEScan
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEScan/BLEScan.ino)

**Notes and Warnings**

Use this member function to start the device to operate as a central BLE
device, after other BLE parameters are set correctly.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::beginPeripheral**

**Description**

Start the BLE stack to operate as a peripheral device.

**Syntax**

void beginPeripheral(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

Use this member function to start the device to operate as a peripheral
BLE device, after other BLE parameters are set correctly.

“BLEDevice.h” must be included to use the class function.

**BLEDevice:: end**

**Description**

Stop the operation of BLE stack as a peripheral or central device.

**Syntax**

void end(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Use this member function to stop the device operating in either BLE
peripheral mode or BLE central mode.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::configServer**

**Description**

Configure the BLE stack for services.

**Syntax**

void configServer(uint8_t maxServiceCount);

**Parameters**

maxServiceCount: Maximum number of services that will run on the device

**Returns**

NA

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

Use this member function before adding any service to the BLE stack.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::addService**

**Description**

Add a new service to the BLE stack.

**Syntax**

void addService(BLEService& newService);

**Parameters**

newService: the service to be added, defined using a BLEService class
object.

**Returns**

NA

**Example Code**

Example: BLEBatteryService
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryService/BLEBatteryService.ino)

**Notes and Warnings**

“BLEDevice.h” must be included to use the class function.

**BLEDevice::configClient**

**Description**

Configure the BLE stack for clients.

**Syntax**

void configClient(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

Use this member function before adding any client to the BLE stack.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::addClient**

**Description**

Add a new client to the BLE stack.

**Syntax**

BLEClient\* addClient(uint8_t connId);

**Parameters**

connId: the connection ID of the connected device to create a client
for.

**Returns**

This function returns a pointer to a BLEClient class object,
corresponding to the device with the specified connection ID, which can
be used to access the services and characteristics on the connected
device.

**Example Code**

Example: BLEBatteryClient
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBatteryClient/BLEBatteryClient.ino)

**Notes and Warnings**

Only one client should be added per connected device.

The BLEClient object and any service, characteristic, descriptor
associated with the connected device will be deleted when the device is
disconnected.

“BLEDevice.h” must be included to use the class function.

**BLEDevice::getLocalAddr**

**Description**

Get local device Bluetooth address.

**Syntax**

void getLocalAddr(uint8_t (&addr)[GAP_BD_ADDR_LEN]);

**Parameters**

addr: 6 byte array to store local device Bluetooth address.

GAP_BD_ADDR_LEN: Default Bluetooth device address length of 6 bytes.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Local device address is only available after starting in central or
peripheral mode. This function will return all zeros for the address if
central or peripheral mode is not in operation.

“BLEDevice.h” must be included to use the class function.
