Class SoftwareSerial
====================

**SoftwareSerial Class**
------------------------

**Description**
~~~~~~~~~~~~~~~

A class for software serial implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class SoftwareSerial

**Members**
~~~~~~~~~~~

+----------------------------------+----------------------------------+
| **Public Constructors**                                             |
+==================================+==================================+
| SoftwareSerial::SoftwareSerial   | Constructs a SoftwareSerial      |
|                                  | object                           |
+----------------------------------+----------------------------------+
| **Public Methods**                                                  |
+----------------------------------+----------------------------------+
| SoftwareSerial::begin            | Initialize and Sets the speed    |
|                                  | (baud rate) for the              |
|                                  | serial communication             |
+----------------------------------+----------------------------------+
| SoftwareSerial::listen           | Enables the selected software    |
|                                  | serial port to listen            |
+----------------------------------+----------------------------------+
| SoftwareSerial::end              | Deinitialize the serial          |
|                                  | communication                    |
+----------------------------------+----------------------------------+
| SoftwareSerial::stopListening    | Check if requested software      |
|                                  | serial port is actively listening|
+----------------------------------+----------------------------------+
| SoftwareSerial::peek             | Get a character that was         |
|                                  | received on the RX pin of the    |
|                                  | software serial port             |
+----------------------------------+----------------------------------+
| SoftwareSerial::write            | Send a single byte to the        |
|                                  | transmit pin of the software     |
|                                  | serial port as raw bytes         |
+----------------------------------+----------------------------------+
| SoftwareSerial::read             | Read data that was received      |
|                                  | from RX pin of the               |
|                                  | software serial port             |
+----------------------------------+----------------------------------+
| SoftwareSerial::available        | Get the number of bytes          |
|                                  | (characters) available for       |
|                                  | reading from a software serial   |
|                                  | port                             |
+----------------------------------+----------------------------------+
| SoftwareSerial::flush            | Clear the received buffer        |
+----------------------------------+----------------------------------+
| SoftwareSerial::setBufferSize    | Set receive buffer size          |
+----------------------------------+----------------------------------+
| Soft                             | Set available callback functions |
| wareSerial::setAvailableCallback |                                  |
+----------------------------------+----------------------------------+
| SoftwareSerial::handle_interrupt | Private methods handles          |
|                                  | interrupt                        |
+----------------------------------+----------------------------------+

--------------------------------------

**SoftwareSerial::SoftwareSerial**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a SoftwareSerial object and sets RX and TX pin, and inverse logic.

**Syntax**
~~~~~~~~~~

.. code:: c++

  SoftwareSerial(uint8_t receivePin, uint8_t transmitPin, bool inverse_logic);

**Parameters**
~~~~~~~~~~~~~~

``receivePin``: the pin on which to receive serial data

``transmitPin``: the pin on which to transmit serial data

``inverse_logic``: used to invert the sense of incoming bits (the default is normal logic). If set, SoftwareSerial treats a LOW (0v on the pin, normally) on the RX pin as a 1-bit (the idle state) and a HIGH (5V on the pin, normally) as a 0-bit. It also affects the way that it writes to the TX pin. (Default: False)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SoftwareSerial_Basic <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/SoftwareSerial_Basic/SoftwareSerial_Basic.ino>`_

.. Caution :: Software Serial is using hardware serial thus DO NOT change the default pins.

.. note :: "SoftwareSerial.h" must be included to use the class function.

-----------------------------

**SoftwareSerial::begin**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize and set the speed (baud rate) for the serial communication.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void begin (long speed);

.. code:: c++

  void begin (long speed, int data_bits, int parity, int stop_bits);

.. code:: c++

  void begin (long speed, int data_bits, int parity, int stop_bits, int flowctrl, int rtsPin, int ctsPin);

**Parameters**
~~~~~~~~~~~~~~

``speed``: the desired baud rate (long). Supported baud rates are: 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 31250, 38400, 57600, and 115200 bauds.

``data_bits``: number of data bits, 8 bits(default) or 7 bits

``stop_bits``: number of stop bits, 1 bit(default), 1.5 bits or 2 bits

``flowctrl``: flow control pin

``rtsPin``: request to send pin

``ctsPin``: clear to send pin

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SoftwareSerial_Basic <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/SoftwareSerial_Basic/SoftwareSerial_Basic.ino>`_

.. note :: "SoftwareSerial.h" must be included to use the class function.

------------------------------------

**SoftwareSerial::listen**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Enables the selected software serial port to listen. Only one SoftwareSerial object can listen at a time; data that arrives for other ports will be discarded. Any data already received is discarded during the call to listen() function (unless the given instance is already listening).

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool listen(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if it is listening, otherwise false.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

-------------------------

**SoftwareSerial::end**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Deinitialize the serial communication by deallocate the receiving buffer.

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

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

--------------------------------------------

**SoftwareSerial::isListening**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Check if requested software serial port is actively listening.

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool isListening(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "True" if the port is actively listening, otherwise returns "False".

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

----------------------------------------

**SoftwareSerial::stopListening**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Selected software serial port stop listening.

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool stopListening(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "True" if the selected software serial port stop listening.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

--------------------------

**SoftwareSerial::peek**
------------------------

**Description**
~~~~~~~~~~~~~~~

Get a character that was received on the RX pin of the software serial port.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the head data read from the receiving buffer or returns "-1" if none is available.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

------------------------------------

**SoftwareSerial::write**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Send a single byte to the transmit pin of the software serial port as raw bytes with 10ms timeout.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual size_t write(uint8_t byte);

**Parameters**
~~~~~~~~~~~~~~

``byte``: data to be sent in 8-bit

**Returns**
~~~~~~~~~~~

This function returns the number of bytes written.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SoftwareSerial_Basic <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/SoftwareSerial_Basic/SoftwareSerial_Basic.ino>`_

.. note :: "SoftwareSerial.h" must be included to use the class function.

----------------------------

**SoftwareSerial::read**
------------------------

**Description**
~~~~~~~~~~~~~~~

Read data that was received from RX pin of the software serial port.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual int read(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the byte read or returns -1 if none is available.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SoftwareSerial_Basic <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/SoftwareSerial_Basic/SoftwareSerial_Basic.ino>`_

.. note :: "SoftwareSerial.h" must be included to use the class function.

----------------------------

**SoftwareSerial::available**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the number of bytes available for reading from a software serial port.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the number of bytes available in the receive buffer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SoftwareSerial_Basic <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/SoftwareSerial_Basic/SoftwareSerial_Basic.ino>`_

.. note :: "SoftwareSerial.h" must be included to use the class function.

------------------------

**SoftwareSerial::flush**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Clear the received buffer.

**Syntax**
~~~~~~~~~~

.. code:: c++

  virtual void flush(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

---------------------------------------

**SoftwareSerial::setBufferSize**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Set buffer size.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void setBufferSize(uint32_t buffer_size)

**Parameters**
~~~~~~~~~~~~~~

``buffer_size``: the size of the receive buffer

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "SoftwareSerial.h" must be included to use the class function.

-----------------------------------

**SoftwareSerial::setAvailableCallback**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set available callback

**Syntax**
~~~~~~~~~~

.. code:: c++

  void setAvailableCallback(void (*callback)(char c))

**Parameters**
~~~~~~~~~~~~~~

``*callback``: user-defined serial callback function

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SoftwareSerialIrqCallback <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/SoftwareSerial_IRQ_Callback/SoftwareSerial_IRQ_Callback.ino>`__

.. note :: "SoftwareSerial.h" must be included to use the class function.
