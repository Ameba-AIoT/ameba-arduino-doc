Materials

AmebaPro2 [AMB82 MINI] x1

Example

Introduction

In this example, we will use the Ameba Pro2 board to stream video and
audio data from the on-board camera sensor (JX-F37P) and audio codec to
a computer via RTSP (Real Time Streaming Protocol).

The following examples shows different use cases of RTSP streaming.

VideoOnly

SingleVideoWithAudio

DoubleVideo

DoubleVideoWithAudio

Procedure

Open one of the StreamRTSP examples in “File” -> “Examples” ->
“AmebaMultimedia” -> “StreamRTSP”.

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address and network port number for RTSP will be shown in
the Serial Monitor.

You may download VLC media player from the link here.

Upon the completion of the software installation, open VLC media player,
and go to “Media” -> “Open Network Stream”.

Make sure your PC is connected to the same network as the Ameba Pro2
board for streaming. Since RTSP is used as the streaming protocol, key
in “rtsp://{IPaddress}:{port}” as the Network URL in VLC media player,
replacing {IPaddress} with the IP address of your Ameba Pro2 board, and
{port} with the RTSP port shown in Serial Monitor (e.g.,
“rtsp://192.168.1.154:554”). The default RTSP port number is 554. In the
case of two simultaneous RTSP streams, the second port number defaults
to 555.

You may choose to change the caching time in “Show more options”. A
lower cache time will result in reduced video latency but may introduce
playback stuttering in the case of poor network conditions.

Next, click “Play” to start RTSP streaming. The video stream from the
camera will be shown in VLC media player. Meanwhile, in your Serial
Monitor, the message “rtp started (UDP)” will appear.

You may also view detailed information about the video stream in “Tools”
-> “Codec Information”.

Code Reference

The camera can produce 3 simultaneous video stream channels, with the
default configuration for each channel as shown. You may choose to edit
the code to use a different video stream.

Channel 0: 1920 x 1080, 30FPS, H264 format

Channel 1: 1280 x 720, 30FPS, H264 format

Channel 2: 1280 x 720, 30FPS, MJPEG format

You may adjust the video bitrate based on your WiFi network quality, by
uncommenting the highlighted code below.

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.png| |image08.png| |image09.png| |image10.png|
|image11.png| |image12.png| |image13.png| |image14.png| |image15.png|

.. |image01.png| image:: ../../../_static/_Other_Guides/image01.png
.. |image02.png| image:: ../../../_static/_Other_Guides/image02.png
.. |image03.png| image:: ../../../_static/_Other_Guides/image03.png
.. |image04.png| image:: ../../../_static/_Other_Guides/image04.png
.. |image05.png| image:: ../../../_static/_Other_Guides/image05.png
.. |image06.png| image:: ../../../_static/_Other_Guides/image06.png
.. |image07.png| image:: ../../../_static/_Other_Guides/image07.png
.. |image08.png| image:: ../../../_static/_Other_Guides/image08.png
.. |image09.png| image:: ../../../_static/_Other_Guides/image09.png
.. |image10.png| image:: ../../../_static/_Other_Guides/image10.png
.. |image11.png| image:: ../../../_static/_Other_Guides/image11.png
.. |image12.png| image:: ../../../_static/_Other_Guides/image12.png
.. |image13.png| image:: ../../../_static/_Other_Guides/image13.png
.. |image14.png| image:: ../../../_static/_Other_Guides/image14.png
.. |image15.png| image:: ../../../_static/_Other_Guides/image15.png
