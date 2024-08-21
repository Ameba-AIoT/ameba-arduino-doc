Class AudioDecoder
==================

.. contents::
  :local:
  :depth: 2

**AAD Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used to decode an audio data stream using AAC (Advanced Audio Codec) standard.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class AAD

**Members**
~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| **Public Constructors**                                              |
+============================+=========================================+
| AAD::AAD                   | Constructs an AAD object.               |
+----------------------------+-----------------------------------------+
| **Public Methods**                                                   |
+----------------------------+-----------------------------------------+
| AAD::configAudio           | Configure AAD module by setting up      |
|                            | audio configuration parameters.         |
+----------------------------+-----------------------------------------+
| AAD::begin                 | Start AAD module audio decoder.         |
+----------------------------+-----------------------------------------+
| AAD::end                   | Stop AAD module audio decoder.          |
+----------------------------+-----------------------------------------+

**AAD::configAudio**
--------------------

**Description**
~~~~~~~~~~~~~~~

Configure AAD module by setting up audio configuration parameters.

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

.. note :: “AudioDecoder.h” must be included to use the class function.

**AAD::begin**
--------------

**Description**
~~~~~~~~~~~~~~~

Start AAD audio decoder.

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

.. note :: “AudioDecoder.h” must be included to use the class function.

**AAD::end**
------------

**Description**
~~~~~~~~~~~~~~~

Stop AAD audio decoder.

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

.. note :: “AudioDecoder.h” must be included to use the class function.


**G711D Class**
---------------

**Description**
~~~~~~~~~~~~~~~

A class used to decode an audio data stream using ITU-T G.711 standard.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class G711D

**Members**
~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| **Public Constructors**                                              |
+============================+=========================================+
| G711D::G711D               | Constructs a G711D object.              |
+----------------------------+-----------------------------------------+
| **Public Methods**                                                   |
+----------------------------+-----------------------------------------+
| G711D::configAudio         | Configure G711D module by setting up    |
|                            | audio configuration parameters.         |
+----------------------------+-----------------------------------------+
| G711D::configCodec         | Configure G711D module companding       |
|                            | algorithm.                              |
+----------------------------+-----------------------------------------+
| G711D::begin               | Start G711D module audio decoder.       |
+----------------------------+-----------------------------------------+
| G711D::end                 | Stop G711D module audio decoder.        |
+----------------------------+-----------------------------------------+

**G711D::configAudio**
----------------------

**Description**
~~~~~~~~~~~~~~~

Configure G711D module by setting up audio configuration parameters.

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

.. note :: “AudioDecoder.h” must be included to use the class function. The G711D audio decoder will only work when the audio sample rate is configured as 8kHz or 16kHz.

**G711D::configCodec**
----------------------

**Description**
~~~~~~~~~~~~~~~

Configure G711D module companding algorithm.

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

.. note :: “AudioDecoder.h” must be included to use the class function. The G711D audio decoder will only work when the audio sample rate is configured as 8kHz or 16kHz.

**G711D::begin**
----------------

**Description**
~~~~~~~~~~~~~~~

Start G711D audio decoder.

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

.. note :: “AudioDecoder.h” must be included to use the class function.

**G711D::end**
--------------

**Description**
~~~~~~~~~~~~~~~

Stop G711D audio decoder.

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

.. note :: “AudioDecoder.h” must be included to use the class function.
