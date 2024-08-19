**SPISettings Class**

| **Description**
| A class to set SPI parameters.

| **Syntax**
| class SPISettings

**Members**

+-------------------+--------------------------------------------------+
| **Public          |                                                  |
| Constructors**    |                                                  |
+===================+==================================================+
| `SPISet           | Create a SPISettings object and set SPI clock    |
| tings::SPISetting | speed, bit order and data mode                   |
| s <https://www.am |                                                  |
| ebaiot.com/en/rtl |                                                  |
| 8722dm-arduino-ap |                                                  |
| i-spisettings_spi |                                                  |
| class/#SPISetting |                                                  |
| s_SPISettings>`__ |                                                  |
+-------------------+--------------------------------------------------+


**SPISettings::SPISettings**

| **Description**
| Construct an object and configure SPI parameters — clock speed, bit
  order and data mode to the preferred default value.

**Syntax**

SPISettings(uint32_t clock, BitOrder bitOrder, uint8_t dataMode)

| **Parameters**
| clock: SPI clock speed. (Default: 4000000(Hz))
| bitOrder: The bit order of transmitting command/address/data. Select
  between MSBFIRST (MSB: Most Significant Bit) or LSBFIRST (LSB: Least
  Significant Bit). (Default: MSBFIRST)
| dataMode: SPI has four modes: SPI_MODE0, SPI_MODE1, SPI_MODE2,
  SPI_MODE3 that correspond to the four possible clocking
  configurations. (Default: SPI_MODE0)

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| This class seldom used alone, it is always used with
  beginTransaction() as a parameter in SPIClass. “SPI.h” must be
  included to use the class function.


**SPIClass Class**

| **Description**
| A class of SPI implementation for Ameba.

| **Syntax**
| class SPIClass

**Members**

+---------------------------+------------------------------------------+
| **Public Constructors**   |                                          |
+===========================+==========================================+
| `SPIClass::SPI            | Constructs an SPI object                 |
| Class <https://www.amebai |                                          |
| ot.com/en/rtl8722dm-ardui |                                          |
| no-api-spisettings_spicla |                                          |
| ss/#SPIClass_SPIClass>`__ |                                          |
+---------------------------+------------------------------------------+
| **Public Methods**        |                                          |
+---------------------------+------------------------------------------+
| `SPIClas                  | Initialise SPI pins on Ameba board       |
| s::begin <https://www.ame |                                          |
| baiot.com/en/rtl8722dm-ar |                                          |
| duino-api-spisettings_spi |                                          |
| class/#SPIClass_begin>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPIClass::tra            | Transfer data through SPI                |
| nsfer <https://www.amebai |                                          |
| ot.com/en/rtl8722dm-ardui |                                          |
| no-api-spisettings_spicla |                                          |
| ss/#SPIClass_transfer>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPIClass::transfe        | Transfer data of 16-bits through SPI     |
| r16 <https://www.amebaiot |                                          |
| .com/en/rtl8722dm-arduino |                                          |
| -api-spisettings_spiclass |                                          |
| /#SPIClass_transfer16>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPIC                     | Set slave select pin and SPI initial     |
| lass::beginTransaction <h | settings                                 |
| ttps://www.amebaiot.com/e |                                          |
| n/rtl8722dm-arduino-api-s |                                          |
| pisettings_spiclass/#SPIC |                                          |
| lass_beginTransaction>`__ |                                          |
+---------------------------+------------------------------------------+
| `                         | Stop SPI transaction                     |
| SPIClass::endTransaction  |                                          |
| <https://www.amebaiot.com |                                          |
| /en/rtl8722dm-arduino-api |                                          |
| -spisettings_spiclass/#SP |                                          |
| IClass_endTransaction>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPIClass::setBitOrd      | Set bit order to either MSB first or LSB |
| er <https://www.amebaiot. | first                                    |
| com/en/rtl8722dm-arduino- |                                          |
| api-spisettings_spiclass/ |                                          |
| #SPIClass_setBitOrder>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPIClass::setDataMo      | Set data mode                            |
| de <https://www.amebaiot. |                                          |
| com/en/rtl8722dm-arduino- |                                          |
| api-spisettings_spiclass/ |                                          |
| #SPIClass_setDataMode>`__ |                                          |
+---------------------------+------------------------------------------+
| `SP                       | Set to correct clock speed (no effect on |
| IClass::setClockDivider < | Ameba)                                   |
| https://www.amebaiot.com/ |                                          |
| en/rtl8722dm-arduino-api- |                                          |
| spisettings_spiclass/#SPI |                                          |
| Class_setClockDivider>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPIClass::               | Set default SPI frequency                |
| setDefaultFrequency <http |                                          |
| s://www.amebaiot.com/en/r |                                          |
| tl8722dm-arduino-api-spis |                                          |
| ettings_spiclass/#SPIClas |                                          |
| s_setDefaultFrequency>`__ |                                          |
+---------------------------+------------------------------------------+
| `SPI                      | Stop SPI master mode                     |
| Class::end <https://www.a |                                          |
| mebaiot.com/en/rtl8722dm- |                                          |
| arduino-api-spisettings_s |                                          |
| piclass/#SPIClass_end>`__ |                                          |
+---------------------------+------------------------------------------+


