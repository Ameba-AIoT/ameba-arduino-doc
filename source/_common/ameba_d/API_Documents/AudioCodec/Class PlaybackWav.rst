Class PlaybackWav
=================

**PlaybackWav Class**
---------------------

**Description**
~~~~~~~~~~~~~~~

A class used for controlling and playback of .wav file format audio data.

**Syntax**
~~~~~~~~~~

.. code:: c++

  class PlaybackWav

**Members**
~~~~~~~~~~~

+---------------------------------+----------------------------------------------------------+
| **Public Constructors**                                                                    |
+=================================+==========================================================+
| PlaybackWav::PlaybackWav        | Constructs a PlaybackWav class object.                   |
+---------------------------------+----------------------------------------------------------+
| **Public Methods**                                                                         |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::openFile           | Open a .wav audio file for playback.                     |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::closeFile          | Close a previously opened audio file.                    |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::fileOpened         | Check if a .wav file is already opened.                  |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::getSampleRate      | Get the sample rate of the .wav file.                    |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::getChannelCount    | Get the number of audio channels in the .wav file.       |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::getBitDepth        | Get the bit depth of each sample in the .wav file.       |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::getLengthMillis    | Get the playback length of the .wav file in milliseconds.|
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::getPositionMillis  | Get the current playback position in milliseconds.       |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::setPositionMillis  | Set the current playback position in milliseconds.       |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::millisToBytes      | Convert a playback duration from milliseconds to bytes.  |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::bytesToMillis      | Convert a playback duration from bytes to milliseconds.  |
+---------------------------------+----------------------------------------------------------+
| PlaybackWav::readAudioData      | Read audio data from the .wav file.                      |
+---------------------------------+----------------------------------------------------------+

**PlaybackWav::PlaybackWav**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a PlaybackWav class object.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void PlaybackWav(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::openFile**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Open a .wav file for playback.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void openFile(const char* absFilepath);

**Syntax**
~~~~~~~~~~

absFilepath: The filepath of the .wav file that will be opened.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::closeFile**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Close a previously opened audio file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void closeFile(void);

**Syntax**
~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::fileOpened**
---------------------------

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

Example: `RecordPlaybackWav <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::getSampleRate**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the sample rate of the .wav file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t getSampleRate(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns sampling rate encoded in the .wav file header.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::getChannelCount**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the number of audio channels in the .wav file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint16_t getChannelCount(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns channel count encoded in the .wav file header.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::getBitDepth**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the bit depth of each sample in the .wav file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint16_t getBitDepth(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns bit depth encoded in the .wav file header.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::getLengthMillis**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the playback length of the .wav file in milliseconds.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t getLengthMillis(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the total playback length of the currently open .wav file in milliseconds.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::getPositionMillis**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the current playback position in milliseconds.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t getPositionMillis(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

The function returns the current playback position of the currently open .wav file in milliseconds.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::setPositionMillis**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Set the current playback position in milliseconds.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void setPositionMillis(uint32_t pos);

**Parameters**
~~~~~~~~~~~~~~

pos: The desired playback position expressed in milliseconds.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: Any changes to playback position will only take effect on the next call to PlaybackWav::readAudioData. If the desired playback position is beyond the total playback length of the file, the playback position will be set to the end of file, and no audio data will be output on subsequent data reads.
  "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::millisToBytes**
------------------------------

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

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::bytesToMillis**
------------------------------

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

.. note :: "PlaybackWav.h" must be included to use the class function.

**PlaybackWav::readAudioData**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Read audio data from the .wav file.

**Syntax**
~~~~~~~~~~

.. code:: c++

  uint32_t readAudioData(int8_t* dst, uint32_t len);
  uint32_t readAudioData(int16_t* dst, uint32_t len);

**Parameters**
~~~~~~~~~~~~~~

dst: Pointer to an array that stores audio data from .wav file to be read .
len: number of audio samples to be read from .wav file.

**Returns**
~~~~~~~~~~~

This function returns number of audio samples to be read.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `PlaybackWavFile <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/AudioCodec/examples/PlaybackWavFile/PlaybackWavFile.ino>`_

.. note :: "PlaybackWav.h" must be included to use the class function.
