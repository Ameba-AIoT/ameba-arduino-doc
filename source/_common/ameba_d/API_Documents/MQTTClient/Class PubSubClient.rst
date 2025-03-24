Class PubSubClient
==================

.. contents::
  :local:
  :depth: 2

.. note :: The Ameba MQTT related APIs and examples are works based on the PubSubClient libraries written by Nicholas O’Leary (http://pubsubclient.knolleary.net).

.. note :: These include, PubSubClient.cpp and PubSubClient.h

.. Caution :: These libraries are under MIT License.

**PubSubClient Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class used for implementing MQTT for Ameba.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class PubSubClient

**Members**
~~~~~~~~~~~

+--------------------------------+------------------------------------+
| **Public Constructors**        | Description                        |
+================================+====================================+
| PubSubClient::PubSubClient     | Constructs a PubSubClient object   |
+--------------------------------+------------------------------------+
| **Public Methods**                                                  |
+--------------------------------+------------------------------------+
| PubSubClient::setServer        | Define the server to connect to    |
+--------------------------------+------------------------------------+
| PubSubClient::setCallback      | Set callback function              |
+--------------------------------+------------------------------------+
| PubSubClient::setClient        | Set the network client to be used  |
+--------------------------------+------------------------------------+
| PubSubClient::setStream        | Set the message stream to store    |
|                                | received messages                  |
+--------------------------------+------------------------------------+
| PubSubClient::setKeepAlive     | Set the keep alive interval used by|
|                                | the client                         |
+--------------------------------+------------------------------------+
| PubSubClient::setSocketTimeout | Set the socket timeout used by     |
|                                | the client                         |
+--------------------------------+------------------------------------+
| PubSubClient::setBufferSize    | Set the size, in bytes, of the     |
|                                | internal send/receive buffer       |
+--------------------------------+------------------------------------+
| PubSubClient::getBufferSize    | Get the current size of the        |
|                                | internal buffer                    |
+--------------------------------+------------------------------------+
| PubSubClient::connect          | Connect the client to the server   |
+--------------------------------+------------------------------------+
| PubSubClient::disconnect       | Disconnect the client from         |
|                                | the server                         |
+--------------------------------+------------------------------------+
| PubSubClient::publish          | Publish a message to specific topic|
+--------------------------------+------------------------------------+
| PubSubClient::publish_P        | Publish a message stored in PROGMEM|
|                                | to a specific topic                |
+--------------------------------+------------------------------------+
| PubSubClient::write            | Write to the publish payload       |
+--------------------------------+------------------------------------+
| PubSubClient::subscribe        | Subscribe to a specified topic     |
+--------------------------------+------------------------------------+
| PubSubClient::unsubscribe      | Unsubscribe from a specified topic |
+--------------------------------+------------------------------------+
| PubSubClient::loop             | Keep MQTT session alive and process|
|                                | any queuing tasks                  |
+--------------------------------+------------------------------------+
| PubSubClient::connected        | Check if client is still connected |
+--------------------------------+------------------------------------+
| PubSubClient::state            | Get current state of the client    |
+--------------------------------+------------------------------------+

-----------------------------------------

**PubSubClient::PubSubClient**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a PubSubClient object and, if applicable, sets server address, port, callback function, data stream and wifi client.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient(void);

.. code:: c++
  
  PubSubClient(Client& client);

.. code:: c++
  
  PubSubClient(IPAddress, uint16_t, Client& client);

.. code:: c++
  
  PubSubClient(IPAddress, uint16_t, Client& client, Stream&);

.. code:: c++
  
  PubSubClient(IPAddress, uint16_t, MQTT_CALLBACK_SIGNATURE, Client& client);

.. code:: c++

  PubSubClient(IPAddress, uint16_t,MQTT_CALLBACK_SIGNATURE, Client& client, Stream&);

.. code:: c++
  
  PubSubClient(uint8_t*, uint16_t, Client& client);

.. code:: c++
  
  PubSubClient(uint8_t*, uint16_t, Client& client, Stream&);

.. code:: c++

  PubSubClient(uint8_t*, uint16_t, MQTT_CALLBACK_SIGNATURE, Client& client);

.. code:: c++

  PubSubClient(uint8_t*, uint16_t,MQTT_CALLBACK_SIGNATURE, Client& client, Stream&);

.. code:: c++

  PubSubClient(const char*, uint16_t, Client& client);

.. code:: c++

  PubSubClient(const char*, uint16_t, Client& client, Stream&);

.. code:: c++

  PubSubClient(const char*, uint16_t, MQTT_CALLBACK_SIGNATURE, Client& client);

.. code:: c++

  PubSubClient(const char*, uint16_t, MQTT_CALLBACK_SIGNATURE, Client& client, Stream&);

**Parameters**
~~~~~~~~~~~~~~

``client``: the network client to use, for example WiFiClient

``IPAddress``: MQTT server address

``port``: the port to connect to for MQTT, usually 1883 for unencrypted connection

``MQTT_CALLBACK_SIGNATURE``: a pointer to a message callback function called when a message arrives for a subscription created by this client.

``Stream``: a message stream to store received messages.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: PubSubClient::PubSubClient(Client& client) would suffice for normal MQTT connection. “PubSubClient.h” must be included to use the class function.

------------------------------------------

**PubSubClient::setServer**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Define the server to connect to by setting the parameters such as IP address, port number and domain.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setServer(uint8_t * ip, uint16_t port);

.. code:: c++

  PubSubClient& setServer(IPAddress ip, uint16_t port);

.. code:: c++

  PubSubClient& setServer(const char* domain, uint16_t port);

**Parameters**
~~~~~~~~~~~~~~

``ip``: the address of the server

``port``: the port to connect to for MQTT, usually 1883 for unencrypted connection. Default: 1883

``domain``: name of the server

**Returns**
~~~~~~~~~~~

This function returns the parameters such as ip address, port number and domain, allowing the function to be chained.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: “PubSubClient.h” must be included to use the class function.

-------------------------

**PubSubClient::setCallback**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Sets the message callback function.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setCallback(MQTT_CALLBACK_SIGNATURE);

**Parameters**
~~~~~~~~~~~~~~

``MQTT_CALLBACK_SIGNATURE``: a pointer to a message callback function called when a message arrives for a subscription created by this client.

**Returns**
~~~~~~~~~~~

This function returns the client instance, allowing the function to be chained.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: “PubSubClient.h” must be included to use the class function.

--------------------

**PubSubClient::setClient**

**Description**
~~~~~~~~~~~~~~~

Set the network client to be used.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setClient(Client& client);

**Parameters**
~~~~~~~~~~~~~~

``client`` : the network client to use, for example WiFiClient

**Returns**
~~~~~~~~~~~

This function returns the client instance, allowing the function to be chained.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

---------------------------

**PubSubClient::setStream**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Set the message stream to store received messages.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setStream(Stream& stream);

**Parameters**
~~~~~~~~~~~~~~

``stream``: a message stream to store received messages.

**Returns**
~~~~~~~~~~~

This function returns the client instance, allowing the function to be chained.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

--------------------------

**PubSubClient::setKeepAlive**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the keep alive interval used by the client

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setKeepAlive(uint16_t keepAlive);

**Parameters**
~~~~~~~~~~~~~~

``keepAlive``: the keep alive interval, in seconds.

**Returns**
~~~~~~~~~~~

This function returns the client instance, allowing the function to be chained.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

--------------------------

**PubSubClient::setSocketTimeout**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the socket timeout used by the client.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setSocketTimeout(uint16_t timeout);

**Parameters**
~~~~~~~~~~~~~~

``Timeout``: the socket timeout, in seconds.

**Returns**
~~~~~~~~~~~

This function returns the client instance, allowing the function to be chained.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

--------------------------

**PubSubClient::setBufferSize**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the size, in bytes, of the internal send/receive buffer.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& setBufferSize(uint16_t size);

**Parameters**
~~~~~~~~~~~~~~

``size``: the size, in bytes, for the internal buffer.

**Returns**
~~~~~~~~~~~

This function returns false when the buffer could not be resized, returns true when the buffer was resized.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

--------------------------

**PubSubClient::getBufferSize**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current size of the internal buffer.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PubSubClient& getBufferSize(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the size of the internal buffer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

--------------------------

**PubSubClient::connect**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Connects the client to the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean connect(const char *id);

.. code:: c++

  boolean connect(const char *id, const char *user, const char *pass);

.. code:: c++

  boolean connect(const char *id, const char* willTopic, uint8_t willQos, boolean willRetain, const char* willMessage);

.. code:: c++

  boolean connect(const char *id, const char *user, const char* pass, const char* willTopic, uint8_t willQos, boolean willRetain, const char* willMessage);

.. code:: c++

  boolean connect(const char *id, const char *user, const char *pass, const char* willTopic, uint8_t willQos, boolean willRetain, const char* willMessage, boolean cleanSession);

**Parameters**
~~~~~~~~~~~~~~

``id`` : Client ID, a unique string identifier

``user``: Username for authentication, default NULL

``pass`` : Password for authentication, default NULL

``willTopic`` : the topic to be used by the will message

``willQoS`` : the quality of service to be used by the will message

``willRetain`` : whether the will should be published with the retain flag

``willMessage`` : the payload of the will message

``cleanSession``: whether the session should be cleared when the client disconnects

**Returns**
~~~~~~~~~~~

This function returns true if the connection is successful, else, return false.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: Client ID is required and should always be unique else connection might be rejected by the server. “PubSubClient.h” must be included to use the class function.

------------------------------

**PubSubClient::disconnect**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Disconnect the client from the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void disconnect(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

---------------------------

**PubSubClient::publish**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Publishes a message to the specified topic.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean publish(const char* topic, const char* payload)

.. code:: c++

  boolean publish(const char* topic, const char* payload, boolean retained)

.. code:: c++

  boolean publish(const char* topic, const uint8_t* payload, unsigned int plength)

.. code:: c++

  boolean publish(const char* topic, const uint8_t* payload, unsigned int plength, boolean retained)

**Parameters**
~~~~~~~~~~~~~~

``topic``: the topic to publish to

``payload``: the message to publish

``plength``: the length of the payload. Required if payload is a byte[]

``retained``: whether the message should be retained False - not retained. True - retained.

**Returns**
~~~~~~~~~~~

This function returns true if it published successfully, else returns false. If publishing fails, it is either due to connection lost or messages too large.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: Default max packet size is 128 bytes. “PubSubClient.h” must be included to use the class function.

------------------------------------

**PubSubClient::publish_P**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Publishes a message stored in PROGMEM to the specified topic.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean publish_P(const char* topic, const char* payload, boolean retained);

.. code:: c++

  boolean publish_P(const char* topic, const uint8_t * payload, unsigned int plength, boolean retained);

**Parameters**
~~~~~~~~~~~~~~

``topic`` : the topic that the message will be publishing to

``payload`` : the contents/messages that will be published to the topic.

``plength`` : the length of the payload. Required if payload is a byte[]

``retained`` : whether the message should be retained. False - not retained. True - retained.

**Returns**
~~~~~~~~~~~

This function returns true if it published successfully, else returns false. If publishing fails, it is either due to connection lost or messages too large.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

-------------------------------------

**PubSubClient::write**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Write a byte from the buffer into the payload.

**Syntax**
~~~~~~~~~~

.. code:: c++

  size_t write(uint8_t data);

**Parameters**
~~~~~~~~~~~~~~

``data``: a byte to write to the publish payload.

**Returns**
~~~~~~~~~~~

This function returns true if it published successfully, else returns false. If publishing fails, it is either due to connection lost or messages too large.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

-------------------------------------

**PubSubClient::subscribe**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Subscribe to a specified topic.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean subscribe(const char* topic);

.. code:: c++
  
  boolean subscribe(const char* topic, uint8_t qos);

**Parameters**
~~~~~~~~~~~~~~

``topic``: the topic to subscribe to

``qos``: MQTT quality of service. Valid value: 0 or 1. 0 – At most once (no guarantee of delivery) 1- At least once (guaranteed).

**Returns**
~~~~~~~~~~~

This function returns true if it published successfully, else returns false. If publishing fails, it is either due to connection lost or messages too large.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: “PubSubClient.h” must be included to use the class function.

---------------------------

**PubSubClient::unsubscribe**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Unsubscribes from the specified topic.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean unsubscribe (const char* topic);

**Parameters**
~~~~~~~~~~~~~~

``topic`` : the topic to unsubscribe to

**Returns**
~~~~~~~~~~~

This function returns true if it published successfully, else returns false. If publishing fails, it is either due to connection lost or messages too large.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “PubSubClient.h” must be included to use the class function.

-------------------------

**PubSubClient::loop**
----------------------

**Description**
~~~~~~~~~~~~~~~

A method that should be called regularly to allow the client to process incoming messages and maintain its connection to the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean loop(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if the client is still connected to the server else return false.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: A required method that should not be blocked for too long. “PubSubClient.h” must be included to use the class function.

-----------------------------

**PubSubClient::connected**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Checks whether the client is still connected to the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  boolean connected(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if the client is connected to the server else return false.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: “PubSubClient.h” must be included to use the class function.

---------------------------

**PubSubClient::state**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Get the current state of the client. For example, if a connection attempt fails, this can be used to get more information about the failure. All of the values have corresponding constants defined in PubSubClient.h.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int PubSubClient::state(void);

.. code:: c++

  int state(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current state of the client as an integer from **-4 to 5** representing different definition.

``-4``: MQTT_CONNECTION_TIMEOUT -- the server didn't respond within the keepalive time

``-3``: MQTT_CONNECTION_LOST -- the network connection was broken

``-2``: MQTT_CONNECT_FAILED -- the network connection failed

``-1``: MQTT_DISCONNECTED -- the client is disconnected cleanly

``0``: MQTT_CONNECTED -- the client is connected

``1``: MQTT_CONNECT_BAD_PROTOCOL -- the server doesn't support the requested version of MQTT

``2``: MQTT_CONNECT_BAD_CLIENT_ID -- the server rejected the client identifier

``3``: MQTT_CONNECT_UNAVAILABLE -- the server was unable to accept the connection

``4``: MQTT_CONNECT_BAD_CREDENTIALS -- the username/password were rejected

``5``: MQTT_CONNECT_UNAUTHORIZED -- the client was not authorized to connect

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MQTT_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/MQTTClient/examples/MQTT_Basic/MQTT_Basic.ino>`_

.. note :: “PubSubClient.h” must be included to use the class function.
