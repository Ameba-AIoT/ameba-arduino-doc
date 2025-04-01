Class SPISettings
=================

.. contents::
  :local:
  :depth: 2

**SPISettings Class**
---------------------

**Description**
~~~~~~~~~~~~~~~

A class to set SPI parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class SPISettings

**Members**
~~~~~~~~~~~

+-------------------------------+--------------------------------------------------+
| **Public Constructors**                                                          |
+===============================+==================================================+
| SPISettings::SPISettings      | Create a SPISettings object and set SPI clock    |
|                               | speed, bit order and data mode                   |
+-------------------------------+--------------------------------------------------+

-----------------------------------------------------------

**SPISettings::SPISettings**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Construct an object and configure SPI parameters — clock speed, bit order and data mode to the preferred default value.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    SPISettings(uint32_t clock, BitOrder bitOrder, uint8_t dataMode)

**Parameters**
~~~~~~~~~~~~~~

``clock``: SPI clock speed in Hz. Default value is 4000000.

``bitOrder``: The bit order of transmitting command/address/data. Default value is MSBFIRST.

    - MSBFIRST (MSB: Most Significant Bit)

    - LSBFIRST (LSB: Least Significant Bit)

``dataMode``: SPI has four modes that correspond to the four possible clocking configurations. Default value is SPI_MODE0.

    - SPI_MODE0, SPI_MODE1, SPI_MODE2, SPI_MODE3

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: This class seldom used alone, it is always used with beginTransaction() as a parameter in SPIClass.

.. note :: "SPI.h" must be included to use the class function.
