AudioClassificationResult Class 
================================

Description
-----------

A class used to represent and retrieve data related to audio recognized
by an audio classification neural network.

Syntax
------

class AudioClassificationResult

**Members**
-----------

**Public Constructors**

+---------------------------+------------------------------------------+
| Au                        | Constructs an AudioClassificationResult  |
| dioClassificationResult:: | object                                   |
| AudioClassificationResult |                                          |
+===========================+==========================================+
+---------------------------+------------------------------------------+

**Public Methods**

+---------------------------+------------------------------------------+
| Objec                     | Get class ID of recognized audio         |
| tDetectionResult::classID |                                          |
+===========================+==========================================+
| Obj                       | Get confidence score of recognized audio |
| ectDetectionResult::score |                                          |
+---------------------------+------------------------------------------+

NNAudioClassification Class 
============================



Description
-----------

A class used to configure, run, and retrieve results of an audio
classification neural network model.



Syntax
------

class NNAudioClassification



**Members**
-----------

**Public Constructors**

+------------------------------------+---------------------------------+
| NNAudioClassification::            | Constructs an                   |
| NNAudioClassification              | NNAudioClassification object    |
+====================================+=================================+
+------------------------------------+---------------------------------+

**Public Methods**

+-----------------------------------+----------------------------------+
| N                                 | Configure input audio stream     |
| NAudioClassification::configAudio | parameters                       |
+===================================+==================================+
| NNAudioClassification::begin      | Start audio classification       |
|                                   | process on input audio           |
+-----------------------------------+----------------------------------+
| NNAudioClassification::end        | Stop audio classification        |
|                                   | process on input audio           |
+-----------------------------------+----------------------------------+
| NNAudio                           | Set a callback function to       |
| Classification::setResultCallback | receive audio classification     |
|                                   | results                          |
+-----------------------------------+----------------------------------+
| NNAu                              | Get number of audio              |
| dioClassification::getResultCount | classification results           |
+-----------------------------------+----------------------------------+
| NNAudioClassification::getResult  | Get audio classification results |
+-----------------------------------+----------------------------------+
|                                   |                                  |
+-----------------------------------+----------------------------------+

AudioClassificationResult::classID
==================================

| **Description**
| Get class ID of recognized audio.

| **Syntax**
| int classID(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino
)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.

Object categories can be obtained from the “AudioClassList.h” file
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassList.h).

AudioClassificationResult::score
================================

| **Description**
| Get confidence score of recognized audio classes.

| **Syntax**
| int score(void);

| **Parameters**
| NA

| **Returns**
| An integer ranging from 0 to 100 representing the confidence of the
  recognized audio class.

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino
)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.

Object categories can be obtained from the “AudioClassList.h” file
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassList.h).

**NNAudioClassification::configAudio**

| **Description**
| Configure input audio stream parameters.

**Syntax**

void configAudio (AudioSetting& config, uint16_t bitDepth = 16);

| **Parameters**
| config: AudioSetting class object containing desired audio
  configuration.

bitDepth: number of bits of information in each audio sample. (Default:
16 bits)

| **Returns**
| NA

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::begin
============================

| **Description**
| Start audio classification process on input audio.

| **Syntax**
| void begin (void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::end
==========================

| **Description**
| Stop audio classification process on input audio.

| **Syntax**
| void end (void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::setResultCallback
========================================

| **Description**
| Set a callback function to receive audio classification results.

| **Syntax**
| void setResultCallback(void
  (\*ac_callback)(std::vector<AudioClassificationResult>));

| **Parameters**
| ac_callback: A callback function that accepts a vector of
  AudioClassificationResult class objects as argument and returns void.

| **Returns**
| NA

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.
  The callback function will be called with the latest results once per
  iteration.

NNAudioClassification::getResultCount
=====================================

| **Description**
| Get number of audio classification results.

| **Syntax**
| uint16_t getResultCount(void);

| **Parameters**
| NA

| **Returns**
| The number of recognized audio classes in the most recent set of
  results, as an unsigned integer.

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::getResult
================================

| **Description**
| Get audio classification results.

| **Syntax**
| AudioClassificationResult getResult(uint16_t index);

std::vector<AudioClassificationResult> getResult(void);

| **Parameters**
| index: index of specific audio classification result to retrieve

| **Returns**
| If no index is specified, the function returns all recognized audio
  classes contained in a vector of AudioClassificationResult class
  objects.

If an index is specified, the function returns the specific recognized
audio class contained in a AudioClassificationResult class object.

| **Example Code**
| Example: AudioClassification

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino)

| **Notes and Warnings**
| “NNAudioClassification.h” must be included to use the class function.
