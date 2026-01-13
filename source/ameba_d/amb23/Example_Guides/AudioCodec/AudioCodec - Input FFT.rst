AudioCodec - Input FFT
=======================

Materials
---------

- AmebaD [ AMB21 / AMB22 / AMB23 / AW-CU488 Thing Plus ] x 1

- Analog microphone x 1 (e.g., Adafruit 1063 / 1064) x 1

Example
-------

This example shows how to use the FFT class to calculate the fast Fourier transform of the audio signal recorded by the microphone.

Connect the microphone to the RTL8722 board following the diagram.

As RTL8722DM MINI have a built in microphone on the board, there is no need for any external microphone.

Next, Open the example, :guilabel:`Files -> Examples -> AmebaAudioCodec -> InputFFT`

|image03|

Upload the code and press the reset button on Ameba once the upload is finished.

Open the serial monitor and change the baud rate to 2000000. A stream of FFT results of audio samples will be displayed. Try playing music or use a smartphone app to generate a sine wave into the microphone, and you should be able to see the FFT output change.

|image04|

.. |image03| image:: ../../../../_static/amebad/Example_Guides/AudioCodec/Audio_Codec_InputFFT/image03.png
   :width: 608 px
   :height: 830 px

.. |image04| image:: ../../../../_static/amebad/Example_Guides/AudioCodec/Audio_Codec_InputFFT/image04.png
   :width: 1206 px
   :height: 578 px
   :scale: 70%
