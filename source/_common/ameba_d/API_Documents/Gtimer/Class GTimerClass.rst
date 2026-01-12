Class GTimerClass
=================

**GTimerClass Class**
---------------------

**Description**
~~~~~~~~~~~~~~~

A class used for managing GTimer settings. GTimer is a hardware timer and occupy same resource as PWM. Please make sure the timer is not conflict with you PWM index.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class GTimerClass

**Members**
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **Public Constructors**                                               |
+===================================+===================================+
| GTimerClass:: GTimerClass         | Constructs a GTimerClass object   |
+-----------------------------------+-----------------------------------+
| **Public Methods**                                                    |
+-----------------------------------+-----------------------------------+
| GTimerClass::begin                | Initialize a timer and start it   |
|                                   | immediately                       |
+-----------------------------------+-----------------------------------+
| GTimerClass::stop                 | Stop a specific timer             |
+-----------------------------------+-----------------------------------+
| GTimerClass::reload               | Reload a specific timer           |
+-----------------------------------+-----------------------------------+
| GTimerClass::read_us              | Read current countdown value      |
+-----------------------------------+-----------------------------------+

**GtimerCass::begin**
---------------------

**Description**
~~~~~~~~~~~~~~~

Initialize a timer and start it immediately.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(uint32_t timerid, uint32_t duration_us, void (*handler)(uint32_t), bool periodical, uint32_t userdata);

**Parameters**
~~~~~~~~~~~~~~

``timerid``: GTimer ID. (There are 5 valid GTimer with timer id 0~4)

``duration_us``: The duration of timer unit is microsecond (us). The precision is 32768Hz.

``periodical``: By default, the timer would keep periodically countdown and reload, which means the handler would periodically be invoked. (Default value: True)

``userdata``: The user data brings to the handler. Default value is 0.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `TimerOneshot <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/GTimer/examples/TimerOneshot/TimerOneshot.ino>`_

.. note :: "GTimer.h" must be included to use the class function.

**GtimerCass::stop**
--------------------

**Description**
~~~~~~~~~~~~~~~

Stop a specific timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void stop(uint32_t timerid);

**Parameters**
~~~~~~~~~~~~~~

``timerid``: Stop the timer with the selected timer id. (There are 5 valid GTimer with timer id 0~4)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `TimerPeriodical <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/GTimer/examples/TimerPeriodical/TimerPeriodical.ino>`_

.. note :: "GTimer.h" must be included to use the class function.

**GtimerCass::reload**
----------------------

**Description**
~~~~~~~~~~~~~~~

Reload a specific timer by changing the duration_us. The GTimer is a countdown timer. Reload it would make it discard the current countdown value and restart countdown based on the duration (in us).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    reload(uint32_t timerid, uint32_t duration_us);

**Parameters**
~~~~~~~~~~~~~~

``timerid``: The timer to be modified. (There are 5 valid GTimer with timer id 0~4)

``duration_us``: The updated duration to be set (in us).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "GTimer.h" must be included to use the class function.

**GtimerCass::read_us**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Read the current countdown time value (in us).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint64_t read_us(uint32_t timerid);

**Parameters**
~~~~~~~~~~~~~~

``timerid``: The timer to be read. (There are 5 valid GTimer with timer id 0~4)

**Returns**
~~~~~~~~~~~

This function returns "0" if the timerid is invalid, otherwise, returns the current countdown time value (in us).

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "GTimer.h" must be included to use the class function.
