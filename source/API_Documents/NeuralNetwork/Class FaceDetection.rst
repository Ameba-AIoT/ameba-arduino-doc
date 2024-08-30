Class FaceDetection
===================

.. contents::
  :local:
  :depth: 2

**FaceDetectionResult Class**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to represent and retrieve data related to faces detected by a face detection neural network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class FaceDetectionResult

**Members**
~~~~~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------------+
| **Public Constructors**                                                                                                              |
+======================================+===============================================================================================+
| FaceDetectionResult::                | Constructs a FaceDetectionResult                                                              |
| FaceDetectionResult                  | object                                                                                        |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| **Public Methods**                                                                                                                   |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::name            | Get name of detected result                                                                   |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::score           | Get confidence score of detected face                                                         |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::xMin            | Get x coordinate of the top left corner of the bounding box containing the detected face      |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::xMax            | Get x coordinate of the bottom right corner of the bounding box containing the detected face  |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::yMin            | Get y coordinate of the top left corner of the bounding box containing the detected face      |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::yMax            | Get y coordinate of the bottom right corner of the bounding box containing the detected face  |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::xFeature        | Get x coordinate of a feature point on the detected face                                      |
+--------------------------------------+-----------------------------------------------------------------------------------------------+
| FaceDetectionResult::yFeature        | Get y coordinate of a feature point on the detected face                                      |
+--------------------------------------+-----------------------------------------------------------------------------------------------+

**FaceDetectionResult::name**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get name of detected result.


**Syntax**
~~~~~~~~~~

.. code-block:: c++

    const char* name(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A pointer to a character array containing the category name. For face detection, the category name is “Face”.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**FaceDetectionResult::score**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get confidence score of detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int score(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

An integer ranging from 0 to 100 representing the confidence of the detected face.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_


.. note :: “NNFaceDetection.h” must be included to use the class function.


**FaceDetectionResult::xMin**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the top left corner of the bounding box containing the detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float xMin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge of the input video frame and 1.00 indicating the right edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_


.. note :: “NNFaceDetection.h” must be included to use the class function.

**FaceDetectionResult::xMax**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the bottom right corner of the bounding box containing the detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float xMax(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge of the input video frame and 1.00 indicating the right edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_


.. note :: “NNFaceDetection.h” must be included to use the class function.

**FaceDetectionResult::yMin**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the top left corner of the bounding box containing the detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float yMin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the top edge of the input video frame and 1.00 indicating the bottom edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_


.. note :: “NNFaceDetection.h” must be included to use the class function.

**FaceDetectionResult::yMax**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the bottom right corner of the bounding box containing the detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float yMax(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the top edge of the input video frame and 1.00 indicating the bottom edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_


.. note :: “NNFaceDetection.h” must be included to use the class function.

**FaceDetectionResult::xFeature**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of a feature point on the detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float xFeature(uint8_t index);

**Parameters**
~~~~~~~~~~~~~~

| index: index number of face feature point. Feature points:
| 0 - right eye
| 1 - left eye
| 2 - nose
| 3 - right mouth corner
| 4 - left mouth corner

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge of the input video frame and 1.00 indicating the right edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**FaceDetectionResult::yFeature**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of a feature point on the detected face.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float yFeature(uint8_t index);

**Parameters**
~~~~~~~~~~~~~~

| index: index number of face feature point. Feature points:
| 0 - right eye
| 1 - left eye
| 2 - nose
| 3 - right mouth corner
| 4 - left mouth corner

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge of the input video frame and 1.00 indicating the right edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection Class**
-------------------------

**Description**
~~~~~~~~~~~~~~~
A class used to configure, run, and retrieve results of a face detection neural network model.

**Syntax**
~~~~~~~~~~
.. code-block:: c++
  
  class NNFaceDetection
  
**Members**
~~~~~~~~~~~

+------------------------------------------------+--------------------------------------------------------------+
| **Public Constructors**                                                                                       |
+================================================+==============================================================+
| NNFaceDetection::NNFaceDetection               | Constructs an NNFaceDetection object.                        |
+------------------------------------------------+--------------------------------------------------------------+
| **Public Methods**                                                                                            |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::configVideo                   | Configure input video stream parameters.                     |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::configFaceRecogCascadedMode   | Configure for running face recognition after face detection  |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::begin                         | Start face detection process on input video                  |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::end                           | Stop face detection process on input video                   |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::setResultCallback             | Set a callback function to receive face detection results    |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::getResultCount                | Get number of face detection results.                        |
+------------------------------------------------+--------------------------------------------------------------+
| NNFaceDetection::getResult                     | Get face detection results                                   |
+------------------------------------------------+--------------------------------------------------------------+

**NNFaceDetection::configVideo**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure input video stream parameters.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void configVideo(VideoSetting& config);

**Parameters**
~~~~~~~~~~~~~~

config: VideoSetting class object containing desired video configuration.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection::configFaceRecogCascadedMode**
------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure for running face recognition after face detection.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void configFaceRecogCascadedMode(uint8_t enable);

**Parameters**
~~~~~~~~~~~~~~

enable: 1 to enable configuration for running face recognition NN model after face detection.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection::begin**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Start face detection process on input video.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection::end**
------------------------

**Description**
~~~~~~~~~~~~~~~

Stop face detection process on input video.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void end(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection::setResultCallback**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to receive face detection results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void setResultCallback(void (*fd_callback)(std::vector));

**Parameters**
~~~~~~~~~~~~~~

fd_callback: A callback function that accepts a vector of FaceDetectionResultclass objects as argument and returns void.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection::getResultCount**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get number of face detection results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  uint16_t getResultCount(void);
  
**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of detected faces in the most recent set of results, as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.

**NNFaceDetection::getResult**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get face detection results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    FaceDetectionResult getResult(uint16_t index);
    std::vector getResult(void);

**Parameters**
~~~~~~~~~~~~~~

index: index of specific face detection result to retrieve.

**Returns**
~~~~~~~~~~~

If no index is specified, the function returns all detected faces contained in a vector of FaceDetectionResult class objects.

If an index is specified, the function returns the specific detected face contained in a FaceDetectionResult class object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “NNFaceDetection.h” must be included to use the class function.