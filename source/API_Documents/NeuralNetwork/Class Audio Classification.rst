Class Audio Classification
==========================

.. contents::
  :local:
  :depth: 2

**AudioClassificationResult Class**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

A class used to represent and retrieve data related to audio recognized by an audio classification neural network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  class AudioClassificationResult

**Members**
~~~~~~~~~~~

+--------------------------------------+------------------------------------------+
| **Public Constructors**                                                         |
+======================================+==========================================+
| AudioClassificationResult::          | Constructs an AudioClassificationResult  |
| AudioClassificationResult            | object                                   |
+--------------------------------------+------------------------------------------+
| **Public Methods**                                                              |
+--------------------------------------+------------------------------------------+
| AudioClassificationResult::classID   | Get class ID of recognized audio         |
+--------------------------------------+------------------------------------------+
| AudioClassificationResult::score     | Get confidence score of recognized audio |
+--------------------------------------+------------------------------------------+


**AudioClassificationResult::classID**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get class ID of recognized audio.


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

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_


.. note :: “NNAudioClassification.h” must be included to use the class function. Object categories can be obtained from the “AudioClassList.h” file. 
  (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassList.h)


**AudioClassificationResult::score**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get confidence score of recognized audio classes.


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

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_

.. note :: “NNAudioClassification.h” must be included to use the class function. Object categories can be obtained from the “AudioClassList.h” file. 
  (https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassList.h)


**NNAudioClassification Class**
-------------------------------

**Description**
~~~~~~~~~~~~~~~
A class used to configure, run, and retrieve results of an audio classification neural network model.

**Syntax**
~~~~~~~~~~
.. code-block:: c++
  
  class NNAudioClassification
  
**Members**
~~~~~~~~~~~

+---------------------------------------------+--------------------------------------------+
| **Public Constructors**                                                                  |
+=============================================+============================================+
| NNAudioClassification::                     | Constructs an NNAudioClassification        |
| NNAudioClassification                       | object                                     |
+---------------------------------------------+--------------------------------------------+
| **Public Methods**                                                                       |
+---------------------------------------------+--------------------------------------------+
| NNAudioClassification::configAudio          | Configure input audio stream               |
|                                             | parameters                                 |
+---------------------------------------------+--------------------------------------------+
| NNAudioClassification::begin                | Start audio classification                 |
|                                             | process on input audio                     |
+---------------------------------------------+--------------------------------------------+
| NNAudioClassification::end                  | Stop audio classification                  |
|                                             | process on input audio                     |
+---------------------------------------------+--------------------------------------------+
| NNAudioClassification::setResultCallback    | Set a callback function to receive audio   |
|                                             | classification results                     |
+---------------------------------------------+--------------------------------------------+
| NNAudioClassification::getResultCount       | Get number of audio classification results |
+---------------------------------------------+--------------------------------------------+
| NNAudioClassification::getResult            | Get audio classification results           |
+---------------------------------------------+--------------------------------------------+

NNAudioClassification::configAudio
----------------------------------

**Description**
~~~~~~~~~~~~~~~
Configure input audio stream parameters.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void configAudio(AudioSetting& config, uint16_t bitDepth = 16);

**Parameters**
~~~~~~~~~~~~~~

config: AudioSetting class object containing desired audio configuration.

bitDepth: number of bits of information in each audio sample. (Default: 16 bits)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_

.. note :: “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::begin
----------------------------

**Description**
~~~~~~~~~~~~~~~

Start audio classification process on input audio.

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

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_

.. note :: “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::end
--------------------------

**Description**
~~~~~~~~~~~~~~~

Stop audio classification process on input audio.

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

.. note :: “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::setResultCallback
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to receive audio classification results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  void setResultCallback(void (*ac_callback)(std::vector));

**Parameters**
~~~~~~~~~~~~~~

ac_callback: A callback function that accepts a vector of AudioClassificationResult class objects as argument and returns void.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_

.. note :: “NNAudioClassification.h” must be included to use the class function. The callback function will be called with the latest results once per iteration.

NNAudioClassification::getResultCount
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get number of audio classification results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  uint16_t getResultCount(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The number of recognized audio classes in the most recent set of results, as an unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_

.. note :: “NNAudioClassification.h” must be included to use the class function.

NNAudioClassification::getResult
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get audio classification results.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  AudioClassificationResult getResult(uint16_t index);
  std::vector getResult(void);

**Parameters**
~~~~~~~~~~~~~~

index: index of specific audio classification result to retrieve

**Returns**
~~~~~~~~~~~

If no index is specified, the function returns all recognized audio classes contained in a vector of AudioClassificationResult class objects.

If an index is specified, the function returns the specific recognized audio class contained in a AudioClassificationResult class object.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `AudioClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/AudioClassification/AudioClassification.ino>`_

.. note :: “NNAudioClassification.h” must be included to use the class function.