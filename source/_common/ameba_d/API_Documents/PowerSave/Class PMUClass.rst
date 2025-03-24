Class PMUClass
==============

.. contents::
  :local:
  :depth: 2

**PMUClass Class**
------------------

**Description**
~~~~~~~~~~~~~~~

A class used for reducing power consumption.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class PMUClass

**Members**
~~~~~~~~~~~

+--------------------------------------+----------------------------------------------+
| **Public Constructors**                                                             |
+======================================+==============================================+
| PMUClass::PMUClass                   | Constructs a PMUClass object.                |
+--------------------------------------+----------------------------------------------+
| **Public Methods**                                                                  |
+--------------------------------------+----------------------------------------------+
| PMUClass::begin                      | Initialize the PMUClass and select sleep     |
|                                      | mode as Deep Sleep mode or Tickless mode.    |
+--------------------------------------+----------------------------------------------+
| PMUClass::AONTimerDuration           | Set the duration of always-on (AON) Timer.   |
+--------------------------------------+----------------------------------------------+
| PMUClass::AONTimerCmd                | Disable the AON Timer.                       |
+--------------------------------------+----------------------------------------------+
| PMUClass::RTCWakeSetup               | Set up RTC Timer for power save usage.       |
+--------------------------------------+----------------------------------------------+
| PMUClass::enable                     | Enable power save Deep Sleep mode.           |
+--------------------------------------+----------------------------------------------+
| PMUClass::AONWakeReason              | Get the source that awakens AON.             |
+--------------------------------------+----------------------------------------------+
| PMUClass::WakePinCheck               | Check for AON GPIO wake pin index used as    |
|                                      | wake-up source.                              |
+--------------------------------------+----------------------------------------------+
| PMUClass::AONWakeClear               | Clear all the AON wakeup sources.            |
+--------------------------------------+----------------------------------------------+
| PMUClass::DsleepWakeStatusGet        | Get deep sleep mode status.                  |
+--------------------------------------+----------------------------------------------+
| PMUClass::TL_sysactive_time          | Set the system active time for tickless      |
|                                      | mode.                                        |
+--------------------------------------+----------------------------------------------+
| PMUClass::TL_wakelock                | Set tickless mode wakelock.                  |
+--------------------------------------+----------------------------------------------+
| PMUClass::DS_AON_TIMER_WAKEUP        | AON timer set as wake-up source for Deep     |
|                                      | Sleep Mode.                                  |
+--------------------------------------+----------------------------------------------+
| PMUClass::DS_RTC_WAKEUP              | RTC timer is set as wake-up source for       |
|                                      | Deep Sleep Mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::TL_UART_WAKEUP             | LOGUART is set as wake-up source for         |
|                                      | Tickless Mode.                               |
+--------------------------------------+----------------------------------------------+
| PMUClass::TL_RTC_WAKEUP              | RTC timer is set as wake-up source for       |
|                                      | Tickless Mode.                               |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA12 | AON GPIO pin 12 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA13 | AON GPIO pin 13 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA14 | AON GPIO pin 14 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA15 | AON GPIO pin 15 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA16 | AON GPIO pin 16 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA17 | AON GPIO pin 17 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA18 | AON GPIO pin 18 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA19 | AON GPIO pin 19 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA20 | AON GPIO pin 20 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA21 | AON GPIO pin 21 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA25 | AON GPIO pin 25 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+
| PMUClass::AON_WAKEPIN_WAKEUP_GPIOA26 | AON GPIO pin 26 set as wake-up source for    |
|                                      | Deep Sleep mode.                             |
+--------------------------------------+----------------------------------------------+

---------------------------------------

