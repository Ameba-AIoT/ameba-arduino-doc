Class WiFi_eap
==============

**WiFi_eapClass Class**
-----------------------

**Description**
~~~~~~~~~~~~~~~

A class of WiFi EAP and network implementation for Ameba.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class WiFi_eapClass

**Members**
~~~~~~~~~~~

+--------------------------------+----------------------------------------+
| **Public Constructors**                                                 |
+================================+========================================+
| WiFi_eapClass::WiFi_eapClass   | Constructs a WiFi_eapClass object and  |
|                                | initializes the Wi-Fi libraries and    |
|                                | network settings                       |
+--------------------------------+----------------------------------------+
| WiFi_eapClass::~ WiFi_eapClass | Deconstructs a WiFi_eapClass object    |
+--------------------------------+----------------------------------------+
| **Public Methods**                                                      |
+--------------------------------+----------------------------------------+
| WiFi_eapClass::begin           | Start Wi-Fi EAP connection             |
+--------------------------------+----------------------------------------+

**WiFi_eapClass::WiFi_eapClass**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a WiFi_eapClass object and initializes the Wi-Fi libraries and network settings.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    WiFi_eapClass(void);
    WiFi_eapClass(char *method, char *ssid, char *identity, char *password, const unsigned char *client_cert, const unsigned char *client_key, const unsigned char *ca_cert);

**Parameters**
~~~~~~~~~~~~~~

method: Pointer to the EAP connection method string.

ssid: Pointer to the SSID string.

identity: Pointer to the ID string.

password: Pointer to the password string.

client_cert: Pointer to the client certificate string.

client_key: Pointer to the client private key string.

ca_cert: Pointer to the CA certificate string.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: An instance of WiFi_eapClass is created as WiFi_eap inside WiFi_eap.h and is extern for direct use. "WiFi_eap.h" must be included to use the class function.

**WiFi_eapClass::begin**
------------------------

**Description**
~~~~~~~~~~~~~~~

Start Wi-Fi connection for OPEN/ WEP/ with passphrase networks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int begin(void);
    int begin(char *method, char *ssid, char *identity, char *password, const unsigned char *client_cert, const unsigned char *client_key, const unsigned char *ca_cert);

**Parameters**
~~~~~~~~~~~~~~

method: Pointer to the EAP connection method string.

ssid: Pointer to the SSID string.

identity: Pointer to the ID string.

password: Pointer to the password string.

client_cert: Pointer to the client certificate string.

client_key: Pointer to the client private key string.

ca_cert: Pointer to the CA certificate string.

**Returns**
~~~~~~~~~~~

This function returns the Wi-Fi eap status.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ConnectToWiFi/WPA_Security <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/WiFi/examples/ConnectToWiFi/WPA2_Enterprise/WPA2_Enterprise.ino>`_

.. note :: "WiFi_eap.h" must be included to use the class function.
