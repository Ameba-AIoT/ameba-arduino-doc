IR - Transmit IR NEC Raw Data and Decode
==========================================

.. contents::
  :local:
  :depth: 2
  
Materials
---------

- AmebaD [ AMB21 / AMB22 / BW16 / AW-CU488 Thing Plus / AMB25 / AMB26 ] x 2

- Grove - Infrared Emitter x1 (Figure 1)

- Grove - Infrared Receiver x1 (Figure 2)

Example
--------

In this example, we use two AmebaD boards that connecting with an infrared (IR) Emitter and an IR Receiver separately to transmit and receive IR NEC Raw data.

|image01|

Figure 1: Grove - Infrared Receiver

|image02|

Figure 2: Grove - Infrared Emitter

On the transmission side, the transmitter will send IR NEC raw data. The raw data can be seen as consecutive durations of “marks” and “spaces” (Figure 3) in microseconds (us).

- Mark: a specific period of sending pulses

- Space: a specific period of sending nothing

|image03|

Figure 3: A typical IR transmission and reception setup implementation

For more details, please refer to SB-Projects' topic of IR Remote Control Theory (https://www.sbprojects.net/knowledge/ir/index.php) to learn the theory of IR remote controls operation and a collection of IR protocol descriptions. In this example, we are going to use NEC (Now Renesas, also known as Japanese Format) as the transmission protocol.

**NEC Features**

- 8-bit address and 8-bit command length.

- Extended mode available, doubling the address size.

- Address and command are transmitted twice for reliability.

- Pulse distance modulation.

- The carrier frequency of 38kHz.

- Bit time of 1.125ms or 2.25ms.

**Modulation**

NEC protocol uses Pulse Distance Encoding of the bits for data communication (Figure 4). A logical "1" is represented by total duration of 2250us, with 560us of “marks” and (2250-560) us of “spaces”. While logical ”0” is represented by total duration of 1120us, with 560us “marks” and (1120-560) us of “spaces”.

|image04|

Figure 4: Modulation of NEC

Since a total number of 32-bit data together with the header and the end-bit will be transferred (Figure 5).

If we separate the data in the time-frame (in us), there will be ( 2 + 32 ) x 2 + 1 = 69 "marks" / "spaces" to be transmitted (Figure 6), which forms the raw NEC data we would like to transmit in our Arduino ".ino" file. This part of the code can be modified by users. Details of how to obtain raw data code for your remote devices, you may refer to Ken Shirriff's blog, where it provides multiple libraries provided online.

|image05|

Figure 5: Sample of a Full NEC Data (in logic 1 or 0)

|image06|

Figure 6: Sample of a Full NEC RAW Data (in us)

**IR Emitter**

|image13|

**IR receiver**

|image14|

After the connection is being set up correctly, we will move to the coding part for this example. First, make sure the correct Ameba development board is selected in Arduino IDE: “Tools” -> “Board”.

Open the “IRSendRAW” example in “File” -> “Examples” -> “AmebaIRDevice” -> “IRSendRAW” and upload to 1st board connected with IR Emitter:

|image19|

After successfully upload the sample code for IRSendRaw, you might need to upload the IRRecvNEC example for the 2nd board connected with IR Receiver from “File” -> “Examples” -> “AmebaIRDevice” -> “IRRecvNEC”.

After opening the serial monitor on the IR Receiver side and press the reset buttons on two boards, the data “48” will be received every 3 seconds (due to the delays () function, not compulsory to wait). After decoding the signal from the receiving Pin D8 and transmitting Pin D9 with Logic Analyser and Pulse View, the result is also shown as “48” after decoding the receiving data with IR NEC Protocol.

|image20| 

Code Reference
----------------

| [1] Seeed Official website for Grove - Infrared Receiver
| https://wiki.seeedstudio.com/Grove-Infrared_Receiver/

| [2] Seed Official website for Grove - Infrared Emitter
| https://wiki.seeedstudio.com/Grove-Infrared_Emitter/

| [3] Ken SHirriff's blog on A Multi-Protocol Infrared Remote Library for the Arduino
| http://www.righto.com/2009/08/multi-protocol-infrared-remote-library.html

| [4] SB-Projects: IR Remote Control Project
| https://www.sbprojects.net/knowledge/ir/index.php

.. |image01| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image01.png
   :width:  688 px
   :height:  686 px
   :scale: 60%
.. |image02| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image02.png
   :width:  394 px
   :height:  323 px
.. |image03| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image03.png
   :width:  531 px
   :height:  188 px
.. |image04| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image04.png
   :width:  425 px
   :height:  125 px
.. |image05| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image05.png
   :width:  550 px
   :height:  110 px
.. |image06| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image06.png
   :width:  830 px
   :height:  109 px
.. |image13| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image13.png
   :width:  510 px
   :height:  776 px
.. |image14| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image14.png
   :width:  553 px
   :height:  721 px
.. |image19| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image19.png
   :width:  554 px
   :height:  537 px
.. |image20| image:: ../../../../_static/amebad/Example_Guides/IR/IR_Transmit_IR_NEC_Raw_Data_And_Decode/image20.png
   :width:  1210 px
   :height:  163 px
   :scale: 70%
