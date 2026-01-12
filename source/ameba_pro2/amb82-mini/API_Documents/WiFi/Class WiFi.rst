Class WiFi
==========

**WiFiClass Class**
-------------------

**Description**
~~~~~~~~~~~~~~~

A class of WiFi and network implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class WiFiClass

**Members**
~~~~~~~~~~~

+-----------------------------+------------------------------------------+
| **Public Constructors**                                                |
+=============================+==========================================+
| WiFiClass::WiFiClass        | Constructs a WiFiClass object and        |
|                             | initializes the Wi-Fi libraries and      |
|                             | network settings                         |
+-----------------------------+------------------------------------------+
| **Public Methods**                                                     |
+-----------------------------+------------------------------------------+
| WiFiClass::firmwareVersion  | Get firmware version                     |
+-----------------------------+------------------------------------------+
| WiFiClass::begin            | Start Wi-Fi connection for OPEN/ WEP/    |
|                             | with passphrase networks.                |
+-----------------------------+------------------------------------------+
| WiFiClass::enableConcurrent | Set concurrent mode (AP + Station)       |
+-----------------------------+------------------------------------------+
| WiFiClass::config           | Configure network IP settings            |
+-----------------------------+------------------------------------------+
| WiFiClass::setDNS           | Set the DNS server IP address to use     |
+-----------------------------+------------------------------------------+
| WiFiClass::disconnect       | Disconnect from the network              |
+-----------------------------+------------------------------------------+
| WiFiClass::macAddress       | Get the interface MAC address            |
+-----------------------------+------------------------------------------+
| WiFiClass::localIP          | Get the interface IP address             |
+-----------------------------+------------------------------------------+
| WiFiClass::subnetMask       | Get the interface subnet mask address    |
+-----------------------------+------------------------------------------+
| WiFiClass::gatewayIP        | Get the interface gateway IP address.    |
+-----------------------------+------------------------------------------+
| WiFiClass::SSID             | Get the current SSID associated with the |
|                             | network                                  |
+-----------------------------+------------------------------------------+
| WiFiClass::BSSID            | Get the current BSSID associated with    |
|                             | the network                              |
+-----------------------------+------------------------------------------+
| WiFiClass::RSSI             | Get the current RSSI (Received Signal    |
|                             | Strength in dBm) associated with the     |
|                             | network                                  |
+-----------------------------+------------------------------------------+
| WiFiClass::encryptionType   | Get the encryption type associated with  |
|                             | the network                              |
+-----------------------------+------------------------------------------+
| WiFiClass::scanNetworks     | Start scanning for available Wi-Fi       |
|                             | networks                                 |
+-----------------------------+------------------------------------------+
| WiFiClass::SSID             | Get the SSID discovered during the       |
|                             | network scan                             |
+-----------------------------+------------------------------------------+
| WiFiClass::encryptionType   | Get the encryption type of the networks  |
|                             | discovered from scanNetworks             |
+-----------------------------+------------------------------------------+
| WiFiClass::encryptionTypeEx | Get the security type and encryption     |
|                             | type of the networks discovered from     |
|                             | scanNetworks                             |
+-----------------------------+------------------------------------------+
| WiFiClass::RSSI             | Get the RSSI of the networks discovered  |
|                             | from scanNetworks                        |
+-----------------------------+------------------------------------------+
| WiFiClass::status           | Get Connection status                    |
+-----------------------------+------------------------------------------+
| WiFiClass::hostByName       | Resolve the given hostname to an IP      |
|                             | address                                  |
+-----------------------------+------------------------------------------+
| WiFiClass::apbegin          | Start AP mode                            |
+-----------------------------+------------------------------------------+
| WiFiClass::disablePowerSave | Disable Wi-Fi Power Save mode            |
+-----------------------------+------------------------------------------+
| WiFiClass:: setHostname     | Set the hostname for an IP address       |
+-----------------------------+------------------------------------------+

