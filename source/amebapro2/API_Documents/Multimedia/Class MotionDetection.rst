Class MotionDetection
=====================

.. contents::
  :local:
  :depth: 2

**MotionDetectionResult Class**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to represent and retrieve data related to motion detected.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class MotionDetectionResult

**Members**
~~~~~~~~~~~

+----------------------------------------------+------------------------------------------+
| **Public Constructors**                                                                 |
+==============================================+==========================================+
| MotionDetectionResult::MotionDetectionResult | Constructs a MotionDetectionResult       |
|                                              |  object                                  |
+----------------------------------------------+------------------------------------------+
| **Public Methods**                                                                      |
+----------------------------------------------+------------------------------------------+
| MotionDetectionResult::xMin                  | Get x coordinate of the top left corner  |
|                                              | of the bounding box containing the       |
|                                              | detected motion                          |
+----------------------------------------------+------------------------------------------+
| MotionDetectionResult::xMax                  | Get x coordinate of the bottom right     |
|                                              | corner of the bounding box containing    |
|                                              | the detected motion                      |
+----------------------------------------------+------------------------------------------+
| MotionDetectionResult::yMin                  | Get y coordinate of the top left corner  |
|                                              | of the bounding box containing the       |
|                                              | detected motion                          |
+----------------------------------------------+------------------------------------------+
| MotionDetectionResult::yMax                  | Get y coordinate of the bottom right     |
|                                              | corner of the bounding box containing    |
|                                              | the detected motion                      |
+----------------------------------------------+------------------------------------------+

**MotionDetectionResult::xMin**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the top left corner of the bounding box containing the detected motion.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetectionResult::xMax**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get x coordinate of the bottom right corner of the bounding box containing the detected motion.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetectionResult::yMin**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the top left corner of the bounding box containing the detected motion.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float yMin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge of the input video frame and 1.00 indicating the right edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetectionResult::yMax**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Get y coordinate of the bottom right corner of the bounding box containing the detected motion.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    float yMax(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge of the input video frame and 1.00 indicating the right edge of the input video frame.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection Class**
-------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to retrieve data when motion is detected by comparing the RGB information of each image frame captured from the on-board camera sensor (JX-F37P).

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class MotionDetection

**Members**
~~~~~~~~~~~

+---------------------------------------+----------------------------------+
| **Public Constructors**                                                  |
+=======================================+==================================+
| MotionDetection::MotionDetection      | Constructs a MotionDetection     |
|                                       | object and set motion detection  |
|                                       | resolution.                      |
+---------------------------------------+----------------------------------+
| **Public Methods**                                                       |
+---------------------------------------+----------------------------------+
| MotionDetection::configResolution     | Configure motion detection grid  |
|                                       | resolution.                      |
+---------------------------------------+----------------------------------+
| MotionDetection::configVideo          | Configure input video stream     |
|                                       | parameters.                      |
+---------------------------------------+----------------------------------+
| MotionDetection::begin                | Start motion detection process   |
|                                       | on input video.                  |
+---------------------------------------+----------------------------------+
| MotionDetection::end                  | Stop motion detection process on |
|                                       | input video.                     |
+---------------------------------------+----------------------------------+
| MotionDetection::setTriggerBlockCount | Set the number of blocks to      |
|                                       | trigger motion detection output. |
+---------------------------------------+----------------------------------+
| MotionDetection::setDetectionMask     | Set a specific region in the     |
|                                       | video stream to enable motion    |
|                                       | detection.                       |
+---------------------------------------+----------------------------------+
| MotionDetection::getResult            | Get motion detection results.    |
+---------------------------------------+----------------------------------+
| MotionDetection::setResultCallback    | Set a callback function to       |
|                                       | receive and display motion       |
|                                       | detection results.               |
+---------------------------------------+----------------------------------+
| MotionDetection::getResultCount       | Get number of motion detection   |
|                                       | results                          |
+---------------------------------------+----------------------------------+
| MotionDetection::rows                 | Get currently configured number  |
|                                       | of rows for motion detection     |
|                                       | grid.                            |
+---------------------------------------+----------------------------------+
| MotionDetection::cols                 | Get currently configured number  |
|                                       | of columns for motion detection  |
|                                       | grid.                            |
+---------------------------------------+----------------------------------+

**MotionDetectionResult::MotionDetection**
------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a MotionDetection object and configure motion detection resolution.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    MotionDetection(uint8_t row, uint8_t col);

**Parameters**
~~~~~~~~~~~~~~

row: Number of rows for motion detection grid resolution.

- 18

- 32

col: Number of columns for motion detection grid resolution.

- 32) (Default value)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::configResolution**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure motion detection resolution.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configResolution(uint8_t row, uint8_t col);

**Parameters**
~~~~~~~~~~~~~~

row: Number of rows for motion detection grid resolution.

- 18 (Default value)

- 32

col: Number of columns for motion detection grid resolution.

- 32 (Default value)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::configVideo**
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

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function. For motion detection, the input video stream uses the RGB format, which is only available on video stream channel 3.

**MotionDetection::begin**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Start motion detection process on input video.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::end**
------------------------

**Description**
~~~~~~~~~~~~~~~

Stop motion detection process on input video.

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

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::setTriggerBlockCount**
-----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the number of blocks to trigger motion detection output.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setTriggerBlockCount(uint16_t count);

**Parameters**
~~~~~~~~~~~~~~

count: Threshold number of blocks with motion.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::setDetectionMask**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a specific region in the motion detection grid to ignore motion.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setDetectionMask(char * mask);

**Parameters**
~~~~~~~~~~~~~~

mask: a pointer to a char array containing the regions where motion detection is enabled or disabled. 

- 1 (Enable motion detection for the grid region)

- 0 (Disable motion detection for the grid region)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::getResult**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get motion detection results.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    MotionDetectionResult getResult(uint16_t index);
    std::vector<MotionDetectionResult> getResult(void);

**Parameters**
~~~~~~~~~~~~~~

index: index of specific motion detection result to retrieve.

**Returns**
~~~~~~~~~~~

If there is no index specified, the function returns all detected motions contained in a vector of MotionDetectionResult class objects.

If there is an index specified, the function returns the specific detected motion contained in a MotionDetectionResult class object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::setResultCallback**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to receive and display motion detection results.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setResultCallback(void(*md_callback)(std::vector<MotionDetectionResult>));

**Parameters**
~~~~~~~~~~~~~~

md_callback: A callback function that accepts a vector of MotionDetectionResult class objects as argument and returns void.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/CallbackPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/CallbackPostProcessing/CallbackPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::getResultCount**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get number of motion detection results.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint16_t getResultCount(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of detected motions in the most recent set of results, as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/CallbackPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/CallbackPostProcessing/CallbackPostProcessing.ino>`_

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::rows**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get currently configured number of rows for motion detection grid.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t rows(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of rows in the motion detection grid, expressed as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MotionDetection.h” must be included to use the class function.

**MotionDetection::cols**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get currently configured number of columns for motion detection grid.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t cols(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of cols in the motion detection grid, expressed as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MotionDetection.h” must be included to use the class function.
