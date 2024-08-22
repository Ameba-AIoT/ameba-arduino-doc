Materials
=========

-  Ameba Pro2 [AMB82-Mini] x 1

Example 
========

Introduction
------------

In this example, we will be using Ameba Pro2 development board to detect
faces. Faces are detected based on 5 face feature points (left eye,
right eye, nose, left side of mouth and right side of mouth).

Procedure
---------

Open face detection example in “File” -> “Examples” -> “AmebaNN” ->
RTSPFaceDetection”.

|image1|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|Application Description automatically generated with medium confidence|

Select Neural Network (NN) task and models using modelSelect() function
highlighted in yellow. This function takes 4 arguments: Neural Network
task, Object Detection model, Face Detection model and Face Recognition
model. Replace with “NA_MODEL” if they are not necessary for your
selected Neural Network task. Note that it is mandatory to call
modelSelect() function before calling the begin() function.

*Valid Neural Network task:* OBJECT_DETECTION, FACE_DETECTION,
FACE_RECOGNITION

*Valid Object Detection model:*

YOLOv3 model: DEFAULT_YOLOV3TINY, CUSTOMIZED_YOLOV3TINY

YOLOv4 model: DEFAULT_YOLOV4TINY, CUSTOMIZED_YOLOV4TINY

YOLOv7 model: DEFAULT_YOLOV7TINY, CUSTOMIZED_YOLOV7TINY

*Valid Face Detection model:* DEFAULT_SCRFD, CUSTOMIZED_SCRFD

*Valid Face Recognition model:* DEFAULT_MOBILEFACENET,
CUSTOMIZED_MOBILEFACENET

Choose the customized option (e.g., CUSTOMIZED_YOLOV4TINY/
CUSTOMIZED_SCRFD/ CUSTOMIZED_MOBILEFACENET) if you would like to use
your own NN model. To learn about the process of converting an AI model,
refer to https://www.amebaiot.com/en/amebapro2-ai-convert-model/ .
Additionally, refer to
https://www.amebaiot.com/en/amebapro2-apply-ai-model-docs/ to understand
how to install and use the converted model.

|image2|

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address and network port number for RTSP will be shown in
the Serial Monitor.

The result of detected faces can be validated using VLC. You may
download VLC media player from the link
`here <https://www.videolan.org/vlc/>`__
(https://www.videolan.org/vlc/).

Upon the completion of the software installation, open VLC media player,
and go to “Media” -> “Open Network Stream”.

|image3|

Make sure your PC is connected to the same network as the Ameba Pro2
board for streaming. Since RTSP is used as the streaming protocol, key
in “rtsp://{IPaddress}:{port}” as the Network URL in VLC media player,
replacing {IPaddress} with the IP address of your Ameba Pro2 board, and
{port} with the RTSP port shown in Serial Monitor (e.g.,
“rtsp://192.168.1.154:554”). The default RTSP port number is 554.

Next, click “Play” to start RTSP streaming to see the result. The video
stream from the camera will be shown in VLC media player.

|image4|

A bounding box with face landmark will be drawn to the RTSP video stream
to highlight faces that are detected by the camera. To note that, on
each channel, it supports up to 6 layers and each layer can support up
to 30 OSD elements.

|image5|

The information of the detected faces will be shown in the Serial
Monitor. Although 8 faces are detected, each channel per layer has a
limitation of displaying only 30 OSD elements. Hence, to avoid
incomplete rendering of OSD elements, only two faces will be depicted
with bounding boxes and landmarks in this example.

|image6|

Code Reference

You may adjust the video bitrate based on your WiFi network quality, by
uncommenting the highlighted code below.

|Graphical user interface, text, application, email Description
automatically generated|

.. |image1| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image01.png
   :width: 3.6in
   :height: 3.8993in
.. |Application Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image02.png
   :width: 3.60697in
   :height: 3.92587in
.. |image2| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image03.png
   :width: 3.96875in
   :height: 4.21308in
.. |image3| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image04.png
   :width: 2.92174in
   :height: 3.25463in
.. |image4| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image05.png
   :width: 2.91304in
   :height: 2.73502in
.. |image5| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image6.jpeg
   :width: 6.26111in
   :height: 3.52153in
.. |image6| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image07.png
   :width: 6.26944in
   :height: 6.69583in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Neural_Network_-_Face_Detection/Neural_Nework_-_Face_Detection_images/image08.png
   :width: 4.06406in
   :height: 4.45399in
