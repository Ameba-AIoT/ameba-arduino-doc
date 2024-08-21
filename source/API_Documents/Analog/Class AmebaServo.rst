Class AmebaServo
================

.. contents::
  :local:
  :depth: 2

**AmebaServo Class**
--------------------

**Description**
~~~~~~~~~~~~~~~

A class used for controlling servo motors connected to Ameba boards.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class AmebaServo

**Members**
~~~~~~~~~~~

+-------------------------------+-----------------------------------------+
| **Public Constructors**                                                 |
+===============================+=========================================+
| AmebaServo::AmebaServo        | Constructs an AmebaServo object.        |
+-------------------------------+-----------------------------------------+
| **Public Methods**                                                      |
+-------------------------------+-----------------------------------------+
| AmebaServo::attach            | Attach a PWM pin to control servo.      |
+-------------------------------+-----------------------------------------+
| AmebaServo::detach            | Detach the servo.                       |
+-------------------------------+-----------------------------------------+
| AmebaServo::write             | Write a value to control servo. The     |
|                               | value is between 0 - 180 degrees.       |
+-------------------------------+-----------------------------------------+
| AmebaServo::writeMicroseconds | Write a value to control servo. The     |
|                               | value is between 544 - 2400us.          |
+-------------------------------+-----------------------------------------+
| AmebaServo::read              | Read the value from servo and returns   |
|                               | current pulse width as an angle between |
|                               | 0 and 180 degrees.                      |
+-------------------------------+-----------------------------------------+
| AmebaServo::readMicroseconds  | Read the value from servo and returns   |
|                               | current pulse width in microseconds.    |
+-------------------------------+-----------------------------------------+
| AmebaServo::attached          | Check if the servo is attached.         |
+-------------------------------+-----------------------------------------+

**AmebaServo::attach**
----------------------

**Description**
~~~~~~~~~~~~~~~

Attach a PWM pin to control servo on Ameba boards. Minimum and maximum pulse width can be set optionally.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t attach(int pin);
    uint8_t attach(int pin, int min, int max);

**Parameters**
~~~~~~~~~~~~~~

pin: A PWM pin that is one of the Ameba boards' PWM pins.

min: Minimum pulse width to be set for PWM. Default value is 544us.

max: Maximum pulse width to be set for PWM. Default value is 2400us.

**Returns**
~~~~~~~~~~~
0

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ServoSweep <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Analog/examples/ServoSweep/ServoSweep.ino>`_


The code demonstrates a servo motor sweeping from 0 - 180 - 0 degrees, in 1-degree intervals.

.. note :: “AmebaServo.h” must be included to use the class function.

**AmebaServo::detach**
----------------------

**Description**
~~~~~~~~~~~~~~~

Detach the servo by disabling the PWM pin previously set in attach().

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void detach(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AmebaServo.h” must be included to use the class function.

**AmebaServo::write**
---------------------

**Description**
~~~~~~~~~~~~~~~

Write an integer value to control servo. The value is between 0 - 180 degrees.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void write(int value);

**Parameters**
~~~~~~~~~~~~~~

value: An integer value.

- 0 to 180 (If the value is < 0, it will be taken as 0 and if the value >180, it will be taken as 180)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~
Example: `ServoSweep <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Analog/examples/ServoSweep/ServoSweep.ino>`_

.. note :: “AmebaServo.h” must be included to use the class function.

**AmebaServo::writeMicroseconds**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Write a value to control servo. The value is between 544 - 2400us that represents pulse width.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void writeMicroseconds(int value);

**Parameters**
~~~~~~~~~~~~~~

value: An integer value (us) as pulse width.

- 544 to 2400 (If the value is < 544, it will be taken as 544 and if the value > 2400, it will be taken as 2400)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AmebaServo.h” must be included to use the class function.

**AmebaServo::read**
--------------------

**Description**
~~~~~~~~~~~~~~~

The function reads the value from servo and returns current pulse width as an angle between 0 - 180 degrees.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int read(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns integer value that represents pulse width between 0 - 180 degrees.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AmebaServo.h” must be included to use the class function.

**AmebaServo::readMicroseconds**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

The function reads and returns the pulse width of the current servo in microseconds.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int readMicroseconds(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns an integer value that represents pulse width in microseconds.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AmebaServo.h” must be included to use the class function.

**AmebaServo::attached**
------------------------

**Description**
~~~~~~~~~~~~~~~

Check if the servo PWM pin is attached successfully.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    bool attached(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns 1 if the servo has been attached, else it returns 0.

**Example Code**
~~~~~~~~~~~~~~~~
Example: `ServoSweep <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Analog/examples/ServoSweep/ServoSweep.ino>`_

.. note :: “AmebaServo.h” must be included to use the class function.
