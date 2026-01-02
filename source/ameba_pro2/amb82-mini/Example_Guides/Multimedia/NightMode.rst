RTSP Streaming Night Mode
=========================

.. contents::
  :local:
  :depth: 2

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1
- Realtek Pro2 to AMB82 MINI sensor adapter board x 1
- Camera sensor with a switchable IR cut filter x 1
- Realtek Amebapro LED board x 1

Example
-------
This example is built on the `"StreamRTSP" -> "VideoOnly" <https://ameba-doc-arduino-sdk.readthedocs-hosted.com/en/latest/ameba_pro2/amb82-mini/Example_Guides/Multimedia/RTSP%20Streaming.html>`_. Please refer to the "VideoOnly" example for more information on how to set up an RTSP stream.


In this example, we will use the AmebaPro2 board to stream video in night mode. This capability requires a camera that has an IR cut filter that can be toggled on and off along with an IR LED light source (or any IR light source).
The adapter board used in this example is to solely connect our camera sensor to the AmebaPro2 board. You may ignore the adapter board requirement if you have alternatives to connect your IR-cut-equipped camera to the AmebaPro2 board.

You can find this particular example under "Files" -> "Examples" -> "StreamRTSP" -> "NightMode" from the top left corner of the ArduinoIDE.

|image01|

The adapter board has a power enable pin which we will be connecting with the GPIO Pin F2 on the AMB82-mini. The IR cut and LED will both be controlled by GPIO Pins F12 and F13 respectively. Pin F12 will connect to the pin TP1 and F13 will connect to pin TP2 on the adapter board.

|image02|

|image03|

If you are using the adapter board ensure that this is in the example before running it.

.. code:: c

    #include "WiFi.h"
    #include "StreamIO.h"
    #include "VideoStream.h"
    #include "RTSP.h"
    #include "Infrared.h"

    #define CHANNEL 0
    #define PWR_EN  9

    pinMode(PWR_EN, OUTPUT);
    digitalWrite(PWR_EN, HIGH);

In the highlighted code snippet, fill in the “ssid” with your WiFi network SSID and “pass” with the network password.
|image04|

Compile the code and upload it to Ameba. After pressing the Reset button, wait for the AmebaPro2 board to connect to the WiFi network. The board's IP address and network port number for RTSP will be shown in the Serial Monitor.

You may download VLC media player from the link (`here <https://www.videolan.org/vlc/>`_).

Upon the completion of the software installation, open VLC media player, and go to “Media” -> “Open Network Stream”.

|image05|

Make sure your PC is connected to the same network as the Ameba Pro2 board for streaming. Since RTSP is used as the streaming protocol, key in `“rtsp://{IPaddress}:{port}”` as the Network URL in VLC media player, replacing {IPaddress} with the IP address of your Ameba Pro2 board, and {port} with the RTSP port shown in Serial Monitor `(e.g., “rtsp://192.168.1.154:554”)`. The default RTSP port number is 554. In the case of two simultaneous RTSP streams, the second port number defaults to 555.

|image06|

You may choose to change the caching time in “Show more options”. A lower cache time will result in reduced video latency but may introduce playback stuttering in the case of poor network conditions.

|image07|

Next, click “Play” to start RTSP streaming. The video stream from the camera will be shown in VLC media player. Meanwhile, in your Serial Monitor, the message “rtp started (UDP)” will appear.

|image08|

|image09|

Code Reference
--------------
The Infrared class controls all the manual IR features of the AmebaPro2. You will need to the following lines before you can begin using any IR features.

.. code:: c
    #include "Infrared.h"

    Infrared ir;

First, the IR cut and/or LED has to be initialized before you can use them. After initializing, you can toggle the IR cut using "IR.setCut()" and control the IR LED brightness using "IR.setLedBrightness()".

.. code:: c

    ir.cutInit();               # Initializes GPIO Pin F12
    ir.ledInit();               # Initializes GPIO Pin F13
    ir.setCut(0);               # 0 to disable, 1 to enable
    ir.setLedBrightness(100);   # Brightness input can be from 0 to 100, [0,100]

It is also important to remember to set the camera to grayscale mode for better clarity and that the ISP auto-tuning has to be set to night mode. This can only be done after data stream has started by the following functions,

.. code:: c

    configCam.setGrayMode(1);       # 0 for RGB, 1 for Grayscale
    configCam.setDayNightMode(1);   # 0 for day mode ISP auto-tuning, 1 for night mode ISP auto-tuning


.. |image01| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image01.jpg
.. |image02| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image02.jpg
.. |image03| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image03.jpg
.. |image04| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image04.jpg
.. |image05| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image05.jpg
.. |image06| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image06.jpg
.. |image07| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image07.jpg
.. |image08| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image08.jpg
.. |image09| image::  ../../../../_static/amebapro2/Example_Guides/Multimedia/NightMode/image09.jpg






