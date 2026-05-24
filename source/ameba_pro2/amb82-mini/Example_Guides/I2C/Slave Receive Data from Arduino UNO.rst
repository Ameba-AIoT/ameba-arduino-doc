Slave Receive Data from Arduino UNO
====================================

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

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

In this example, the AMB82-mini is configured as an I2C slave receiver
at address 0x08, while the Arduino UNO acts as the I2C master writer.
The Arduino UNO repeatedly sends 6 bytes of data to the AMB82-mini,
and the AMB82-mini prints the received data on its Serial Monitor.

Procedure
~~~~~~~~~

-  **Setting up Arduino Uno to be I2C Master**

| First, select Arduino in the Arduino IDE in :guilabel:`Tools -> Board -> Arduino Uno`
| Open the "Master Writer" example in :guilabel:`Examples -> Wire -> master_writer`

|image01|

Then click :guilabel:`Sketch -> Upload` to compile and upload the example to Arduino Uno.

-  **Setting up AMB82-mini to be I2C Slave**

| Next, open another window of Arduino IDE, make sure to choose your AMB82-mini development board in the IDE :guilabel:`Tools -> Board`
| Open the "Slave Receive Data" example in :guilabel:`File -> Examples -> AmebaWire -> SlaveReceiveData`

|image02|

Click :guilabel:`Sketch -> Upload` to compile and upload the example to AMB82-mini.

-  **Wiring**

| The Arduino UNO uses A4 as the I2C SDA and A5 as the I2C SCL.
| Connect the SDA pin (pin 12) of AMB82-mini to the SDA pin (A4) of Arduino UNO with a pull-up resistor (3.3V).
| Connect the SCL pin (pin 13) of AMB82-mini to the SCL pin (A5) of Arduino UNO with a pull-up resistor (3.3V).
| Another important thing is that the GND pins of Arduino UNO and AMB82-mini should be connected to each other.


| Open the Serial Monitor of AMB82-mini in :guilabel:`Tools -> Serial Monitor`
| Press the reset button on AMB82-mini first to initialize the slave, then press the reset button on Arduino UNO to start sending data.
| The AMB82-mini will receive and print the data from the master continuously in the Serial Monitor.

|image03|

Code Reference
--------------

| Use ``Wire.begin(address)`` to join the I2C bus as a slave with the given address.
| https://www.arduino.cc/en/Reference/WireBegin

| Use ``Wire.onReceive(handler)`` to register a callback function that is called when the slave receives data from the master.
| https://www.arduino.cc/en/Reference/WireOnReceive

| Use ``Wire.available()`` to return the number of bytes available for retrieval with ``Wire.read()``.
| https://www.arduino.cc/en/Reference/WireAvailable

| Use ``Wire.read()`` to read a byte that was transmitted from a master device to a slave device.
| https://www.arduino.cc/en/Reference/WireRead

| Use ``Wire.slaveReadLen()`` to set the expected number of bytes to read from the master.

| Use ``Wire.slaveClrRxFlag()`` to clear the receive flag, allowing the slave to be ready for the next transmission from the master.

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Slave_Receive_Data_from_Arduino_UNO/image01.png
   :width: 646 px
   :height: 696 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Slave_Receive_Data_from_Arduino_UNO/image02.png
   :width: 634 px
   :height: 678 px
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/I2C/Slave_Receive_Data_from_Arduino_UNO/image03.png
   :width: 239 px
   :height: 346 px