**PMUClass::PMUClass**
----------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a PMUClass object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    PMUClass(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::begin**
-------------------

**Description**
~~~~~~~~~~~~~~~

Initialize the PMUClass and select sleep mode as Deep Sleep mode or Tickless mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin (uint32_t sleep_mode);

**Parameters**
~~~~~~~~~~~~~~

``sleep_mode``: “11” indicates Deep Sleep Mode, “22” indicates Tickless Mode.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AONTimerDuration**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the duration of Always ON (AON) Timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AONTimerDuration(uint32_t duration_ms);

**Parameters**
~~~~~~~~~~~~~~

``duration_ms``: Set Always ON timer duration (in ms), acceptable range between 0 – 32,760,000ms.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AONTimerCmd**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Disable the AON timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AONTimerDuration(uint32_t duration_ms);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::RTCWakeSetup**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Set up a RTC timer for power usage.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void RTCWakeSetup(uint32_t duration_d, uint32_t duration_h, uint32_t duration_m, uint32_t duration_s);

**Parameters**
~~~~~~~~~~~~~~

``duration_d``: set the duration in days. Minimum valid value from 0. Valid value must be 0 or greater than 0.

``duration_h``: set the duration in hours. Minimum valid value from 0. Valid value must be 0 or greater than 0.

``duration_m``: set the duration in minutes. Minimum valid value from 0. Valid value must be 0 or greater than 0.

``duration_s``: set the duration in seconds. Minimum valid value from 0. Valid value must be 0 or greater than 0.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::enable**
--------------------

**Description**
~~~~~~~~~~~~~~~

Enable power save deep sleep mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void enable(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AONWakeReason**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get the source that awakens AON. There are a total of 3 sources, using AON GPIO, RTC timer and AON timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t AONWakeReason(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the wake-up source represented as an integer value.

``1111``: wake by AON timer

``2222``: wake by RTC timer

``3333``: wake by AON GPIO pin

``0``: NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::WakePinCheck**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Check for AON GPIO pins that are used as wake up source.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int WakePinCheck(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the wake-up source represented as an integer value.

``1``: BIT(0): wakepin0

``2``: BIT(1): wakepin1

``4``: BIT(2): wakepin2

``8``: BIT(3): wakepin3

``0``: NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AONWakeClear**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Clear all AON Wakeup source.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AONWakeClear(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::DsleepWakeStatusGet**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get Deep Sleep mode status, check if Deep Sleep mode is set.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool DsleepWakeStatusGet(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns “true” when Deep Sleep mode is entered. Otherwise, return “false”.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::TL_sysactive_time**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the system active time for tickless mode.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void TL_sysactive_time(uint32_t duration_ms);

**Parameters**
~~~~~~~~~~~~~~

``duration_ms``: Set the duration of system active time (in ms).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::TL_wakelock**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Set tickless mode wakelock.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void TL_wakelock(uint32_t select_lock);

**Parameters**
~~~~~~~~~~~~~~

select_lock:

``1``: acquire to avoid KM4 from entering the Deep Sleep mode.
``0``: release and allow KM4 to enter the Deep Sleep mode.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::DS_AON_TIMER_WAKEUP**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

AON timer is set as the wake-up source for Deep Sleep Mode. “Set Deepsleep wakeup AON timer.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void DS_AON_TIMER_WAKEUP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::DS_RTC_WAKEUP**
---------------------------

**Description**
~~~~~~~~~~~~~~~

RTC timer is set as the wake-up source for Deep Sleep Mode. “Set Deepsleep wakeup RTC.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void DS_RTC_WAKEUP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::TL_UART_WAKEUP**
----------------------------

**Description**
~~~~~~~~~~~~~~~

LOGUART is set as the wake-up source for Tickless Mode. “Set Tickless wakeup LOGUART.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void TL_UART_WAKEUP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::TL_RTC_WAKEUP**
---------------------------

**Description**
~~~~~~~~~~~~~~~

RTC timer is set as the wake-up source for Tickless Mode. “Set Tickless wakeup RTC.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void TL_RTC_WAKEUP(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA12**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 12 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA12.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA12(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA13**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 13 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA13.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA13(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA14**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 14 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA14.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA14(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA15**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 15 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA15.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA15(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA16**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 16 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA16.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA16(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA17**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 17 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA17.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA17(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA18**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 18 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA18.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA18(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA19**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 19 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA19.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA19(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA20**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 20 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA20.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA20(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA21**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 21 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA21.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA21(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA25**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 25 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA25.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA25(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.

---------------------------------------

**PMUClass::AON_WAKEPIN_WAKEUP_GPIOA26**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

AON GPIO pin 26 is set as the wake-up source for Deep Sleep mode. “Set Deepsleep wakeup AON pin GPIOA26.” will be printed on Serial Monitor when this function is called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void AON_WAKEPIN_WAKEUP_GPIOA26(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DeepSleep_DHT_Eink_Example <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/PowerSave/examples/DeepSleep_DHT_Eink_Example/DeepSleep_DHT_Eink_Example.ino>`_

.. note :: “PMUClass.h” must be included to use the class function.
