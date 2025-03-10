Class FFT
=========

.. contents::
  :local:
  :depth: 2

**FFT Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used for performing FFT calculations with real-number inputs and outputs.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class FFT

**Members**
~~~~~~~~~~~

+---------------------------+---------------------------------------------+
| **Public Constructors**                                                 |
+===========================+=============================================+
| FFT::FFT                  | Constructs a FFT class object.              |
+---------------------------+---------------------------------------------+
| **Public Methods**                                                      |
+---------------------------+---------------------------------------------+
| FFT::setWindow            | Set window function used for FFT            |
|                           | calculations                                |
+---------------------------+---------------------------------------------+
| FFT::calculate            | Calculate FFT for an array of input values. |
+---------------------------+---------------------------------------------+
| FFT::getFrequencyBins     | Get the FFT output frequency bins.          |
+---------------------------+---------------------------------------------+
| FFT::getFFTSize           | Get the size of FFT output for a given      |
|                           | SampleCount.                                |
+---------------------------+---------------------------------------------+

**FFT::FFT**
------------

**Description**
~~~~~~~~~~~~~~~

Constructs a FFT class object.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void FFT(Void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FFT <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/FFT/FFT.ino>`_

.. note :: “FFT.h” must be included to use the class function.

**FFT::setWindow**
------------------

**Description**
~~~~~~~~~~~~~~~

Set window function used for FFT calculations.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void setWindow(FFTWindow_t window, uint16_t sampleCount);

**Parameters**
~~~~~~~~~~~~~~

window: The window function to be used in FFT calculations.
Valid values:
- None (Default rectangular window)
- Hann
- Hamming
sampleCount: Number of sample datapoints in the input array. Valid values: 16, 32, 64, 128, 256, 512, 1024, 2048.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FFT <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/FFT/FFT.ino>`_

.. note :: The window function is used to reduce the effects of discontinuities that occur when the input signal has frequencies that do not fit an integer number of periods in the sample datapoints.
  More information on FFTs and window functions can be seen at:
  https://download.ni.com/evaluation/pxi/Understanding%20FFTs%20and%20Windowing.pdf
  https://en.wikipedia.org/wiki/Window_function
  “FFT.h” must be included to use the class function.

**FFT::Calculate**
------------------

**Description**
~~~~~~~~~~~~~~~

Calculate FFT for an array of input values.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void calculate(float* inputBuf, float* outputBuf, uint16_t sampleCount);
  void calculate(int16_t* inputBuf, float* outputBuf, uint16_t sampleCount);

**Parameters**
~~~~~~~~~~~~~~

inputBuf: pointer to an array of sampleCount size, containing input sample datapoints, in float or uint16_t format.
outputBuf: pointer to a float array of (sampleCount / 2) size, for containing calculated FFT result.
sampleCount: number of sample datapoints in the input array. Valid values: 16, 32, 64, 128, 256, 512, 1024, 2048.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FFT <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/FFT/FFT.ino>`_

.. note :: Larger sample counts will require more time for FFT calculations, but will provide a higher frequency resolution output.
  “FFT.h” must be included to use the class function.

**FFT::getFrequencyBins**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get a corresponding output FFT frequency bin for a given sample rate and sample count.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void getFrequencyBins(uint16_t* outputBuf, uint16_t sampleCount, uint32_t sampleRate);

**Parameters**
~~~~~~~~~~~~~~

outputBuf: pointer to a uint16_t array of (sampleCount / 2) size, for containing the calculated center frequency of each FFT output element.
sampleCount: number of sample datapoints in the input array. Valid values: 16, 32, 64, 128, 256, 512, 1024, 2048.
sampleRate: Defines how many times an audio signal is sampled in a second. In the example “FFT.ino”, sample rate is set at 16000, which means that each audio signal contains 16000 individual samples.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `FFT <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/FFT/FFT.ino>`_

.. note :: “FFT.h” must be included to use the class function.

**FFT::getFFTSize**
-------------------

**Description**
~~~~~~~~~~~~~~~

Get the size of FFT output for a given sampleCount.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint16_t getFFTSize(uint16_t sampleCount);

**Parameters**
~~~~~~~~~~~~~~

sampleCount: number of sample datapoints in the input array. Valid values: 16, 32, 64, 128, 256, 512, 1024, 2048.

**Returns**
~~~~~~~~~~~

This function returns the FFT output size for the given sampleCount, which is (sampleCount / 2).

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “FFT.h” must be included to use the class function.
