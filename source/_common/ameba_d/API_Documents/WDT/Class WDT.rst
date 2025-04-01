Class WDT
=========

.. contents::
  :local:
  :depth: 2

**WDT Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used for initializing, starting, stopping watchdog timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class WDT

**Members**
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **Public Constructors**                                               |
+===================================+===================================+
| A public constructor should not be used as this class is intended to  |
| be a singleton class. Access member functions using the object        |
| instance named WDT.                                                   |
+-----------------------------------+-----------------------------------+
| **Public Methods**                                                    |
+-----------------------------------+-----------------------------------+
| WDT::InitWatchdog                 | Initialize the watchdog,          |
|                                   | including time setting, and mode  |
|                                   | register.                         |
+-----------------------------------+-----------------------------------+
| WDT::StartWatchdog                | Enable and start the watchdog     |
|                                   | timer                             |
+-----------------------------------+-----------------------------------+
| WDT::StopWatchdog                 | Stop the watchdog timer.          |
+-----------------------------------+-----------------------------------+
| WDT::RefreshWatchdog              | Refresh the watchdog timer to     |
|                                   | prevent WDT timeout.              |
+-----------------------------------+-----------------------------------+
| WDT::InitWatchdogIRQ              | Switch the watchdog timer to      |
|                                   | interrupt mode and register a     |
|                                   | watchdog timer timeout interrupt  |
|                                   | handler.                          |
+-----------------------------------+-----------------------------------+

**WDT::InitWatchdog**
----------------------

**Description**
~~~~~~~~~~~~~~~

Initialize the watchdog, including time setting, and mode register.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void InitWatchdog(uint32_t timeout_ms);

**Parameters**
~~~~~~~~~~~~~~

``timeout_ms``: the watch-dog timer timeout value in millisecond (ms). The default action after watchdog timer timeout is to reset the whole system.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WatchdogTimer <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/WatchdogTimer/WatchdogTimer.ino>`_

.. note :: "WDT.h" must be included to use the class function.

**WDT::StartWatchdog**
----------------------

**Description**
~~~~~~~~~~~~~~~

Start the watchdog timer by enabling the WDG state.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void StartWatchdog(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WatchdogTimer <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/WatchdogTimer/WatchdogTimer.ino>`_

.. note :: "WDT.h" must be included to use the class function.

**WDT::StopWatchdog**
---------------------

**Description**
~~~~~~~~~~~~~~~

Stop the watchdog timer by disabling the WDG state.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void StopWatchdog(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WatchdogTimer <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/WatchdogTimer/WatchdogTimer.ino>`_

.. note :: "WDT.h" must be included to use the class function.

**WDT::RefreshWatchdog**
------------------------

**Description**
~~~~~~~~~~~~~~~

Clear watchdog timer and refresh to prevent timeout.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void RefreshWatchdog(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WatchdogTimer <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/WatchdogTimer/WatchdogTimer.ino>`_

.. note :: "WDT.h" must be included to use the class function.

**WDT::InitWatchdogIRQ**
------------------------

**Description**
~~~~~~~~~~~~~~~

Switch the watchdog timer to interrupt mode and register a watchdog timer timeout interrupt handler. The interrupt handler will be called when the watchdog timer is timeout.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void InitWatchdogIRQ(wdt_irq_handler handler, uint32_t id);

**Parameters**
~~~~~~~~~~~~~~

``handler``: the callback function for WDT timeout interrupt.

``id``: the parameter for the callback function

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WatchdogTimer <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/WatchdogTimer/WatchdogTimer.ino>`_

.. note :: "WDT.h" must be included to use the class function.
