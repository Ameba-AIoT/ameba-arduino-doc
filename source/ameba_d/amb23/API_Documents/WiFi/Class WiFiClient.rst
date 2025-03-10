Class WiFiClient
================

.. contents::
  :local:
  :depth: 2

**WiFiClient Class**
--------------------

**Description**
~~~~~~~~~~~~~~~

A class of WiFi Client implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class WiFiClient

**Members**
~~~~~~~~~~~

+------------------------------+---------------------------------------+
| **Public Constructors**                                              |
+==============================+=======================================+
| WiFiClient::WiFiClient       | Constructs a WiFiClient instance that |
|                              | connects to the specified IP address  |
|                              | and port.                             |
+------------------------------+---------------------------------------+
| **Public Methods**                                                   |
+------------------------------+---------------------------------------+
| WiFiClient::connect          | Connect to the IP address and port.   |
+------------------------------+---------------------------------------+
| WiFiClient::write            | Write data (single byte) to the       |
|                              | server.                               |
+------------------------------+---------------------------------------+
| WiFiClient::available        | Get the number of bytes available for |
|                              | reading.                              |
+------------------------------+---------------------------------------+
| WiFiClient::read             | Read the incoming byte from the       |
|                              | server.                               |
+------------------------------+---------------------------------------+
| WiFiClient::recv             | Read the received byte from the       |
|                              | server that the client is connected   |
|                              | to.                                   |
+------------------------------+---------------------------------------+
| WiFiClient::peek             | Get the next byte from the current    |
|                              | packet without moving on to the next  |
|                              | byte.                                 |
+------------------------------+---------------------------------------+
| WiFiClient::flush            | Clear all the bytes that have been    |
|                              | written to the client but not yet     |
|                              | read.                                 |
+------------------------------+---------------------------------------+
| WiFiClient::stop             | Disconnect from the server.           |
+------------------------------+---------------------------------------+
| WiFiClient::connected        | Check if client is connected.         |
+------------------------------+---------------------------------------+
| WiFiClient::setRecvTimeout   | Set the amount of time the client     |
|                              | will wait for new data to arrive each |
|                              | time WiFiClient::read() is called.    |
+------------------------------+---------------------------------------+
| WiFiClient::setBlockingMode  | Set WiFi Client to blocking mode.     |
+------------------------------+---------------------------------------+
| WiFiClient::                 | Set WiFi Client to non-blocking mode. |
| setNonBlocking Mode          |                                       |
+------------------------------+---------------------------------------+

**WiFiClient::WiFiClient**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WiFiClient instance that connects to a specified IP address and port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    WiFiClient(void);
    WiFiClient(uint8_t sock);
    WiFiClient(tPortMode portMode);
    WiFiClient(tBlockingMode blockMode);
    WiFiClient(uint8_t sock, tPortMode portMode);
    WiFiClient(uint8_t sock, tPortMode portMode, tBlockingMode blockMode);

**Parameters**
~~~~~~~~~~~~~~

sock: socket state

portMode: 0-TCP_MODE, 1-UDP_MODE

blockMode: 0-BLOCKING_MODE, 1-NON_BLOCKING_MODE

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::connect**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Connect to the IP address and port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int connect(const char *host, uint16_t port);
    int connect(IPAddress ip, uint16_t port);

**Parameters**
~~~~~~~~~~~~~~

ip: IP address that the client will connect to.

host: Host name that the client will connect to.

port: the port that the client will connect to.

**Returns**
~~~~~~~~~~~

This function returns "1" if the connection is successful, else returns
"0".

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::write**
---------------------

**Description**
~~~~~~~~~~~~~~~

Write data (single byte) to the server that the client is connected to.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    size_t write(uint8_t b);
    size_t write(const uint8_t *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

b: the byte or char to write
buf: a pointer to an array containing the outgoing message
size: the size of the buffer

**Returns**
~~~~~~~~~~~

This function returns the byte / character that will be written to the
server or the size of the buffer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::available**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the number of bytes available for reading.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns 1 and number of bytes available for reading if there are available data, else returns 0.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::read**
--------------------

**Description**
~~~~~~~~~~~~~~~

Read the incoming byte from the server that the client is connected to.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int read(void);
    int read(uint8_t *buf, size_t size);
    int read(char *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: buffer to hold incoming byte

size: maximum size of the buffer

**Returns**
~~~~~~~~~~~

This function returns the size of the buffer or returns -1 if no buffer is available.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::recv**
--------------------

**Description**
~~~~~~~~~~~~~~~

Read the received byte from the server that the client is connected to.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int recv (uint8_t *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: buffer to hold received byte

size: maximum size of the buffer

**Returns**
~~~~~~~~~~~

This function returns 1 and number of bytes received or returns -1 if no data is available.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::peek**
--------------------

**Description**
~~~~~~~~~~~~~~~

Get the next byte from the current packet without moving on to the next byte.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next byte or character, else returns -1 if none is available.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::flush**
---------------------

**Description**
~~~~~~~~~~~~~~~

Clear all the bytes that have been written to the client but not yet read.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void flush(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::stop**
--------------------

**Description**
~~~~~~~~~~~~~~~

Disconnect from the server.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void stop(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::connected**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Check if client is connected.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    virtual uint8_t connected(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "1" if connected, returns "0" if not connected.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiWebClient <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiWebClient/WiFiWebClient.ino>`_

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::setRecvTimeout**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the amount of time the client will wait for new data to arrive each time WiFiClient::read() is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int setRecvTimeout(int timeout);

**Parameters**
~~~~~~~~~~~~~~

timeout: timeout in seconds

**Returns**
~~~~~~~~~~~

This function returns "0" if client is not connected.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFiClient.h" must be included to use the class function.

**WiFiClient::setBlockingMode**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set WiFi Client to blocking mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setBlockingMode(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

**WiFiClient::setNonBlockingMode**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set WiFi Client to non-blocking mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setNonBlockingMode(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA