Class FaceDetectionRecognition
==============================

.. contents::
  :local:
  :depth: 2

**Description**
~~~~~~~~~~~~~~~

A class used to represent and retrieve data related to faces recognized by a face recognition neural network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class FaceRecognitionResult

**Members**
~~~~~~~~~~~

+----------------------------------------+---------------------------------------------------------------------------------------------------+
| **Public Constructors**                                                                                                                    |
+========================================+===================================================================================================+
| FaceRecognitionResult::                | Constructs a FaceDetectionResult                                                                  |
| FaceRecognitionResult                  | object                                                                                            |
+----------------------------------------+---------------------------------------------------------------------------------------------------+
| **Public Methods**                                                                                                                         |
+----------------------------------------+---------------------------------------------------------------------------------------------------+
| FaceRecognitionResult::name            | Get name of recognized face.                                                                      |
+----------------------------------------+---------------------------------------------------------------------------------------------------+
| FaceRecognitionResult::xMin            | Get x coordinate of the top left corner of the bounding box containing the recognized face.       |
+----------------------------------------+---------------------------------------------------------------------------------------------------+
| FaceRecognitionResult::xMax            | Get x coordinate of the bottom right corner of the bounding box containing the recognized face.   |
+----------------------------------------+---------------------------------------------------------------------------------------------------+
| FaceRecognitionResult::yMin            | Get y coordinate of the top left corner of the bounding box containing the recognized face.       |
+----------------------------------------+---------------------------------------------------------------------------------------------------+
| FaceRecognitionResult::yMax            | Get y coordinate of the bottom right corner of the bounding box containing the recognized face.   |
+----------------------------------------+---------------------------------------------------------------------------------------------------+

FaceRecognitionResult::name
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get name of recognized face.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  const char* name(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A pointer to a character array containing the name of the recognized face.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

FaceRecognitionResult::xMin
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the top left corner of the bounding box containing the recognized face.

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

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

FaceRecognitionResult::yMin
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the top left corner of the bounding box containing the recognized face.

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

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

FaceRecognitionResult::yMax
---------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the bottom right corner of the bounding box containing the recognized face.

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

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

+---------------------------------------------------+--------------------------------------------------------------------+
| **Public Constructors**                                                                                                |
+===================================================+====================================================================+
| NNFaceDetectionRecognition::                      | Constructs an NNFaceDetectionRecognition object.                   |
| NNFaceDetectionRecognition                        |                                                                    |
+---------------------------------------------------+--------------------------------------------------------------------+
| **Public Methods**                                                                                                     |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::begin                 | Start face recognition process on input video.                     |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::end                   | Stop face recognition process on input video.                      |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::registerFace          | Register a detected face and assign it a name.                     |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::exitRegisterMode      | Exit face registration mode.                                       |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::resetRegisteredFace   | Reset all previously registered faces.                             |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::backupRegisteredFace  | Save currently registered faces to flash.                          |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::restoreRegisteredFace | Load registered faces from flash.                                  |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::setThreshold          | Set minimum threshold for face recognition confidence level.       |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::setResultCallback     | Set a callback function to receive face recognition results.       |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::getResultCount        | Get number of face recognition results.                            |
+---------------------------------------------------+--------------------------------------------------------------------+
| NNFaceDetectionRecognition::getResult             | Get face recognition results.                                      |
+---------------------------------------------------+--------------------------------------------------------------------+

NNFaceDetectionRecognition::begin
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Start face recognition process on input video.

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

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::end
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Stop face recognition process on input video.

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

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::registerFace
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Register a detected face and assign it a name.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    void registerFace(String name);
    void registerFace(const char* name);

**Parameters**
~~~~~~~~~~~~~~

name: name to assign to newly registered face, expressed as a String class object or a pointer to a character array.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::exitRegisterMode
--------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Exit face registration mode.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void exitRegisterMode(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::resetRegisteredFace
-----------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Reset all previously registered faces.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void resetRegisteredFace(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::backupRegisteredFace
------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Save currently registered faces to flash.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void backupRegisteredFace(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::restoreRegisteredFace
-------------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Load registered faces from flash.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void restoreRegisteredFace(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::setThreshold
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set minimum threshold for face recognition confidence level.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void setThreshold(uint8_t threshold);

**Parameters**
~~~~~~~~~~~~~~

threshold: Face recognition confidence threshold, expressed as an unsigned integer ranging from 0 to 100. Default value of 1.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “NNFaceRecognition.h” must be included to use the class function. A higher threshold results in a stricter face recognition process. For example increasing the threshold may cause recognition to fail if the face is turned sideways. The default value of 1 has been tested to minimize false positives, while maximizing the conditions for recognizing a registered face.

NNFaceDetectionRecognition::setResultCallback
---------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to receive face recognition results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void setResultCallback(void (*fr_callback)(std::vector));

**Parameters**
~~~~~~~~~~~~~~

fr_callback: A callback function that accepts a vector of FaceRecognitionResult class objects as argument and returns void.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function. The callback function will be called with the latest results once per iteration.

NNFaceDetectionRecognition::getResultCount
------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get number of face recognition results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  uint16_t getResultCount(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of recognized faces in the most recent set of results, as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.

NNFaceDetectionRecognition::getResult
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get face recognition results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

    FaceRecognitionResult getResult(uint16_t index);
    std::vector getResult(void);

**Parameters**
~~~~~~~~~~~~~~

index: index of specific face recognition result to retrieve.


**Returns**
~~~~~~~~~~~

If no index is specified, the function returns all recognized faces contained in a vector of FaceRecognitionResult class objects.

If an index is specified, the function returns the specific recognized face contained in a FaceRecognitionResult class object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceRecognition <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceRecognition/RTSPFaceRecognition.ino>`_

.. note :: “NNFaceRecognition.h” must be included to use the class function.