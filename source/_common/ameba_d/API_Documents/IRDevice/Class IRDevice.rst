Class IRDevice
==============

**IRDevice Class**
------------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing, sending, and receiving data using IR (Infra-Red).

**Syntax**
~~~~~~~~~~

.. code:: c++

  class IRDevice

**Members**
~~~~~~~~~~~

+---------------------------+-----------------------------------------+
| **Public Constructors**                                             |
+===========================+=========================================+
| A public constructor should not be used as this class is            |
| intended to be a singleton class. Access member functions using     |
| the object instance named IR.                                       |
+---------------------------+-----------------------------------------+
| **Public Methods**                                                  |
+---------------------------+-----------------------------------------+
| IRDevice::getFreq         | Get the current IR modulation frequency |
+---------------------------+-----------------------------------------+
| IRDevice::begin           | Allocate resources and start the IR     |
|                           | device  with a custom frequency         |
+---------------------------+-----------------------------------------+
| IRDevice::end             | Stop the IR device operations and       |
|                           | free up resources                       |
+---------------------------+-----------------------------------------+
| IRDevice::send            | Send IR raw data                        |
+---------------------------+-----------------------------------------+
| IRDevice::beginNEC        | Allocate resources and start the        |
|                           | IR device with a frequency suitable for |
|                           | the NEC protocol                        |
+---------------------------+-----------------------------------------+
| IRDevice::sendNEC         | Send data using the NEC protocol        |
+---------------------------+-----------------------------------------+
| IRDevice::recvNEC         | Receive data using the NEC protocol     |
+---------------------------+-----------------------------------------+

---------------------------------------------------------------------------------

**IRDevice::getFreq**
---------------------

**Description**
~~~~~~~~~~~~~~~

Get the current IR modulation frequency.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t getFreq(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the IR modulation frequency (in Hz) set currently.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "IRDevice.h" must be included to use the class function.

----------------------------------------------------------------------------------

**IRDevice::begin**
-------------------

**Description**
~~~~~~~~~~~~~~~

Select IR mode as transmitting or receiving mode on IR transmitting or receiving pin. Allocate resources and start the IR device with a custom frequency.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void begin(uint8_t irPin, uint32_t irMode, uint32_t freq);

.. code:: c++

  void begin(uint8_t receivePin, uint8_t transmitPin, uint32_t irMode, uint32_t freq);

**Parameters**
~~~~~~~~~~~~~~

``irPin``: define pin for IR receiver and transmitter if irMode == IR_MODE_TX or IR_MODE_RX.

``receivePin``: Hardware IR receiving pin that connected with the IR Receiver.

``transmitPin``: Hardware IR transmitting pin that connected with the IR Transmistter.

``irMode``: set IR transmit or receive mode. (Valid values: IR_MODE_TX and IR_MODE_RX)

``freq``: modulation frequency for IR signal (in Hz).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: IR device can only operate in either transmit or receive mode. "IRDevice.h" must be included to use the class function.

-------------------------------------

**IRDevice::end**
-----------------

**Description**
~~~~~~~~~~~~~~~

Stop the IR device operations and free up resources allocated to the IR transmitting and receiving pins.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void end(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `IRSendRaw <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/IRDevice/examples/IRSendRAW/IRSendRAW.ino>`_

.. note :: "IRDevice.h" must be included to use the class function.

-----------------------------------

**IRDevice::send**
------------------

**Description**
~~~~~~~~~~~~~~~

Send data by entering customized IR raw data and data length in IR transmission buffer.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void send(const unsigned int buf[ ] , uint16_t len);

**Parameters**
~~~~~~~~~~~~~~

``buf[ ]``: IR raw signals (in us) in an array form.

``len``: total length of the IR raw signal array.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `IRSendRaw <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/IRDevice/examples/IRSendRAW/IRSendRAW.ino>`_

.. note :: "IRDevice.h" must be included to use the class function. IR Raw Data array contains information in the form of consecutive microseconds (us). For more details, please refer to: http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html.

--------------------------------

**IRDevice::beginNEC**
----------------------

**Description**
~~~~~~~~~~~~~~~

Allocate resources and start the IR device with a frequency suitable for the NEC protocol.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void beginNEC(uint8_t receivePin, uint8_t transmitPin, uint32_t irMode);

**Parameters**
~~~~~~~~~~~~~~

``receivePin``: Hardware IR receiving pin that connected with the IR Receiver.

``transmitPin``: Hardware IR transmitting pin that connected with the IR Transmistter.

``irMode``: transmit or receive mode. (Valid values: IR_MODE_TX and IR_MODE_RX).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `IRRecvNEC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/IRDevice/examples/IRRecvNEC/IRRecvNEC.ino>`_

.. note :: "IRDevice.h" must be included to use the class function. IR device can only operate in either transmit or receive mode. Refer to https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol for the NEC protocol.

--------------------------------

**IRDevice::sendNEC**
---------------------

**Description**
~~~~~~~~~~~~~~~

Send data using the NEC protocol.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void sendNEC(uint8_t adr, uint8_t cmd);

**Parameters**
~~~~~~~~~~~~~~

``adr``: 8-bit NEC address data to be transmit

``cmd``: 8-bit NEC command data to be transmit

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `IRSendNEC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/IRDevice/examples/IRSendNEC/IRSendNEC.ino>`_

.. note :: IR device can only operate in either transmit or receive mode. Refer to https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol for the NEC protocol. "IRDevice.h" must be included to use the class function.

---------------------------------

**IRDevice::recvNEC**
---------------------

**Description**
~~~~~~~~~~~~~~~

Receive data using the NEC protocol.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void recvNEC(uint8_t& adr, uint8_t& cmd uint32_t timeout);

**Parameters**
~~~~~~~~~~~~~~

``adr``: 8-bit NEC address data to be transmit

``cmd``: 8-bit NEC command data to be transmit

``timeout``: time duration (in ms) to wait for an incoming transmission

**Returns**
~~~~~~~~~~~

This function returns "1" if data has been received or returns "0" if no data has been received within the timeout period.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `IRRecvNEC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/IRDevice/examples/IRRecvNEC/IRRecvNEC.ino>`_

.. note :: "IRDevice.h" must be included to use the class function. IR device can only operate in either transmit or receive mode. Refer to https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol for the NEC protocol.

