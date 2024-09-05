Class WiFiSSLClient
===================

.. contents::
  :local:
  :depth: 2

**WiFiSSLClient Class**
-----------------------

**Description**
~~~~~~~~~~~~~~~

A class for Wi-Fi Secure Socket Layer Client implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class WiFiSSLClient

**Members**
~~~~~~~~~~~

+---------------------------------------+----------------------------------------------------------------------+
| **Public Constructors**                                                                                      |
+=======================================+======================================================================+
| WiFiSSLClient::WiFiSSLClient          | Constructs a WiFiSSLClient instance that always connects in SSL      |
|                                       | to the specified IP address and port.                                |
+---------------------------------------+----------------------------------------------------------------------+
| **Public Methods**                                                                                           |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::connect                | Connect to the IP address and port.                                  |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::write                  | Write data (single byte) to the server.                              |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::available              | Get the availability of the Wi-Fi SSL socket for reading.            |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::read                   | Read the incoming byte from the server.                              |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::peek                   | Get the next byte from the current packet without moving on          |
|                                       | to the next byte.                                                    |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::flush                  | Clear all the bytes that have been written to the client but not     |
|                                       | yet read.                                                            |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::stop                   | Disconnect from the server.                                          |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::connected              | Check if SSL client is connected.                                    |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::setRootCA              | Set Root CA for authentication.                                      |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::setClientCertificate   | Set certificate of the client.                                       |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::setRecvTimeout         | Set receiving timeout.                                               |
+---------------------------------------+----------------------------------------------------------------------+
| WiFiSSLClient::setPreSharedKey        | Set the Pre Shared Key (PSK) to use for authentication.              |
+---------------------------------------+----------------------------------------------------------------------+


**WiFiSSLClient::WiFiSSLClient**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WiFiSSLClient instance that always connects in SSL to the specified IP address and port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  WiFiSSLClient(void);

  WiFiSSLClient(uint8_t sock);

**Parameters**
~~~~~~~~~~~~~~

sock: socket state, default -1

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiSSLClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiSSLClient/WiFiSSLClient.ino>`_

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::connect**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Connect to the IP address and port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual int connect(IPAddress ip, uint16_t port);

  virtual int connect(const char *host, uint16_t port);

  virtual uint8_t connected(void);

  int connect(const char *host, uint16_t port, unsigned char *rootCABuff, unsigned char *cli_cert, unsigned char *cli_key);

  int connect(IPAddress ip, uint16_t port, unsigned char *rootCABuff, unsigned char *cli_cert, unsigned char *cli_key);

  int connect(const char *host, uint16_t port, unsigned char *pskIdent, unsigned char *psKey);

  int connect(IPAddress ip, uint16_t port, unsigned char *pskIdent, unsigned char *psKey);

**Parameters**
~~~~~~~~~~~~~~

ip: IP address

host: Host name

port: the port to listen to

rootCABuff: buffer that store root CA

cli_cert: buffer that store client certificate

cli_key: buffer that store client key pair

pskIdent: identity for PSK

psKey: Pre shared key

**Returns**
~~~~~~~~~~~

This function returns “1” if successful, else returns “0”.

**Example Code**
~~~~~~~~~~~~~~~~
Example: `WiFiSSLClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiSSLClient/WiFiSSLClient.ino>`_

.. note :: “WiFiSSLClient.h” must be included to use the class function.

**WiFiSSLClient::write**
------------------------

**Description**
~~~~~~~~~~~~~~~

Write data (single byte) to the server the SSL client is connected to.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual size_t write(uint8_t);

  virtual size_t write(const uint8_t *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: a pointer to an array containing the outgoing message

size: the size of the buffer

**Returns**
~~~~~~~~~~~

This function returns the byte/ character that will be written to the server or the size of the buffer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::available**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the availability of the Wi-Fi SSL socket for reading.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual int available(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns “1” and number of bytes available for reading if there are available data, else returns 0.

**Example Code**
~~~~~~~~~~~~~~~~
Example: `WiFiSSLClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiSSLClient/WiFiSSLClient.ino>`_

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::read**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Read the incoming byte from the server that the SSL client is connected to.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual int read(void);

  virtual int read(uint8_t *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

buf: buffer that holds incoming data in 8-bit

size: maximum size of the buffer

**Returns**
~~~~~~~~~~~

This function returns the size of the buffer or returns “-1” if no buffer is available.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiSSLClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiSSLClient/WiFiSSLClient.ino>`_

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::peek**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Get the next byte from the current packet without moving on to the next byte.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual int peek(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next byte or character, else returns -1 if none is available.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::flush**
------------------------

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


.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::stop**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Disconnect from the server.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual void stop (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WiFiSSLClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiSSLClient/WiFiSSLClient.ino>`_

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::connected**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Check if SSL client is connected.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual uint8_t connected(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns “1” if the SSLClient socket is connected, else returns “0” if not connected.

**Example Code**

Example: `WiFiSSLClient <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiSSLClient/WiFiSSLClient.ino>`_

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::setRootCA**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set Root CA(certification authority) for SSL authentication.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  void setRootCA(unsigned char *rootCA);

**Parameters**
~~~~~~~~~~~~~~

rootCA: a string of rootCA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::setClientCertificate**
---------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set certificate of the client.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  void setClientCertificate(unsigned char *client_ca, unsigned char *private_key);

**Parameters**
~~~~~~~~~~~~~~

client_ca: Client certificate

private_key: client's private key pair

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~
NA

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::setRecvTimeout**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

This function sets the SSL client socket receiving timeout.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  int setRecvTimeout(int timeout);

**Parameters**
~~~~~~~~~~~~~~

timeout: timeout in seconds

**Returns**
~~~~~~~~~~~

The function returns “0”.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “WiFiSSLClient.h” must be included to use the class function.


**WiFiSSLClient::setPreSharedKey**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the Pre Shared Key (PSK) to use for authentication.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  void setPreSharedKey(unsigned char *pskIdent, unsigned char *psKey);

**Parameters**
~~~~~~~~~~~~~~

pskIdent: identity for PSK

psKey: Pre shared key

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Do not set a root CA and client certificate if PSK should be used for
  authentication. If root CA, client certificate and PSK are all set,
  certificate-based authentication will be used. “WiFiSSLClient.h” must
  be included to use the class function.
