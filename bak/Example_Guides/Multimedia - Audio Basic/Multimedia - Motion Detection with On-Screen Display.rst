Materials
=========

-  Ameba Pro2 [AMB82-Mini] x 1

Example 
========

Introduction
------------

In this example, we will be using Ameba Pro2 development board to detect
motion and highlight it on a RTSP video stream. Motion Detection is
achieved by comparing the RGB information of each image frame captured
from the on-board camera sensor (JX-F37P).

The following examples shows how Motion Detection, and the On-Screen
Display is used. The main difference between the two examples is where
the Motion Detection results are processed. “CallbackPostProcessing”
uses a callback function, while “LoopPostProcessing” deals with the
results in the loop function.

1. LoopPostProcessing

2. CallbackPostProcessing

Procedure
---------

Open one of the Motion Detection examples in “File” -> “Examples” ->
“AmebaMultimedia” -> “MotionDetection”->” LoopPostProcessing”.

|image1|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|Graphical user interface, text, application Description automatically
generated|

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address and network port number for RTSP will be shown in
the Serial Monitor.

|Graphical user interface, text, application, email Description
automatically generated|

You may download VLC media player from the link
`here <https://www.videolan.org/vlc/>`__
(https://www.videolan.org/vlc/).

Upon the completion of the software installation, open VLC media player,
and go to “Media” -> “Open Network Stream”.

|image2|

Make sure your PC is connected to the same network as the Ameba Pro2
board for streaming. Since RTSP is used as the streaming protocol, key
in “rtsp://{IPaddress}:{port}” as the Network URL in VLC media player,
replacing {IPaddress} with the IP address of your Ameba Pro2 board, and
{port} with the RTSP port shown in Serial Monitor (e.g.,
“rtsp://192.168.1.174:554”). The default RTSP port number is 554.

You may choose to change the caching time in “Show more options”. The
default value of 1000 will introduce a one second delay between what the
camera sees and what is displayed on screen. A lower cache time will
result in reduced video latency but may introduce playback stuttering in
the case of poor network conditions.

|image3|

Next, click “Play” to start RTSP streaming. The video stream from the
camera will be shown in VLC media player.

Multiple green boxes will be generated to identify the regions that are
in motion.

|image4|

Code Reference

You may adjust the video bitrate based on your WiFi network quality, by
uncommenting the highlighted code below.

|image5|

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image01.png
   :width: 3.61983in
   :height: 3.92079in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image02.png
   :width: 3.18764in
   :height: 3.55493in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image03.png
   :width: 4.39583in
   :height: 2.69078in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image04.png
   :width: 2.78958in
   :height: 3.11039in
.. |image3| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image05.png
   :width: 3.89643in
   :height: 3.82292in
.. |image4| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image06.png
   :width: 4.89552in
   :height: 3.48495in
.. |image5| image:: ../../_static/Example_Guides/Multimedia_-_Motion_Detection_with_On-Screen_Display/Multimedia_-_Motion_Detection_with_On-Screen_Display_images/image07.png
   :width: 3.70336in
   :height: 4.05868in
