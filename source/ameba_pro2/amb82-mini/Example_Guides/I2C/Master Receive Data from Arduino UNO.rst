Master Receive Data from Arduino UNO
====================================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  Arduino UNO x 1

Example
-------

I2C Introduction
~~~~~~~~~~~~~~~~

There are two roles in the operation of I2C, one is "master", the other
is "slave". Only one master is allowed and can be connected to many
slaves. Each slave has its unique address, which is used in the
communication between master and the slave. I2C uses two pins, one is
for data transmission (SDA), the other is for the clock (SCL). Master
uses the SCL to inform slave of the upcoming data transmission, and the
data is transmitted through SDA. The I2C example was named "Wire" in the
Arduino example.

Introduction
~~~~~~~~~~~~

In the example "I2C - Send Data to Arduino Uno", Ameba, the I2C master, transmits data to the Arduino UNO, the I2C slave.
As to this example, Ameba is the I2C master, and receives data from the Arduino UNO, which is the I2C slave.

Procedure
~~~~~~~~~

-  **Setting up Arduino Uno to be I2C Slave**

| First, select Arduino in the Arduino IDE in "Tools" -> "Board" -> "Arduino Uno":
| Open "Examples" -> "Wire" -> "slave_sender"

|image01|

Then click "Sketch" -> "Upload" to compile and upload the example to Arduino Uno.

-  **Setting up Ameba to be I2C Master**

| Next, open another window of Arduino IDE, make sure to choose your Ameba development board in the IDE: "Tools" -> "Board"
| Open "File" -> "Examples" -> "AmebaWire" -> "MasterReceiveData"

|image02|

Click "Sketch" -> "Upload" to compile and upload the example to Ameba.

-  **Wiring**

| The Arduino example uses A4 as the I2C SDA and A5 as the I2C SCL.
| Another important thing is that the GND pins of Arduino and Ameba should be connected to each other.

**AMB82 MINI** wiring diagram:

|image03|

| Next, we will observe the data receive by Ameba in the Serial Monitor.
| (Note: If you do not know which port the Ameba development board is
  connected to, please find it in the Device Manager of Windows first.
  Ameba is connected as "mbed Serial Port". For example, if you find
  mbed Serial Port (COM15) means Ameba is connected to port COM15.)

|image04|

| We select the port in "Tools" -> "Port" -> "COM15" (the port connected to Ameba)
| Open the Arduino IDE window of the Ameba, go to "Tools" -> "Serial Monitor" to display the messages printed by Ameba.
| Press the reset button on Arduino Uno, Arduino Uno now waits for connection from I2C master.
| Then press the reset button on Ameba, Ameba will start to receive
  messages from Arduino Uno. And you can see the "hello" message
  printed every half second in serial monitor.
| (NOTE: If the message does not show in the Serial Monitor of Ameba,
  please close and open the serial monitor again.)

|image05|

Code Reference
--------------

| You can find detailed information of this example in the documentation of Arduino:
| https://www.arduino.cc/en/Tutorial/MasterReader

| First use ``Wire.begin()`` / ``Wire.begin(address)`` to join the I2C bus as a master or slave, in the Master case the address is not required.
| https://www.arduino.cc/en/Reference/WireBegin

| Next, the Master uses ``Wire.requestFrom()`` to specify from which Slave to request data.
| https://www.arduino.cc/en/Reference/WireRequestFrom

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Master_Receive_Data_from_Arduino_UNO/image01.png
   :width: 683 px
   :height: 1028 px
   :scale: 80%
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Master_Receive_Data_from_Arduino_UNO/image02.png
   :width: 602 px
   :height: 849 px
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Master_Receive_Data_from_Arduino_UNO/image03.png
   :width: 1233 px
   :height: 824 px
   :scale: 70%
.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Master_Receive_Data_from_Arduino_UNO/image04.png
   :width: 434 px
   :height: 405 px
.. |image05| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Master_Receive_Data_from_Arduino_UNO/image05.png
   :width: 649 px
   :height: 410 px
