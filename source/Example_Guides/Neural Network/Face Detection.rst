Face Detection
==============

.. contents::
  :local:
  :depth: 2

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

Example 
-------
In this example, we will be using Ameba Pro2 development board to detect faces. Faces are detected based on 5 face feature points (left eye, right eye, nose, left side of mouth and right side of mouth).

Open face detection example in “File” -> “Examples” -> “AmebaNN” -> “RTSPFaceDetection”.

|image01|

In the highlighted code snippet, fill in the “ssid” with your WiFi network SSID and “pass” with the network password.

|image02|

Select Neural Network (NN) task and models using modelSelect() function highlighted in yellow. This function takes 4 arguments: Neural Network task, Object Detection model, Face Detection model and Face Recognition
model. Replace with “NA_MODEL” if they are not necessary for your selected Neural Network task. Note that it is mandatory to call modelSelect() function before calling the begin() function.

Valid Neural Network task: OBJECT_DETECTION, FACE_DETECTION, FACE_RECOGNITION

Valid Object Detection model:

YOLOv3 model: DEFAULT_YOLOV3TINY, CUSTOMIZED_YOLOV3TINY

YOLOv4 model: DEFAULT_YOLOV4TINY, CUSTOMIZED_YOLOV4TINY

YOLOv7 model: DEFAULT_YOLOV7TINY, CUSTOMIZED_YOLOV7TINY

Valid Face Detection model: DEFAULT_SCRFD, CUSTOMIZED_SCRFD

Valid Face Recognition model: DEFAULT_MOBILEFACENET, CUSTOMIZED_MOBILEFACENET

Choose the customized option (e.g., CUSTOMIZED_YOLOV4TINY/ CUSTOMIZED_SCRFD/ CUSTOMIZED_MOBILEFACENET) if you would like to use your own NN model. To learn about the process of converting an AI model,
refer to https://www.amebaiot.com/en/amebapro2-ai-convert-model/ . Additionally, refer to https://www.amebaiot.com/en/amebapro2-apply-ai-model-docs/ to understand how to install and use the converted model.

|image03|

Compile the code and upload it to Ameba. After pressing the Reset button, wait for the Ameba Pro 2 board to connect to the WiFi network. The board’s IP address and network port number for RTSP will be shown in the Serial Monitor.

The result of detected faces can be validated using VLC. You may download VLC media player from the link `here <https://www.videolan.org/vlc/>`__.

Upon the completion of the software installation, open VLC media player, and go to “Media” -> “Open Network Stream”.

|image04|

Make sure your PC is connected to the same network as the Ameba Pro2 board for streaming. Since RTSP is used as the streaming protocol, key in `“rtsp://{IPaddress}:{port}”` as the Network URL in VLC media player, replacing {IPaddress} with the IP address of your Ameba Pro2 board, and {port} with the RTSP port shown in Serial Monitor `(e.g., “rtsp://192.168.1.154:554”)`. The default RTSP port number is 554.

Next, click “Play” to start RTSP streaming to see the result. The video stream from the camera will be shown in VLC media player.

|image05|

A bounding box with face landmark will be drawn to the RTSP video stream to highlight faces that are detected by the camera. To note that, on each channel, it supports up to 6 layers and each layer can support up to 30 OSD elements.

|image06|

The information of the detected faces will be shown in the Serial Monitor. Although 8 faces are detected, each channel per layer has a limitation of displaying only 30 OSD elements. Hence, to avoid incomplete rendering of OSD elements, only two faces will be depicted with bounding boxes and landmarks in this example.

|image07|

Code Reference
--------------

You may adjust the video bitrate based on your WiFi network quality, by uncommenting the highlighted code below.

|image08|

.. |image01| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image01.png
   :width:  960 px
   :height:  1040 px

.. |image02| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image02.png
   :width:  905 px
   :height:  985 px

.. |image03| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image03.png
   :width:  903 px
   :height:  958 px

.. |image04| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image04.png
   :width:  432 px
   :height:  482 px

.. |image05| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image05.png
   :width:  633 px
   :height:  594 px

.. |image06| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image06.png
   :width:  793 px
   :height:  530 px

.. |image07| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image07.png
   :width:  744 px
   :height:  795 px

.. |image08| image:: ../../_static/Example_Guides/Neural_Network/Neural_Network_-_Face_Detection/image08.png
   :width:  750 px
   :height:  822 px
