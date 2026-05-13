TensorFlow Lite - Person Detection
==================================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

- Arducam Mini 2MP Plus OV2640 SPI Camera Module x 1

- LED up to 3

Example
-------

Connect the camera and LEDs to the Ameba board.

1. Download Ameba_ArduCAM library at `GitHub Repo <https://github.com/Ameba-AIoT/ameba-arduino-pro2/tree/dev/Arduino_zip_libraries>`__ Follow the instructions at `Arduino document <https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries>`__ to install it.

2. In the Arduino IDE library manager, install the "JPEGDecoder" library. This example has been tested with version 1.8.0 of the JPEGDecoder library. Once the library has installed, you will need to configure it to disable some optional components that are not compatible with the Ameba. Open the following file: ``Arduino/libraries/JPEGDecoder/src/User_Config.h`` Make sure that both ``#define LOAD_SD_LIBRARY`` and ``#define LOAD_SDFAT_LIBRARY`` are commented out, as shown in this excerpt from the file:

.. code-block:: c

   //#define LOAD_SD_LIBRARY // Default SD Card library
   //#define LOAD_SDFAT_LIBRARY // Use SdFat library instead, so SD Card SPI can be bit bashed

Open the example, :guilabel:`Files -> Examples -> AmebaTensorFlowLite -> person_detection`

| User can define the LED pins by using any GPIO pins on the boards.
| Upload the code and press the reset button on Ameba once the upload is finished.

| Once it is running, you should see the blue LED flashing once every few seconds, indicating that it has finished processing an image.
| The red LED will light up if it determines that there is no person in the previous image captured, and the green LED will light up if it determines that there is a person.

| The inference results are also output to the Arduino serial monitor, which appear as follows:

|image09|

Code Reference
--------------

More information on TensorFlow Lite for Microcontrollers can be found at: https://www.tensorflow.org/lite/microcontrollers

.. |image09| image:: ../../../../_static/amebapro2/Example_Guides/TensorFlowLite/Person_Detection/image09.png
   :width: 639
   :height: 477
   :scale: 100 %
