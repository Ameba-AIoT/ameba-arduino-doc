Class Adafruit_GPS
==================

.. contents::
  :local:
  :depth: 2

**Adafruit_GPS Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class used to configure GPS module settings on Ameba.

**Syntax**
~~~~~~~~~~

.. code:: c++
    
    class Adafruit_GPS

**Members**
~~~~~~~~~~~

+---------------------------------+-----------------------------------+
| **Public Constructors**                                             |
+=================================+===================================+
| Adafruit_GPS::Adafruit_GPS      | Constructs an Adafruit_GPS object |
+---------------------------------+-----------------------------------+
| **Public Methods**                                                  |
+---------------------------------+-----------------------------------+
| Adafruit_GPS::begin             | Initialize serial communication   |
+---------------------------------+-----------------------------------+
| \*Adafruit_GPS:: lastNMEA       | Get the last National Marine      |
|                                 | Electronics Association (NMEA)    |
|                                 | line received and set the         |
|                                 | received flag to false            |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: newNMEAreceived  | Check to see if a new NMEA line   |
|                                 | has been received                 |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: common_init      | Initialization code used by all   |
|                                 | constructor types                 |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: sendCommand      | Send a command to the GPS device  |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: pause            | Pause/resume receiving new data   |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: parseHex         | Read a Hex value and convert into |
|                                 | decimal value                     |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: read             | Read one character from the GPS   |
|                                 | device                            |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: parse            | Parse data such as latitude,      |
|                                 | longitude, speed, angle, etc      |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: wakeup           | Wake the sensor up                |
+---------------------------------+-----------------------------------+
| Adafruit_GPS:: standby          | Standby Mode Switches             |
+---------------------------------+-----------------------------------+
| Adafruit_GPS::waitForSentence   | Wait for a specified sentence     |
|                                 | from the device                   |
+---------------------------------+-----------------------------------+
| Adafruit_GPS::LOCUS_StartLogger | Start the LOCUS logger            |
+---------------------------------+-----------------------------------+
| Adafruit_GPS::LOCUS_StopLogger  | Stop the LOCUS logger             |
+---------------------------------+-----------------------------------+
| Adafruit_GPS::LOCUS_ReadStatus  | Read the logger status            |
+---------------------------------+-----------------------------------+

--------------------------------------------------------------------------------------

**Adafruit_GPS::Adafruit_GPS**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs an Adafruit_GPS object and initialize serial using a SoftSerial object.

**Syntax**
~~~~~~~~~~

.. code:: c++

    Adafruit_GPS(SoftwareSerial *ser);

.. code:: c++

    Adafruit_GPS(HardwareSerial *ser);

**Parameters**
~~~~~~~~~~~~~~

``ser``: a Serial instance

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: important: SoftSerial is using hardware serial so pin mapping cannot be altered.

.. note :: “Adafruit_GPS.h” must be included to use the class function.

-------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::begin**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Initialize baud rate for gps serial communication.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(uint16_t baud);

**Parameters**

``baud``: gps serial baud rate

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: “Adafruit_GPS.h” must be included to use the class function.

-----------------------------------------------------------------------------------------------------------

**Adafruit_GPS::lastNMEA**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Get the last National Marine Electronics Association (NMEA) line received and set the received flag to false.

**Syntax**
~~~~~~~~~~

.. code:: c++

    char *lastNMEA(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns a pointer to the last line of the string.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: “Adafruit_GPS.h” must be included to use the class function.

------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::newNMEAreceived**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Check if a new NMEA line has been received.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean newNMEAreceived(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns "true” if a new NMEA line has been received. Otherwise, returns “false”.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: “Adafruit_GPS.h” must be included to use the class function.

------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::common_init**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Initialization code used by all constructor types.

**Syntax**
~~~~~~~~~~

.. code:: c++
    
    void common_init(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::sendCommand**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Send a command to the GPS device via GPS serial communication.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void sendCommand(const char *str);

**Parameters**

``str``: Pointer to a string holding the command to send

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: “Adafruit_GPS.h” must be included to use the class function.

---------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::pause**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Pause/ resume receiving new data.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void pause (boolean p);

**Parameters**

``p``: True = pause, false = resume

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

---------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::parseHex**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Read a Hexadecimal value and convert into a decimal value.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint8_t parseHex (char c);

**Parameters**

``c``: Hexadecimal value

**Returns**
~~~~~~~~~~~

This function returns the decimal equivalent of the Hexadecimal value.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

--------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::read**
----------------------

**Description**
~~~~~~~~~~~~~~~

Read one character from the GPS device.

**Syntax**
~~~~~~~~~~

.. code:: c++

    char read(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

The function returns the character that we received or returns 0 if nothing was received.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: “Adafruit_GPS.h” must be included to use the class function.
 
------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::parse**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Parse data such as latitude, longitude, speed, angle, etc.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean parse(char *nmea)

**Parameters**

``nmea``: an NMEA string

**Returns**
~~~~~~~~~~~

This function returns “true” if there are valid data to be parsed, “false” if it has invalid data.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Adafruit_GPS_parsing <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/SoftwareSerial/examples/Adafruit_GPS_parsing/Adafruit_GPS_parsing.ino>`_ 

.. note :: “Adafruit_GPS.h” must be included to use the class function.

----------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::wakeup**
------------------------

**Description**
~~~~~~~~~~~~~~~

Wake the sensor by disabling the GPD sensor stand by ode.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean wakeup(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns “true” if the sensor is awake, otherwise return “false” if the sensor is not on standby or failed to wake.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

------------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::standby**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Standby mode switches.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean standby (void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns “false” if it is already in standby mode so that no commands need to be sent to the GPS to wake it up. Otherwise, returns “true” if it entered standby mode.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

--------------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::waitForSentence**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Wait for a specified NEMA sentence from the device.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean waitForSentence (const char *wait4me, uint8_t max)

**Parameters**

``wait4me``: Pointer to a string holding the desired response

``max``: maximum duration to wait for the sentence, default value: 5

**Returns**
~~~~~~~~~~~

This function returns “true” if we the sentence is received, otherwise returns “false”. 

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.
 
--------------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::LOCUS_StartLogger**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Start the LOCUS logger.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean LOCUS_StartLogger(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns “true” if the logger starts successfully. Otherwise, returns “false”. 

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

--------------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::LOCUS_StopLogger**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Stop the LOCUS logger.

**Syntax**
~~~~~~~~~~

.. code:: c++

    boolean LOCUS_StopLogger(void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns “true” if the logger stops successfully. Otherwise, returns “false”. 

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.

--------------------------------------------------------------------------------------------------------------------------

**Adafruit_GPS::LOCUS_ReadStatus**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Read the logger status.

**Syntax**
~~~~~~~~~~

.. code:: c++
    
    boolean LOCUS_ReadStatus (void);

**Parameters**

NA

**Returns**
~~~~~~~~~~~

This function returns “true” if the logger reads the status successfully. Otherwise, returns “false” if there was no response.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “Adafruit_GPS.h” must be included to use the class function.