**WiFiClass::WiFiClass**
------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WiFiClass object and initializes the Wi-Fi libraries and network settings.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    WiFiClass(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: An instance of WiFiClass is created as WiFi inside WiFi.h and is extern for direct use. "WiFi.h" must be included to use the class function.

**WiFiClass::firmwareVersion**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get WiFi firmware version that is compatible to Arduino.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    char* firmwareVersion(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns WiFi firmware version, default "1.0.0".

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::begin**
--------------------

**Description**
~~~~~~~~~~~~~~~

Start Wi-Fi connection for OPEN/ WEP/ with passphrase networks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int begin(char* ssid);
    int begin(char* ssid, uint8_t key_idx, const char* key);
    int begin(char* ssid, const char *passphrase);

**Parameters**
~~~~~~~~~~~~~~

ssid: Pointer to the SSID string.

key_idx: The key index to set and only needed for WEP mode.

- 0 - 3 (Default value is 0)

key: Key input buffer.

passphrase: Valid characters in a passphrase must be ASCII decimal value.

- 32 - 126

**Returns**
~~~~~~~~~~~

This function returns the Wi-Fi status.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::enableConcurrent**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set Concurrent mode (AP + Station).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void enableConcurrent(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConcurrentMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConcurrentMode/ConcurrentMode.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::config**
---------------------

**Description**
~~~~~~~~~~~~~~~

Configure network settings including the IP address of local host, DNS server, default gateway and subnet, for the Wi-Fi network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void config(IPAddress local_ip);
    void config(IPAddress local_ip, IPAddress dns_server);
    void config(IPAddress local_ip, IPAddress dns_server, IPAddress gateway);
    void config(IPAddress local_ip, IPAddress dns_server, IPAddress gateway, IPAddress subnet);

**Parameters**
~~~~~~~~~~~~~~

local_ip: Local device IP address to use on the network

dns_server: IP address of the DNS server to use

gateway: IP address of the gateway device on the network

subnet: Subnet mask for the network, expressed as an IP address

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: This will disable the DHCP client when connecting to a network and will require the network accepts a static IP. The configured IP addresses will also apply to AP mode, but the DHCP server will not be disabled in AP mode. "WiFi.h" must be included to use the class function.

**WiFiClass::setDNS**
---------------------

**Description**
~~~~~~~~~~~~~~~

Set the IP address for DNS servers.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setDNS(IPAddress dns_server1);
    void setDNS(IPAddress dns_server1, IPAddress dns_server2);

**Parameters**
~~~~~~~~~~~~~~

dns_server1: IP address for DNS server 1

dns_server2: IP address for DNS server 2

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::disconnect**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Disconnect from the network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int disconnect (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns an integer value of 6, corresponding to "WL_DISCONNECTED" in the 'wl_status_t' enumeration, that represents the WiFi disconnected state.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFi.h" must be included to use the class function. 'wl_status_t' enumeration consists of the following Wi-Fi status, WL_NO_SHIELD, WL_IDLE_STATUS, WL_NO_SSID_AVAIL, WL_SCAN_COMPLETED, WL_CONNECTED, WL_CONNECT_FAILED, WL_CONNECTION_LOST, WL_DISCONNECTED.

**WiFiClass::macAddress**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the interface MAC address.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t* macAddress(uint8_t* mac)

**Parameters**
~~~~~~~~~~~~~~

mac: an array of to store MAC address (in 8-bit unsigned integer).

**Returns**
~~~~~~~~~~~

This function returns uint8_t array containing the macAddress with length WL_MAC_ADDR_LENGTH (6 bit).

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::localIP**
----------------------

**Description**
~~~~~~~~~~~~~~~

Get the interface IP address.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    IPAddress localIP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the IP address of the interface.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::subnetMask**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the interface subnet mask address.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    IPAddress subnetMask(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns subnet mask address of the interface.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/NoEncryption <https://github.com/Ameba-AIoT/ameba-arduino-pro2/tree/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/NoEncryption>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::gatewayIP**
------------------------

**Description**
~~~~~~~~~~~~~~~

Get the interface gateway IP address.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    IPAddress gatewayIP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the gateway IP address of interface.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/NoEncryption <https://github.com/Ameba-AIoT/ameba-arduino-pro2/tree/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/NoEncryption>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::SSID**
-------------------

**Description**
~~~~~~~~~~~~~~~

Get the current SSID (Service Set Identifier) associated with the network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    char* SSID(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns current SSID associate with the network.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::BSSID**
--------------------

**Description**
~~~~~~~~~~~~~~~

Get the current BSSID (Basic Service Set Identifier) associated with the network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t* BSSID(uint8_t* bssid)

**Parameters**
~~~~~~~~~~~~~~

bssid: an array to store bssid (8-bit unsigned integer)

**Returns**
~~~~~~~~~~~

This function returns the uint8_t array storing BSSID with length WL_MAC_ADDR_LENGTH (6 bit).

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::RSSI**
-------------------

**Description**
~~~~~~~~~~~~~~~

Get the current RSSI (Received Signal Strength in dBm) associated with the network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int32_t RSSI(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current RSSI as a 32-bit signed value.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::encryptionType**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the encryption type associated with the network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t encryptionType(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns an integer value corresponding to the current encryption type of the Wi-Fi connection in the 'wl_enc_type' enumeration.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function. 'wl_enc_type' enumeration consists of the following encryption type - ENC_TYPE_WEP, ENC_TYPE_WPA, ENC_TYPE_WPA3, ENC_TYPE_WPA2, ENC_TYPE_NONE and ENC_TYPE_AUTO.

**WiFiClass::scanNetworks**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Start scanning for available WiFi networks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int8_t scanNetworks(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the number of discovered networks as an 8-bit integer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ScanNetworks
<https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::SSID**
-------------------

**Description**
~~~~~~~~~~~~~~~

Get the SSID (Service Set Identifier) discovered during the network scan.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    char* SSID(uint8_t networkItem);

**Parameters**
~~~~~~~~~~~~~~

networkItem: Specify the network item that retrieves the information required. Network item indicates the index of scanNetwork result that stored in the network scan list array arranging in RSSI descending order.

**Returns**
~~~~~~~~~~~

This function returns the SSID string of the specified network item on the network scan list.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ScanNetworks
<https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::encryptionType**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the encryption type of the networks discovered from scanNetworks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t encryptionType(uint8_t networkItem);

**Parameters**
~~~~~~~~~~~~~~

networkItem: Specify the network item that retrieves the information required. Network item indicates the index of scanNetwork result that stored in the network scan list array arranging in RSSI descending order.

**Returns**
~~~~~~~~~~~

This function returns an integer value corresponding to the current Wi-Fi encryption type of the specified item on the network scanned list in the 'wl_enc_type' enumeration.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ScanNetworks
<https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino>`_

.. note :: "WiFi.h" must be included to use the class function. 'wl_enc_type' enumeration consists of the following encryption type - ENC_TYPE_WEP, ENC_TYPE_WPA, ENC_TYPE_WPA3, ENC_TYPE_WPA2, ENC_TYPE_NONE and ENC_TYPE_AUTO.

**WiFiClass::encryptionTypeEx**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the security type and encryption type of the networks discovered from scanNetworks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t encryptionTypeEx(uint8_t networkItem);

**Parameters**
~~~~~~~~~~~~~~

networkItem: specify the network item that retrieves the information required. Network item indicates the index of scanNetwork result that stored in the network scan list array arranging in RSSI descending order.

**Returns**
~~~~~~~~~~~

This function returns security and encryption type of the specified item on the network scanned list.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ScanNetworks
<https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::RSSI**
-------------------

**Description**
~~~~~~~~~~~~~~~

Get the RSSI of the networks discovered from scanNetworks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int32_t RSSI(uint8_t networkItem);

**Parameters**
~~~~~~~~~~~~~~

networkItem: specify the network item that retrieves the information required. Network item indicates the index of scanNetwork result that stored in the network scan list array arranging in RSSI descending order.

**Returns**
~~~~~~~~~~~

This function returns the signed value of RSSI of the specified item on the network scanned list.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ScanNetworks
<https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::status**
---------------------

**Description**
~~~~~~~~~~~~~~~

Get the connection status.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t status(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns an integer value of 3 corresponding to "WL_CONNECTED" in the 'wl_status_t' enumeration, if Wi-Fi is connected. Else returns integer value of 6, corresponding to "WL_DISCONNECTED" in the 'wl_status_t' enumeration, that represents the WiFi disconnected state.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA_Security/WPA_Security.ino>`_

.. note :: "WiFi.h" must be included to use the class function. 'wl_status_t' enumeration consists of the following Wi-Fi status, WL_NO_SHIELD, WL_IDLE_STATUS, WL_NO_SSID_AVAIL, WL_SCAN_COMPLETED, WL_CONNECTED, WL_CONNECT_FAILED, WL_CONNECTION_LOST, WL_DISCONNECTED.

**WiFiClass::hostByName**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Resolve the given hostname to an IP address.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int hostByName(const char* aHostname, IPAddress& aResult);

**Parameters**
~~~~~~~~~~~~~~

aHostname: Name to be resolved

aResult: IPAddress structure to store the returned IP address

**Returns**
~~~~~~~~~~~

The function returns "WL_SUCCESS" if a host name was successfully converted to an IPv4 address, else, it will return as "WL_FAILURE".

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::apbegin**
----------------------

**Description**
~~~~~~~~~~~~~~~

Set to Wi-Fi AP (Access Point) mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int apbegin(char* ssid, char* channel, uint8_t hidden_ssid);
    int apbegin(char* ssid, char* password, char* channel, uint8_t hidden_ssid);

**Parameters**
~~~~~~~~~~~~~~

ssid: SSID of the AP network

channel: AP's channel (Default value is 1)

password: AP's password

hidden_ssid: hidden SSID value (Default value is 0)

**Returns**
~~~~~~~~~~~

This function returns the status of AP.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `CreateWiFiAP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/CreateWiFiAP/CreateWiFiAP.ino>`_

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass::disablePowerSave**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Disable the WiFi driver Power Save mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int disablePowerSave(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "0" if PowerSave disable successfully, else "-1" if error occurs.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WiFi.h" must be included to use the class function.

**WiFiClass:: setHostname**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Set the hostname for an IP address

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setHostname(const char* hostname);

**Parameters**
~~~~~~~~~~~~~~

Hostname: Name to be set

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA
