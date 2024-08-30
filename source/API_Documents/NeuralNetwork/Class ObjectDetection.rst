Class ObjectDetection
=====================

.. contents::
  :local:
  :depth: 2

**ObjectDetectionResult Class**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to represent and retrieve data related to objects recognized by an object detection neural network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class ObjectDetectionResult

**Members**
~~~~~~~~~~~

+-------------------------------+----------------------------------------------------------------------------------------------------+
| **Public Constructors**                                                                                                            |
+===============================+====================================================================================================+
| ObjectDetectionResult::       | Constructs an NNImageClassification object                                                         |
| ObjectDetectionResult         |                                                                                                    |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| **Public Methods**                                                                                                                 |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::type   | Get type index of recognized object.                                                               |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::name   | Get name of recognized object.                                                                     |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::score  | Get confidence score of recognized object.                                                         |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::xMin   | Get x coordinate of the top left corner of the bounding box containing the recognized object.      |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::xMax   | Get x coordinate of the bottom right corner of the bounding box containing the recognized object.  |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::yMin   | Get y coordinate of the top left corner of the bounding box containing the recognized object.      |
+-------------------------------+----------------------------------------------------------------------------------------------------+
| ObjectDetectionResult::yMax   | Get y coordinate of the bottom right corner of the bounding box containing the recognized object.  |
+-------------------------------+----------------------------------------------------------------------------------------------------+

**ObjectDetectionResult::type**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get type index of recognized object, corresponding to the object category in the COCO image dataset.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    int type(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

An integer indicating the category of the recognized object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. Object categories can be obtained from the “ObjectClassList.h” file (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

**ObjectDetectionResult::name**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get name of recognized object.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    const char* name(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A pointer to a character array containing the category name of the recognized object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. Object categories can be obtained from the “ObjectClassList.h” file (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

**ObjectDetectionResult::score**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get confidence score of recognized object.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    int score(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

An integer ranging from 0 to 100 representing the confidence of the recognized object category.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. 

**ObjectDetectionResult::xMin**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the top left corner of the bounding box containing the recognized object.

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

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. Object categories can be obtained from the “ObjectClassList.h” file (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

**ObjectDetectionResult::xMax**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the bottom right corner of the bounding box containing the recognized object.

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

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. Object categories can be obtained from the “ObjectClassList.h” file (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

**ObjectDetectionResult::yMin**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the top left corner of the bounding box containing the recognized object.

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

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. Object categories can be obtained from the “ObjectClassList.h” file (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

**ObjectDetectionResult::yMax**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the bottom right corner of the bounding box containing the recognized object.

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

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. Object categories can be obtained from the “ObjectClassList.h” file (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

**NNObjectDetection Class**
---------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to configure, run, and retrieve results of an object detection neural network model.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class NNObjectDetection

**Members**
~~~~~~~~~~~

+-----------------------------------------------+--------------------------------------------------------------------+
| **Public Constructors**                                                                                            |
+===============================================+====================================================================+
| NNObjectDetection::                           | Constructs an NNObjectDetection object.                            |
| NNObjectDetection                             |                                                                    |
+-----------------------------------------------+--------------------------------------------------------------------+
| **Public Methods**                                                                                                 |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::configVideo                | Configure input video stream parameters.                           |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::configRegionOfInterest     | Configure object detection region of interest.                     |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::configThreshold            | Configure object detection threshold.                              |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::begin                      | Start object detection process on input video.                     |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::end                        | Stop object detection process on input video.                      |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::setResultCallback          | Set a callback function to receive object detection results.       |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::getResultCount             | Get number of object detection results.                            |
+-----------------------------------------------+--------------------------------------------------------------------+
| NNObjectDetection::getResult                  | Get object detection results.                                      |
+-----------------------------------------------+--------------------------------------------------------------------+

**NNObjectDetection::configVideo**
----------------------------------

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

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. The object detection model requires that the input video stream uses the RGB format, which is only available on video stream channel 3. The input video stream needs to be configured before object detection can begin.

**NNObjectDetection::configRegionOfInterest**
---------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure object detection region of interest. Object detection will only be performed on the image frame within the region of interest.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    void configRegionOfInterest(int xmin, int xmax, int ymin, int ymax);

**Parameters**
~~~~~~~~~~~~~~

| xmin: left boundary of region of interest, expressed in units of pixel.
| xmax: right boundary of region of interest, expressed in units of pixel.
| ymin: top boundary of region of interest, expressed in units of pixel.
| ymax: bottom boundary of region of interest, expressed in units of pixel.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function.

**NNObjectDetection::configThreshold**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure object detection threshold.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    void configThreshold(float confidence_threshold, float nms_threshold);

**Parameters**
~~~~~~~~~~~~~~

| confidence_threshold: Object detection confidence threshold. Default value of 0.5.
| nms_threshold: Non-Maximal Suppression threshold. Default value of 0.3. Affects the selection of appropriate and accurate bounding boxes. A smaller value results in less accurate bounding boxes.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “NNObjectDetection.h” must be included to use the class function.

**NNObjectDetection::begin**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Start object detection process on input video.

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

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function.

**NNObjectDetection::end**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Stop object detection process on input video.

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

.. note :: “NNObjectDetection.h” must be included to use the class function.

**NNObjectDetection::setResultCallback**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to receive object detection results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    void setResultCallback(void (*od_callback)(std::vector));

**Parameters**
~~~~~~~~~~~~~~

od_callback: A callback function that accepts a vector of ObjectDetectionResult class objects as argument and returns void.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function. The callback function will be called with the latest results once per iteration.

**NNObjectDetection::getResultCount**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get number of object detection results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    uint16_t getResultCount(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of detected objects in the most recent set of results, as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionCallback <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function.


**NNObjectDetection::getResult**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get object detection results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    ObjectDetectionResult getResult(uint16_t index);
    std::vector getResult(void);

**Parameters**
~~~~~~~~~~~~~~

index: index of specific object detection result to retrieve

**Returns**
~~~~~~~~~~~

If no index is specified, the function returns all detected objects contained in a vector of ObjectDetectionResult class objects.

If an index is specified, the function returns the specific detected object contained in a ObjectDetectionResult class object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `ObjectDetectionLoop <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionLoop/ObjectDetectionLoop.ino>`_

.. note :: “NNObjectDetection.h” must be included to use the class function.
