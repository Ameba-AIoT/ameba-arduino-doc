Class BLESecurity
=================

.. contents::
  :local:
  :depth: 2

**BLESecurity Class**
---------------------

**Description**
~~~~~~~~~~~~~~~

A class used for creating and managing BLE bonding security parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class BLESecurity

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------+
| **Public Constructors**                                              |
+====================================+=================================+
| No public constructor is available as this class is intended to be a |
| singleton class. You can get a pointer to this class using           |
| BLEDevice::configSecurity                                            |
+------------------------------------+---------------------------------+
| **Public Methods**                                                   |
+------------------------------------+---------------------------------+
| BLESecurity::setPairable           | Enable pairing and bonding after|
|                                    | BLE connection                  |
+------------------------------------+---------------------------------+
| BLESecurity::setAuthFlags          | Set BLE bonding security        |
|                                    | requirements                    |
+------------------------------------+---------------------------------+
| BLESecurity::setIOCapability       | Set input and output            |
|                                    | capabilities of the device      |
+------------------------------------+---------------------------------+
| BLESecurity::setSecReqEnable       | Enable sending SMP security     |
|                                    | request when BLE connected      |
+------------------------------------+---------------------------------+
| BLESecurity::setSecReqFlags        | Set security request            |
|                                    | requirements                    |
+------------------------------------+---------------------------------+
| BLESecurity::setStaticPin          | Configure device to use static  |
|                                    | pin input for BLE bonding       |
+------------------------------------+---------------------------------+
| BLESecurity::                      | Set a user callback function for|
| setPasskeyDisplayCallback          | passkey display during BLE      |
|                                    | bonding                         |
+------------------------------------+---------------------------------+
| BLESecurity::                      | Set a user callback function for|
| setPasskeyInputCallback            | passkey input during BLE bonding|
+------------------------------------+---------------------------------+
| BLESecurity::                      | Set a user callback function for|
| setNumericComparisonCallback       | numeric comparison during BLE   |
|                                    | bonding                         |
+------------------------------------+---------------------------------+

**BLESecurity::setPairable**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Enable pairing and bonding after BLE connection.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setPairable(bool pairMode);

**Parameters**
~~~~~~~~~~~~~~

pairMode: True to enable pairing and bonding, False to disable.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEHIDMouse <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino>`_

.. note :: "BLESecurity.h" must be included to use the class function.

**BLESecurity::setAuthFlags**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Set BLE bonding security requirements.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setAuthFlags(uint16_t authFlags);

**Parameters**
~~~~~~~~~~~~~~

authFlags: desired BLE bonding security requirements.

-  GAP_AUTHEN_BIT_NONE

-  GAP_AUTHEN_BIT_BONDING_FLAG

-  GAP_AUTHEN_BIT_MITM_FLAG

-  GAP_AUTHEN_BIT_SC_FLAG

-  GAP_AUTHEN_BIT_SC_ONLY_FLAG

-  GAP_AUTHEN_BIT_FORCE_BONDING_FLAG

Default value: GAP_AUTHEN_BIT_NONE

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BLEHIDMouse <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/BLE/examples/BLEHIDMouse/BLEHIDMouse.ino>`_

.. note :: "BLESecurity.h" must be included to use the class function.

**BLESecurity::setIOCapability**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Set BLE device input and output capabilities.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setIOCap(uint8_t ioCap);

**Parameters**
~~~~~~~~~~~~~~

ioCap: desired device input output capabilities. Default value is GAP_IO_CAP_NO_INPUT_NO_OUTPUT.

-  GAP_IO_CAP_NO_INPUT_NO_OUTPUT

-  GAP_IO_CAP_DISPLAY_ONLY

-  GAP_IO_CAP_DISPLAY_YES_NO

-  GAP_IO_CAP_KEYBOARD_ONLY

-  GAP_IO_CAP_KEYBOARD_DISPLAY

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: The IO capabilities of the peripheral and central device will determine which bonding authentication method is used. "BLESecurity.h" must be included to use the class function.

**BLESecurity::setSecReqEnable**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Enable sending SMP security request when BLE connected.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setSecReqEnable(bool secReq);

**Parameters**
~~~~~~~~~~~~~~

secReq: TRUE to enable, FALSE to disable. Default value is FALSE.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLESecurity.h" must be included to use the class function.

**BLESecurity::setSecReqFlags**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set security request requirements.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setSecReqFlags(uint16_t secReqFlags);

**Parameters**
~~~~~~~~~~~~~~

secReqFlags: desired security requirements. Default value is GAP_AUTHEN_BIT_NONE.

-  GAP_AUTHEN_BIT_NONE

-  GAP_AUTHEN_BIT_BONDING_FLAG

-  GAP_AUTHEN_BIT_MITM_FLAG

-  GAP_AUTHEN_BIT_SC_FLAG

-  GAP_AUTHEN_BIT_SC_ONLY_FLAG

-  GAP_AUTHEN_BIT_FORCE_BONDING_FLAG

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLESecurity.h" must be included to use the class function.

**BLESecurity::setStaticPin**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Configure device to use static pin input for BLE bonding.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setStaticPin(uint32_t pin);

**Parameters**
~~~~~~~~~~~~~~

pin: BLE bonding static pin. Valid values are 6-digit integers.

- 000000 to 999999.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Using a static pin will enable BLE bonding and pairing, set the IO capability to GAP_IO_CAP_DISPLAY_ONLY and set the bonding security requirements flags to (GAP_AUTHEN_BIT_BONDING_FLAG | GAP_AUTHEN_BIT_MITM_FLAG | GAP_AUTHEN_BIT_SC_FLAG). "BLESecurity.h" must be included to use the class function.

**BLESecurity::setPasskeyDisplayCallback**
------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a user callback function for passkey display during BLE bonding.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setPasskeyDisplayCallback(void (*fCallback) (uint8_t conn_id, uint32_t passkey));

**Parameters**
~~~~~~~~~~~~~~

fCallback: A user callback function that returns void and takes two arguments.

conn_id: connection ID of connecting device.

passkey: bonding passkey to display to user to confirm connection.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLESecurity.h" must be included to use the class function.

**BLESecurity::setPasskeyInputCallback**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a user callback function for passkey input during BLE bonding.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setPasskeyInputCallback(uint32_t (*fCallback) (uint8_t conn_id));

**Parameters**
~~~~~~~~~~~~~~

fCallback: A user callback function that takes no arguments and returns the bonding passkey entered by the user.

conn_id: connection ID of connecting device.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLESecurity.h" must be included to use the class function.

**BLESecurity::setNumericComparisonCallback**
---------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a user callback function for numeric comparison during BLE bonding.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setNumericComparisonCallback(bool (*fCallback) (uint8_t conn_id, uint32_t passkey));

**Parameters**
~~~~~~~~~~~~~~

fCallback: A user callback function that takes two arguments and returns a Boolean to indicate user approval for the numeric comparison.

conn_id: connection ID of connecting device.

passkey: bonding passkey to display to user to confirm connection.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "BLESecurity.h" must be included to use the class function.
