WiFiClass Class

Description A class of WiFi and network implementation for Ameba.

Syntax class WiFiClass

Members

WiFiClass::WiFiClass

Description Constructs a WiFiClass object and initializes the Wi-Fi
libraries and network settings.

Syntax WiFiClass(void);

Parameters NA

Returns NA

Example Code NA

Notes and Warnings An instance of WiFiClass is created as WiFi inside
WiFi.h and is extern for direct use. “WiFi.h” must be included to use
the class function.

WiFiClass::firmwareVersion

Description Get WiFi firmware version that is compatible to Arduino.

Syntax char\* firmwareVersion(void);

Parameters NA

Returns This function returns WiFi firmware version, default “1.0.0”.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::begin

Description Start Wi-Fi connection for OPEN/ WEP/ with passphrase
networks.

Syntax

int begin(char\* ssid);

int begin(char\* ssid, uint8_t key_idx, const char\* key);

int begin(char\* ssid, const char \*passphrase);

Parameters ssid: Pointer to the SSID string key_idx: The key index to
set. (Default value: 0, valid values are 0-3.) The key index is only
needed for WEP mode. key: Key input buffer. passphrase: Valid characters
in a passphrase must be between ASCII 32-126 (decimal).

Returns This function returns the Wi-Fi status.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::enableConcurrent

Description Set Concurrent mode (AP + Station).

Syntax

void enableConcurrent(void);

Parameters NA

Returns NA

Example Code Example: Concurrent Mode ()

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::config

Description Configure network settings including the IP address of local
host, DNS server, default gateway and subnet, for the Wi-Fi network.

Syntax

void config(IPAddress local_ip);

void config(IPAddress local_ip, IPAddress dns_server);

void config(IPAddress local_ip, IPAddress dns_server, IPAddress
gateway);

void config(IPAddress local_ip, IPAddress dns_server, IPAddress gateway,
IPAddress subnet);

Parameters local_ip: Local device IP address to use on the network
dns_server: IP address of the DNS server to use gateway: IP address of
the gateway device on the network subnet: Subnet mask for the network,
expressed as an IP address

Returns NA

Example Code NA

Notes and Warnings This will disable the DHCP client when connecting to
a network and will require the network accepts a static IP. The
configured IP addresses will also apply to AP mode, but the DHCP server
will not be disabled in AP mode. “WiFi.h” must be included to use the
class function.

WiFiClass::setDNS

Description Set the IP address for DNS servers.

Syntax void setDNS(IPAddress dns_server1); void setDNS(IPAddress
dns_server1, IPAddress dns_server2);

Parameters dns_server1: IP address for DNS server 1 dns_server2: IP
address for DNS server 2

Returns NA

Example Code NA

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::disconnect

Description Disconnect from the network.

Syntax int disconnect (void);

Parameters NA

Returns

This function returns an integer value of 6, corresponding to
“WL_DISCONNECTED” in the ‘wl_status_t’ enumeration, that represents the
WiFi disconnected state.

Example Code NA

Notes and Warnings “WiFi.h” must be included to use the class function.

‘wl_status_t’ enumeration consists of the following Wi-Fi status,

WL_NO_SHIELD, WL_IDLE_STATUS, WL_NO_SSID_AVAIL, WL_SCAN_COMPLETED,
WL_CONNECTED, WL_CONNECT_FAILED, WL_CONNECTION_LOST, WL_DISCONNECTED.

WiFiClass::macAddress

Description Get the interface MAC address.

Syntax uint8_t\* macAddress(uint8_t\* mac)

Parameters mac: an array of to store MAC address (in 8-bit unsigned
integer).

Returns This function returns uint8_t array containing the macAddress
with length WL_MAC_ADDR_LENGTH (6 bit).

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::localIP

Description Get the interface IP address.

Syntax IPAddress localIP(void);

Parameters NA

Returns This function returns the IP address of the interface.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::subnetMask

Description Get the interface subnet mask address.

Syntax IPAddress subnetMask(void);

Parameters NA

Returns This function returns subnet mask address of the interface.

Example Code Example: ConnectNoEncryption
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectNoEncryption/ConnectNoEncryption.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::gatewayIP

Description Get the interface gateway IP address.

Syntax IPAddress gatewayIP(void);

Parameters NA

Returns This function returns the gateway IP address of interface.

Example Code Example: ConnectNoEncryption
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectNoEncryption/ConnectNoEncryption.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::SSID

Description Get the current SSID (Service Set Identifier) associated
with the network.

Syntax char\* SSID(void);

Parameters NA

Returns This function returns current SSID associate with the network.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::BSSID

Description Get the current BSSID (Basic Service Set Identifier)
associated with the network.

Syntax uint8_t\* BSSID(uint8_t\* bssid)

Parameters bssid: an array to store bssid (8-bit unsigned integer)

Returns This function returns the uint8_t array storing BSSID with
length WL_MAC_ADDR_LENGTH (6 bit).

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino).

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::RSSI

Description Get the current RSSI (Received Signal Strength in dBm)
associated with the network.

Syntax int32_t RSSI(void);

Parameters NA

Returns This function returns the current RSSI as a 32-bit signed value.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::encryptionType

Description

Get the encryption type associated with the network.

Syntax uint8_t encryptionType(void);

