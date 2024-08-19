Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Arduino UNO x 1

Example

In the previous example *“I2C – Communicate with Arduino UNO via I2C” *,
Ameba, the I2C master, transmits data to the Arduino UNO, the I2C slave.
As to this example, Ameba is the I2C master, and receives data from the
Arduino UNO, which is the I2C slave.

-  **Setting up Arduino Uno to be I2C Slave

| First, select Arduino in the Arduino IDE in “Tools” -> “Board” ->
  “Arduino Uno”:
| Open “Examples” -> “Wire” -> “slave_sender”

|per-5-1|

Then click “Sketch” -> “Upload” to compile and upload the example to
Arduino Uno.

-  **Setting up Ameba to be I2C Master

| Next, open another window of Arduino IDE, make sure to choose your
  Ameba development board in the IDE: “Tools” -> “Board”
| Open “File” -> “Examples” -> “AmebaWire” -> “MasterReceiveData”

|image1|

Click “Sketch” -> “Upload” to compile and upload the example to Ameba.

-  **Wiring**

| The Arduino example uses A4 as the I2C SDA and A5 as the I2C SCL.
| Another important thing is that the GND pins of Arduino and Ameba
  should be connected to each other.

**AMB82 MINI** wiring diagram:

|image2|

| Next, we will observe the data receive by Ameba in the Serial Monitor.
| (Note: If you do not know which port the Ameba development board is
  connected to, please find it in the Device Manager of Windows first.
  Ameba is connected as “mbed Serial Port”. For example, if you find
  mbed Serial Port (COM15) means Ameba is connected to port COM15.)

|per-5-6|

| We select the port in “Tools” -> “Port” -> “COM15” (the port connected
  to Ameba)
| Open the Arduino IDE window of the Ameba, go to “Tools” -> “Serial
  Monitor” to display the messages printed by Ameba.
| Press the reset button on Arduino Uno, Arduino Uno now waits for
  connection from I2C master.
| Then press the reset button on Ameba, Ameba will start to receive
  messages from Arduino Uno. And you can see the “hello ” message
  printed every half second in serial monitor.
| (NOTE: If the message does not show in the Serial Monitor of Ameba,
  please close and open the serial monitor again.)

|per-5-8|

Code Reference

| You can find detailed information of this example in the documentation
  of Arduino:
| https://www.arduino.cc/en/Tutorial/MasterReader

 

| First use Wire.begin()/Wire.begin(address) to join the I2C bus as a
  master or slave, in the Master case the address is not required.
| https://www.arduino.cc/en/Reference/WireBegin

 

| Next, the Master uses Wire.requestFrom() to specify from which Slave
  to request data.
| https://www.arduino.cc/en/Reference/WireRequestFrom

.. |per-5-1| image:: ../../_static/Example_Guides/I2C_-_Master_Receive_Data_from_Arduino_UNO/I2C_-_Master_Receive_Data_from_Arduino_UNO_images/image01.png
   :width: 3.31304in
   :height: 4.98572in
.. |image1| image:: ../../_static/Example_Guides/I2C_-_Master_Receive_Data_from_Arduino_UNO/I2C_-_Master_Receive_Data_from_Arduino_UNO_images/image02.png
   :width: 3.43329in
   :height: 4.84373in
.. |image2| image:: ../../_static/Example_Guides/I2C_-_Master_Receive_Data_from_Arduino_UNO/I2C_-_Master_Receive_Data_from_Arduino_UNO_images/image03.png
   :width: 6.26111in
   :height: 4.18423in
.. |per-5-6| image:: ../../_static/Example_Guides/I2C_-_Master_Receive_Data_from_Arduino_UNO/I2C_-_Master_Receive_Data_from_Arduino_UNO_images/image04.png
   :width: 4.52153in
   :height: 4.21736in
.. |per-5-8| image:: ../../_static/Example_Guides/I2C_-_Master_Receive_Data_from_Arduino_UNO/I2C_-_Master_Receive_Data_from_Arduino_UNO_images/image05.png
   :width: 6.26806in
   :height: 3.96111in
