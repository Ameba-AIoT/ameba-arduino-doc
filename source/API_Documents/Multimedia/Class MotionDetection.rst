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

Description
-----------

A class used to retrieve data when motion is detected by comparing the
RGB information of each image frame captured from the on-board camera
sensor (JX-F37P).


Syntax
------

Class MotionDetection

Members
-------

+-----------------------------------+----------------------------------+
| **Public Constructors**                                              |
+===================================+==================================+
| MotionDetection::MotionDetection  | Constructs a MotionDetection     |
|                                   | object and set motion detection  |
|                                   | resolution.                      |
+-----------------------------------+----------------------------------+

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
| Example: [LoopPostProcessing](https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

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
| Example: [LoopPostProcessing](https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

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
| Example: [LoopPostProcessing](https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

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

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

| **Notes and Warnings**
| “NNMotionDetection.h” must be included to use the class function.

**MotionDetection::MotionDetection**



Description
-----------

Constructs a MotionDetection object and configure motion detection
resolution.



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
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::configResolution**



Description
-----------

Configure motion detection resolution.



Syntax
------

void configResolution(uint8_t row, uint8_t col);



Parameters
----------

row: Number of rows for motion detection grid resolution. Default value
of 18. (Valid value, 18 or 32)

col: Number of columns for motion detection grid resolution. Default
value of 32. (Valid value: 32)



Returns
-------

NA



Example Code
------------

NA



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::configVideo**



Description
-----------

Configure input video stream parameters.



Syntax
------

void configVideo(VideoSetting& config);



Parameters
----------

config: VideoSetting class object containing desired video
configuration.



Returns
-------

NA



Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function. For
motion detection, the input video stream uses the RGB format, which is
only available on video stream channel 3.

**MotionDetection::begin**



Description
-----------

Start motion detection process on input video.



Syntax
------

void begin(void);



Parameters
----------

NA



Returns
-------

NA



Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::end**



Description
-----------

Stop motion detection process on input video.



Syntax
------

void end(void);



Parameters
----------

NA



Returns
-------

NA



Example Code
------------

NA



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::setTriggerBlockCount**



Description
-----------

Set the number of blocks to trigger motion detection output.



Syntax
------

void setTriggerBlockCount(uint16_t count);



Parameters
----------

count: Threshold number of blocks with motion.



Returns
-------

NA



Example Code
------------

NA



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::setDetectionMask**



Description
-----------

Set a specific region in the motion detection grid to ignore motion.



Syntax
------

void setDetectionMask(char \* mask);



Parameters
----------

mask: a pointer to a char array containing the regions where motion
detection is enabled or disabled. A value of 1 will enable motion
detection for the grid region, a value of 0 will disable motion
detection for the grid region.



Returns
-------

NA



Example Code
------------

NA



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::getResult**



Description
-----------

Get motion detection results.



Syntax
------

MotionDetectionResult getResult(uint16_t index);

std::vector<MotionDetectionResult> getResult(void);



Parameters
----------

index: index of specific motion detection result to retrieve.



Returns
-------

If no index is specified, the function returns all detected motions
contained in a vector of MotionDetectionResult class objects.

If an index is specified, the function returns the specific detected
motion contained in a MotionDetectionResult class object.



Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::setResultCallback**



Description
-----------

Set a callback function to receive and display motion detection results.



Syntax
------

void setResultCallback(void
(\*md_callback)(std::vector<MotionDetectionResult>));



Parameters
----------

md_callback: : A callback function that accepts a vector of
MotionDetectionResult class objects as argument and returns void.



Returns
-------

NA



Example Code
------------

Example: CallbackPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/CallbackPostProcessing/CallbackPostProcessing.ino)



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::getResultCount**



Description
-----------

Get number of motion detection results.



Syntax
------

uint16_t getResultCount(void);



Parameters
----------

NA



Returns
-------

The number of detected motions in the most recent set of results, as an
unsigned integer.



Example Code
------------

Example: CallbackPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/CallbackPostProcessing/CallbackPostProcessing.ino)



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::rows**



Description
-----------

Get currently configured number of rows for motion detection grid.



Syntax
------

uint8_t rows(void);



Parameters
----------

NA



Returns
-------

The number of rows in the motion detection grid, expressed as an
unsigned integer.



Example Code
------------

NA



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.

**MotionDetection::cols**



Description
-----------

Get currently configured number of columns for motion detection grid.



Syntax
------

uint8_t cols(void);



Parameters
----------

NA



Returns
-------

The number of cols in the motion detection grid, expressed as an
unsigned integer.



Example Code
------------

NA



Notes and Warnings
------------------

“MotionDetection.h” must be included to use the class function.
