Materials

AmebaPro2 [AMB82-MINI] x 1

Android / iOS mobile phone x1

L9110S Servo Motor Controller x1

TT Motor x2

Example

Introduction

In this example, we will use Ameba Pro2 as the BLE Peripheral device and
the servo motor controller to communicate with the V7RC mobile app.
Besides, video will be streamed from the on-board camera sensor (JXF37P)
to V7RC mobile app via RTSP (Real Time Streaming Protocol). V7RC is a
remote controller APP that provides two kinds of control UI: one is 2
channels for RC cars, and the other is 4 channels for tanks and
bulldozers.

Procedure

Setup RTSP Streaming

Open the example, “Files” -> “Examples” -> “AmebaBLE” ->
“BLEV7RC_CAR_VIDEO”:

Since the video receiving end is mobile devices, in the highlighted code
snippet, instead of using the default video settings, we will set the
video resolution to VIDEO_D1 (720x480) to limit the video receiving
latency.

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password. Since the video
streaming receiving end is mobile phone, we suggested to use 5G network
since it features lower latency, higher capacity, and increased
bandwidth to provide a better video streaming quality.

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the board to connect to the Wi-Fi network. The board’s
IP address and network port number for RTSP will be shown in the Serial
Monitor.

You may download V7RC APP from the links provided below.

Android Users:
https://play.google.com/store/apps/details?id=com.v7idea.v7rcliteandroidsdkversion&hl=en_US

iPhone Users:

https://apps.apple.com/nz/app/v7rc/id1390983964

Upon the completion of the APP installation, make sure your smart phone
is connected to the same network as the Ameba Pro2 board for streaming.
Open V7RC APP and select “Control Centre”:

Under NETWORK section, select “WIFI”. Under CAMERA section select
“RTSP”. Since RTSP is used as the streaming protocol, key in
“rtsp://{IPaddress}:{port}” as the Network URL in V7RC in the text box
below CAMERA section, replacing {IPaddress} with the IP address of your
Ameba Pro2 board, and {port} with the RTSP port shown in Serial Monitor.
The default RTSP port number is 554. In the case of two simultaneous
RTSP streams, the second port number defaults to 555. Lastly, click the
“Save” button and return to the home page:

Back to the V7RC home page, you can check the Wi-Fi connection status on
the top of the APP. Click video button (orange) to monitor the video
streaming in real-time.

The video stream from the camera will be shown in V7RC APP. Meanwhile,
in your Serial Monitor, the message “rtp started (UDP)” will appear:

Establish BLE Connection

Open V7RC APP and select “Control Centre”:

Under NETWORK section, select “BLE”:

Click DEVICE, and select AMEBA_BLE_DEV and click “LINK” button to
connect to your Ameba board:

Open the Arduino serial monitor, and you should see log of Ameba board
is successfully connected to mobile phone:

Back to the V7RC home page, you can monitor the log printed data
received when moving the two controller buttons indicated in the image
below. Successfully data receiving indicating the BLE connection has
been established:

Setup Servo Motors

We will use two sets of servo motor to control the movement of the car
upon the BLE connection has been established. The two servo motors will
be connected to L9110S servo controller first using predefined MotoA_1A,
MotoA_1B, MotoA_1B, and MotoA_1B pins.

1A pins are connected to GPIO pins, used for controlling the motor
directions.

1B pins are connected to PWM pins, used for controlling the motor speed.

In this example, we will use BW16 as a demonstration. A detailed
connection pin map can be found below. Upon the connection being
established, the user can remotely control the servo motors via the V7RC
App BLE.

Code Reference

ParseCMDString(String cmd) is a customized function will take a string
“cmd” as input and process it. Currently, there are 6 available commands
from V7RC App, which are: "SS2","SS4","SRT","SR2", and "SRV".

The settings below have been tested for better V7RC RTSP streaming
quality:

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.jpeg| |image08.png| |image09.jpeg| |image10.png|
|image11.png| |image12.png| |image13.jpeg| |image14.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image03.png
.. |image04.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image04.png
.. |image05.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image05.png
.. |image06.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image06.png
.. |image07.jpeg| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image07.jpeg
.. |image08.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image08.png
.. |image09.jpeg| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image09.jpeg
.. |image10.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image10.png
.. |image11.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image11.png
.. |image12.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image12.png
.. |image13.jpeg| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image13.jpeg
.. |image14.png| image:: ../../../_static/_Example_Guides/_BLE%20-%20V7RC%20Car%20With%20Video%20Streaming/image14.png
