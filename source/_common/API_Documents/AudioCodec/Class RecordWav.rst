Class RecordWav
===============

.. contents::
  :local:
  :depth: 2

**RecordWav Class**
-------------------

**Description**
~~~~~~~~~~~~~~~

A class used for control and recording of .wav file format audio data.

**Syntax**
~~~~~~~~~~

.. code:: c++

    class RecordWav

**Members**
~~~~~~~~~~~

+------------------------------+-------------------------------------------------------------------+
| **Public Constructors**      |                                                                   |
+==============================+===================================================================+
| RecordWav::RecordWav         | Constructs and initializes a RecordWav class object.              |
+------------------------------+-------------------------------------------------------------------+
| **Public Methods**           |                                                                   |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::openFile          | Open a .wav audio file for recording.                             |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::closeFile         | Close a previously opened audio file.                             |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::fileOpened        | Check if a .wav file is already opened.                           |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::setSampleRate     | Set the recording sample rate of the .wav file.                   |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::setChannelCount   | Set the number of audio channels in the .wav file.                |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::setBitDepth       | Set the bit depth of each sample in the .wav file.                |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::getLengthMillis   | Get the current length of the recorded .wav file in milliseconds. |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::millisToBytes     | Convert a playback duration from milliseconds to bytes.           |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::bytesToMillis     | Convert a playback duration from bytes to milliseconds.           |
+------------------------------+-------------------------------------------------------------------+
| RecordWav::writeAudioData    | Write audio data to the .wav file.                                |
+------------------------------+-------------------------------------------------------------------+

**RecordWav::RecordWav**
------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a RecordWav class object.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void RecordWav(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/RecordWavFile/RecordWavFile.ino>`_

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::openFile**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Open a .wav audio file for recording.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void openFile(const char* absFilepath);

**Parameters**
~~~~~~~~~~~~~~

absFilepath: The absolute filepath of the .wav file that to be opened.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/RecordWavFile/RecordWavFile.ino>`_

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::closeFile**
------------------------

**Description**
~~~~~~~~~~~~~~~

Close a previously opened audio file.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void closeFile(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/RecordWavFile/RecordWavFile.ino>`_

.. note :: After recording is complete, any open.wav files should be closed; otherwise, recorded audio data may be lost.
    “RecordWav.h” must be included to use the class function.

**RecordWav::fileOpened**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Check if a .wav file is already opened.

**Syntax**
~~~~~~~~~~

.. code:: c++

    bool fileOpened(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if a .wav file is already open, false otherwise.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/RecordWavFile/RecordWavFile.ino>`_

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::setSampleRate**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set the recording sample rate of the .wav file.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setSampleRate(uint32_t sampleRate);

**Parameters**
~~~~~~~~~~~~~~

sampleRate: recording sample rate.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/RecordWavFile/RecordWavFile.ino>`_

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::setChannelCount**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the number of recording audio channels in the .wav file.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setChannelCount(uint16_t channelCount);

**Parameters**
~~~~~~~~~~~~~~

channelCount: number of recording audio channels.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::setBitDepth**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Set the recording bit depth of each sample in the .wav file.

**Syntax**
~~~~~~~~~~
.. code:: c++
    
    void setBitDepth(uint16_t bitDepth);

**Parameters**
~~~~~~~~~~~~~~

bitDepth: number of bits per sample.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::getLengthMillis**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current length of the recorded .wav file in milliseconds.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint32_t getLengthMillis(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current length of the recorded .wav file in milliseconds.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::millisToBytes**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Convert a playback duration from milliseconds to bytes.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint32_t millisToBytes(uint32_t ms);

**Parameters**
~~~~~~~~~~~~~~

ms: playback duration in milliseconds.

**Returns**
~~~~~~~~~~~

This function returns the number of bytes that is equivalent to the input playback duration in ms, converted using the current sample rate, number of channels and bit depth.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::bytesToMillis**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Convert a playback duration from bytes to milliseconds.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint32_t bytesToMillis(uint32_t bytes);

**Parameters**
~~~~~~~~~~~~~~

bytes: playback duration in number of bytes.

**Returns**
~~~~~~~~~~~

This function returns the time duration in milliseconds that is equivalent to the input number of bytes, converted using the current sample rate, number of channels and bit depth.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RecordWav.h” must be included to use the class function.

**RecordWav::writeAudioData**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Write audio data to the .wav file.

**Syntax**
~~~~~~~~~~
.. code:: c++

    uint32_t writeAudioData(int8_t* src, uint32_t len);
    uint32_t writeAudioData(int16_t* src, uint32_t len);

**Parameters**
~~~~~~~~~~~~~~

src: pointer to array containing data to write to .wav file.
len: number of audio samples to write to .wav file.

**Returns**
~~~~~~~~~~~

The function returns number of audio samples written to the .wav file.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/RecordWavFile/RecordWavFile.ino>`_

.. note :: “RecordWav.h” must be included to use the class function.
