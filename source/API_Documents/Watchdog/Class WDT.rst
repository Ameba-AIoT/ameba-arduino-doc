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
| **Public Constructors**           |                                   |
+===================================+===================================+
| WDT::WDT                          | Constructs an WDT object.         |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
| **Public Methods**                |                                   |
+-----------------------------------+-----------------------------------+
| WDT::init                         | Initialize the watchdog,          |
|                                   | including time setting, and mode  |
|                                   | register.                         |
+-----------------------------------+-----------------------------------+
| WDT::start                        | Enable and start the watchdog     |
|                                   | timer                             |
+-----------------------------------+-----------------------------------+
| WDT::stop                         | Stop the watchdog timer.          |
+-----------------------------------+-----------------------------------+
| WDT::refresh                      | Refresh the watchdog timer to     |
|                                   | prevent WDT timeout.              |
+-----------------------------------+-----------------------------------+
| WDT::init_irq                     | Switch the watchdog timer to      |
|                                   | interrupt mode and register a     |
|                                   | watchdog timer timeout interrupt  |
|                                   | handler.                          |
+-----------------------------------+-----------------------------------+

**WDT::init**
-------------

**Description**
~~~~~~~~~~~~~~~

Initialize the watchdog, including time setting, and mode register.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void init(uint32_t timeout_ms);

**Parameters**
~~~~~~~~~~~~~~

timeout_ms: the watch-dog timer timeout value in millisecond (ms). The default action after watchdog timer timeout is to reset the whole system.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleWDT <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/SimpleWDT/SimpleWDT.ino>`_

.. note :: “WDT.h” must be included to use the class function.

**WDT::start**
--------------

**Description**
~~~~~~~~~~~~~~~

Start the watchdog timer by enabling the WDG state.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void start(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleWDT <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/SimpleWDT/SimpleWDT.ino>`_

.. note :: “WDT.h” must be included to use the class function.

**WDT::stop**
-------------

**Description**
~~~~~~~~~~~~~~~

Stop the watchdog timer by disabling the WDG state.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void stop(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleWDT <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/SimpleWDT/SimpleWDT.ino>`_

.. note :: “WDT.h” must be included to use the class function.

**WDT::refresh**
----------------

**Description**
~~~~~~~~~~~~~~~

Clear watchdog timer and refresh to prevent timeout.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void refresh(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleWDT <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/SimpleWDT/SimpleWDT.ino>`_

.. note :: “WDT.h” must be included to use the class function.

**WDT::init_irq**
-----------------

**Description**
~~~~~~~~~~~~~~~

Switch the watchdog timer to interrupt mode and register a watchdog  timer timeout interrupt handler. The interrupt handler will be called when the watchdog timer is timeout.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void init_irq(wdt_irq_handler handler, uint32_t id);

**Parameters**
~~~~~~~~~~~~~~

handler: the callback function for WDT timeout interrupt.

id: the parameter for the callback function.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleWDT <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Watchdog/examples/SimpleWDT/SimpleWDT.ino>`_

.. note :: “WDT.h” must be included to use the class function.
