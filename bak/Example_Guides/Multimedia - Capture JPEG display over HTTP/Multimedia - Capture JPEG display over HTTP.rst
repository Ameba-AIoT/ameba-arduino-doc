Materials
=========

-  Ameba Pro2 [AMB82-Mini] x 1

Example 
========

Introduction
------------

In this example, we will be using Ameba Pro2 development board to
capture a JPEG image and send the image to a browser using HTTP.

The following examples shows different use cases of capturing JPEG
images.

1. HTTPDisplayJPEG

2. HTTPDisplayJPEGContinuous

For the “HTTPDisplayJPEG” example, use any browser and key in the IP
address of the board in browser’s address bar after the board is
connected to the WiFi to view the image.

For the “HTTPDisplayJPEGContinuous” example, use the Firefox browser and
key in the IP address of the board in browser’s address bar after the
board is connected to the WiFi to view the image.

Procedure
---------

Open one of the CaptureJPEG examples in “File” -> “Examples” ->
“AmebaMultimedia” -> “CaptureJPEG” -> “HTTPDisplayJPEG”.

|image1|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|Graphical user interface, text, application, email Description
automatically generated|

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address will be shown in the Serial Monitor.

|image2|

Next, using a computer or a cell phone in the same network domain, open
a browser window and enter the IP address shown in the Serial Monitor.

|image3|

You can view the JPEG image that was captured by the camera on the
webpage. To view a new JPEG image taken by the camera, simply refresh
the page. By running “HTTPDisplayJPEGContinuous”, image will be taken
repeatedly, and the image will be sent to the browser using HTTP,
creating the effect of a video. Note that for the
“HTTPDisplayJPEGContinuous” example, Firefox browser has been tested to
work best.

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_Capture_JPEG_display_over_HTTP/Multimedia_-_Capture_JPEG_display_over_HTTP_images/image01.png
   :width: 3.65482in
   :height: 3.95868in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_Capture_JPEG_display_over_HTTP/Multimedia_-_Capture_JPEG_display_over_HTTP_images/image02.png
   :width: 3.93835in
   :height: 4.33454in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_Capture_JPEG_display_over_HTTP/Multimedia_-_Capture_JPEG_display_over_HTTP_images/image03.png
   :width: 4.34883in
   :height: 2.66201in
.. |image3| image:: ../../_static/Example_Guides/Multimedia_-_Capture_JPEG_display_over_HTTP/Multimedia_-_Capture_JPEG_display_over_HTTP_images/image04.png
   :width: 4.26415in
   :height: 2.04226in
