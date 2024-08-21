Class MP4Recording
==================

.. contents::
  :local:
  :depth: 2

**MP4Recording Class**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class used to record video and audio data streams into a MP4 file on the SD card.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class MP4Recording

**Members**
~~~~~~~~~~~

+-------------------------------------+------------------------------------+
| **Public Constructors**                                                  |
+=====================================+====================================+
| MP4Recording::MP4Recording          | Constructs a MP4Recording object   |
+-------------------------------------+------------------------------------+
| **Public Methods**                                                       |
+-------------------------------------+------------------------------------+
| MP4Recording::configVideo           | Initialize MP4Recording video      |
|                                     | stream parameters.                 |
+-------------------------------------+------------------------------------+
| MP4Recording::configAudio           | Initialize MP4Recording audio      |
|                                     | stream parameters.                 |
+-------------------------------------+------------------------------------+
| MP4Recording::begin                 | Start recording MP4 to SD card.    |
+-------------------------------------+------------------------------------+
| MP4Recording::end                   | Stop recording MP4 to SD card.     |
+-------------------------------------+------------------------------------+
| MP4Recording::setRecordingFileName  | Set base file name of recorded MP4 |
|                                     | files.                             |
+-------------------------------------+------------------------------------+
| MP4Recording::setRecordingDuration  | Set per-file MP4 recording         |
|                                     | duration.                          |
+-------------------------------------+------------------------------------+
| MP4Recording::setRecordingFileCount | Set total number of MP4 files to   |
|                                     | record.                            |
+-------------------------------------+------------------------------------+
| MP4Recording::setLoopRecording      | Enable loop recording mode for     |
|                                     | continuous recording.              |
+-------------------------------------+------------------------------------+
| MP4Recording::setRecordingDataType  | Enable recording video data and    |
|                                     | audio data.                        |
+-------------------------------------+------------------------------------+
| MP4Recording::getRecordingFileName  | Get currently configured base file |
|                                     | name of recorded MP4 files.        |
+-------------------------------------+------------------------------------+
| MP4Recording::getRecordingDuration  | Get currently configured per-file  |
|                                     | MP4 recording duration.            |
+-------------------------------------+------------------------------------+
| MP4Recording::getRecordingFileCount | Get currently configured total     |
|                                     | number of MP4 files to record.     |
+-------------------------------------+------------------------------------+
| MP4Recording::getRecordingState     | Get current MP4 recording state.   |
+-------------------------------------+------------------------------------+
| MP4Recording::printInfo             | Print current MP4 recording        |
|                                     | parameters.                        |
+-------------------------------------+------------------------------------+

**MP4Recording::configVideo**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize MP4Recording video stream parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideo(VideoSetting& config);

**Parameters**
~~~~~~~~~~~~~~

config: VideoSetting class object containing desired video configuration.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::configAudio**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize MP4Recording audio stream parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configAudio(AudioSetting& config, Audio_Codec_T codec);

**Parameters**
~~~~~~~~~~~~~~

config: AudioSetting object containing desired audio configuration.

codec: Codec format of Audio stream input.

- CODEC_AAC

- CODEC_G711_PCMU

- CODEC_G711_PCMA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::begin**
-----------------------

**Description**
~~~~~~~~~~~~~~~

Start MP4 recording to SD card.

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

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::end**
---------------------

**Description**
~~~~~~~~~~~~~~~

Stop MP4 recording to SD card.

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

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::setRecordingFileName**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set base file name of recorded MP4 files.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRecordingFileName(const char* filename);
    void setRecordingFileName(String filename);

**Parameters**
~~~~~~~~~~~~~~

filename: Desired recorded MP4 filename, expresses as a character array or String class object.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: Filename can be up to 127 characters long.

“MP4Recording.h” must be included to use the class function.

**MP4Recording::setRecordingDuration**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set per-file MP4 recording duration.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRecordingDuration(uint32_t secs);

**Parameters**
~~~~~~~~~~~~~~

secs: Duration of MP4 to record, expressed in seconds.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::setRecordingFileCount**
---------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set total number of MP4 files to record.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRecordingFileCount(uint32_t count);

**Parameters**
~~~~~~~~~~~~~~

count: Total number of MP4 files to record to SD card.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: If configured to record more than 1 file, a number will be appended to the end of the base file name.

“MP4Recording.h” must be included to use the class function.

**MP4Recording::setLoopRecording**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Enable loop recording mode for continuous recording.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setLoopRecording(int enable);

**Parameters**
~~~~~~~~~~~~~~

enable: Enable or disable loop recording.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: Enabling loop recording will overwrite the oldest previously recorded MP4 file when the total number of MP4 files to record has been reached.

“MP4Recording.h” must be included to use the class function.

**MP4Recording::setRecordingDataType**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Enable recording video data and audio data.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setRecordingDataType(uint8_t type);

**Parameters**
~~~~~~~~~~~~~~

type: one of the following values, default value of STORAGE_ALL.

- STORAGE_ALL – record both video data and audio data.

- STORAGE_VIDEO – record only video data.

- STORAGE_AUDIO – record only audio data.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/VideoOnly <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/VideoOnly/VideoOnly.ino>`_

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::getRecordingFileName**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get currently configured base file name of recording MP4 files.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    String getRecordingFileName(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

A String class object containing the currently configured MP4 base file name.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::getRecordingDuration**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get currently configured per-file MP4 recording duration.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t getRecordingDuration(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

Currently configured per-file recording duration, expressed in seconds.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::getRecordingFileCount**
---------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get currently configured total number of MP4 files to record.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t getRecordingFileCount(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

Currently configured total number of MP4 files to record.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::getRecordingState**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current MP4 recording state.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint8_t getRecordingState(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

TRUE if MP4 is currently recording, FALSE if MP4 recording has stopped.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “MP4Recording.h” must be included to use the class function.

**MP4Recording::printInfo**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Print out current configuration of MP4 recording.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void printInfo(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “MP4Recording.h” must be included to use the class function.
