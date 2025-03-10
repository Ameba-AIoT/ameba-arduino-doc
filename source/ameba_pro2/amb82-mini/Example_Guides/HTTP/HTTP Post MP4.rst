HTTP Post MP4
=============

.. contents::
  :local:
  :depth: 2

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  PushButton x1

-  220 ohm resistor x1

Example
-------

These examples illustrate how to send HTTP Post request of MP4 audio file to a HTTP server.

This guide will be relevant to 2 examples:

1) HTTP_Post_MP4_Whisper_Server

2) RecordMP4_HTTP_Post_Whisper_Server

The difference between these 2 examples is that for HTTP_Post_MP4_Whisper_Server.ino, one is expected to have an MP4 file already saved inside the SD card. Whereas for the RecordMP4_HTTP_Post_Whisper_Server.ino, it is not necessary to have a MP4 file inside the SD card.

This is the block diagram for the example flow.

|image01|

Connect the pushbutton and resistor to AMB82 Mini as shown below.

|image02|

Open “File”-> “Examples” -> “AmebaHTTP” -> “HTTP_Post_MP4_Whisper_Server” OR “RecordMP4_HTTP_Post_Whisper_Server”.

|image03|

Compile and run the code.

Set up the http server by locating the python script called “whisper_llm_server.py” in src folder. Go to command prompt and go to the src folder and execute this command: python3 whisper_llm_server.py. Follow the readme in the python script.

Press the push button for 2s to trigger the recording. Speak into the microphone to ask the AI. This should be the expected output on the terminal that was running the python script. Please note that if you are
to use a more powerful model such as MediaTek 7B model, you will need a
PC with a powerful GPU to test. Purely CPU will not be able to run that
model.

Please note that this server can only be run on Linux OS. Mac OS and Windows have not been supported yet.

|image04|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/HTTP/HTTP_Post_MP4/image01.png
   :width: 722 px
   :height: 255 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/HTTP/HTTP_Post_MP4/image02.png
   :width: 988 px
   :height: 802 px
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/HTTP/HTTP_Post_MP4/image03.png
   :width: 1032 px
   :height: 645 px
.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/HTTP/HTTP_Post_MP4/image04.png
   :width: 1157 px
   :height: 234 px
