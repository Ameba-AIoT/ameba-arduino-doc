NNModelSelection Class 
=======================

Description
-----------

A class used to select Neural Network (NN) task and models.

Syntax
------

class NNModelSelection

**Members**
-----------

**Public Constructors**

+-------------------------------------+--------------------------------+
| NNModelSelection:: NNModelSelection | Constructs a NNModelSelection  |
|                                     | object                         |
+=====================================+================================+
+-------------------------------------+--------------------------------+

**Public Methods**

+-------------------------------------+--------------------------------+
| NNModelSelection::modelSelect       | Select NN task and models.     |
+=====================================+================================+
+-------------------------------------+--------------------------------+

NNModelSelection::modelSelect
=============================

| **Description**
| Select Neural Network (NN) task and models.

| **Syntax**
| void modelSelect(unsigned char nntask);

void modelSelect(unsigned char nntask, unsigned char objdetmodel,
unsigned char facedetmodel, unsigned char facerecogmodel);

void modelSelect(unsigned char nntask, unsigned char objdetmodel,
unsigned char facedetmodel, unsigned char facerecogmodel, unsigned char
audclassmodel);

| **Parameters**
| nntask: Neural network task to perform. The default value is
  “NA_MODEL”. (Valid value: OBJECT_DETECTION, FACE_DETECTION,
  FACE_RECOGNITION, AUDIO_CLASSIFICATION)

objdetmodel: Neural network model used for Object Detection. The default
value is “NA_MODEL”. (Valid value:

YOLOv3 model: DEFAULT_YOLOV3TINY, CUSTOMIZED_YOLOV3TINY

YOLOv4 model: DEFAULT_YOLOV4TINY, CUSTOMIZED_YOLOV4TINY

YOLOv7 model: DEFAULT_YOLOV7TINY, CUSTOMIZED_YOLOV7TINY)

facedetmodel: Neural network model used for Face Detection. The default
value is “NA_MODEL”. (Valid value: DEFAULT_SCRFD, CUSTOMIZED_SCRFD)

facerecogmodel: Neural network model used for Face Recognition. The
default value is “NA_MODEL”. (Valid value: DEFAULT_MOBILEFACENET,
CUSTOMIZED_MOBILEFACENET)

audclassmodel: Neural network model used for Audio Classification. The
default value is “NA_MODEL”. (Valid value: DEFAULT_YAMNET,
CUSTOMIZED_YAMNET)

| **Returns**
| NA

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNModelSelection.h” must be included to use the class function.

Replace objdetmodel , facedetmodel, facerecogmodel and audclassmodel
arguments with “NA_MODEL” if they are not necessary for your selected NN
Task.
