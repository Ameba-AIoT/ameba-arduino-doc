**AmebaServo Class**

**Description**

A class used for controlling servo motors connected to Ameba boards.

**Syntax**

class AmebaServo

**Members**

+-----------------------+---+----------------------------------------------+
| **Public              |   |                                              |
| Constructors**        |   |                                              |
+=======================+===+==============================================+
| A                     | C |                                              |
| mebaServo::AmebaServo | o |                                              |
|                       | n |                                              |
|                       | s |                                              |
|                       | t |                                              |
|                       | r |                                              |
|                       | u |                                              |
|                       | c |                                              |
|                       | t |                                              |
|                       | s |                                              |
|                       | a |                                              |
|                       | n |                                              |
|                       | A |                                              |
|                       | m |                                              |
|                       | e |                                              |
|                       | b |                                              |
|                       | a |                                              |
|                       | S |                                              |
|                       | e |                                              |
|                       | r |                                              |
|                       | v |                                              |
|                       | o |                                              |
|                       | o |                                              |
|                       | b |                                              |
|                       | j |                                              |
|                       | e |                                              |
|                       | c |                                              |
|                       | t |                                              |
|                       | . |                                              |
+-----------------------+---+----------------------------------------------+

**Public Methods**

+----------------------------+-----------------------------------------+
| AmebaServo::attach         | Attach a PWM pin to control servo.      |
+============================+=========================================+
| AmebaServo::detach         | Detach the servo.                       |
+----------------------------+-----------------------------------------+
| AmebaServo::write          | Write a value to control servo. The     |
|                            | value is between 0 -180 degrees.        |
+----------------------------+-----------------------------------------+
| Ame                        | Write a value to control servo. The     |
| baServo::writeMicroseconds | value is between 544 - 2400us.          |
+----------------------------+-----------------------------------------+
| AmebaServo::read           | Read the value from servo and returns   |
|                            | current pulse width as an angle between |
|                            | 0 and 180 degrees.                      |
+----------------------------+-----------------------------------------+
| Am                         | Read the value from servo and returns   |
| ebaServo::readMicroseconds | current pulse width in microseconds.    |
+----------------------------+-----------------------------------------+
| AmebaServo::attached       | Check if the servo is attached.         |
+----------------------------+-----------------------------------------+

**AmebaServo::attach**
======================

**Description**

Attach a PWM pin to control servo on Ameba boards. Minimum and maximum
pulse width can be set optionally.

**Syntax**

uint8_t attach(int pin);

uint8_t attach(int pin, int min, int max);

**Parameters**

pin: A PWM pin that is one of the Ameba boards' PWM pins.

min: Minimum pulse width to be set for PWM. By default, the min is
544us.

max: Maximum pulse width to be set for PWM. By default, the max is
2400us.

**Returns**

0

**Example Code**

Example: ServoSweep
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Analog/examples/ServoSweep/ServoSweep.ino)

The code demonstrates a servo motor sweeping from 0 - 180 - 0 degrees,
in 1-degree intervals.

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.


**AmebaServo::detach**

**Description**

Detach the servo by disabling the PWM pin previously set in attach().

**Syntax**

void detach(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.

 
=

AmebaServo::write
=================

**Description**

Write an integer value to control servo. The value is between 0 -180
degrees.

**Syntax**

void write(int value);

**Parameters**

value: An integer value that should be between 0 -180. If the value is <
0, it will be taken as 0 and if the value >180, it will be taken as 180.

**Returns**

NA

**Example Code**

Example: ServoSweep
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Analog/examples/ServoSweep/ServoSweep.ino)

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.


**AmebaServo::writeMicroseconds**

**Description**

Write a value to control servo. The value is between 544 - 2400us that
represents pulse width.

**Syntax**

void writeMicroseconds(int value);

**Parameters**

value: An integer value that should be between 544 - 2400us as pulse
width. If the value is < 544us, it will be taken as 544us and if the
value > 2400us, it will be taken as 2400us.

**Returns**

NA

**Example Code**

NA

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.


**AmebaServo::read**

**Description**

The function reads the value from servo and returns current pulse width
as an angle between 0 -180 degrees.

**Syntax**

int read(void);

**Parameters**

NA

**Returns**

This function returns integer value that represents pulse width between
0 - 180 degrees.

**Example Code**

NA

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.


**AmebaServo::readMicroseconds**

**Description**

The function reads and returns the pulse width of the current servo in
microseconds.

**Syntax**

int readMicroseconds(void);

**Parameters**

NA

**Returns**

This function returns an integer value that represents pulse width in
microseconds.

**Example Code**

NA

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.


**AmebaServo::attached**

**Description**

Check if the servo PWM pin is attached successfully.

**Syntax**

bool attached(void);

**Parameters**

NA

**Returns**

This function returns 1 if the servo has been attached, else it returns
0.

**Example Code**

Example: ServoSweep
(https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Analog/examples/ServoSweep/ServoSweep.ino)

**Notes and Warnings**

“AmebaServo.h” must be included to use the class function.