**SPIClass::SPIClass**

| **Description**
| Construct an SPI object, create a pointer to the SPI master object,
  and assign “MOSI, MISO, CLK, and SS” to the corresponding pins on
  Ameba boards. Default SPI tranmission frequency is set to 20,000,000
  Hz.

| **Syntax**
| SPIClass(void \*pSpiObj, int mosi, int miso, int clk, int ss);

| **Parameters**
| pSpiObj: A pointer to a structure that stores SPI configuration.

| mosi: Master Out, Slave In, a.k.a. Data transmission from a Host to
  Device.
| miso: Master In, Slave Out, a.k.a. Data transmission from a Device to
  Host.
| clk: Serial Clock. Oscillating signal generated by a Host that keeps
  the transmission of data bits in sync.
| ss: Slave Select. Allows a Host to select individual Device(s)
  connected to the bus in order to send or receive data.
| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| Depending on the Ameba hardware, up to 2 SPIClass objects are created
  in the spi.cpp library, please use “SPI” for first hardware SPI object
  and “SPI1” for the second. “SPI.h” must be included to use the class
  function.


**SPIClass::begin**

| **Description**
| Initialize MOSI, MISO, CLK, and SS pins on Ameba boards, select
  SPIClass object, and set SPI format and frequency.

| **Syntax**
| void begin(void);

void begin(int ss);

| **Parameters**
| ss: Slave Select. Allows a Host to select individual Device(s)
  connected to the bus in order to send or receive data.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| This is a required method to use SPI on Ameba. “SPI.h” must be
  included to use the class function.

**SPIClass::transfer**

| **Description**
| Transfer data through SPI to the slave.

**Syntax**

byte transfer(byte \_pin, uint8_t \_data, SPITransferMode \_mode =
SPI_LAST);

byte transfer(uint8_t \_data, SPITransferMode \_mode = SPI_LAST);

void transfer(byte \_pin, void \*_buf, size_t \_count, SPITransferMode
\_mode = SPI_LAST);

void transfer(void \*_buf, size_t \_count, SPITransferMode \_mode =
SPI_LAST);

| **Parameters**
| \_pin: Slave Select pin
| \_data: Data of 8-bits that transfer from SPI master to the slave

| \_buf: Data buffer stores data to be written to Tx FIFO
| \_mode: defines SS pin status after data transmission is finished,
  available values are SPI_CONTINUE and SPI_LAST. SPI_LAST indicates SS
  pin will be set to 1 upon data transmission ends.
| \_count: number of data bytes to be send

| **Returns**
| This function either returns NA or data of 8-bits that transferred
  through SPI master to the slave.

| **Example Code**
| NA

| **Notes and Warnings**
| “SPI.h” must be included to use the class function.

**SPIClass::transfer16**

**Description**

Transfer data of 16-bits through SPI master to the slave.

