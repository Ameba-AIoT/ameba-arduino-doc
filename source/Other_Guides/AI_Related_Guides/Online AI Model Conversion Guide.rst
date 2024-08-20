Online AI Model Conversion Guide
================================

.. contents::
  :local:
  :depth: 2

Note: Please Log in to access the page, https://www.amebaiot.com/en/amebapro2-ai-convert-model/ 

Refer to the following table for online conversion supported models currently.

+-----------------------+-----------------------+----------------------+
| **Models**            | **Basic functions**   | **Required files**   |
+=======================+=======================+======================+
| yolov3-tiny, darknet  | Object Detection      | “.cfg”, “.weights”   |
+-----------------------+-----------------------+----------------------+
| yolov4-tiny, darknet  | Object Detection      | “.cfg”, “.weights”   |
+-----------------------+-----------------------+----------------------+
| yolov7-tiny, darknet  | Object Detection      | “.cfg”, “.weights”   |
+-----------------------+-----------------------+----------------------+
| yolov7-tiny, pytorch  | Object Detection      | “.pt”                |
+-----------------------+-----------------------+----------------------+
| scrfd/mobilefacenet   | Face Detection &      | “.pt” or “.onnx”     |
|                       | Recognition           |                      |
+-----------------------+-----------------------+----------------------+
| yamnet                | Sound Classification  | “.h5”                |
+-----------------------+-----------------------+----------------------+
| CNN Gray/RGB          | Image Classification  | “.h5” or “.onnx”     |
+-----------------------+-----------------------+----------------------+

The quantize images are optional for uploading that up to 10.

For CNN Gray/RGB, please refer to the following instructions to get the correct converted models.

- When training model: supported tensorflow version up to 2.14.1

|image01|

- When saving model: set flag as “include_optimizer=False”

|image02|

After AI Model Conversion, there will be download link send out by email.

For more information, please refer to the Customized AI model Installation Guide at https://www.amebaiot.com/en/ameba-arduino-summary/

Please refer to AMB82 MobileFaceNet Convert To ONNX at https://www.amebaiot.com/amebapro2-mobilefacenet-convert-to-onnx

Please refer to AMB82 SCRFD Convert To ONNX at https://www.amebaiot.com/amebapro2-scrfd-convert-to-onnx

.. |image01| image:: ../../_static/Other_Guides/AI_Related_Guides/Online_AI_Model_Conversion_Guide/image01.png
   :width:  1072 px
   :height:  188 px
   :scale: 80%
.. |image02| image:: ../../_static/Other_Guides/AI_Related_Guides/Online_AI_Model_Conversion_Guide/image02.png
   :width:  1041 px
   :height:  170 px
   :scale: 80%
