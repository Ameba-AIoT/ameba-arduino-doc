Class PMClass
=============

**PMClass Class**
-----------------

**Description**
~~~~~~~~~~~~~~~~~

A class used for PowerMode control.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class PMClass

**Members**
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **Public Constructors**                                               |
+===================================+===================================+
| PMClass::PMClass                  | Constructs an PMClass object.     |
+-----------------------------------+-----------------------------------+
| **Public Methods**                                                    |
+-----------------------------------+-----------------------------------+
| PMClass::begin                    | Initializes the PowerMode         |
|                                   | settings for device, include type |
|                                   | of the mode, wake up sources      |
|                                   | , retention and related source    |
|                                   | settings.                         |
+-----------------------------------+-----------------------------------+
| PMClass::start                    | Start the PowerMode of device.    |
+-----------------------------------+-----------------------------------+

**PMClass::begin**
~~~~~~~~~~~~~~~~~~

**Description**
~~~~~~~~~~~~~~~

Initializes the PowerMode settings for device, include type of the mode, wake up sources, retention and related source settings.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(uint32_t sleep_mode, int wakeup_source, uint32_t retention, uint32_t wakeup_setting = 0);

**Parameters**
~~~~~~~~~~~~~~

sleep_mode: Power Mode selection.

- Deepsleep mode: DEEPSLEEP_MODE; Standby mode: STANDBY_MODE

wakeup_source: Wake up source selection.

- AON timer, AON GPIO, RTC, PON GPIO, UART/Serial1, and Gtimer0 (0 to 5).

retention: Retention on/off
- On: 1; Off: 0

wakeup_setting: Settings for different wakeup sources. Default value is 0.

- For AON time, it is a pointer to an array that stores clock(1:4MHz; 0:100kHz) and duration(by seconds).

- For AON GPIO, it is pin number 21 or 22.

- For RTC, it is a pointer to an array that stores time duration as day, hour, min and sec(0, 0:0:0, to 365, 23:59:59).

- For PON GPIO, it is pin number 0 to 11.

- For Gtimer0, it is time duration in seconds. (start from 1s)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleepMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/DeepSleepMode/DeepSleepMode.ino>`__ `StandbyMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/StandbyMode/StandbyMode.ino>`__ `RetentionDeepSleepMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/RetentionDeepSleepMode/RetentionDeepSleepMode.ino>`__ `RetentionStandbyMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/RetentionStandbyMode/RetentionStandbyMode.ino>`_

.. note :: "PowerMode.h" must be included to use the class function.

**PMClass::start**
------------------

**Description**
~~~~~~~~~~~~~~~

Start the PowerMode of device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void start(void);
    void start(int year, int month, int day, int hour, int min, int sec);

**Parameters**
~~~~~~~~~~~~~~

Optional when wake up source is RTC. Default start time is 1970.1.100:00:00.

year: Start time by year.

- Starts from 1900

month: Start time by month.

- 0 to 11

day: Start time by day.

- 1 to 365

hour: Start time by hour

- 0 to 23

min: Start time by min.

- 0 to 59

sec: Start time by sec.

- 0 to 59

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleepMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/DeepSleepMode/DeepSleepMode.ino>`__ `StandbyMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/StandbyMode/StandbyMode.ino>`__ `RetentionDeepSleepMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/RetentionDeepSleepMode/RetentionDeepSleepMode.ino>`__ `RetentionStandbyMode <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/PowerMode/examples/RetentionStandbyMode/RetentionStandbyMode.ino>`_

.. note :: "PowerMode.h" must be included to use the class function.
