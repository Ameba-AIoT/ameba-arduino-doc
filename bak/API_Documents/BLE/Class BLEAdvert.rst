**BLEAdvert Class**

**Description**

A class used for managing BLE advertising settings.

**Syntax**

class BLEAdvert

**Members**

**Public Constructors**

No public constructor is available as this class is intended to be a
singleton class. You can get a pointer to this class using
BLEDevice::configAdvert().

**Public Methods**

+----------------------------------+-----------------------------------+
| BLEAdvert::updateAdvertParams    | Update the current BLE            |
|                                  | advertisement settings.           |
+==================================+===================================+
| BLEAdvert::startAdv              | Start BLE advertising.            |
+----------------------------------+-----------------------------------+
| BLEAdvert::stopAdv               | Stop BLE advertising.             |
+----------------------------------+-----------------------------------+
| BLEAdvert::setAdvType            | Set the BLE advertising type.     |
+----------------------------------+-----------------------------------+
| BLEAdvert::setMinInterval        | Set the BLE advertising minimum   |
|                                  | interval.                         |
+----------------------------------+-----------------------------------+
| BLEAdvert::setMaxInterval        | Set the BLE advertising maximum   |
|                                  | interval.                         |
+----------------------------------+-----------------------------------+
| BLEAdvert::setAdvData            | Set BLE advertising data.         |
+----------------------------------+-----------------------------------+
| BLEAdvert::setScanRspData        | Set BLE scan response data.       |
+----------------------------------+-----------------------------------+


**BLEAdvert::updateAdvertParams**

**Description**

Update the current BLE advertisement settings.

**Syntax**

void updateAdvertParams(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

Please use the other class member functions to set the BLE advertising
parameters before using this function to update the advert data.

“BLEAdvert.h” must be included to use the class function.


**BLEAdvert::startAdv**

**Description**

Start BLE advertising.

**Syntax**

void startAdv(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

This function gives you more control and flexibility over BLE
advertising parameters. This function should not be used to start the
BLE advertising process without first registering the necessary callback
and handler functions. Call BLEDevice::beginPeripheral() to register the
necessary functions and start advertising for the first time.

“BLEAdvert.h” must be included to use the class function.


**BLEAdvert::stopAdv**

**Description**

Stop BLE advertising.

**Syntax**

void stopAdv(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

This function gives you more control and flexibility over BLE
advertising parameters. This function should not be used to directly
stop the BLE advertising process. Call BLEDevice::end() to stop
advertising and free up used resources.

“BLEAdvert.h” must be included to use the class function.


**BLEAdvert::setAdvType**

**Description**

Set the BLE advertising type.

**Syntax**

void setAdvType(uint8_t advType);

**Parameters**

advType: the desired advertisement type. Valid values:

-  0 = GAP_ADTYPE_ADV_IND : connectable undirected advertisement

-  1 = GAP_ADTYPE_ADV_HDC_DIRECT_IND : connectable high duty cycle
   directed advertisement

-  2 = GAP_ADTYPE_ADV_SCAN_IND : scannable undirected advertisement

-  3 = GAP_ADTYPE_ADV_NONCONN_IND : Non-connectable undirected
   advertisement

-  4 = GAP_ADTYPE_ADV_LDC_DIRECT_IND : connectable low duty cycle
   directed advertisement

**Returns**

NA

**Example Code**

Example: BLEBeacon
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEBeacon/BLEBeacon.ino)

**Notes and Warnings**

If connection requests should be allowed, call this function with
GAP_ADTYPE_ADV_IND. If all connection requests should be rejected, call
this function with GAP_ADTYPE_ADV_NONCONN_IND.

“BLEAdvert.h” must be included to use the class function.


**BLEAdvert::setMinInterval**

**Description**

Set the minimum BLE advertising interval.

**Syntax**

void setMinInterval(uint16_t minInt_ms);

**Parameters**

minInt_ms: the desired advertisement minimum interval, expressed in
milliseconds. The valid values for the interval are from 20ms to
10240ms.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

BLE advertisements will repeat with an interval between the set minimum
and maximum intervals. Set a shorter interval for the BLE device to be
discovered rapidly and set a longer interval to conserve power.

“BLEAdvert.h” must be included to use the class function.

**BLEAdvert::setMaxInterval**

**Description**

Set the maximum BLE advertising interval.

**Syntax**

void setMaxInterval(uint16_t minInt_ms);

**Parameters**

minInt_ms: the desired advertisement maximum interval, expressed in
milliseconds. The valid values for the interval are from 20ms to
10240ms.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

BLE advertisements will repeat with an interval between the set minimum
and maximum intervals. Set a shorter interval for the BLE device to be
discovered rapidly and set a longer interval to conserve power.

“BLEAdvert.h” must be included to use the class function.

**BLEAdvert::setAdvData**

**Description**

Set BLE advertising data.

**Syntax**

void setAdvData(BLEAdvertData adData);

void setAdvData(uint8_t\* pData, uint8_t size);

**Parameters**

adData: advertising data formatted in a BLEAdvertData class object

pData: pointer to a byte array containing the required advertising data.

size: number of bytes the advertising data contains, maximum of 31
bytes.

**Returns**

NA

**Example Code**

Example: BLEWifiConfig
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEWifiConfig/BLEWifiConfig.ino)

**Notes and Warnings**

“BLEAdvert.h” must be included to use the class function.


**BLEAdvert::setScanRspData**

**Description**

Set BLE scan response data.

**Syntax**

void setScanRspData(BLEAdvertData adData);

void setScanRspData(uint8_t\* pData, uint8_t size);

**Parameters**

adData: scan response data formatted in a BLEAdvertData class object

pData: pointer to a byte array containing the required scan response
data.

size: number of bytes the scan response data contains, maximum of 31
bytes.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“BLEAdvert.h” must be included to use the class function.
