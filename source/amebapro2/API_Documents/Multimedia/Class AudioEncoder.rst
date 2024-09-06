Class AudioEncoder
==================

.. contents::
  :local:
  :depth: 2

**AAC Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used to encode an audio data stream using AAC (Advanced Audio Codec) standard.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class AAC

**Members**
~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| **Public Constructors**                                              |
+============================+=========================================+
| AAC::AAC                   | Constructs an AAC object.               |
+----------------------------+-----------------------------------------+
| **Public Methods**                                                   |
+----------------------------+-----------------------------------------+
| AAC::configAudio           | Configure AAC module by setting up      |
|                            | audio configuration parameters.         |
+----------------------------+-----------------------------------------+
| AAC::begin                 | Start AAC module audio encoder.         |
+----------------------------+-----------------------------------------+
| AAC::end                   | Stop AAC module audio encoder.          |
+----------------------------+-----------------------------------------+

**AAC::configAudio**
--------------------

**Description**
~~~~~~~~~~~~~~~

Configure AAC module by setting up audio configuration parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configAudio(AudioSetting& config);

**Parameters**
~~~~~~~~~~~~~~

config: AudioSetting object containing desired audio configuration.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Audio/RTSPAudioStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino>`_

.. note :: “AudioEncoder.h” must be included to use the class function.

**AAC::begin**
--------------

**Description**
~~~~~~~~~~~~~~~

Start AAC audio encoder.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(void);

**Parameters**
~~~~~~~~~~~~~~

config: AudioSetting object containing desired audio configuration.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Audio/RTSPAudioStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino>`_

.. note :: “AudioEncoder.h” must be included to use the class function.

**AAC::end**
------------

**Description**
~~~~~~~~~~~~~~~

Stop AAC audio encoder.

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

.. note :: “AudioEncoder.h” must be included to use the class function.


**G711E Class**
---------------

**Description**
~~~~~~~~~~~~~~~

A class used to encode an audio data stream using ITU-T G.711 standard.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class G711E

**Members**
~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| **Public Constructors**                                              |
+============================+=========================================+
| G711E::G711E               | Constructs a G711E object.              |
+----------------------------+-----------------------------------------+
| **Public Methods**                                                   |
+----------------------------+-----------------------------------------+
| G711E::configAudio         | Configure G711E module by setting up    |
|                            | audio configuration parameters.         |
+----------------------------+-----------------------------------------+
| G711E::configCodec         | Configure G711E module companding       |
|                            | algorithm.                              |
+----------------------------+-----------------------------------------+
| G711E::begin               | Start G711E module audio encoder.       |
+----------------------------+-----------------------------------------+
| G711E::end                 | Stop G711E module audio encoder.        |
+----------------------------+-----------------------------------------+

**G711E::configAudio**
----------------------

**Description**
~~~~~~~~~~~~~~~

Configure G711E module by setting up audio configuration parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configAudio(AudioSetting& config);

**Parameters**
~~~~~~~~~~~~~~

config: AudioSetting object containing desired audio configuration.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Audio/RTPAudioStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTPAudioStream/RTPAudioStream.ino>`_

.. note :: “AudioEncoder.h” must be included to use the class function. The G711E audio encoder will only work when the audio sample rate is configured as 8kHz or 16kHz.

**G711E::configCodec**
----------------------

**Description**
~~~~~~~~~~~~~~~

Configure G711E module companding algorithm.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configCodec(Audio_Codec_T codec);

**Parameters**
~~~~~~~~~~~~~~

codec: Codec format of audio stream.

- CODEC_G711_PCMU (Default value)

- CODEC_G711_PCMA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Audio/RTPAudioStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTPAudioStream/RTPAudioStream.ino>`_

.. note :: “AudioEncoder.h” must be included to use the class function. The G711E audio encoder will only work when the audio sample rate is configured as 8kHz or 16kHz.

**G711E::begin**
----------------

**Description**
~~~~~~~~~~~~~~~

Start G711E audio encoder.

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

Example: `Audio/RTPAudioStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTPAudioStream/RTPAudioStream.ino>`_

.. note :: “AudioEncoder.h” must be included to use the class function.

**G711E::end**
--------------

**Description**
~~~~~~~~~~~~~~~

Stop G711E audio encoder.

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

.. note :: “AudioEncoder.h” must be included to use the class function.
