PWM - Servo Control
===================

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 / AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1
- Servo x 1 (Ex. Tower Pro SG90)

Example
-------

**Introduction**
~~~~~~~~~~~~~~~~

A typical servo has 3 wires, the red wire is for power, black or brown one should be connected to GND, and the other one is for signal data. We use PWM signal to control the rotation angle of the axis of the servo. The frequency of the signal is 50Hz, that is length 20ms. Each servo defines its pulse bandwidth, which is usually 1ms~2ms.

To control the rotation angle, for example if 1ms-length pulse rotates the axis to degree 0, then 1.5 ms pulse rotates the axis to 90 degrees, and 2 ms pulse rotates the axis to 180 degrees. Furthermore, a servo defines the "dead bandwidth", which stands for the required minimum difference of the length of two consecutive pulse for the servo to work.

**Procedure**
~~~~~~~~~~~~~

.. only:: amb21

**AMB21 / AMB22** Wiring Diagram:

|image01|

.. only:: end amb21

.. only:: amb23

**AMB23** Wiring Diagram:

|image02|

.. only:: end amb23

.. only:: bw16-typeb

**BW16** Wiring Diagram:

|image03|

.. only:: end bw16-typeb

.. only:: bw16-typec

**BW16-TypeC** Wiring Diagram:

|image04|

.. only:: end bw16-typec

.. only:: aw-cu488

**AW-CU488 Thing Plus** Wiring Diagram:

|image05|

.. only:: end aw-cu488

.. only:: amb25

**AMB25** Wiring Diagram:

|image06|

.. only:: end amb25

.. only:: amb26

**AMB26** Wiring Diagram:

|image07|

.. only:: end amb26

Open the example, ``"File" → "Examples" → "AmebaAnalog" → "ServoSweep"``

This example makes the servo to rotate from degree 0 to 180, and then rotate back to degree 0.

Code Reference
--------------

The Servo API of Ameba is similar to the API of Arduino. To distinguish Ameba’s Servo API from the original API of Arduino, we name the header file "AmebaServo.h" and the Class "AmebaServo". Usage is identical to the Arduino API.

The default pulse bandwidth of Arduino Servo is 0.5ms~2.4ms, which is the same as Tower Pro SG90. Therefore, we set the attached pin directly:

.. code-block:: c++

  myservo.attach(9);

Next, rotate the axis to desired position:

.. code-block:: c++

  myservo.write(pos);

.. |image01| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image01.png
   :width: 1249
   :height: 974
   :scale: 60%
.. |image02| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image02.png
   :width: 800
   :height: 633
.. |image03| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image03.png
   :width: 809
   :height: 598
.. |image04| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image04.png
   :width: 837
   :height: 620
.. |image05| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image05.png
   :width: 631
   :height: 749
.. |image06| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image06.png
   :width: 485
   :height: 450
.. |image07| image:: ../../../../_static/amebad/Example_Guides/PWM/PWM_Servo_Control/image07.png
   :width: 920
   :height: 654
   :scale: 80%
