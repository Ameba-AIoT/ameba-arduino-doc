Class WiFiServer
================

.. contents::
  :local:
  :depth: 2

**WiFiServer Class**
--------------------

**Description**
~~~~~~~~~~~~~~~

A class of WiFi server implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class WiFiServer

**Members**
~~~~~~~~~~~

+----------------------------+---------------------------------------------+
| **Public Constructors**                                                  |
+============================+=============================================+
| WiFiServer::WiFiServer     | Constructs a WiFiServer object and creates  |
|                            | a server that listens for incoming          |
|                            | connections on the specified port.          |
|                            |                                             |
|                            |                                             |
|                            |                                             |
+----------------------------+---------------------------------------------+
| **Public Methods**                                                       |
+----------------------------+---------------------------------------------+
| WiFiServer::available      | Gets a client that is connected to the      |
|                            | server and has data available for reading.  |
|                            |                                             |
|                            |                                             |
|                            |                                             |
+----------------------------+---------------------------------------------+
| WiFiServer::begin          | Server start listening for incoming         |
|                            | connections.                                |
|                            |                                             |
|                            |                                             |
|                            |                                             |
+----------------------------+---------------------------------------------+
| WiFiServer::write          | Write data to all the clients connected to  |
|                            | a server.                                   |
|                            |                                             |
|                            |                                             |
|                            |                                             |
+----------------------------+---------------------------------------------+


**WiFiServer::WiFiServer**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WiFiServer object and creates a server that listens for incoming connections on the specified port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  WiFiServer (uint16_t port);

**Parameters**
~~~~~~~~~~~~~~

port: The port number being connected to.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleServerWiFi <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleServerWiFi/SimpleServerWiFi.ino>`_

.. note :: “WiFiServer.h” must be included to use the class function.


**WiFiServer::available**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Gets a client that is connected to the server and has data available for reading. The connection persists when the returned client object goes out of scope; you can close it by calling the client.stop().

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  WiFiClient available(uint8_t *status = NULL);

**Parameters**
~~~~~~~~~~~~~~

status: Wi-Fi availability status. Default value: NULL

**Returns**
~~~~~~~~~~~

This function returns a client object; if no Client has data available for reading, this object will evaluate to false in an if-statement

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleServerWiFi <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleServerWiFi/SimpleServerWiFi.ino>`_

.. note :: “WiFiServer.h” must be included to use the class function.


**WiFiServer::begin**
---------------------

**Description**
~~~~~~~~~~~~~~~

Server start listening for incoming connections.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleServerWiFi <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleServerWiFi/SimpleServerWiFi.ino>`_

.. note :: “WiFiServer.h” must be included to use the class function.

**WiFiServer::connected**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Check if server is still connected

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint8_t connected();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "1" if connected, returns "0" if not connected.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “WiFiServer.h” must be included to use the class function.

**WiFiServer::write**
---------------------

**Description**
~~~~~~~~~~~~~~~

Write data to all the clients connected to a server.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  virtual size_t write(uint8_t b);

**Parameters**
~~~~~~~~~~~~~~

b: byte to be written
buf: data buffer
size: size of the data buffer

**Returns**
~~~~~~~~~~~

This function returns the number of bytes written. It is not necessary to read this.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleServerWiFi <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/SimpleServerWiFi/SimpleServerWiFi.ino>`_

.. note :: “WiFiServer.h” must be included to use the class function.
