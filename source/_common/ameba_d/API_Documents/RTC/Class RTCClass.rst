Class RTC
=========

**RTCClass Class**
------------------

**Description**
~~~~~~~~~~~~~~~

A class used for displaying date and time. It is also used for alarm configuration using RTC (Real Time Clock), the independent BCD (Binary-Coded-Decimal) timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class RTC

**Members**
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **Public Constructors**                                               |
+===================================+===================================+
| A public constructor should not be used as this class is intended     |
| to be a singleton class. Access member functions using the            |
| object instance named RTC.                                            |
+-----------------------------------+-----------------------------------+
| **Public Methods**                                                    |
+-----------------------------------+-----------------------------------+
| RTC::Init                         | Initializes the RTC device,       |
|                                   | include clock, RTC registers and  |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+
| RTC::DeInit                       | Deinitializes the RTC device.     |
+-----------------------------------+-----------------------------------+
| RTC::Write                        | Set the specified timestamp in    |
|                                   | seconds to RTC.                   |
+-----------------------------------+-----------------------------------+
| RTC::Read                         | Get current timestamp in seconds  |
|                                   | from RTC.                         |
+-----------------------------------+-----------------------------------+
| RTC::Wait                         | Wait for 1 second (1,000,000 us)  |
+-----------------------------------+-----------------------------------+
| RTC::SetEpoch                     | Convert human readable time to    |
|                                   | epoch time.                       |
+-----------------------------------+-----------------------------------+

-----------------------------------------

**RTC::Init**
------------------

**Description**
~~~~~~~~~~~~~~~

Initialize the RTC device, including the RTC clock source, the RTC registers, and RTC peripheral with corresponding configurations.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void Init(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/RTC/examples/RTC/RTC.ino>`_

.. note :: "rtc.h" must be included to use the class function.

------------------------------------

**RTC::DeInit**
--------------------

**Description**
~~~~~~~~~~~~~~~

Deinitialize the RTC device by disable RTC flag and disable the RTC alarm.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void DeInit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/RTC/examples/RTC/RTC.ino>`_

.. note :: "rtc.h" must be included to use the class function.

------------------------------------

**RTC::Write**
-------------------

**Description**
~~~~~~~~~~~~~~~

Set the specified timestamp (in s) to RTC.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void Write(int t);

**Parameters**
~~~~~~~~~~~~~~

``t``: seconds from 1970-01-01 00:00:00 (YEAR.MONTH.DAY, HOUR: MIN: SECONDS) to specified date and time which is to be set.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/RTC/examples/RTC/RTC.ino>`_

.. note :: "rtc.h" must be included to use the class function.

------------------------------------

**RTC::Read**
------------------

**Description**
~~~~~~~~~~~~~~~

Get the current timestamp in seconds from RTC.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int32_t Read(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current timestamp in seconds which is calculated from 1970.1.1 00:00:00 (YEAR.MONTH.DAY, HOUR: MIN: SECONDS).

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/RTC/examples/RTC/RTC.ino>`_

.. note :: "rtc.h" must be included to use the class function.

------------------------------------

**RTC::Wait**
------------------

**Description**
~~~~~~~~~~~~~~~

Wait for 1s/1000000 us.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void wait (float s);

**Parameters**
~~~~~~~~~~~~~~

``s``: delay time in seconds.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/RTC/examples/RTC/RTC.ino>`_

.. note :: "rtc.h" must be included to use the class function.

------------------------------------

**RTC::SetEpoch**
----------------------

**Description**
~~~~~~~~~~~~~~~

Convert human-readable time to epoch time.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int SetEpoch (int year, int month, int day, int hour, int min, int sec);

**Parameters**
~~~~~~~~~~~~~~

``year``: user input year (Default 4 digits year value - 1970)

``month``: user input month (Acceptable value ranges from 0 - 11, 0 represents January)

``day``: user input day of the month (Acceptable value ranges from 1-31)

``hour``: user input hour (Acceptable value ranges from 0-23)

``min``: user input minutes (Acceptable value ranges from 0-59)

``sec``: user input seconds (Acceptable value ranges from 0-59 or 60 for leap seconds)

**Returns**
~~~~~~~~~~~

This function returns epoch time in seconds for RTC use.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTC <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/RTC/examples/RTC/RTC.ino>`_

.. note :: "rtc.h" must be included to use the class function.
