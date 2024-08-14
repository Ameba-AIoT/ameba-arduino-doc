Materials

AmebaPro2 [AMB82 MINI] x 1

Android / iOS mobile phone x1

Example

Introduction

In this example, the Ameba board is used to stream video from the
on-board camera sensor (JXF37) to V7RC mobile app via RTSP (Real Time
Streaming Protocol). V7RC is a remote controller APP that provides two
kinds of control UI: 2 channels for RC cars, and 4 channels for tanks
and bulldozers.

Procedure

Open the StreamRTSP example in “File” -> “Examples” -> “AmebaMultimedia”
-> “StreamRTSP” -> “V7RC”.

Since the video receiving end is mobile devices, in the highlighted code
snippet, instead of using the default video settings, we will set the
video resolution to VIDEO_D1 (720x480) to limit the video receiving
latency.

Fill in the “ssid” with your WiFi network SSID and “pass” with the
network password. Since the video streaming receiving end is mobile
phone, it is suggested to use 5G network to features lower latency,
higher capacity, and more bandwidth, that provides better video
streaming quality.

Compile and Upload. After pressing the Reset button, wait for the board
to connect to the Wi-Fi network. The board’s IP address and network port
number for RTSP will be shown in the Serial Monitor.

Download V7RC APP from the links provided below.

Android Users:
https://play.google.com/store/apps/details?id=com.v7idea.v7rcliteandroidsdkversion&hl=en_US

iOS Users:

https://apps.apple.com/nz/app/v7rc/id1390983964

Upon the completion of the APP installation to the device, make sure the
smart device is connected to the same network as the Ameba board for
streaming. Open V7RC APP and select “Control Centre”:

Under NETWORK section, select “WIFI”. Under CAMERA section select
“RTSP”. Since RTSP is used as the streaming protocol, key in
“rtsp://{IPaddress}:{port}” as the Network URL in V7RC in the text box
below CAMERA section, replacing {IPaddress} with the IP address of Ameba
board, and {port} with the RTSP port shown in Serial Monitor. The
default RTSP port number is 554. In the case of two simultaneous RTSP
streams, the second port number defaults to 555. Lastly, click the
“Save” button and return to the home page:

Back to the V7RC home page, check the Wi-Fi connection status on the top
of the APP. Click video button (orange) to monitor the video streaming
in real-time.

The video stream from the camera will be shown in V7RC APP.

Code Reference

The settings below have been tested for better V7RC RTSP streaming
quality:

|image01.png| |image02.jpeg| |image03.png| |image04.jpeg| |image05.png|
|image06.png| |image07.jpeg|

.. |image01.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image01.png
.. |image02.jpeg| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image02.jpeg
.. |image03.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image03.png
.. |image04.jpeg| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image04.jpeg
.. |image05.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image05.png
.. |image06.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image06.png
.. |image07.jpeg| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20RTSP%20Streaming%20V7RC/image07.jpeg
