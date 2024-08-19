**WiFiUDP Class**

| **Description**
| A class used for managing WiFi UDP implementation for Ameba.

| **Syntax**
| class WiFiUDP

**Members**

+----------------------+-----------------------------------------------+
| **Public             |                                               |
| Constructors**       |                                               |
+======================+===============================================+
| `WiFiUDP::WiFiUDP    | Constructs a WiFiUDP instance of the Wi-Fi    |
|  <https://www.amebai | UDP class that can send and receive UDP       |
| ot.com/en/rtl8722dm- | messages                                      |
| arduino-api-wifiudp/ |                                               |
| #WiFiUDP_WiFiUDP>`__ |                                               |
+----------------------+-----------------------------------------------+
| **Public Methods**   |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::beg        | Initialize Wi-Fi UDP library, network         |
| in <https://www.ameb | settings and start listening at specified     |
| aiot.com/en/rtl8722d | local port.                                   |
| m-arduino-api-wifiud |                                               |
| p/#WiFiUDP_begin>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::s          | Disconnect from the server                    |
| top <https://www.ame |                                               |
| baiot.com/en/rtl8722 |                                               |
| dm-arduino-api-wifiu |                                               |
| dp/#WiFiUDP_stop>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFi                | Start building up a packet to send to the     |
| UDP::beginPacket <ht | remote host-specific in IP and port           |
| tps://www.amebaiot.c |                                               |
| om/en/rtl8722dm-ardu |                                               |
| ino-api-wifiudp/#WiF |                                               |
| iUDP_beginPacket>`__ |                                               |
+----------------------+-----------------------------------------------+
| `                    | Finish off this packet and send it            |
| WiFiUDP::endPacket < |                                               |
| https://www.amebaiot |                                               |
| .com/en/rtl8722dm-ar |                                               |
| duino-api-wifiudp/#W |                                               |
| iFiUDP_endPacket>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::wri        | Write UDP data (single byte) to remote        |
| te <https://www.ameb | connection                                    |
| aiot.com/en/rtl8722d |                                               |
| m-arduino-api-wifiud |                                               |
| p/#WiFiUDP_write>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::write      | Send packet immediately from the buffer       |
| Immediately <https:/ |                                               |
| /www.amebaiot.com/en |                                               |
| /rtl8722dm-arduino-a |                                               |
| pi-wifiudp/#WiFiUDP_ |                                               |
| writeImmediately>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFi                | Check for the presence of a UDP packets and   |
| UDP::parsePacket <ht | start processing the next available incoming  |
| tps://www.amebaiot.c | packet                                        |
| om/en/rtl8722dm-ardu |                                               |
| ino-api-wifiudp/#WiF |                                               |
| iUDP_parsePacket>`__ |                                               |
+----------------------+-----------------------------------------------+
| `                    | Get the number of bytes (characters)          |
| WiFiUDP::available < | available for reading from the buffer         |
| https://www.amebaiot |                                               |
| .com/en/rtl8722dm-ar |                                               |
| duino-api-wifiudp/#W |                                               |
| iFiUDP_available>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::r          | Read UDP data from specified buffer           |
| ead <https://www.ame |                                               |
| baiot.com/en/rtl8722 |                                               |
| dm-arduino-api-wifiu |                                               |
| dp/#WiFiUDP_read>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::p          | Get the next byte from the current packet     |
| eek <https://www.ame | without moving on to the next byte            |
| baiot.com/en/rtl8722 |                                               |
| dm-arduino-api-wifiu |                                               |
| dp/#WiFiUDP_peek>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::flu        | Clear all the bytes that have been written to |
| sh <https://www.ameb | the client but not yet read                   |
| aiot.com/en/rtl8722d |                                               |
| m-arduino-api-wifiud |                                               |
| p/#WiFiUDP_flush>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::remoteIP   | Get the IP address of the remote connection   |
| <https://www.amebaio | who sent the current incoming packet          |
| t.com/en/rtl8722dm-a |                                               |
| rduino-api-wifiudp/# |                                               |
| WiFiUDP_remoteIP>`__ |                                               |
+----------------------+-----------------------------------------------+
| `Wi                  | Get the port of the remote UDP connection who |
| FiUDP::remotePort <h | sent the current incoming packet              |
| ttps://www.amebaiot. |                                               |
| com/en/rtl8722dm-ard |                                               |
| uino-api-wifiudp/#Wi |                                               |
| FiUDP_remotePort>`__ |                                               |
+----------------------+-----------------------------------------------+
| `WiFiUDP::s          | Set receiving timeout                         |
| etRecvTimeout <https |                                               |
| ://www.amebaiot.com/ |                                               |
| en/rtl8722dm-arduino |                                               |
| -api-wifiudp/#WiFiUD |                                               |
| P_setRecvTimeout>`__ |                                               |
+----------------------+-----------------------------------------------+


**WiFiUDP::WiFiUDP**

| **Description**
| Constructs a WiFiUDP instance of the Wi-Fi UDP class that can send and
  receive UDP messages.

| **Syntax**
| WiFiUDP (void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| This constructor does not take in any parameter, thus use another
  method to set up the IP address and port number. “WiFiUdp.h” must be
  included to use the class function.


**WiFiUDP::begin**

| **Description**
| Initialize Wi-Fi UDP library, network settings and start listening at
  specified local port.

| **Syntax**
| virtual uint8_t begin(uint16_t);

| **Parameters**
| port: the local port to listen on

**Returns**

This function returns 1 if successful, else returns 0 if there are no
sockets available to use.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::stop**

| **Description**
| Disconnect from the server. Release any resource being used during the
  UDP session.

| **Syntax**
| virtual void stop(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::beginPacket**

**Description**

Start building up a packet to send to the remote host-specific in IP and
port.

| **Syntax**
| virtual int beginPacket(IPAddress ip, uint16_t port);

virtual int beginPacket(const char \*host, uint16_t port);

| **Parameters**
| host: remote host name
| port: the port of the remote connection
| ip: IP address of the remote connection

**Returns**

This function returns “1” of successful, else returns “0” if there is a
problem with the given IP address or port.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::endPacket**

| **Description**
| Finish off the packet and send it.

| **Syntax**
| virtual int endPacket(void);

| **Parameters**
| NA

**Returns**

This function returns “1” if packet was sent successfully, else returns
“0” if there was an error.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::write**

**Description**

Write UDP data (single byte) to remote connection.

| **Syntax**
| virtual size_t write(uint8_t);

virtual size_t write(const uint8_t \*buffer, size_t size);

| **Parameters**
| buf: a pointer to an array containing the outgoing message
| size: the size of the buffer

| **Returns**
| This function returns the byte/ character that will be written to the
  server or the size of the buffer.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| This function must be wrapped between beginPacket() and endPacket().
  beginPacket() initializes the packet of data, it is not sent until
  endPacket() is called. “WiFiUdp.h” must be included to use the class
  function.


**WiFiUDP::writeImmediately**

| **Description**
| Send packet immediately from the buffer.

| **Syntax**
| size_t writeImmediately(const uint8_t \*buffer, size_t size);

| **Parameters**
| buf: a pointer to an array containing the outgoing message
| size: the size of the buffer

| **Returns**
| This function returns the byte/ character that will be written to the
  server or the size of the buffer.

| **Example Code**
| NA

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::parsePacket**

| **Description**
| Check for the presence of a UDP packets and start processing the next
  available incoming packet.

| **Syntax**
| virtual int parsePacket(void);

| **Parameters**
| NA

**Returns**

This function returns the number of bytes available in the current
packet, will return "0” if WiFiUDP.parsePacket() hasn't been called yet.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::available**

| **Description**
| Get the number of bytes (characters) available for reading from the
  buffer.

| **Syntax**
| virtual int available(void);

| **Parameters**
| NA

**Returns**

This function returns the number of bytes available in the current
packet, else returns “0” if WiFiUDP.parsePacket() hasn’t been called
yet.

| **Example Code**
| NA

| **Notes and Warnings**
| This function can only be successfully called after
  WiFiUDP.parsePacket(). “WiFiUdp.h” must be included to use the class
  function.


**WiFiUDP::read**

| **Description**
| Read UDP data from specified buffer.

| **Syntax**
| virtual int read (void);
| virtual int read (char\* buffer, size_t len);

| **Parameters**
| buf: buffer to hold incoming byte
| size: maximum size of the buffer

| **Returns**
| This function returns the size of the buffer or returns -1 if no
  buffer is available.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| This function can only be successfully called after
  WiFiUDP.parsePacket(). “WiFiUdp.h” must be included to use the class
  function.


**WiFiUDP::peek**

| **Description**
| Get the next byte from the current packet without moving on to the
  next byte.

| **Syntax**
| virtual int peek (void);

| **Parameters**
| NA

**Returns**

This function returns the next byte or character or returns -1 if none
is available.

| **Example Code**
| NA

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.\ **

**WiFiUDP::flush**

| **Description**
| Clear all the bytes that have been written to the client but not yet
  read.

| **Syntax**
| virtual void flush(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.


**WiFiUDP::remoteIP**

| **Description**
| Get the IP address of the remote connection who sent the current
  incoming packet.

| **Syntax**
| virtual IPAddress remoteIP(void);

| **Parameters**
| NA

| **Returns**
| This function returns the IP address of the remote connection.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

**Notes and Warnings**

This function must be called after WiFiUDP.parsePacket(). “WiFiUdp.h”
must be included to use the class function.


**WiFiUDP::remotePort**

| **Description**
| Get the port of the remote UDP connection who sent the current
  incoming packet.

| **Syntax**
| virtual uint16_t remotePort(void);

| **Parameters**
| NA

| **Returns**
| This function returns the port of the remote connection.

| **Example Code**
| Example: WiFiUdpSendReceiveString
  (https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiUdpSendReceiveString/WiFiUdpSendReceiveString.ino)

| **Notes and Warnings**
| This function must be called after WiFiUDP.parsePacket(). “WiFiUdp.h”
  must be included to use the class function.


**WiFiUDP::setRecvTimeout**

| **Description**
| Set receiving timeout

| **Syntax**
| void setRecvTimeout(int timeout);

| **Parameters**
| timeout: timeout in seconds

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “WiFiUdp.h” must be included to use the class function.