| **Syntax**
| uint16_t transfer16(byte \_pin, uint16_t \_data, SPITransferMode
  \_mode = SPI_LAST);

uint16_t transfer16(uint16_t \_data, SPITransferMode \_mode = SPI_LAST);

| **Parameters**
| \_pin: Slave Select pin
| \_data: Data of 16-bits that transfer from SPI master to the slave

\_mode: defines SS pin status after data transmission is finished,
available values are SPI_CONTINUE and SPI_LAST. SPI_LAST indicates SS
pin will be set to 1 upon data transmission ends.

| **Returns**
| This function returns data of 16-bits being transferred.

| **Example Code**
| NA

| **Notes and Warnings**
| “SPI.h” must be included to use the class function.


**SPIClass::beginTransaction**

| **Description**
| Set Slave Select pin and initialize SPI with default settings
  including SPI format, SPI frequency that have been declared in the
  SPISettings class.

| **Syntax**
| void beginTransaction(uint8_t pin, SPISettings settings);

void beginTransaction(SPISettings settings);

| **Parameters**
| pin: Slave Select pin
| settings: an object of SPISettings class defined previously

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| Refer to SPISettings class for details of the initial settings.
  “SPI.h” must be included to use the class function.


**SPIClass::endTransaction**

| **Description**
| Set Slave Select pin to 1 for ending the SPI transaction process.

| **Syntax**
| void endTransaction(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “SPI.h” must be included to use the class function.


**SPIClass::setBitOrder**

| **Description**
| Set bit order to either MSB first or LSB first and set slave select
  pin.

| **Syntax**
| void setBitOrder(uint8_t \_pin, BitOrder \_bitOrder);

void setBitOrder(BitOrder \_order);

| **Parameters**
| \_pin: slave select
| \_bitOrder: The bit order of transmitting command/address/data. Select
  between MSBFIRST (MSB: Most Significant Bit) or LSBFIRST (LSB: Least
  Significant Bit). (Default: MSBFIRST)
| \_order: same as \_bitOrder (Default: MSBFIRST)

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “SPI.h” must be included to use the class function.


**SPIClass::setDataMode**

| **Description**
| Set SPI data mode. A total of 4 modes and set slave select pin.

| **Syntax**
| void SPIClass::setDataMode(uint8_t \_pin, uint8_t \_mode)
| void SPIClass::setDataMode(uint8_t \_mode)

| **Parameters**
| \_pin: Slave Select pin
| \_mode: SPI has four modes: SPI_MODE0, SPI_MODE1, SPI_MODE2, SPI_MODE3
  that correspond to the four possible clocking configurations.
  (Default: SPI_MODE0)

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “SPI.h” must be included to use the class function.


**SPIClass::setClockDivider**

| **Description**
| Set clock divider in order to get correct clock speed.

| **Syntax**
| void setClockDivider(uint8_t \_pin, uint8_t \_divider);

| void setClockDivider(uint8_t \_div);
| **Parameters**
| \_pin: Slave Select pin
| \_divider: clock divider
| \_div: clock divider

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| This function does not affect the Ameba board. “SPI.h” must be
  included to use the class function.


**SPIClass::setDefaultFrequency**

| **Description**
| Set default SPI frequency.

| **Syntax**
| void setDefaultFrequency(int \_frequency);

| **Parameters**
| \_frequency: the default SPI frequency (Default: 20,000,000Hz)

| **Returns**
| NA

| **Example Code**
| Example: ILI9341_TFT_LCD_PM2.5

(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SPI/examples/ILI9341_TFT_LCD_PM2.5/ILI9341_TFT_LCD_PM2.5.ino)

| **Notes and Warnings**
| Take note that defaultFrequency = \_frequency. “SPI.h” must be
  included to use the class function.

**SPIClass::end**

| **Description**
| This function will finish the communication and release all the
  allocated resources to stop SPI master mode.

| **Syntax**
| void end(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| After calling end(), you need to use begin() again to enable SPI
  function. “SPI.h” must be included to use the class function.
