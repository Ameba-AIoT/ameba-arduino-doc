MotionDetectionResult Class 
============================

Description
-----------

A class used to represent and retrieve data related to motion detected.

Syntax
------

class MotionDetectionResult

**Members**
-----------

**Public Constructors**

+---------------------------------------+------------------------------+
| MotionDetectionResult::               | Constructs a                 |
| MotionDetectionResult                 | MotionDetectionResult object |
+=======================================+==============================+
+---------------------------------------+------------------------------+

**Public Methods**

+---------------------------+------------------------------------------+
| Mo                        | Get x coordinate of the top left corner  |
| tionDetectionResult::xMin | of the bounding box containing the       |
|                           | detected motion                          |
+===========================+==========================================+
| Mo                        | Get x coordinate of the bottom right     |
| tionDetectionResult::xMax | corner of the bounding box containing    |
|                           | the detected motion                      |
+---------------------------+------------------------------------------+
| Mo                        | Get y coordinate of the top left corner  |
| tionDetectionResult::yMin | of the bounding box containing the       |
|                           | detected motion                          |
+---------------------------+------------------------------------------+
| Mo                        | Get y coordinate of the bottom right     |
| tionDetectionResult::yMax | corner of the bounding box containing    |
|                           | the detected motion                      |
+---------------------------+------------------------------------------+

MotionDetection Class 
======================

.. _description-1:

Description
-----------

A class used to retrieve data when motion is detected by comparing the
RGB information of each image frame captured from the on-board camera
sensor (JX-F37P).

.. _syntax-1:

Syntax
------

Class MotionDetection

.. _members-1:

Members
-------

**Public Constructors**

+-----------------------------------+----------------------------------+
| MotionDetection::MotionDetection  | Constructs a MotionDetection     |
|                                   | object and set motion detection  |
|                                   | resolution.                      |
+===================================+==================================+
+-----------------------------------+----------------------------------+

.. _members-2:

Members
-------

**Public Constructors**

+-----------------------------------+----------------------------------+
| MotionDetection::configResolution | Configure motion detection grid  |
|                                   | resolution.                      |
+===================================+==================================+
| MotionDetection::configVideo      | Configure input video stream     |
|                                   | parameters.                      |
+-----------------------------------+----------------------------------+
| MotionDetection::begin            | Start motion detection process   |
|                                   | on input video.                  |
+-----------------------------------+----------------------------------+
| MotionDetection::end              | Stop motion detection process on |
|                                   | input video.                     |
+-----------------------------------+----------------------------------+
| Moti                              | Set the number of blocks to      |
| onDetection::setTriggerBlockCount | trigger motion detection output. |
+-----------------------------------+----------------------------------+
| MotionDetection::setDetectionMask | Set a specific region in the     |
|                                   | video stream to enable motion    |
|                                   | detection.                       |
+-----------------------------------+----------------------------------+
| MotionDetection::getResult        | Get motion detection results.    |
+-----------------------------------+----------------------------------+
| M                                 | Set a callback function to       |
| otionDetection::setResultCallback | receive and display motion       |
|                                   | detection results.               |
+-----------------------------------+----------------------------------+
| MotionDetection::getResultCount   | Get number of motion detection   |
|                                   | results                          |
+-----------------------------------+----------------------------------+
| MotionDetection::rows             | Get currently configured number  |
|                                   | of rows for motion detection     |
|                                   | grid.                            |
+-----------------------------------+----------------------------------+
| MotionDetection::cols             | Get currently configured number  |
|                                   | of columns for motion detection  |
|                                   | grid.                            |
+-----------------------------------+----------------------------------+

MotionDetectionResult::xMin
===========================

| **Description**
| Get x coordinate of the top left corner of the bounding box containing
  the detected motion.

