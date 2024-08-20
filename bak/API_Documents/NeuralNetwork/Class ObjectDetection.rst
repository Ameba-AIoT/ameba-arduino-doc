ObjectDetectionResult Class 
============================

Description
-----------

A class used to represent and retrieve data related to objects
recognized by an object detection neural network.

Syntax
------

class ObjectDetectionResult

**Members**
-----------

**Public Constructors**

+-------------------------------------+--------------------------------+
| ObjectDet                           | Constructs an                  |
| ectionResult::ObjectDetectionResult | ObjectDetectionResult object   |
+=====================================+================================+
+-------------------------------------+--------------------------------+

**Public Methods**

+---------------------------+------------------------------------------+
| Ob                        | Get type index of recognized object      |
| jectDetectionResult::type |                                          |
+===========================+==========================================+
| Ob                        | Get name of recognized object            |
| jectDetectionResult::name |                                          |
+---------------------------+------------------------------------------+
| Obj                       | Get confidence score of recognized       |
| ectDetectionResult::score | object                                   |
+---------------------------+------------------------------------------+
| Ob                        | Get x coordinate of the top left corner  |
| jectDetectionResult::xMin | of the bounding box containing the       |
|                           | recognized object                        |
+---------------------------+------------------------------------------+
| Ob                        | Get x coordinate of the bottom right     |
| jectDetectionResult::xMax | corner of the bounding box containing    |
|                           | the recognized object                    |
+---------------------------+------------------------------------------+
| Ob                        | Get y coordinate of the top left corner  |
| jectDetectionResult::yMin | of the bounding box containing the       |
|                           | recognized object                        |
+---------------------------+------------------------------------------+
| Ob                        | Get y coordinate of the bottom right     |
| jectDetectionResult::yMax | corner of the bounding box containing    |
|                           | the recognized object                    |
+---------------------------+------------------------------------------+

NNObjectDetection Class 
========================



Description
-----------

A class used to configure, run, and retrieve results of an object
detection neural network model.



Syntax
------

class NNObjectDetection



**Members**
-----------

**Public Constructors**

+--------------------------------+-------------------------------------+
| NNObje                         | Constructs an NNObjectDetection     |
| ctDetection::NNObjectDetection | object                              |
+================================+=====================================+
+--------------------------------+-------------------------------------+

**Public Methods**

+-----------------------------------+----------------------------------+
| NNObjectDetection::configVideo    | Configure input video stream     |
|                                   | parameters                       |
+===================================+==================================+
| NNObject                          | Configure object detection       |
| Detection::configRegionOfInterest | region of interest               |
+-----------------------------------+----------------------------------+
| N                                 | Configure object detection       |
| NObjectDetection::configThreshold | threshold                        |
+-----------------------------------+----------------------------------+
| NNObjectDetection::begin          | Start object detection process   |
|                                   | on input video                   |
+-----------------------------------+----------------------------------+
| NNObjectDetection::end            | Stop object detection process on |
|                                   | input video                      |
+-----------------------------------+----------------------------------+
| NNO                               | Set a callback function to       |
| bjectDetection::setResultCallback | receive object detection results |
+-----------------------------------+----------------------------------+
| NNObjectDetection::getResultCount | Get number of object detection   |
|                                   | results                          |
+-----------------------------------+----------------------------------+
| NNObjectDetection::getResult      | Get object detection results     |
+-----------------------------------+----------------------------------+

ObjectDetectionResult::type
===========================

| **Description**
| Get type index of recognized object, corresponding to the object
  category in the COCO image dataset.

| **Syntax**
| int type(void);

| **Parameters**
| NA

| **Returns**
| An integer indicating the category of the recognized object.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

Object categories can be obtained from the “ObjectClassList.h” file
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

ObjectDetectionResult::name
===========================

| **Description**
| Get name of recognized object.

| **Syntax**
| const char\* name(void);

| **Parameters**
| NA

| **Returns**
| A pointer to a character array containing the category name of the
  recognized object.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

Object category names can be obtained from the “ObjectClassList.h” file
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectClassList.h).

ObjectDetectionResult::score
============================

| **Description**
| Get confidence score of recognized object.

| **Syntax**
| int score(void);

| **Parameters**
| NA

| **Returns**
| An integer ranging from 0 to 100 representing the confidence of the
  recognized object category.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

ObjectDetectionResult::xMin
===========================

