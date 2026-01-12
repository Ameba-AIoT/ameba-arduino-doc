Class Image Classification
===========================

**ImageClassification Class**
------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to represent and retrieve data related to objects recognized by an image classification neural network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class ImageClassificationResult

**Members**
~~~~~~~~~~~

+-------------------------------------+-------------------------------------------+
| **Public Constructors**                                                         |
+=====================================+===========================================+
| ImageClassificationResult::         | Constructs an ImageClassificationResult   |
| ImageClassificationResult           | object.                                   |
+-------------------------------------+-------------------------------------------+
| **Public Methods**                                                              |
+-------------------------------------+-------------------------------------------+
| ImageClassificationResult::classID  | Get class ID of recognized object.        |
+-------------------------------------+-------------------------------------------+
| ImageClassificationResult::score    | Get confidence score of recognized object.|
+-------------------------------------+-------------------------------------------+

**ImageClassificationResult::classID**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get class ID of recognized object.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int classID(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: "NNImageClassification.h" must be included to use the class function. Object categories can be obtained from the "ClassificationClassList.h" file.

**ImageClassificationResult::score**
------------------------------------

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

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: "NNImageClassification.h" must be included to use the class function. Object categories can be obtained from the "ClassificationClassList.h" file.

**NNImageClassification Class**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to configure, run, and retrieve results of an image classification neural network model.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class NNImageClassification

**Members**
~~~~~~~~~~~

+------------------------------------------------+-------------------------------------------------------------------+
| **Public Constructors**                                                                                            |
+================================================+===================================================================+
| NNImageClassification::NNImageClassification   | Constructs an NNImageClassification object                        |
+------------------------------------------------+-------------------------------------------------------------------+
| **Public Methods**                                                                                                 |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::configInputImageColor   | Configure input image color used during model training process    |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::configVideo             | Configure input video stream parameters                           |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::configRegionOfInterest  | Configure image classification region of interest                 |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::begin                   | Start image classification process on input video                 |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::end                     | Stop image classification process on input video                  |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::setResultCallback       | Set a user callback function                                      |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::getResultCount          | Get number of object detection results                            |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::getResult               | Get image classification results                                  |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::parseModelMetaData      | Parses and extracts key information from the model's metadata for |
|                                                | use in image classification                                       |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::getClassNameFromMeta    | Retrieves the class label name from the model's metadata          |
|                                                | using the given class index                                       |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::useModelMetaData        | Check whether the use of model metadata is currently enabled      |
+------------------------------------------------+-------------------------------------------------------------------+

**NNImageClassification::configInputImageColor**
------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure input image color used during model training process.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configInputImageColor(int color);

**Parameters**
~~~~~~~~~~~~~~

color: Color of images used for model training.

- 0 (Grayscale)

- 1 (RGB)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::configVideo**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure input video stream parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideo(VideoSetting &config);

**Parameters**
~~~~~~~~~~~~~~

config: VideoSetting class object containing desired video configuration.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::configRegionOfInterest**
-------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure image classification region of interest.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configRegionOfInterest(int xmin, int xmax, int ymin, int ymax);

**Parameters**
~~~~~~~~~~~~~~

xmin: left boundary of region of interest, expressed in units of pixel.

xmax: right boundary of region of interest, expressed in units of pixel.

ymin: top boundary of region of interest, expressed in units of pixel.

ymax: bottom boundary of region of interest, expressed in units of pixel.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::begin**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Start image classification process on input video.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::end**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Stop image classification process on input video.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void end (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::setResultCallback**
--------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a user callback function.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setResultCallback(void (*ic_callback)(void));

**Parameters**
~~~~~~~~~~~~~~

ic_callback: user callback function.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::getResultCount**
--------------------------------------------

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

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::getResult**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get image classification results.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    ImageClassificationResult getResult(uint16_t index);
    std::vector<ImageClassificationResult> getResult(void);

**Parameters**
~~~~~~~~~~~~~~

index: index of specific image classification result to retrieve

**Returns**
~~~~~~~~~~~

If no index is specified, the function returns all detected objects contained in a vector of ImageClassificationResult class objects.

If an index is specified, the function returns the specific detected object contained in a ImageClassificationResult class object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::parseModelMetaData**
------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Parses and extracts key information from the model's metadata for use in image classification.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    char *parseModelMetaData(mm_context_t *vipnn_ctx);

**Parameters**
~~~~~~~~~~~~~~

vipnn_ctx: pointer to the mm_context_t that holds the model information.

**Returns**
~~~~~~~~~~~

A pointer to a string containing the parsed model metadata.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::getClassNameFromMeta**
------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Retrieves the class label name from the model's metadata using the given class index.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    char *getClassNameFromMeta(char *meta_data, int class_id, int prob);

**Parameters**
~~~~~~~~~~~~~~

meta_data: pointer to metadata buffer that contains class information.

class_id: numeric ID of the class to look up.

prob: probability or confidence value associated with the class.

**Returns**
~~~~~~~~~~~

A pointer to a string containing the class name.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.

**NNImageClassification::useModelMetaData**
---------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Check whether the use of model metadata is currently enabled.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void useModelMetaData(int use_meta_data);

**Parameters**
~~~~~~~~~~~~~~

use_meta_data: flag (1 = enable, 0 = disable) to control whether model metadata is used.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h" must be included to use the class function.