| **Syntax**
| float xMin(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge
  of the input video frame and 1.00 indicating the right edge of the
  input video frame.

| **Example Code**
| Example: LoopPostProcessing

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

| **Notes and Warnings**
| “NNMotionDetection.h” must be included to use the class function.

MotionDetectionResult::xMax
===========================

| **Description**
| Get x coordinate of the bottom right corner of the bounding box
  containing the detected motion.

| **Syntax**
| float xMax(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge
  of the input video frame and 1.00 indicating the right edge of the
  input video frame.

| **Example Code**
| Example: LoopPostProcessing

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

| **Notes and Warnings**
| “NNMotionDetection.h” must be included to use the class function.

MotionDetectionResult::yMin
===========================

| **Description**
| Get y coordinate of the top left corner of the bounding box containing
  the detected motion.

| **Syntax**
| float yMin(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge
  of the input video frame and 1.00 indicating the right edge of the
  input video frame.

| **Example Code**
| Example: LoopPostProcessing

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

| **Notes and Warnings**
| “NNMotionDetection.h” must be included to use the class function.

MotionDetectionResult::yMax
===========================

| **Description**
| Get y coordinate of the bottom right corner of the bounding box
  containing the detected motion.

| **Syntax**
| float yMax(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge
  of the input video frame and 1.00 indicating the right edge of the
  input video frame.

| **Example Code**
| Example: LoopPostProcessing

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

| **Notes and Warnings**
| “NNMotionDetection.h” must be included to use the class function.

**MotionDetection::MotionDetection**

.. _description-2:

Description
-----------

Constructs a MotionDetection object and configure motion detection
resolution.

.. _syntax-2:

Syntax
------

MotionDetection(uint8_t row, uint8_t col);

Parameters
----------

row: Number of rows for motion detection grid resolution. Default value
of 18. (Valid value: 18 or 32)

col: Number of columns for motion detection grid resolution. Default
value of 32. (Valid value: 32)

Returns
-------

NA

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::configResolution**

.. _description-3:

Description
-----------

Configure motion detection resolution.

.. _syntax-3:

Syntax
------

void configResolution(uint8_t row, uint8_t col);

.. _parameters-1:

Parameters
----------

row: Number of rows for motion detection grid resolution. Default value
of 18. (Valid value, 18 or 32)

col: Number of columns for motion detection grid resolution. Default
value of 32. (Valid value: 32)

.. _returns-1:

Returns
-------

NA

.. _example-code-1:

Example Code
------------

NA

.. _notes-and-warnings-1:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::configVideo**

.. _description-4:

Description
-----------

Configure input video stream parameters.

.. _syntax-4:

Syntax
------

void configVideo(VideoSetting& config);

.. _parameters-2:

Parameters
----------

config: VideoSetting class object containing desired video
configuration.

.. _returns-2:

Returns
-------

NA

.. _example-code-2:

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-2:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function. For
motion detection, the input video stream uses the RGB format, which is
only available on video stream channel 3.

**MotionDetection::begin**

.. _description-5:

Description
-----------

Start motion detection process on input video.

.. _syntax-5:

Syntax
------

void begin(void);

.. _parameters-3:

Parameters
----------

NA

.. _returns-3:

Returns
-------

NA

.. _example-code-3:

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-3:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::end**

.. _description-6:

Description
-----------

Stop motion detection process on input video.

.. _syntax-6:

Syntax
------

void end(void);

.. _parameters-4:

Parameters
----------

NA

.. _returns-4:

Returns
-------

NA

.. _example-code-4:

Example Code
------------

NA

.. _notes-and-warnings-4:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::setTriggerBlockCount**

.. _description-7:

Description
-----------

Set the number of blocks to trigger motion detection output.

.. _syntax-7:

Syntax
------

void setTriggerBlockCount(uint16_t count);

.. _parameters-5:

Parameters
----------

count: Threshold number of blocks with motion.

.. _returns-5:

Returns
-------

NA

.. _example-code-5:

Example Code
------------

NA

.. _notes-and-warnings-5:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::setDetectionMask**

.. _description-8:

Description
-----------

Set a specific region in the motion detection grid to ignore motion.

.. _syntax-8:

Syntax
------

void setDetectionMask(char \* mask);

.. _parameters-6:

Parameters
----------

mask: a pointer to a char array containing the regions where motion
detection is enabled or disabled. A value of 1 will enable motion
detection for the grid region, a value of 0 will disable motion
detection for the grid region.

.. _returns-6:

Returns
-------

NA

.. _example-code-6:

Example Code
------------

NA

.. _notes-and-warnings-6:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::getResult**

.. _description-9:

Description
-----------

Get motion detection results.

.. _syntax-9:

Syntax
------

MotionDetectionResult getResult(uint16_t index);

std::vector<MotionDetectionResult> getResult(void);

.. _parameters-7:

Parameters
----------

index: index of specific motion detection result to retrieve.

.. _returns-7:

Returns
-------

If no index is specified, the function returns all detected motions
contained in a vector of MotionDetectionResult class objects.

If an index is specified, the function returns the specific detected
motion contained in a MotionDetectionResult class object.

.. _example-code-7:

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-7:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::setResultCallback**

.. _description-10:

Description
-----------

Set a callback function to receive and display motion detection results.

.. _syntax-10:

Syntax
------

void setResultCallback(void
(\*md_callback)(std::vector<MotionDetectionResult>));

.. _parameters-8:

Parameters
----------

md_callback: : A callback function that accepts a vector of
MotionDetectionResult class objects as argument and returns void.

.. _returns-8:

Returns
-------

NA

.. _example-code-8:

Example Code
------------

Example: CallbackPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/CallbackPostProcessing/CallbackPostProcessing.ino)

.. _notes-and-warnings-8:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::getResultCount**

.. _description-11:

Description
-----------

Get number of motion detection results.

.. _syntax-11:

Syntax
------

uint16_t getResultCount(void);

.. _parameters-9:

Parameters
----------

NA

.. _returns-9:

Returns
-------

The number of detected motions in the most recent set of results, as an
unsigned integer.

.. _example-code-9:

Example Code
------------

Example: CallbackPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/CallbackPostProcessing/CallbackPostProcessing.ino)

.. _notes-and-warnings-9:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.


**MotionDetection::rows**

.. _description-12:

Description
-----------

Get currently configured number of rows for motion detection grid.

.. _syntax-12:

Syntax
------

uint8_t rows(void);

.. _parameters-10:

Parameters
----------

NA

.. _returns-10:

Returns
-------

The number of rows in the motion detection grid, expressed as an
unsigned integer.

.. _example-code-10:

Example Code
------------

NA

.. _notes-and-warnings-10:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::cols**

.. _description-13:

Description
-----------

Get currently configured number of columns for motion detection grid.

.. _syntax-13:

Syntax
------

uint8_t cols(void);

.. _parameters-11:

Parameters
----------

NA

.. _returns-11:

Returns
-------

The number of cols in the motion detection grid, expressed as an
unsigned integer.

.. _example-code-11:

Example Code
------------

NA

.. _notes-and-warnings-11:

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.