| **Description**
| Get x coordinate of the top left corner of the bounding box containing
  the recognized object.

| **Syntax**
| float xMin(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge
  of the input video frame and 1.00 indicating the right edge of the
  input video frame.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

ObjectDetectionResult::xMax
===========================

| **Description**
| Get x coordinate of the bottom right corner of the bounding box
  containing the recognized object.

| **Syntax**
| float xMax(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the left edge
  of the input video frame and 1.00 indicating the right edge of the
  input video frame.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

ObjectDetectionResult::yMin
===========================

| **Description**
| Get y coordinate of the top left corner of the bounding box containing
  the recognized object.

| **Syntax**
| float yMin(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the top edge
  of the input video frame and 1.00 indicating the bottom edge of the
  input video frame.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

ObjectDetectionResult::yMax
===========================

| **Description**
| Get y coordinate of the bottom right corner of the bounding box
  containing the recognized object.

| **Syntax**
| float yMax(void);

| **Parameters**
| NA

| **Returns**
| A float ranging from 0.00 to 1.00, with 0.00 indicating the top edge
  of the input video frame and 1.00 indicating the bottom edge of the
  input video frame.

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

NNObjectDetection::configVideo
==============================

| **Description**
| Configure input video stream parameters.

| **Syntax**
| void configVideo(VideoSetting& config);

| **Parameters**
| config: VideoSetting class object containing desired video
  configuration.

| **Returns**
| NA

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

The object detection model requires that the input video stream uses the
RGB format, which is only available on video stream channel 3. The input
video stream needs to be configured before object detection can begin.

NNObjectDetection::configRegionOfInterest
=========================================

| **Description**
| Configure object detection region of interest. Object detection will
  only be performed on the image frame within the region of interest.

| **Syntax**
| void configRegionOfInterest(int xmin, int xmax, int ymin, int ymax);

| **Parameters**
| xmin: left boundary of region of interest, expressed in units of
  pixel.

xmax: right boundary of region of interest, expressed in units of pixel.

ymin: top boundary of region of interest, expressed in units of pixel.

ymax: bottom boundary of region of interest, expressed in units of
pixel.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

NNObjectDetection::configThreshold
==================================

| **Description**
| Configure object detection threshold.

| **Syntax**
| void configThreshold(float confidence_threshold, float nms_threshold);

| **Parameters**
| confidence_threshold: Object detection confidence threshold. Default
  value of 0.5.

nms_threshold: Non-Maximal Suppression threshold. Default value of 0.3.
Affects the selection of appropriate and accurate bounding boxes. A
smaller value results in less accurate bounding boxes.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

NNObjectDetection::begin
========================

| **Description**
| Start object detection process on input video.

| **Syntax**
| void begin(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

NNObjectDetection::end
======================

| **Description**
| Stop object detection process on input video.

| **Syntax**
| void end(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

NNObjectDetection::setResultCallback
====================================

| **Description**
| Set a callback function to receive object detection results.

| **Syntax**
| void setResultCallback(void
  (\*od_callback)(std::vector<ObjectDetectionResult>));

| **Parameters**
| od_callback: A callback function that accepts a vector of
  ObjectDetectionResult class objects as argument and returns void.

| **Returns**
| NA

| **Example Code**
| Example: ObjectDetectionCallback

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionCallback/ObjectDetectionCallback.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function. The
  callback function will be called with the latest results once per
  iteration.

NNObjectDetection::getResultCount
=================================

| **Description**
| Get number of object detection results.

| **Syntax**
| uint16_t getResultCount(void);

| **Parameters**
| NA

| **Returns**
| The number of detected objects in the most recent set of results, as
  an unsigned integer.

| **Example Code**
| NA

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.

NNObjectDetection::getResult
============================

| **Description**
| Get object detection results.

| **Syntax**
| ObjectDetectionResult getResult(uint16_t index);

std::vector<ObjectDetectionResult> getResult(void);

| **Parameters**
| index: index of specific object detection result to retrieve

| **Returns**
| If no index is specified, the function returns all detected objects
  contained in a vector of ObjectDetectionResult class objects.

If an index is specified, the function returns the specific detected
object contained in a ObjectDetectionResult class object.

| **Example Code**
| Example: ObjectDetectionLoop

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/ObjectDetectionLoop/ObjectDetectionLoop.ino)

| **Notes and Warnings**
| “NNObjectDetection.h” must be included to use the class function.
