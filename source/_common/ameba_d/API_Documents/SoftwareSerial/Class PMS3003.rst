Class PMS3003
=============

**PMS3003 Class**
------------------

**Description**
~~~~~~~~~~~~~~~

Defines a class to work with PMS3003 air quality sensor on Ameba.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class PMS3003

**Members**
~~~~~~~~~~~

+-----------------------------------+-----------------------------------------+
| **Public Constructors**                                                     |
+===================================+=========================================+
| PMS3003::PMS3003                  | Constructs a PMS3003 object             |
+-----------------------------------+-----------------------------------------+
| **Public Methods**                                                          |
+-----------------------------------+-----------------------------------------+
| PMS3003::begin                    | Initialize hardware UART                |
+-----------------------------------+-----------------------------------------+
| PMS3003::end                      | Free allocated space thus stopping UART |
+-----------------------------------+-----------------------------------------+
| PMS3003::get_pm1p0_cf1            | Get PM1.0 under correction factor = 1   |
+-----------------------------------+-----------------------------------------+
| PMS3003:: get_pm2p5_cf1           | Get PM2.5 under correction factor = 1   |
+-----------------------------------+-----------------------------------------+
| PMS3003:: get_pm10_cf1            | Get PM10 under correction factor = 1    |
+-----------------------------------+-----------------------------------------+
| PMS3003:: get_pm1p0_air           | Get PM1.0 air quality                   |
+-----------------------------------+-----------------------------------------+
| PMS3003:: get_pm2p5_air           | Get PM2.5 air quality                   |
+-----------------------------------+-----------------------------------------+
| PMS3003:: get_pm10_air            | Get PM10 air quality                    |
+-----------------------------------+-----------------------------------------+
| PMS3003:update_cache              | Updates the cache memory                |
+-----------------------------------+-----------------------------------------+
| PMS3003::pms3003_handle_interrupt | Set up the serial event handler         |
+-----------------------------------+-----------------------------------------+

---------------------------------------------------------------------------------------

**PMS3003::PMS3003**
--------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a PMS3003 object and initialize the pin mapping.

**Syntax**
~~~~~~~~~~

.. code:: c++

  PMS3003(int _rx, int _tx, int _set, int _reset);

**Parameters**
~~~~~~~~~~~~~~

``_rx``: RX pin of UART

``_tx``: TX pin of UART

``_set``: Set pin value (Default: -1)

``_reset``: Reset pin value (Default: -1)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

-----------------------------------------------------------------------------------

**PMS3003::begin**
------------------

**Description**
~~~~~~~~~~~~~~~

Initialize hardware UART and allocate space for serial buffer

**Syntax**
~~~~~~~~~~

.. code:: c++

  void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

-----------------------------------------------------------------------------------

**PMS3003::end**
----------------

**Description**
~~~~~~~~~~~~~~~

Free serial buffer space and stop UART

**Syntax**
~~~~~~~~~~

.. code:: c++

  void end(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

----------------------------------------------------------------------------------

**PMS3003::get_pm1p0_cf1**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Get value of PM1.0 under correction factor = 1.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int get_pm1p0_cf1(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the value "pm1p0_cf1" as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

--------------------------------------------------------------------------------

**PMS3003::get_pm2p5_cf1**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Get value of PM2.5 under correction factor = 1

**Syntax**
~~~~~~~~~~

.. code:: c++

  int get_pm2p5_cf1(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the value of "pm2p5_cf1" as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

------------------------------------------------------------------------------

**PMS3003::get_pm10_cf1**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the value of PM10 under correction factor = 1.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int get_pm10_cf1(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the value of "pm10_cf1" as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

------------------------------------------------------------------------------

**PMS3003::get_pm1p0_air**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Get PM1.0 air quality

**Syntax**
~~~~~~~~~~

.. code:: c++

  int PMS3003::get_pm1p0_air(void)

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the value of "pm1p0_air" as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

-----------------------------------------------------------------------------

**PMS3003::get_pm2p5_air**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Get PM2.5 air quality.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int get_pm2p5_air(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the value of "pm2p5_air" as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

------------------------------------------------------------------------------

**PMS3003::get_pm10_air**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get PM10 air quality.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int get_pm10_air(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the value of "pm10_air" as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.

------------------------------------------------------------------------------

**PMS3003::pms3003_handle_interrupt**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set up the serial event handler

**Syntax**
~~~~~~~~~~

.. code:: c++

  void pms3003_handle_interrupt(uint32_t id, uint32_t event);

**Parameters**
~~~~~~~~~~~~~~

``id``: The device identifier

``event``: Serial event for handling incoming data

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PMS3003.h" must be included to use the class function.
