AudioSetting Class
==================

Description
-----------

A class used to contain audio configuration parameters for the audio
codec.

Syntax
------

class AudioSetting

Members
-------

+----------------------------+-----------------------------------------+
| .. rubric:: Public         |                                         |
|    Constructors            |                                         |
|                            |                                         |
| :name: public-constructors |                                         |
+============================+=========================================+
| AudioSetting::AudioSetting | Constructs an AudioSetting object.      |
+----------------------------+-----------------------------------------+

Audio Class
===========

.. _description-1:

Description
-----------

A class used to configure and initialize the on-board Audio Codec to
generate an audio data stream.

.. _syntax-1:

Syntax
------

class Audio

.. _members-1:

Members
-------

**Public Constructors**

+----------------------------+-----------------------------------------+
| Audio::Audio               | Constructs an Audio object.             |
+============================+=========================================+
+----------------------------+-----------------------------------------+

Public Methods
~~~~~~~~~~~~~~

+----------------------------+-----------------------------------------+
| Audio::configAudio         | Configure audio module by setting up    |
|                            | audio parameters.                       |
+============================+=========================================+
| Audio::configMicAEC        | Configure Acoustic Echo Cancellation    |
|                            | algorithm for microphone audio input.   |
+----------------------------+-----------------------------------------+
| Audio::configMicAGC        | Configure Automatic Gain Control        |
|                            | algorithm for microphone audio input.   |
+----------------------------+-----------------------------------------+
| Audio::configMicNS         | Configure Noise Suppression algorithm   |
|                            | for microphone audio input.             |
+----------------------------+-----------------------------------------+
| Audio::configSpkAGC        | Configure Automatic Gain Control        |
|                            | algorithm for speaker audio output.     |
+----------------------------+-----------------------------------------+
| Audio::configSpkNS         | Configure Noise Suppression algorithm   |
|                            | for speaker audio output.               |
+----------------------------+-----------------------------------------+
| Audio::begin               | Start audio data streaming.             |
+----------------------------+-----------------------------------------+
| Audio::end                 | Stop audio data streaming.              |
+----------------------------+-----------------------------------------+
| Audio::setAMicBoost        | Adjust input sensitivity boost for      |
|                            | analog mic.                             |
+----------------------------+-----------------------------------------+
| Audio::setDMicBoost        | Adjust input sensitivity boost for      |
|                            | digital mic.                            |
+----------------------------+-----------------------------------------+
| Audio::setMicGain          | Adjust microphone input volume.         |
+----------------------------+-----------------------------------------+
| Audio::setSpkGain          | Adjust speaker output volume.           |
+----------------------------+-----------------------------------------+
| Audio::muteMic             | Mute microphone input.                  |
+----------------------------+-----------------------------------------+
| Audio::muteSpk             | Mute speaker output.                    |
+----------------------------+-----------------------------------------+
| Audio::printInfo           | Print out current configuration of      |
|                            | audio channels.                         |
+----------------------------+-----------------------------------------+

Audio::configAudio
==================

.. _description-2:

Description
-----------

Initialize audio stream settings for the audio codec.

.. _syntax-2:

Syntax
------

void configAudio(AudioSetting& config);

Parameters
----------

config: AudioSetting object containing desired audio configuration.

Returns
-------

NA

Example Code
------------

LoopbackTest

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/LoopbackTest/LoopbackTest.ino)

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::configMicAEC
===================

.. _description-3:

Description
-----------

Configure Acoustic Echo Cancellation algorithm for microphone audio
input.

.. _section-1:

.. _syntax-3:

Syntax
------

void configMicAEC(uint8_t enable, uint8_t level);

.. _parameters-1:

Parameters
----------

enable: Enable or disable Acoustic Echo Cancellation algorithm.

level: Strength of echo cancellation effect, default value of 5. Valid
values range from 0 to 17.

.. _returns-1:

Returns
-------

NA

.. _example-code-1:

Example Code
------------

EchoCancellation

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/EchoCancellation/EchoCancellation.ino)

.. _notes-and-warnings-1:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz. The Acoustic Echo Cancellation algorithm is intended to
prevent the microphone audio input from picking up sounds produced by
the speaker audio output.

Audio::configMicAGC
===================

.. _description-4:

Description
-----------

Configure Automatic Gain Control algorithm for microphone audio input.

.. _section-2:

.. _syntax-4:

Syntax
------

void configMicAGC(uint8_t enable, uint8_t dBFS);

.. _parameters-2:

Parameters
----------

enable: Enable or disable Automatic Gain Control algorithm.

level: Target reference level of gain control algorithm, default value
of 6. Valid values range from 0 to 30, corresponding to 0 dBFS to -30
dBFS.

.. _returns-2:

Returns
-------

NA

.. _example-code-2:

Example Code
------------

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

.. _notes-and-warnings-2:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::configMicNS
==================

.. _description-5:

Description
-----------

Configure Noise Suppression algorithm for microphone audio input.

.. _section-3:

.. _syntax-5:

Syntax
------

void configMicNS(uint8_t enable, uint8_t level);

.. _parameters-3:

Parameters
----------

enable: Enable or disable Noise Suppression algorithm.

level: Strength of Noise Suppression effect, default value of 12. Valid
values range from 0 to 12.

.. _returns-3:

Returns
-------

NA

.. _example-code-3:

Example Code
------------

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

.. _notes-and-warnings-3:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::configSpkAGC
===================

.. _description-6:

Description
-----------

Configure Acoustic Echo Cancellation algorithm for speaker audio output.

.. _section-4:

.. _syntax-6:

Syntax
------

void configMicAGC(uint8_t enable, uint8_t dBFS);

.. _parameters-4:

Parameters
----------

enable: Enable or disable Automatic Gain Control algorithm.

level: Target reference level of gain control algorithm, default value
of 6. Valid values range from 0 to 30, corresponding to 0 dBFS to -30
dBFS.

.. _returns-4:

Returns
-------

NA

.. _example-code-4:

Example Code
------------

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

.. _notes-and-warnings-4:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::configSpkNS
==================

.. _description-7:

Description
-----------

Configure Noise Suppression algorithm for speaker audio output.

.. _section-5:

.. _syntax-7:

Syntax
------

void configMicNS(uint8_t enable, uint8_t level);

.. _parameters-5:

Parameters
----------

enable: Enable or disable Noise Suppression algorithm.

level: Strength of Noise Suppression effect, default value of 12. Valid
values range from 0 to 12.

.. _returns-5:

Returns
-------

NA

.. _example-code-5:

Example Code
------------

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

.. _notes-and-warnings-5:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::begin
============

.. _description-8:

Description
-----------

Start audio data streaming.

.. _syntax-8:

Syntax
------

void begin(void);

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

LoopbackTest

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/LoopbackTest/LoopbackTest.ino)

.. _notes-and-warnings-6:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::end
==========

.. _description-9:

Description
-----------

Stop audio data streaming.

.. _section-6:

.. _syntax-9:

Syntax
------

void end(void);

.. _parameters-7:

Parameters
----------

NA

.. _returns-7:

Returns
-------

NA

.. _example-code-7:

Example Code
------------

NA

.. _notes-and-warnings-7:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::setAMicBoost
===================

.. _description-10:

Description
-----------

Adjust input sensitivity boost for analog mic.

.. _section-7:

.. _syntax-10:

Syntax
------

void setAMicBoost(uint8_t amicBoost);

.. _parameters-8:

Parameters
----------

amicBoost: Sensitivity boost for analog mic input. Default value of 0.
Valid values range from 0 to 3, corresponding to sensitivity boosts of
0dB, 20dB, 30dB, 40dB.

.. _returns-8:

Returns
-------

NA

.. _example-code-8:

Example Code
------------

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

.. _notes-and-warnings-8:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::setDMicBoost
===================

.. _description-11:

Description
-----------

Adjust input sensitivity boost for digital mic.

.. _section-8:

.. _syntax-11:

Syntax
------

void setDMicBoost(uint8_t dmicBoost);

.. _parameters-9:

Parameters
----------

dmicBoost: Sensitivity boost for analog mic input. Default value of 0.
Valid values range from 0 to 3, corresponding to sensitivity boosts of
0dB, 12dB, 24dB, 36dB.

.. _returns-9:

Returns
-------

NA

.. _example-code-9:

Example Code
------------

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

.. _notes-and-warnings-9:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::setMicGain
=================

.. _description-12:

Description
-----------

Adjust microphone input volume.

.. _section-9:

.. _syntax-12:

Syntax
------

void setMicGain(uint8_t gain);

.. _parameters-10:

Parameters
----------

gain: Volume level of microphone input. Valid values range from 0 to
100.

.. _returns-10:

Returns
-------

NA

.. _example-code-10:

Example Code
------------

AudioVolumeAdjust

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioVolumeAdjust/AudioVolumeAdjust.ino)

.. _notes-and-warnings-10:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::setSpkGain
=================

.. _description-13:

Description
-----------

Adjust speaker output volume.

.. _section-10:

.. _syntax-13:

Syntax
------

void setSpkGain(uint8_t gain);

.. _parameters-11:

Parameters
----------

gain: Volume level of speaker output. Valid values range from 0 to 100.

.. _returns-11:

Returns
-------

NA

.. _example-code-11:

Example Code
------------

AudioVolumeAdjust

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioVolumeAdjust/AudioVolumeAdjust.ino)

.. _notes-and-warnings-11:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::muteMic
==============

.. _description-14:

Description
-----------

Mute microphone input.

.. _section-11:

.. _syntax-14:

Syntax
------

void muteMic(uint8_t mute);

.. _parameters-12:

Parameters
----------

mute: Mute or unmute microphone input.

.. _returns-12:

Returns
-------

NA

.. _example-code-12:

Example Code
------------

NA

.. _notes-and-warnings-12:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::muteSpk
==============

.. _description-15:

Description
-----------

Mute speaker output.

.. _section-12:

.. _syntax-15:

Syntax
------

void muteSpk(uint8_t mute);

.. _parameters-13:

Parameters
----------

mute: Mute or unmute speaker output.

.. _returns-13:

Returns
-------

NA

.. _example-code-13:

Example Code
------------

NA

.. _notes-and-warnings-13:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.

Audio::printInfo
================

.. _description-16:

Description
-----------

Print out current configuration of audio channel.

.. _syntax-16:

Syntax
------

void printInfo(void);

.. _parameters-14:

Parameters
----------

NA

.. _returns-14:

Returns
-------

NA

.. _example-code-14:

Example Code
------------

SingleVideoWithAudio
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/StreamRTSP/SingleVideoWithAudio/SingleVideoWithAudio.ino)

.. _notes-and-warnings-14:

Notes and Warnings
------------------

“AudioStream.h” must be included to use the class function.
