Class AudioCodec 
================

.. contents::
  :local:
  :depth: 2

**AudioCodec Class**
--------------------

**Description**
~~~~~~~~~~~~~~~


A class used for general control and management of the hardware audio
codec functions.

**Syntax**
~~~~~~~~~~


.. code:: c++

    class AudioCodec
    

**Members**
~~~~~~~~~~~

+-------------------------------+-----------------------------------------+
| **Public Constructors**                                                 |
+===============================+=========================================+
| The public constructor is not recommended to be used as a               |
| singleton class. Class is for built-in Audio Codec.                     |
+-------------------------------+-----------------------------------------+
| **Public Methods**                                                      |
+-------------------------------+-----------------------------------------+
| AudioCodec::begin             | Configure Audio Codec to start          |
|                               | transmitting and receiving operations.  |
+-------------------------------+-----------------------------------------+
| AudioCodec::end               | Deinitialize all Audio Codec operations.|
+-------------------------------+-----------------------------------------+
| AudioCodec::getBufferPageSize | Get byte size per page, and default     |
|                               | value is 1024.                          |
+-------------------------------+-----------------------------------------+
| AudioCodec::setSampleRate     | Set the sample rate for transmitting    |
|                               | and receiving.                          |
+-------------------------------+-----------------------------------------+
| AudioCodec::setBitDepth       | Set the bit depth (bits per sample) for |
|                               | transmitting and receiving.             |
+-------------------------------+-----------------------------------------+
| AudioCodec::setChannelCount   | Set the number of channels for          |
|                               | transmitting and receiving              |
|                               | (Mono or Stereo).                       |
+-------------------------------+-----------------------------------------+
| AudioCodec::setInputMicType   | Set microphone type input               |
|                               | (analog or digital).                    |
+-------------------------------+-----------------------------------------+
| AudioCodec::setInputLRMux     | Set input for audio multiplexing        |
|                               | (left and right).                       |
+-------------------------------+-----------------------------------------+
| AudioCodec::setDMicBoost      | Set boost gain for digital              |
|                               | microphone input                        |
+-------------------------------+-----------------------------------------+
| AudioCodec::setAMicBoost      | Set boost gain for analog               |
|                               | microphone input                        |
+-------------------------------+-----------------------------------------+
| AudioCodec::setADCGain        | Set Analog Digital Converter (ADC)      |
|                               | gain to obtain analog input.            |
+-------------------------------+-----------------------------------------+
| AudioCodec::muteInput         | Mute input audio.                       |
+-------------------------------+-----------------------------------------+
| AudioCodec::setOutputVolume   | Set output audio volume.                |
+-------------------------------+-----------------------------------------+
| AudioCodec::muteOutput        | Mute output audio                       |
+-------------------------------+-----------------------------------------+
| AudioCodec::writeAvaliable    | Check if data buffer is                 |
|                               | available for data writing.             |
+-------------------------------+-----------------------------------------+
| AudioCodec::writeDataPage     | Write audio data to the available       |
|                               | data buffer for data transmission.      |
+-------------------------------+-----------------------------------------+
| AudioCodec::readAvaliable     | Check for data buffer with audio data   |
|                               | to be read.                             |
+-------------------------------+-----------------------------------------+
| AudioCodec::readDataPage      | Read received audio data from buffer.   |
+-------------------------------+-----------------------------------------+
| AudioCodec::setWriteCallback  | Set a callback function to be notified  |
|                               | when a data buffer is available         |
|                               | for data write.                         |
+-------------------------------+-----------------------------------------+
| AudioCodec::setReadCallback   | Set a callback function to be notified  |
|                               | when there is available data buffer with|
|                               | audio data to be read.                  |
+-------------------------------+-----------------------------------------+

**AudioCodec::begin**
---------------------

**Description**
~~~~~~~~~~~~~~~

Configure and start the audio codec for transmit and receive operation.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void begin(bool input, bool output);

**Parameters**
~~~~~~~~~~~~~~

input: enable Audio Codec data input
output: enable Audio Codec data output

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::end**
-------------------

**Description**
~~~~~~~~~~~~~~~

