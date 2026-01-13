Image Classification
====================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

Example
-------

In this example, we will be using Ameba Pro2 development board to identify images and perform classification.

Open image classification example in :guilabel:`File -> Examples -> AmebaNN -> RTSPImageClassification`

|image01|

If the model was trained with metadata, set USE_MODEL_META_DATA_EN to 1.

|image02|

In the highlighted code snippet, fill in the "ssid" with your WiFi network SSID and "pass" with the network password.

|image03|

Select Neural Network (NN) task and models using modelSelect() function highlighted in a red box. This function takes 6 arguments: Neural Network task, Object Detection model, Face Detection model and Face Recognition model, Audio Classification model and Image Classification model. Replace with "NA_MODEL" if they are not necessary for your selected Neural Network task. Note that it is mandatory to call modelSelect() function before calling the begin() function.

Valid Neural Network task: OBJECT_DETECTION, FACE_DETECTION, FACE_RECOGNITION, AUDIO_CLASSIFICATION, IMAGE_CLASSIFICATION

Valid Object Detection model:

YOLOv3 model: DEFAULT_YOLOV3TINY, CUSTOMIZED_YOLOV3TINY

YOLOv4 model: DEFAULT_YOLOV4TINY, CUSTOMIZED_YOLOV4TINY

YOLOv7 model: DEFAULT_YOLOV7TINY, CUSTOMIZED_YOLOV7TINY

Valid Face Detection model: DEFAULT_SCRFD, CUSTOMIZED_SCRFD

Valid Face Recognition model: DEFAULT_MOBILEFACENET, CUSTOMIZED_MOBILEFACENET

Valid Audio Classification model: DEFAULT_YAMNET, CUSTOMIZED_YAMNET

Valid Image Classification custom CNN model: DEFAULT_IMGCLASS, CUSTOMIZED_IMGCLASS

Valid Image Classification MobileNetV2 model: DEFAULT_IMGCLASS_MOBILENETV2, CUSTOMIZED_IMGCLASS_MOBILENETV2

Choose the customized option (e.g., CUSTOMIZED_YOLOV4TINY/ CUSTOMIZED_SCRFD/ CUSTOMIZED_MOBILEFACENET/ CUSTOMIZED_YAMNET/ CUSTOMIZED_IMGCLASS, CUSTOMIZED_IMGCLASS_MOBILENETV2) if you would like to use your own NN model. To learn about the process of converting an AI model, refer to https://www.amebaiot.com/en/amebapro2-ai-convert-model/ . Additionally, refer to https://www.amebaiot.com/en/amebapro2-apply-ai-model-docs/ to understand how to install and use the converted model.

|image04|

To note: If you would like to customize your own model, currently only Sequential CNN model is supported. Kindly refer to https://www.amebaiot.com/en/amebapro2-ai-convert-model/ to take note of some points when training models.

Compile the code and upload it to Ameba. After pressing the Reset button, wait for the Ameba Pro 2 board to connect to the WiFi network. The board's IP address and network port number for RTSP will be shown in the Serial Monitor.

The live feed capture from Ameba Pro2 board's camera sensor can be viewed on VLC media player. You may download VLC media player from the link `here <https://www.videolan.org/vlc/>`__

Upon the completion of the software installation, open VLC media player, and go to :guilabel:`Media -> Open Network Stream`

|image05|

Make sure your PC is connected to the same network as the Ameba Pro2 board for streaming. Since RTSP is used as the streaming protocol, key in ``rtsp://{IPaddress}:{port}`` as the Network URL in VLC media player, replacing {IPaddress} with the IP address of your Ameba Pro2 board, and {port} with the RTSP port shown in Serial Monitor ``e.g., rtsp://192.168.1.154:554`` The default RTSP port number is 554.

Next, click "Play" to start RTSP streaming to see the result. The video stream from the camera will be shown in VLC media player.

|image06|

Now, you will be able to see what the camera is capturing. The detected class and its probability will be displayed in the Serial Monitor and at the top-left corner of the video stream.

Custom CNN Model (e.g Sequential):  Without metadata and can classify various types of garbage, including cardboard, glass, metal, paper, plastic, and general trash.

|image07|

|image08|

MobileNetV2 Model: With metadata which can classify types of flowers such as Daisy, Lavender, Lily, Rose and Sunflower.

|image09|

|image10|

The items can be found in ClassificationClassList.h. The index number for each object is fixed and should not be changed. To deactivate the detection of certain objects, set the filter value to 0.

|image11|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image01.png
   :width:  1127 px
   :height:  1040 px
   :scale: 80%

.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image02.png
   :width:  837 px
   :height:  335 px

.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image03.png
   :width:  902 px
   :height:  1040 px

.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image04.png
   :width:  851 px
   :height:  165 px

.. |image05| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image05.png
   :width:  432 px
   :height:  482 px

.. |image06| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image06.png
   :width:  633 px
   :height:  594 px

.. |image07| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image07.png
   :width:  1920 px
   :height:  1020 px
   :scale: 60%

.. |image08| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image08.png
   :width:  778 px
   :height:  376 px

.. |image09| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image09.png
   :width:  1942 px
   :height:  1030 px
   :scale: 60%

.. |image10| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image10.png
   :width:  476 px
   :height:  507 px

.. |image11| image:: ../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Image_Classification/image11.png
   :width:  688 px
   :height:  744 px
