Materials

Ameba Pro2 [AMB82-Mini] x 1

Example

Introduction

In this example, we will be using Ameba Pro2 development board to
capture a JPEG image and send the image to a browser using HTTP.

The following examples shows different use cases of capturing JPEG
images.

HTTPDisplayJPEG

HTTPDisplayJPEGContinuous

For the “HTTPDisplayJPEG” example, use any browser and key in the IP
address of the board in browser’s address bar after the board is
connected to the WiFi to view the image.

For the “HTTPDisplayJPEGContinuous” example, use the Firefox browser and
key in the IP address of the board in browser’s address bar after the
board is connected to the WiFi to view the image.

Procedure

Open one of the CaptureJPEG examples in “File” -> “Examples” ->
“AmebaMultimedia” -> “CaptureJPEG” -> “HTTPDisplayJPEG”.

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address will be shown in the Serial Monitor.

Next, using a computer or a cell phone in the same network domain, open
a browser window and enter the IP address shown in the Serial Monitor.

You can view the JPEG image that was captured by the camera on the
webpage. To view a new JPEG image taken by the camera, simply refresh
the page. By running “HTTPDisplayJPEGContinuous”, image will be taken
repeatedly, and the image will be sent to the browser using HTTP,
creating the effect of a video. Note that for the
“HTTPDisplayJPEGContinuous” example, Firefox browser has been tested to
work best.

|image01.png| |image02.png| |image03.png| |image04.png|

.. |image01.png| image:: ../../../_static/_Other_Guides/image01.png
.. |image02.png| image:: ../../../_static/_Other_Guides/image02.png
.. |image03.png| image:: ../../../_static/_Other_Guides/image03.png
.. |image04.png| image:: ../../../_static/_Other_Guides/image04.png
