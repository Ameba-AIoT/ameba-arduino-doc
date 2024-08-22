Introduction of I2C

There are two roles in the operation of I2C, one is “master”, the other
is “slave”. Only one master is allowed and can be connected to many
slaves. Each slave has its unique address, which is used in the
communication between master and the slave. I2C uses two pins, one is
for data transmission (SDA), the other is for the clock (SCL). Master
uses the SCL to inform slave of the upcoming data transmission, and the
data is transmitted through SDA. The I2C example was named “Wire” in the
Arduino example.

Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Arduino UNO x 1

Example

In this example, we use Ameba as the I2C master writer, and use Arduino
as the I2C slave receiver.

When the I2C slave receives string sent from I2C master, it prints the
received string.

-  **Setting up Arduino Uno to be I2C Slave**

| First, select Arduino in the Arduino IDE in “Tools” -> “Board” ->
  “Arduino Uno”
| Open the “Slave Receiver” example in “Examples” -> “Wire” ->
  “slave_receiver”:

|4-1|

Then click “Sketch” -> “Upload” to compile and upload the example to
Arduino Uno.

-  Setting up Ameba to be I2C Master

| Next, open another window of Arduino IDE, make sure to choose your
  Ameba development board in the IDE: “Tools” -> “Board”
| Then open the “Master Writer” example in “File” -> “Examples” ->
  “AmebaWire” -> “MasterSendData”

|image1|

-  Wiring

| The Arduino example uses A4 as the I2C SDA and A5 as the I2C SCL.
| Another important thing is that the GND pins of Arduino and Ameba
  should be connected to each other.

AMB82 MINI wiring diagram:

|image2|

| Open the Arduino IDE of the Arduino Uno and open the serial monitor
  (“Tools” -> “Serial Monitor”).
| In the Serial Monitor, you can see the messages printed from Arduino
  Uno.
| Next, press the reset button on Arduino Uno. Now the Arduino Uno is
  waiting for the connection from I2C Master.
| We press the reset button on Ameba to start to send messages. Then
  observe the serial monitor, you can see the messages show up every
  half second.

|4-6|

Code Reference

| You can find detailed information of this example in the documentation
  of Arduino:
| https://www.arduino.cc/en/Tutorial/MasterWriter

| First use Wire.begin()/Wire.begin(address) to join the I2C bus as a
  master or slave, in the Master case the address is not required.
| https://www.arduino.cc/en/Reference/WireBegin

| Next, the Master uses Wire.beginTransmission(address) to begin a
  transmission to the I2C slave with the given address:
| https://www.arduino.cc/en/Reference/WireBeginTransmission

| Uses Wire.write() to send data, and finally use Wire.endTransmission()
  to end a transmission to a Slave and transmits the bytes that were
  queued:
| https://www.arduino.cc/en/Reference/WireEndTransmission

.. |4-1| image:: ../../_static/Example_Guides/I2C_-_Master_Send_Data_to_Arduino_UNO/I2C_-_Master_Send_Data_to_Arduino_UNO_images/image01.png
   :width: 3.81798in
   :height: 6.7913in
.. |image1| image:: ../../_static/Example_Guides/I2C_-_Master_Send_Data_to_Arduino_UNO/I2C_-_Master_Send_Data_to_Arduino_UNO_images/image02.png
   :width: 3.70343in
   :height: 5.12515in
.. |image2| image:: ../../_static/Example_Guides/I2C_-_Master_Send_Data_to_Arduino_UNO/I2C_-_Master_Send_Data_to_Arduino_UNO_images/image03.png
   :width: 3.93982in
   :height: 2.6004in
.. |4-6| image:: ../../_static/Example_Guides/I2C_-_Master_Send_Data_to_Arduino_UNO/I2C_-_Master_Send_Data_to_Arduino_UNO_images/image04.png
   :width: 6.26806in
   :height: 3.96111in
