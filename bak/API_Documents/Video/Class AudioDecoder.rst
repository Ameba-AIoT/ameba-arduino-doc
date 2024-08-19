AAD Class
=========

Description
-----------

A class used to decode an audio data stream using AAC (Advanced Audio
Codec) standard.

Syntax
------

class AAD

Members
-------

**Public Constructors**

+----------------------------+-----------------------------------------+
| AAD::AAD                   | Constructs an AAD object.               |
+============================+=========================================+
+----------------------------+-----------------------------------------+

Public Methods
~~~~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| AAD::configAudio           | Configure AAD module by setting up      |
|                            | audio configuration parameters.         |
+============================+=========================================+
| AAD::begin                 | Start AAD module audio decoder.         |
+----------------------------+-----------------------------------------+
| AAD::end                   | Stop AAD module audio decoder.          |
+----------------------------+-----------------------------------------+
|                            |                                         |
+----------------------------+-----------------------------------------+

AAD::configAudio
================

.. _description-1:

Description
-----------

Configure AAD module by setting up audio configuration parameters.
------------------------------------------------------------------

.. _syntax-1:

Syntax
------

void configAudio(AudioSetting& config);
---------------------------------------

Parameters
----------

config: AudioSetting object containing desired audio configuration.

Returns
-------

NA

Example Code
------------

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

.. _section-1:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function.

AAD::begin
==========

.. _description-2:

Description
-----------

Start AAD audio decoder.

.. _syntax-2:

Syntax
------

void begin(void);

.. _parameters-1:

Parameters
----------

NA

.. _returns-1:

Returns
-------

NA

.. _example-code-1:

Example Code
------------

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

.. _notes-and-warnings-1:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function.

AAD::end
========

.. _description-3:

Description
-----------

Stop AAD audio decoder.

.. _syntax-3:

Syntax
------

void end(void);

.. _parameters-2:

Parameters
----------

NA

.. _returns-2:

Returns
-------

NA

.. _example-code-2:

Example Code
------------

NA

.. _notes-and-warnings-2:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function.

G711D Class
===========

.. _description-4:

Description
-----------

A class used to decode an audio data stream using ITU-T G.711 standard.

.. _syntax-4:

Syntax
------

class G711D

.. _members-1:

Members
-------

**Public Constructors**

+----------------------------+-----------------------------------------+
| G711D::G711D               | Constructs a G711D object.              |
+============================+=========================================+
+----------------------------+-----------------------------------------+

.. _public-methods-1:

Public Methods
~~~~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| G711D::configAudio         | Configure G711D module by setting up    |
|                            | audio configuration parameters.         |
+============================+=========================================+
| G711D::configCodec         | Configure G711D module companding       |
|                            | algorithm.                              |
+----------------------------+-----------------------------------------+
| G711D::begin               | Start G711D module audio decoder.       |
+----------------------------+-----------------------------------------+
| G711D::end                 | Stop G711D module audio decoder.        |
+----------------------------+-----------------------------------------+
|                            |                                         |
+----------------------------+-----------------------------------------+

G711D::configAudio
==================

.. _description-5:

Description
-----------

Configure G711D module by setting up audio configuration parameters.
--------------------------------------------------------------------

.. _syntax-5:

Syntax
------

.. _void-configaudioaudiosetting-config-1:

void configAudio(AudioSetting& config);
---------------------------------------

.. _parameters-3:

Parameters
----------

config: AudioSetting object containing desired audio configuration.

.. _returns-3:

Returns
-------

NA

.. _section-2:

.. _example-code-3:

Example Code
------------

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

.. _section-3:

.. _notes-and-warnings-3:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function. The G711D
audio decoder will only work when the audio sample rate is configured as
8kHz or 16kHz.

G711D::configCodec
==================

.. _description-6:

Description
-----------

Configure G711D module companding algorithm.
--------------------------------------------

.. _syntax-6:

Syntax
------

void configCodec(Audio_Codec_T codec);
--------------------------------------

.. _parameters-4:

Parameters
----------

codec: Codec format of audio stream. Valid values: CODEC_G711_PCMU,
CODEC_G711_PCMA. Default value of CODEC_G711_PCMU.

.. _returns-4:

Returns
-------

NA

.. _section-4:

.. _example-code-4:

Example Code
------------

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

.. _section-5:

.. _notes-and-warnings-4:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function. The G711D
audio decoder will only work when the audio sample rate is configured as
8kHz or 16kHz.

G711D::begin
============

.. _description-7:

Description
-----------

Start G711D audio decoder.

.. _syntax-7:

Syntax
------

void begin(void);

.. _parameters-5:

Parameters
----------

NA

.. _returns-5:

Returns
-------

NA

.. _example-code-5:

Example Code
------------

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

.. _notes-and-warnings-5:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function.

G711D::end
==========

.. _description-8:

Description
-----------

Stop G711D audio decoder.

.. _syntax-8:

Syntax
------

void end(void);

.. _parameters-6:

Parameters
----------

NA

.. _returns-6:

Returns
-------

NA

.. _example-code-6:

Example Code
------------

NA

.. _notes-and-warnings-6:

Notes and Warnings
------------------

“AudioDecoder.h” must be included to use the class function.
