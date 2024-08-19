**BLEHIDDevice Class**

**Description**

A class used for creating and managing HID over GATT Profile (HOGP)
services.

**Syntax**

class BLEHIDDevice

**Members**

**Public Constructors**

The public constructor should not be used as this class is intended to
be a singleton class. Access member functions using the object instance
named BLEHIDDev.

**Public Methods**

+------------------------------------+---------------------------------+
| BLEHIDDevice::init                 | Initialize the HID Device       |
|                                    | Profile by creating the         |
|                                    | required services and           |
|                                    | characteristics                 |
+====================================+=================================+
| BLEHIDDevice::setNumOutputReport   | Set the number of HID output    |
|                                    | reports to be generated.        |
+------------------------------------+---------------------------------+
| BLEHIDDevice::setNumInputReport    | Set the number of HID input     |
|                                    | reports to be generated.        |
+------------------------------------+---------------------------------+
| BLEHIDDevice::setReportMap         | Set the HID report map          |
|                                    | characteristics with a HID      |
|                                    | report descriptor               |
+------------------------------------+---------------------------------+
| BLEHIDDevice::inputReport          | Send a HID input report to      |
|                                    | connected device                |
+------------------------------------+---------------------------------+
| BLE                                | Set a user callback function    |
| HIDDevice::setOutputReportCallback | for receiving HID output        |
|                                    | reports                         |
+------------------------------------+---------------------------------+
| BLEHIDDevice::bootKeyboardReport   | Send a HID boot keyboard input  |
|                                    | report to connected device      |
+------------------------------------+---------------------------------+
| BLEHIDDevice::setHidInfo           | Set HID info of the HID service |
+------------------------------------+---------------------------------+
| BLEHIDDevice::setBattLevel         | Set battery level info of the   |
|                                    | Battery service                 |
+------------------------------------+---------------------------------+
| BLEHIDDevice::setPNPInfo           | Set PNP information of the      |
|                                    | Device Information service      |
+------------------------------------+---------------------------------+
| B                                  | Set manufacturer information of |
| LEHIDDevice::setManufacturerString | the Device Information service  |
+------------------------------------+---------------------------------+
| BLEHIDDevice::setModelString       | Set model information of the    |
|                                    | Device Information service      |
+------------------------------------+---------------------------------+
| BLEHIDDevice::hidService           | Get reference to HID service    |
+------------------------------------+---------------------------------+
| BLEHIDDevice::devInfoService       | Get reference to Device         |
|                                    | Information service             |
+------------------------------------+---------------------------------+
| BLEHIDDevice::battService          | Get reference to Battery        |
|                                    | service                         |
+------------------------------------+---------------------------------+


**BLEHIDDevice::init**

**Description**

Initialize the HID Device profile by creating the required services and
characteristics.

**Syntax**

void init(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEHIDGamepad
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

**Notes and Warnings**

The HID Device object should be initialized before any HID reports can
be sent.

“BLEHIDDevice.h” must be included to use the class function.\ **

**BLEHIDDevice::setNumOutputReport**

**Description**

Set the number of HID output reports to be generated.

**Syntax**

void setNumOutputReport (uint8_t numOutputReports);

**Parameters**

numOutputReports: number of output reports.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

The number of output reports should be set before BLEHIDDevice init()
function is called.The default number of HID output report to be
generated is 1 if it is not set.

“BLEHIDDevice.h” must be included to use the class function.\ **

**BLEHIDDevice::setNumInputReport**

**Description**

Set the number of HID input reports to be generated.

**Syntax**

void setNumInputReport (uint8_t numInputReports);

**Parameters**

numInputReports: number of input reports.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

The number of input reports should be set before BLEHIDDevice init()
function is called.The default number of HID input report to be
generated is 3 if it is not set.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::setReportMap**

**Description**

Set the HID report map characteristics with a HID report descriptor.

**Syntax**

void setReportMap (uint8_t\* report_map, uint16_t len);

**Parameters**

report_map: pointer to HID report descriptor

len: HID report descriptor length in bytes

**Returns**

NA

**Example Code**

Example: BLEHIDGamepad
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDGamepad/BLEHIDGamepad.ino)

**Notes and Warnings**

The HID report map characteristic can only be configured after
BLEHIDDevice init() function is called.

HID report descriptor is a hard coded array of bytes that describe the
device’s data packets. For example, how many packets the device
supports, how large are the packets and the purpose of each byte and bit
in the packets.

For more information on HID report descriptor, refer to
https://eleccelerator.com/tutorial-about-usb-hid-report-descriptors/ .

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::inputReport**

**Description**

Send a HID input report to connected device.

**Syntax**

void inputReport (uint8_t reportID, uint8_t\* data, uint16_t len,
uint8_t conn_id);

**Parameters**

reportID: HID report ID of input report