Deintialize all Audio Codec input and output operations.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void end(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::getBufferPageSize**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get byte size per page, and default value is 1024 bytes.

**Syntax**
~~~~~~~~~~


.. code:: c++

    uint32_t getBufferPageSize(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the size per page, in number of bytes (default: 1024).

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: The AudioCodec class includes a Tx and Rx buffer for storing audio sample data while it is being transferred to and from the DAC output and ADC input. The buffer is divided into fixed-size pages, allowing audio data to be read and written one page at a time. A buffer page may contain a different number of audio samples depending on the bit depth (bits per audio sample) and channel count set.
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setSampleRate**

**Description**
~~~~~~~~~~~~~~~

Set the sample rate for transmitting and receiving.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setSampleRate(uint32_t sampleRate);

**Parameters**
~~~~~~~~~~~~~~

sampleRate: Audio Codec's sampling rate in Hz. (Default: 48000 Hz). Supported values: 8000, 16000, 32000, 44100, 48000, 88200, 96000 (in Hz).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: Higher sample rates beyond 48000Hz will require more frequent buffer read and write operations to keep up with the large amount of data input and output. If there is insufficient processing time dedicated to this task, audio quality will be degraded.
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setBitDepth**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Set the bit depth (bits per sample) for transmitting and receiving.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setBitDepth(uint8_t bitDepth);

**Parameters**
~~~~~~~~~~~~~~

bitDepth: Number of bits per sample. (Default: 16 bits).
Supported values:
- 8 bits
- 16 bits
- 24 bits

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Setting a bit depth of 24 bits per sample will require 32 bits (4 bytes) of buffer space for storing each sample, with the most significant byte ignored.
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setChannelCount**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the number of channels for transmitting and receiving (Mono or Stereo).

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setChannelCount(uint8_t monoStereo);

**Parameters**
~~~~~~~~~~~~~~

monoStereo: number of channels. (Default: 1).
Supported values:
- 1 (Mono Channel)
- 2 (Stereo Channel)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::setInputMicType**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set microphone type input (analog or digital).

**Syntax**
~~~~~~~~~~

.. code:: c++

    Void setInputMicType(Mic_Type micType);

**Parameters**
~~~~~~~~~~~~~~

micType: Input microphone type. (Default: ANALOGMIC).
Valid values:
- ANALOGMIC - microphone with an analog output
- PDMMIC - digital microphone with a PDM output

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: For analog single-ended output, connect to PA_4 for the left channel and PA_2 for the right channel.
    For digital PDM output, connect the PDM clock to PB_1 and PDM data to PB_2.
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setInputLRMux**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Set input for audio multiplexing (left and right).

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setInputLRMux(uint32_t mux);

**Parameters**
~~~~~~~~~~~~~~

mux: Left and right audio channel multiplexing setting. (Default value: RX_CH_LL).
Valid values:
- RX_CH_LR: Rx selected as left and right channel
- RX_CH_RL : Rx selected as right and left channel
- RX_CH_LL : Rx selected as only left channel
- RX_CH_RR : Rx selected as only right channel

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: In mono channel mode, by selecting RX_CH_LR or RX_CH_LL will result in getting sampling input data from the left channel of the microphone while by selecting RX_CH_RL or RX_CH_RR will result in getting sampling input data from the right channel of the microphone.
    In stereo channel mode, RX_CH_RL will switch the positions of input data sampled from the microphones. RX_CH_RR and RX_CH_LL will result in duplicated samples from the right and left microphones respectively.
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setDMicBoost**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set boost gain for digital microphone input.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setDMicBoost(uint32_t leftBoost, uint32_t rightBoost);

**Parameters**
~~~~~~~~~~~~~~

leftBoost: boost gain for left channel digital microphone input (Default: 0).
rightBoost: boost gain for right channel digital microphone input (Default: 0).
Valid boost gain values:

-  0 : 0dB
-  1 : 12dB
-  2 : 24dB
-  3 : 36dB

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::setAMicBoost**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Set boost gain for analog microphone input.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setAMicBoost(uint32_t leftBoost, uint32_t rightBoost);

**Parameters**
~~~~~~~~~~~~~~

leftBoost: boost gain for left channel analog microphone input (Default: 0).
rightBoost: boost gain for right channel analog microphone input (Default: 0).
Valid boost gain values:

-  0 : 0dB
-  1 : 20dB
-  2 : 30dB
-  3 : 40dB

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Only use this function if additional gain is required after using setADCGain function. 
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setADCGain**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Set Analog Digital Converter (ADC) gain to obtain analog input.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setADCGain(uint32_t leftGain, uint32_t rightGain);

**Parameters**
~~~~~~~~~~~~~~

leftGain: Gain for left channel ADC (Default: 0).
rightGain: Gain for right channel ADC (Default: 0).
Valid value range is from 0x00 to 0x7f. Gain increases by 0.375dB for every increment in value:

-  0x00 : -17.625dB
-  0x01 : -17.25dB
-  0x2f : 0dB
-  0x30 : 0.375dB
-  0x7f : 30dB

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::muteInput**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Mute input audio.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void muteInput(uint8_t leftMute, uint8_t rightMute);

**Parameters**
~~~~~~~~~~~~~~

leftMute: 1 to mute left channel input, 0 to unmute (Default: 1).
rightMute: 1 to mute right channel input, 0 to unmute (Default: 1).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::setOutputVolume**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set output audio volume. Valid value ranges from 0 to 100 corresponding to a volume of -65.625dB to 0dB. If value > 100, it will be taken as 100.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setOutputVolume(uint8_t leftVol, uint8_t rightVol);

**Parameters**
~~~~~~~~~~~~~~

leftVol: left channel output volume
rightVol: right channel output volume

**Returns**
~~~~~~~~~~~

Na

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::muteOutput**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Mute output audio.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void muteOutput(uint8_t leftMute, uint8_t rightMute);

**Parameters**
~~~~~~~~~~~~~~

leftMute: 1 to mute left channel output, 0 to unmute (Default: 1).
rightMute: 1 to mute right channel output, 0 to unmute (Default: 1).

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::writeAvaliable**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Check if data buffer is available for data writing.

**Syntax**
~~~~~~~~~~

.. code:: c++

    bool writeAvaliable(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if there is a data buffer available for writing data. It returns false if no data buffers are available.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::writeDataPage**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Write audio data to the available data buffer for data transmission.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint32_t writeDataPage(int8_t* src, uint32_t len);
    uint32_t writeDataPage(int16_t* src, uint32_t len);

**Parameters**
~~~~~~~~~~~~~~

src: pointer to array containing audio samples to write to Audio Codec.
len: number of audio samples in array.

**Returns**
~~~~~~~~~~~

This function returns the total number of audio samples written to the Audio Codec if there is available data buffer for data writting. Otherwise, it will return 0.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::readAvaliable**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Check for data buffer with audio data to be read.

**Syntax**
~~~~~~~~~~

.. code:: c++

    bool readAvaliable(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if there is a data buffer with new data to be read. It returns false if all pages are empty.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::readDataPage**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Read received audio data from data buffer.

**Syntax**
~~~~~~~~~~

.. code:: c++

    uint32_t readDataPage(int8_t* dst, uint32_t len);
    uint32_t readDataPage(int16_t* dst, uint32_t len);

**Parameters**
~~~~~~~~~~~~~~

dst: pointer to array to contain audio samples read from Audio Codec.
len: number of audio samples to read.

**Returns**
~~~~~~~~~~~

This function returns the total number of audio samples read from Audio Codec if data buffer with new data is present. Otherwise, it will return 0.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `BasicInputOutput <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/BasicInputOutput/BasicInputOutput.ino>`_

.. note :: “AudioCodec.h” must be included to use the class function.

**AudioCodec::setWriteCallback**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to be notified when a data buffer is available for data write.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setWriteCallback(void(*writeCB)(void));

**Parameters**
~~~~~~~~~~~~~~

writeCB: function to be called when data buffer becomes available for data write. Takes no arguments and returns nothing.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: After starting the Audio Codec with AudioCodec::begin(), the callback function will be called each time the Audio Codec finishes outputting the data in a buffer page.
    “AudioCodec.h” must be included to use the class function.

**AudioCodec::setReadCallback**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Set a callback function to be notified when there is available data buffer with audio data to be read.

**Syntax**
~~~~~~~~~~

.. code:: c++

    void setReadCallback(void(*readCB)(void));

**Parameters**
~~~~~~~~~~~~~~

readCB: function to be called when data buffer with new data becomes available for data read. Takes no arguments and returns nothing.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: After starting the Audio Codec with AudioCodec::begin(), the callback function will be called each time the Audio Codec fills up a buffer page with newly acquired audio samples.
    “AudioCodec.h” must be included to use the class function.
