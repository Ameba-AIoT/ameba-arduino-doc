TensorFlow Lite - Micro Speech
==============================

.. contents::
  :local:
  :depth: 2
  
Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 / AW-CU488 Thing Plus] x 1

- Adafruit PDM MEMS microphone

- LED x 4

Example
-------

Connect the microphone and LEDs to the Ameba board according to the diagram below.
  
|image01|

Download the Ameba customized version of TensorFlow Lite for Microcontrollers library at https://github.com/Ameba-AIoT/ameba-arduino-d/blob/master/Arduino_zip_libraries/Ameba_TensorFlowLite.zip.

Follow the instructions at https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries to install it. 

Ensure that the patch files found at https://github.com/Ameba-AIoT/ameba-arduino-d/tree/master/Ameba_misc/TensorFlowLite_patch are also installed.

Open the example, "Files" → "Examples" → “TensorFlowLite_Ameba” → “micro_speech”.

|image04|

| Upload the code and press the reset button on Ameba once the upload is finished.
| Once it is running, you should see one of the LEDs flashing, indicating that it is processing audio. Saying the word "yes" will cause the green
  LED to light up. Saying the word “no” will cause the red LED to light up. If the word is not recognized, the blue LED will to light up.
| The inference results are also output to the Arduino serial monitor, which appear as follows:
  
|image05|

If you are having trouble in getting the words recognized, here are some tips:

- Ensure that your surroundings are quiet with minimal noise.

- Experiment with varying the distance of the microphone, starting with it at an arm's length.

- Experiment with different tones and volume when saying the words.

- Depending on how you pronounce the words, the characteristics of the microphone used, getting one keyword recognized may be easier than the other.

Code Reference
--------------

More information on TensorFlow Lite for Microcontrollers can be found at: https://www.tensorflow.org/lite/microcontrollers

.. |image01| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Micro_Speech/image01.png
   :width: 1250
   :height: 820
   :scale: 70 %
.. |image04| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Micro_Speech/image04.png
   :width: 556
   :height: 830
   :scale: 100 %
.. |image05| image:: ../../../../_static/amebad/Example_Guides/TensorFlowLite/TensorFlow_Lite_Micro_Speech/image05.png
   :width: 607
   :height: 379
   :scale: 100 %