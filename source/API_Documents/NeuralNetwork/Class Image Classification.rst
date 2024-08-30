Class Image Classification
===========================

.. contents::
  :local:
  :depth: 2

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
| NNImageClassification::                        | Constructs an NNImageClassification object                        |
| NNImageClassification                          |                                                                   |
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
| NNImageClassification::classID                 | Get class ID of class with highest probability                    |
+------------------------------------------------+-------------------------------------------------------------------+
| NNImageClassification::score                   | Get the probability of the class with the highest likelihood      |
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

color: Color of images used for model training (0: Grayscale, 1: RGB)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h” must be included to use the class function.

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

Example: `RTSPImageClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h” must be included to use the class function.

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

| xmin: left boundary of region of interest, expressed in units of pixel.
| xmax: right boundary of region of interest, expressed in units of pixel.
| ymin: top boundary of region of interest, expressed in units of pixel.
| ymax: bottom boundary of region of interest, expressed in units of pixel.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: NNImageClassification.h” must be included to use the class function.

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

Example: `RTSPImageClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h” must be included to use the class function.

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

.. note :: NNImageClassification.h” must be included to use the class function.

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

Example: `RTSPImageClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h” must be included to use the class function.

**NNImageClassification::classID**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the class ID of class with highest probability.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  int classID(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

An integer representing the class ID of class with highest probability.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h” must be included to use the class function.

**NNImageClassification::score**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the probability of the class with the highest likelihood.

**Syntax**
~~~~~~~~~~
.. code-block:: c++

  int score(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A floating-point number between 0 and 1 representing the probability of the class with the highest likelihood.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPImageClassification <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPImageClassification/RTSPImageClassification.ino>`_

.. note :: NNImageClassification.h” must be included to use the class function.

