Class NNModelSelection
======================

.. contents::
  :local:
  :depth: 2

**NNModelSelection Class**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to select Neural Network (NN) task and models.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class NNModelSelection

**Members**
~~~~~~~~~~~

+------------------------------------+---------------------------------------+
| **Public Constructors**                                                    |
+====================================+=======================================+
| NNModelSelection::NNModelSelection | Constructs a NNModelSelection object. |
+------------------------------------+---------------------------------------+
| **Public Methods**                                                         |
+------------------------------------+---------------------------------------+
| NNModelSelection::modelSelect      | Select NN task and models.            |
+------------------------------------+---------------------------------------+

**NNModelSelection::modelSelect**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Select Neural Network (NN) task and models.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void modelSelect(unsigned char nntask);
    void modelSelect(unsigned char nntask, unsigned char objdetmodel, unsigned char facedetmodel, unsigned char facerecogmodel);

**Parameters**
~~~~~~~~~~~~~~

nntask: Neural network task to perform. Default value is NA_MODEL.

- OBJECT_DETECTION, FACE_DETECTION, FACE_RECOGNITION


objdetmodel: Neural network model used for Object Detection. Default value is NA_MODEL.

- DEFAULT_YOLOV3TINY, CUSTOMIZED_YOLOV3TINY (YOLOv3 model)

- DEFAULT_YOLOV4TINY, CUSTOMIZED_YOLOV4TINY (YOLOv4 model)

- DEFAULT_YOLOV7TINY, CUSTOMIZED_YOLOV7TINY (YOLOv7 model)

facedetmodel: Neural network model used for Face Detection. Default value is NA_MODEL.

- DEFAULT_SCRFD, CUSTOMIZED_SCRFD

facerecogmodel: Neural network model used for Face Recognition. Default value is NA_MODEL.

- DEFAULT_MOBILEFACENET, CUSTOMIZED_MOBILEFACENET

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: "NNModelSelection.h" must be included to use the class function. Replace objdetmodel, facedetmodel and facerecogmodel arguments with "NA_MODEL" if they are not necessary for your selected NN Task.