Parameters NA

Returns

This function returns an integer value corresponding to the current
encryption type of the Wi-Fi connection in the ‘wl_enc_type’
enumeration.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

‘wl_enc_type’ enumeration consists of the following encryption type -
ENC_TYPE_WEP, ENC_TYPE_WPA, ENC_TYPE_WPA3, ENC_TYPE_WPA2, ENC_TYPE_NONE
and ENC_TYPE_AUTO.

WiFiClass::scanNetworks

Description Start scanning for available WiFi networks.

Syntax int8_t scanNetworks(void);

Parameters NA

Returns This function returns the number of discovered networks as an
8-bit integer.

Example Code Example: ScanNetworks
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::SSID

Description Get the SSID (Service Set Identifier) discovered during the
network scan.

Syntax char\* SSID(uint8_t networkItem);

Parameters networkItem: specify the network item that retrieves the
information required. Network item indicates the index of scanNetwork
result that stored in the network scan list array arranging in RSSI
descending order.

Returns This function returns the SSID string of the specified network
item on the network scan list.

Example Code Example: ScanNetworks
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::encryptionType

Description Get the encryption type of the networks discovered from
scanNetworks.

Syntax uint8_t encryptionType(uint8_t networkItem);

Parameters networkItem: specify the network item that retrieves the
information required. Network item indicates the index of scanNetwork
result that stored in the network scan list array arranging in RSSI
descending order.

Returns

This function returns an integer value corresponding to the current
Wi-Fi encryption type of the specified item on the network scanned list
in the ‘wl_enc_type’ enumeration.

Example Code Example: ScanNetworks
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

‘wl_enc_type’ enumeration consists of the following encryption type -
ENC_TYPE_WEP, ENC_TYPE_WPA, ENC_TYPE_WPA3, ENC_TYPE_WPA2, ENC_TYPE_NONE
and ENC_TYPE_AUTO.

WiFiClass::encryptionTypeEx

Description Get the security type and encryption type of the networks
discovered from scanNetworks.

Syntax uint32_t encryptionTypeEx(uint8_t networkItem);

Parameters networkItem: specify the network item that retrieves the
information required. Network item indicates the index of scanNetwork
result that stored in the network scan list array arranging in RSSI
descending order.

Returns This function returns security and encryption type of the
specified item on the network scanned list.

Example Code Example: ScanNetworks
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::RSSI

Description Get the RSSI of the networks discovered from scanNetworks.

Syntax int32_t RSSI(uint8_t networkItem);

Parameters networkItem: specify the network item that retrieves the
information required. Network item indicates the index of scanNetwork
result that stored in the network scan list array arranging in RSSI
descending order.

Returns This function returns the signed value of RSSI of the specified
item on the network scanned list.

Example Code Example: ScanNetworks
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ScanNetworks/ScanNetworks.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::status

Description Get the connection status.

Syntax uint8_t status(void);

Parameters NA

Returns

This function returns an integer value of 3 corresponding to
“WL_CONNECTED” in the ‘wl_status_t’ enumeration, if Wi-Fi is connected.
Else returns integer value of 6, corresponding to “WL_DISCONNECTED” in
the ‘wl_status_t’ enumeration, that represents the WiFi disconnected
state.

Example Code Example: ConnectWithWPA
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectWithWiFi/ConnectWithWPA/ConnectWithWPA.ino).

Notes and Warnings “WiFi.h” must be included to use the class function.

‘wl_status_t’ enumeration consists of the following Wi-Fi status,

WL_NO_SHIELD, WL_IDLE_STATUS, WL_NO_SSID_AVAIL, WL_SCAN_COMPLETED,
WL_CONNECTED, WL_CONNECT_FAILED, WL_CONNECTION_LOST, WL_DISCONNECTED.

WiFiClass::hostByName

Description Resolve the given hostname to an IP address.

Syntax int hostByName(const char\* aHostname, IPAddress& aResult);

Parameters aHostname: Name to be resolved aResult: IPAddress structure
to store the returned IP address

Returns The function returns “WL_SUCCESS” if a host name was
successfully converted to an IPv4 address, else, it will return as
“WL_FAILURE”.

Example Code NA

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::apbegin

Description Set to Wi-Fi AP (Access Point) mode.

Syntax int apbegin(char\* ssid, char\* channel, uint8_t hidden_ssid);

int apbegin(char\* ssid, char\* password, char\* channel, uint8_t
hidden_ssid);

Parameters ssid: SSID of the AP network channel: AP’s channel (Default
value: 1) password: AP’s password

hidden_ssid: hidden SSID value (Default value: 0)

Returns This function returns the status of AP.

Example Code Example:
WiFiAPMode(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/WiFiAPMode/WiFiAPMode.ino)

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass::disablePowerSave

Description Disable the WiFi driver Power Save mode.

Syntax int disablePowerSave(void);

Parameters NA

Returns This function returns “0” if PowerSave disable successfully,
else “-1” if error occurs.

Example Code NA

Notes and Warnings “WiFi.h” must be included to use the class function.

WiFiClass:: setHostname

Description

Set the hostname for an IP address

Syntax

void setHostname(const char\* hostname);

Parameters

Hostname: Name to be set

Returns

NA

Example Code

NA

Notes and Warnings

NA
