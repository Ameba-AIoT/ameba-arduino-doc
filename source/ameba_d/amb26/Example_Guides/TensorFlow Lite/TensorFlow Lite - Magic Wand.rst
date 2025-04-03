TensorFlow Lite - Magic Wand
============================

.. contents::
  :local:
  :depth: 2

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 / BW16 / AW-CU488 Thing Plus / AMB25 / AMB26] x 1

- Adafruit LSM9DS1 accelerometer

- LED x 2

Example
-------

Wiring Diagram:

Connect the accelerometer and LEDs to the AMB25 according to the diagram below.

|image07|

Download the Ameba customized version of TensorFlow Lite for Microcontrollers library at https://github.com/Ameba-AIoT/ameba-arduino-d/blob/master/Arduino_zip_libraries/Ameba_TensorFlowLite.zip.

|image08|

Follow the instructions at https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries to install it. 

Ensure that the patch files found at https://github.com/Ameba-AIoT/ameba-arduino-d/tree/master/Ameba_misc/TensorFlowLite_patch are also installed.

In the Arduino IDE library manager, install the Arduino_LSM9DS1 library. This example has been tested with version 1.1.0 of the LSM9DS1 library.

Open the example, "Files" → "Examples" → “TensorFlowLite_Ameba” → “magic_wand”.
  
|image09|

Upload the code and press the reset button on Ameba once the upload is finished.

Holding the accelerometer steady, with the positive x-axis pointing to the right and the positive z-axis pointing upwards, move it following the shapes as shown, moving it in a smooth motion over 1 to 2 seconds, avoiding any sharp movements.
  
|image10|

If the movement is recognised by the Tensorflow Lite model, you should see the same shape output to the Arduino serial monitor. Different LEDs will light up corresponding to different recognized gestures. Note that the wing shape is easy to achieve, while the slope and ring shapes tend to be harder to get right.

|image11|

Code Reference
--------------

More information on TensorFlow Lite for Microcontrollers can be found at: https://www.tensorflow.org/lite/microcontrollers

.. |image07| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Magic_Wand/image07.png
   :width: 624
   :height: 338
   :scale: 100 %
.. |image08| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Magic_Wand/image08.png
   :width: 583
   :height: 329
   :scale: 100 %
.. |image09| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Magic_Wand/image09.png
   :width: 556
   :height: 830
   :scale: 100 %
.. |image10| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Magic_Wand/image10.png
   :width: 777
   :height: 337
   :scale: 100 %
.. |image11| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Magic_Wand/image11.png
   :width: 639
   :height: 458
   :scale: 100 %