data: pointer to the HID input report data to be sent

len: length of HID input report data in bytes

conn_id: connection ID of device that the HID report will be sent to

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

HID input reports can only be sent after BLEHIDDevice init() function
has been called.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::setOutputReportCallback**

**Description**

Set a user callback function for receiving HID output report data.

**Syntax**

void setOutputReportCallback (uint8_t reportID, void (\*fCallback)
(BLECharacteristic\* chr, uint8_t conn_id));

**Parameters**

reportID: HID report ID of output report

chr: BLECharacteristic class object containing received HID output
report data

conn_id: connection ID of the device that send out HID report data

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Setting a user callback function for output reports can only occur after
BLEHIDDevice init() function has been called.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::bootKeyboardReport**

**Description**

Send a HID boot keyboard input report to connected device.

**Syntax**

void bootKeyboardReport (uint8_t\* data, uint16_t len, uint8_t conn_id);

**Parameters**

data: pointer to the HID input report data to be sent

len: length of HID input report data in bytes

conn_id: connection ID of device that the HID input report will be sent
to.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

By default, the HID service Protocol Mode characteristic has boot mode
disabled. To send boot keyboard input reports, the Protocol Mode
characteristic needs to have boot mode enabled.

“BLEHIDDevice.h” must be included to use the class function.\ **

**BLEHIDDevice::setHidInfo**

**Description**

Set HID information such as HID class specification version, country
code and flags for HID service.

**Syntax**

void setHidInfo (uint16_t bcd, uint8_t country, uint8_t flags);

**Parameters**

bcd: 16-bit unsigned integer representing version number of base USB HID
Specification implemented by HID Device

country: 8-bit integer identifying country HID Device hardware is
localized for. Most hardware is not localized (value 0x00).

flags: Bit flags indicating remote-wake capability and advertising when
bonded but not connected.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

For detailed information on the characteristic, refer to Bluetooth SIG
HID Service specifications.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::setBattLevel**

**Description**

Set battery level data of the Battery service.

**Syntax**

void setBattLevel (uint8_t level);

**Parameters**

level: battery level expressed as % of full charge

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Battery level is set to 100% by default. For detailed information refer
to Bluetooth SIG Battery service specifications.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::setPNPInfo**

**Description**

Set PNP data of the Device Information service.

**Syntax**

void setPNPInfo (uint8_t sig, uint16_t vid, uint16_t pid, uint16_t
version);

**Parameters**

sig: The Vendor ID Source field designates which organization assigned
the value used in the Vendor ID field value.

vid: The Vendor ID field is intended to uniquely identify the vendor of
the device.

pid: The Product ID field is intended to distinguish between different
products made by the vendor.

version: The Product Version field is a numeric expression identifying
the device release number in Binary-Coded Decimal.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

By default, sig and vid are configured to indicate Realtek as the
vendor. For detailed information refer to Bluetooth SIG Device
Information service specifications.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::setManufacturerString**

**Description**

Set manufacturer information of the Device Information service.

**Syntax**

void setManufacturerString (const char\* manufacturer);

**Parameters**

manufacturer: pointer to character string containing manufacturer name.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Manufacturer is set to “Realtek” by default. For detailed information
refer to Bluetooth SIG Device Information service specifications.

“BLEHIDDevice.h” must be included to use the class function.

**BLEHIDDevice::setModelString**

**Description**

Set model information of the Device Information service.

**Syntax**

void setModelString (const char\* model);

**Parameters**

model: pointer to character string containing device model info.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

Model is set to “Ameba_BLE_HID” by default. For detailed information
refer to Bluetooth SIG Device Information service specifications.

“BLEHIDDevice.h” must be included to use the class function.\ **

**BLEHIDDevice::hidService**

**Description**

Get reference to HID service.

**Syntax**

BLEService& hidService (void);

**Parameters**

NA

**Returns**

This function returns a pointer to the BLEService class object for the
HID service.

**Example Code**

Example: BLEHIDMouse
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

**Notes and Warnings**

“BLEHIDDevice.h” must be included to use the class function.\ **

**BLEHIDDevice::devInfoService**

**Description**

Get reference to Device Information service

**Syntax**

BLEService& devInfoService (void);

**Parameters**

NA

**Returns**

This function returns a pointer to the BLEService class object for the
Device Information service.

**Example Code**

Example: BLEHIDMouse
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

**Notes and Warnings**

“BLEHIDDevice.h” must be included to use the class function.\ **

**BLEHIDDevice::battService**

**Description**

Get reference to Battery service.

**Syntax**

BLEService& battService (void);

**Parameters**

NA

**Returns**

This function returns a pointer to the BLEService class object for the
Battery service.

**Example Code**

Example: BLEHIDMouse
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino)

**Notes and Warnings**

“BLEHIDDevice.h” must be included to use the class function.
