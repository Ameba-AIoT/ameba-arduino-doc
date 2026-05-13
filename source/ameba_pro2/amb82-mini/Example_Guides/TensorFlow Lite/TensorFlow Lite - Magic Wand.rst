TensorFlow Lite - Magic Wand
============================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

- Adafruit LSM9DS1 accelerometer

Example
-------

Connect the accelerometer to the Ameba.

In the Arduino IDE library manager, install the Arduino_LSM9DS1 library. This example has been tested with version 1.1.0 of the LSM9DS1 library.

Open the example, :guilabel:`Files -> Examples -> AmebaTensorFlowLite -> magic_wand`

Upload the code and press the reset button on Ameba once the upload is finished.

Holding the accelerometer steady, with the positive x-axis pointing to the right and the positive z-axis pointing upwards, move it following the shapes as shown, moving it in a smooth motion over 1 to 2 seconds, avoiding any sharp movements.

|image10|

If the movement is recognised by the Tensorflow Lite model, you should see the same shape output to the Arduino serial monitor. Different LEDs will light up corresponding to different recognized gestures. Note that the wing shape is easy to achieve, while the slope and ring shapes tend to be harder to get right.

|image11|

Code Reference
--------------

More information on TensorFlow Lite for Microcontrollers can be found at: https://www.tensorflow.org/lite/microcontrollers

.. |image10| image:: ../../../../_static/amebapro2/Example_Guides/TensorFlowLite/Magic_Wand/image10.png
   :width: 777
   :height: 337
   :scale: 100 %
.. |image11| image:: ../../../../_static/amebapro2/Example_Guides/TensorFlowLite/Magic_Wand/image11.png
   :width: 639
   :height: 458
   :scale: 100 %
