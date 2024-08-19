Materials
=========

-  AmebaPro2 [AMB82 MINI] x1

Example 
========

Introduction
------------

This example shows how to use the Ameba Pro2 board to stream audio
recorded by the onboard analogue microphone in different formats.

Procedure
---------

Open the example in “File” -> “Examples” -> “AmebaMultimedia” -> “Audio”
-> “RTSPAudioStream”.

|image1|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|Graphical user interface, text, application Description automatically
generated|

Compile the code and upload it to Ameba.

After pressing the Reset button, wait for the Ameba Pro 2 board to
connect to the WiFi network. The board’s IP address and network port
number for RTSP will be shown in the Serial Monitor.

On a computer connected to the same WiFi network, open VLC media player,
and go to “Media” -> “Open Network Stream”.

|image2|

Since RTSP is used as the streaming protocol, key in
“rtsp://{IPaddress}:{port}” as the Network URL in VLC media player,
replacing {IPaddress} with the IP address of your Ameba Pro2 board, and
{port} with the RTSP port shown in Serial Monitor. The default RTSP port
number is 554.

|Graphical user interface, text, application, email Description
automatically generated|

Next, click “Play” to start RTSP streaming. You should be able to hear
sounds picked up by the onboard microphone replayed through computer.

Code Reference
--------------

The code can be modified to use the G.711 audio codec (PCMU/PCMA)
instead of the default AAC. The G.711 audio codec is optimized for human
speech and can maintain the clarity and understandability of spoken
speech while reducing the data bandwidth needed.

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Audio_Stream/Multimedia_-_RTSP_Audio_Stream_images/image01.png
   :width: 3.94595in
   :height: 4.2755in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Audio_Stream/Multimedia_-_RTSP_Audio_Stream_images/image02.png
   :width: 4.22095in
   :height: 5.04167in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Audio_Stream/Multimedia_-_RTSP_Audio_Stream_images/image03.png
   :width: 3.29167in
   :height: 3.67265in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Audio_Stream/Multimedia_-_RTSP_Audio_Stream_images/image04.png
   :width: 3in
   :height: 2.32429in
