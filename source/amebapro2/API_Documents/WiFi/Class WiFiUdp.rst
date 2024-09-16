Class WiFiUdp
=============

.. contents::
  :local:
  :depth: 2

**WiFiUDP Class**
-----------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing WiFi UDP implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class WiFiUDP

**Members**
~~~~~~~~~~~

+-------------------------------------+-----------------------------------------------+
| **Public Constructors**                                                             |
+=====================================+===============================================+
| WiFiUDP::WiFiUDP                    | Constructs a WiFiUDP instance of the Wi-Fi    |
|                                     | UDP class that can send and receive UDP       |
|                                     | messages.                                     |
+-------------------------------------+-----------------------------------------------+
| **Public Methods**                                                                  |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::begin                      | Initialize Wi-Fi UDP library, network         |
|                                     | settings and start listening at specified     |
|                                     | local port.                                   |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::stop                       | Disconnect from the server.                   |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::beginPacket                | Start building up a packet to send to the     |
|                                     | remote host-specific in IP and port.          |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::endPacket                  | Finish off this packet and send it.           |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::write                      | Write UDP data (single byte) to remote        |
|                                     | connection.                                   |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::write                      | Send packet immediately from the buffer.      |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::parsePacket                | Check for the presence of a UDP packets and   |
|                                     | start processing the next available incoming  |
|                                     | packet.                                       |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::available                  | Get the number of bytes (characters)          |
|                                     | available for reading from the buffer.        |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::read                       | Read UDP data from specified buffer.          |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::peek                       | Get the next byte from the current packet     |
|                                     | without moving on to the next byte.           |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::flush                      | Clear all the bytes that have been written to |
|                                     | the client but not yet read.                  |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::remoteIP                   | Get the IP address of the remote connection   |
|                                     | who sent the current incoming packet.         |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::remotePort                 | Get the port of the remote UDP connection who |
|                                     | sent the current incoming packet.             |
+-------------------------------------+-----------------------------------------------+
| WiFiUDP::setRecvTimeout             | Set receiving timeout.                        |
+-------------------------------------+-----------------------------------------------+

**WiFiUDP::WiFiUDP**
--------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WiFiUDP instance of the Wi-Fi UDP class that can send and receive UDP messages.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    WiFiUDP (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: This constructor does not take in any parameter, thus use another
  method to set up the IP address and port number. "WiFiUdp.h" must be
  included to use the class function.

**WiFiUDP::begin**
------------------

**Description**
~~~~~~~~~~~~~~~

Initialize Wi-Fi UDP library, network settings and start listening at specified local port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual uint8_t begin(uint16_t);

**Parameters**
~~~~~~~~~~~~~~

port: the local port to listen on

**Returns**
~~~~~~~~~~~

This function returns 1 if successful, else returns 0 if there are no
sockets available to use.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::stop**
-----------------

**Description**
~~~~~~~~~~~~~~~

Disconnect from the server. Release any resource being used during the UDP session.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual void stop(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::beginPacket**
------------------------

**Description**
~~~~~~~~~~~~~~~

Start building up a packet to send to the remote host-specific in IP and port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int beginPacket(IPAddress ip, uint16_t port);
    virtual int beginPacket(const char *host, uint16_t port);

**Parameters**
~~~~~~~~~~~~~~

host: remote host name.

port: the port of the remote connection.

ip: IP address of the remote connection.

**Returns**
~~~~~~~~~~~

This function returns "1" of successful, else returns "0" if there is a problem with the given IP address or port.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::endPacket**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Finish off the packet and send it.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int endPacket(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "1" if packet was sent successfully, else returns "0" if there was an error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::write**
------------------

**Description**
~~~~~~~~~~~~~~~

Write UDP data (single byte) to remote connection.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual size_t write(uint8_t);
    virtual size_t write(const uint8_t *buffer, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: a pointer to an array containing the outgoing message.

size: the size of the buffer.

**Returns**
~~~~~~~~~~~

This function returns the byte / character that will be written to the server or the size of the buffer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: This function must be wrapped between beginPacket() and endPacket(). beginPacket() initializes the packet of data, it is not sent until endPacket() is called. "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::writeImmediately**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Send packet immediately from the buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    size_t writeImmediately(const uint8_t *buffer, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: a pointer to an array containing the outgoing message.

size: the size of the buffer.

**Returns**
~~~~~~~~~~~

This function returns the byte / character that will be written to the server or the size of the buffer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::parsePacket**
------------------------

**Description**
~~~~~~~~~~~~~~~

Check for the presence of a UDP packets and start processing the next available incoming packet.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int parsePacket(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the number of bytes available in the current packet, will return "0" if WiFiUDP.parsePacket() hasn't been called yet.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::available**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Get the number of bytes (characters) available for reading from the buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the number of bytes available in the current packet, else returns "0" if WiFiUDP.parsePacket() hasn't been called yet.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: This function can only be successfully called after WiFiUDP.parsePacket(). "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::read**
-----------------

**Description**
~~~~~~~~~~~~~~~

Read UDP data from specified buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int read (void);
    virtual int read (char *buffer, size_t len);

**Parameters**
~~~~~~~~~~~~~~

buf: buffer to hold incoming byte.

size: maximum size of the buffer.

**Returns**
~~~~~~~~~~~

This function returns the size of the buffer or returns -1 if no buffer is available.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: This function can only be successfully called after WiFiUDP.parsePacket(). "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::peek**
-----------------

**Description**
~~~~~~~~~~~~~~~

Get the next byte from the current packet without moving on to the next byte.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual int peek (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next byte or character or returns -1 if none is available.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::flush**
------------------

**Description**
~~~~~~~~~~~~~~~

Clear all the bytes that have been written to the client but not yet read.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

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

.. note :: "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::remoteIP**
---------------------

**Description**
~~~~~~~~~~~~~~~

Get the IP address of the remote connection who sent the current incoming packet.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual IPAddress remoteIP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the IP address of the remote connection.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: This function must be called after WiFiUDP.parsePacket(). "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::remotePort**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Get the port of the remote UDP connection who sent the current incoming packet.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual uint16_t remotePort(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the port of the remote connection.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleUDP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleUDP/SimpleUDP.ino>`_

.. note :: This function must be called after WiFiUDP.parsePacket(). "WiFiUdp.h" must be included to use the class function.

**WiFiUDP::setRecvTimeout**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Set receiving timeout.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRecvTimeout(int timeout);

**Parameters**
~~~~~~~~~~~~~~

timeout: timeout in seconds.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiUdp.h" must be included to use the class function.
