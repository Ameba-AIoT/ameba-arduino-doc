Materials
=========

-  Ameba Pro2 [AMB82-Mini] x 1

-  SD card x 1

-  Button x 1

-  Green LED x 1

-  Red LED x 1

-  220 Ohm resistor x 2

-  10K Ohm resistor x 1

Example 
========

Introduction
------------

In this example, we will be using Ameba Pro2 development board to create
a simple surveillance system with Face Recognition that will take a
snapshot of unrecognized faces and save it as JPEG on an SD Card.

Procedure
---------

**AMB82 MINI** wiring diagram:

|image1|

Open the Neural Network example in “File” -> “Examples” -> “AmebaNN” ->
“CaptureJPEGFaceRecognition”.

|image2|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|Graphical user interface, text, application Description automatically
generated|

You may also set the maximum number of snapshots to be captured by
changing the value highlighted in yellow. Currently, the value is set to
5, therefore only 5 snapshots will be taken in total and saved into SD
card. No more snapshots will be taken after 5, even if an unrecognized
person is detected. Increase the value of MAX_UNKNOWN_COUNT to take more
snapshots.

|image3|

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

|image4|

Compile the code and upload it to Ameba. After pressing the Reset
button, wait for the Ameba Pro 2 board to connect to the WiFi network.
The board’s IP address and network port number for RTSP will be shown in
the Serial Monitor.

The result can be validated using VLC. You may download VLC media player
from the link `here <https://www.videolan.org/vlc/>`__
(https://www.videolan.org/vlc/).

Upon the completion of the software installation, open VLC media player,
and go to “Media” -> “Open Network Stream”.

|image5|

Make sure your PC is connected to the same network as the Ameba Pro2
board for streaming. Since RTSP is used as the streaming protocol, key
in “rtsp://{IPaddress}:{port}” as the Network URL in VLC media player,
replacing {IPaddress} with the IP address of your Ameba Pro2 board, and
{port} with the RTSP port shown in Serial Monitor (e.g.,
“rtsp://192.168.1.154:554”). The default RTSP port number is 554.

Next, click “Play” to start RTSP streaming to see the result. The video
stream from the camera will be shown in VLC media player.

|image6|

The faces detected by the face recognition neural network model are
initially labelled as “unknown”, faces need to be first registered with
a name before they can be recognized.

|image7|

Aim the camera at a face and enter the following commands in the Serial
Monitor. When it is in face registration mode, the green and red LEDs
will be blinking.

**To register a face:**

Note: Multiple faces can be registered. However, when registering a
face, ensure that there is only one face in the frame.

To register a face, aim the camera to a targeted face and enter
**“REG={Name}”** to give the targeted face a name. For example,
“REG=SAM”.

|image8|

|image9|

**To exit registration mode:**

[STRIKEOUT:Enter the command “EXIT” to exit from registration mode. This
command can be used to stop the face registering process before it is
completed.]

**To remove a specific registered face:**

Enter the command **“DEL={Name}”** to delete a certain registered face.
For example, “DEL=SAM”.

**To reset all registered faces:**

Enter the command **“RESET”** to forget all previously registered faces.
All previously assigned faces and names will be removed. You may
register a face again by entering the face registration mode.

**To backup and restore registered faces to and from flash:**

Enter the command **“BACKUP”** to save a copy of registered faces to
flash. If a backup exists, enter the command **“RESTORE”** to load
registered faces from flash.

Press and hold the button for 2 seconds to enter snapshot mode to take
snapshots when unrecognized faces are detected. The unknown faces will
then be registered as Stranger and saved to an SD card as
Stranger{strangerCounter}.jpg. Red LED will light up when one or more
unknown faces are detected.

|image10|\ |image11|

.. |image1| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image01.png
   :width: 4.62609in
   :height: 2.82717in
.. |image2| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image02.png
   :width: 3.74573in
   :height: 4.05714in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image03.png
   :width: 3.77877in
   :height: 4.0936in
.. |image3| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image04.png
   :width: 3.80012in
   :height: 4.11673in
.. |image4| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image05.png
   :width: 3.95041in
   :height: 4.27889in
.. |image5| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image06.png
   :width: 2.92174in
   :height: 3.25463in
.. |image6| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image07.png
   :width: 3.05217in
   :height: 2.86565in
.. |image7| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image08.png
   :width: 3.71528in
   :height: 1.99156in
.. |image8| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image09.png
   :width: 4.13913in
   :height: 3.15753in
.. |image9| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image10.png
   :width: 4.08696in
   :height: 2.50902in
.. |image10| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image11.png
   :width: 4.82777in
   :height: 2.86956in
.. |image11| image:: ../../_static/Example_Guides/Neural_Network_-_Capture_JPEG_Face_Recognition/Neural_Network_-_Capture_JPEG_Face_Recognition_images/image12.png
   :width: 4.82708in
   :height: 3.22679in
