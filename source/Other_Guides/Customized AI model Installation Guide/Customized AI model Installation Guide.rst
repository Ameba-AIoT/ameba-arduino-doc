Customized AI model Installation Guide

After the AI model conversion and successful gets the “.nb” file, please
refer to the following steps to apply into Arduino SDK.

Rename the customized “.nb” files

Objects Detection, “yolov3_tiny.nb”, “yolov4_tiny.nb”, or
“yolov7_tiny.nb”.

Face Detection, “scrfd_500m_bnkps_640x640_u8.nb".

Face Recognition, "mobilefacenet_int16.nb".

Audio related, “yamnet_fp16.nb”or “yamnet_s_hybrid.nb”.

Copy/Replace “.nb” file into the project folder.

For Windows user,

C:\\Users\\USERNAME\\AppData\\Local\\Arduino15\\packages\\realtek\\hardware\\AmebaPro2\\VERSION\\libraries\\NeuralNetwork\\examples

Or user customized project folder with “.ino” file.

For Linux user,

\\home\\USERNAME\\.arduino15\\packages\\realtek\\hardware\\AmebaPro2\\VERSION
\\libraries\\NeuralNetwork\\examples

Or user customized project folder with “.ino” file.

Compile and run examples.

Open Arduino IDE and run AmebaNN example that related to the model
transferred.

For specific model selection please refer to the example guide and API
documents below.

https://www.amebaiot.com/en/amebapro2-amb82-mini-arduino-peripherals-examples/#ambpro2-arduino-ai

https://www.amebaiot.com/en/rtl8735b-arduino-online-api-documents/
“NeuralNetwork” section

Load Neural Network models via SD card

Open one of the Ameba Neural Network examples by navigating to “File” ->
“Examples” -> “AmebaNN”. Let’s take ObjectDetectionCallback as an
example.

After opening the example on Arduino IDE, navigate to “Tools” -> “NN
Model Load from:” and select SD card as the option.

Next, in the code under modelSelect function, simply change from
“DEFAULT” to “CUSTOMIZED” for the model used.

In the SD card, create a folder name “NN_MDL”

and save your models in the folder by naming your models as stated
below,

Object Detection:

yolov3_tiny.nb

yolov4_tiny.nb

yolov7_tiny.nb

Face Detection:

scrfd.nb

Face Recognition:

mobilefacenet.nb

Audio Classification:

yamnet.nb

Image Classification:

imgclassification.nb

You can change to your preferred .nb file names in SD_Model.cpp by
navigating to \\Arduino15\\packages\\realtek\\hardware\\AmebaPro2\\{SDK
Version}\\libraries\\NeuralNetwork\\src to match the name on your SD
card if you would like to use a different name for the .nb file that is
saved there.

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|

.. |image01.png| image:: ../../../_static/_Other_Guides/image01.png
.. |image02.png| image:: ../../../_static/_Other_Guides/image02.png
.. |image03.png| image:: ../../../_static/_Other_Guides/image03.png
.. |image04.png| image:: ../../../_static/_Other_Guides/image04.png
.. |image05.png| image:: ../../../_static/_Other_Guides/image05.png
