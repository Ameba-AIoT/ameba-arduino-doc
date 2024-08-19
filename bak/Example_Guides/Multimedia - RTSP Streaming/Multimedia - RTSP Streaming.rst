Materials
=========

-  AmebaPro2 [AMB82 MINI] x1

Example 
========

Introduction
------------

In this example, we will use the Ameba Pro2 board to stream video and
audio data from the on-board camera sensor (JX-F37P) and audio codec to
a computer via RTSP (Real Time Streaming Protocol).

The following examples shows different use cases of RTSP streaming.

1. VideoOnly

2. SingleVideoWithAudio

3. DoubleVideo

4. DoubleVideoWithAudio

Procedure
---------

Open one of the StreamRTSP examples in “File” -> “Examples” ->
“AmebaMultimedia” -> “StreamRTSP”.

|image1|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|image2|

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address and network port number for RTSP will be shown in
the Serial Monitor.

You may download VLC media player from the link
`here <https://vlc-media-player.en.softonic.com/?utm_source=SEM&utm_medium=paid&utm_campaign=EN_UK_DSA&gclid=Cj0KCQjw1vSZBhDuARIsAKZlijTRUgX93pTAjakY9p0Vw6tr04-k-4K-OvoDdnPTl89ggsxDttC2JycaAoYhEALw_wcB>`__.

Upon the completion of the software installation, open VLC media player,
and go to “Media” -> “Open Network Stream”.

|Graphical user interface, text, application Description automatically
generated|

Make sure your PC is connected to the same network as the Ameba Pro2
board for streaming. Since RTSP is used as the streaming protocol, key
in “rtsp://{IPaddress}:{port}” as the Network URL in VLC media player,
replacing {IPaddress} with the IP address of your Ameba Pro2 board, and
{port} with the RTSP port shown in Serial Monitor (e.g.,
“rtsp://192.168.1.154:554”). The default RTSP port number is 554. In the
case of two simultaneous RTSP streams, the second port number defaults
to 555.

|image3|

You may choose to change the caching time in “Show more options”. A
lower cache time will result in reduced video latency but may introduce
playback stuttering in the case of poor network conditions.

|image4|

Next, click “Play” to start RTSP streaming. The video stream from the
camera will be shown in VLC media player. Meanwhile, in your Serial
Monitor, the message “rtp started (UDP)” will appear.

|image5|

|Graphical user interface, text, application, email Description
automatically generated|

You may also view detailed information about the video stream in “Tools”
-> “Codec Information”.

+------------------------------+---------------------------------------+
| Example                      | Stream details                        |
+==============================+=======================================+
| StreamRTSPVideoOnly          | Single RTSP stream of video only, on  |
|                              | network port 554.                     |
|                              |                                       |
|                              | |image6|                              |
+------------------------------+---------------------------------------+
| St                           | Single RTSP stream of video and       |
| reamRTSPSingleVideoWithAudio | audio, on network port 554.           |
|                              |                                       |
|                              | |image7|                              |
+------------------------------+---------------------------------------+
| StreamRTSPDoubleVideo        | Two RTSP streams of video only, on    |
|                              | network ports 554 and 555.            |
|                              |                                       |
|                              | |image8|                              |
|                              |                                       |
|                              | |image9|                              |
+------------------------------+---------------------------------------+
| St                           | Two RTSP streams of video and audio,  |
| reamRTSPDoubleVideoWithAudio | on network ports 554 and 555.         |
|                              |                                       |
|                              | |image10|                             |
|                              |                                       |
|                              | |image11|                             |
+------------------------------+---------------------------------------+

Code Reference
--------------

The camera can produce 3 simultaneous video stream channels, with the
default configuration for each channel as shown. You may choose to edit
the code to use a different video stream.

Channel 0: 1920 x 1080, 30FPS, H264 format

Channel 1: 1280 x 720, 30FPS, H264 format

Channel 2: 1280 x 720, 30FPS, MJPEG format

|Text Description automatically generated with medium confidence|

You may adjust the video bitrate based on your WiFi network quality, by
uncommenting the highlighted code below.

|image12|

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image01.png
   :width: 4.12025in
   :height: 4.46281in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image02.png
   :width: 4.04167in
   :height: 4.2433in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image03.png
   :width: 3.09091in
   :height: 3.44637in
.. |image3| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image04.png
   :width: 4.35848in
   :height: 2.77077in
.. |image4| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image05.png
   :width: 2.86784in
   :height: 3.52434in
.. |image5| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image06.png
   :width: 6.21739in
   :height: 6.42431in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image07.png
   :width: 4.10825in
   :height: 2.66176in
.. |image6| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image08.png
   :width: 3.22642in
   :height: 3.76559in
.. |image7| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image09.png
   :width: 3.30102in
   :height: 3.784in
.. |image8| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image10.png
   :width: 3.36493in
   :height: 3.83019in
.. |image9| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image11.png
   :width: 3.38298in
   :height: 3.87922in
.. |image10| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image12.png
   :width: 3.23197in
   :height: 3.71039in
.. |image11| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image13.png
   :width: 3.23194in
   :height: 3.68825in
.. |Text Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image14.png
   :width: 3.15539in
   :height: 2.79562in
.. |image12| image:: ../../_static/Example_Guides/Multimedia_-_RTSP_Streaming/Multimedia_-_RTSP_Streaming_images/image15.png
   :width: 3.09316in
   :height: 3.50714in
