AudioSetting Class

Description

A class used to contain audio configuration parameters for the audio
codec.

Syntax

class AudioSetting

Members

Audio Class

Description

A class used to configure and initialize the on-board Audio Codec to
generate an audio data stream.

Syntax

class Audio

Members

Public Constructors

Public Methods

Audio::configAudio

Description

Initialize audio stream settings for the audio codec.

Syntax

void configAudio(AudioSetting& config);

Parameters

config: AudioSetting object containing desired audio configuration.

Returns

NA

Example Code

LoopbackTest

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/LoopbackTest/LoopbackTest.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::configMicAEC

Description

Configure Acoustic Echo Cancellation algorithm for microphone audio
input.

Syntax

void configMicAEC(uint8_t enable, uint8_t level);

Parameters

enable: Enable or disable Acoustic Echo Cancellation algorithm.

level: Strength of echo cancellation effect, default value of 5. Valid
values range from 0 to 17.

Returns

NA

Example Code

EchoCancellation

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/EchoCancellation/EchoCancellation.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz. The Acoustic Echo Cancellation algorithm is intended to
prevent the microphone audio input from picking up sounds produced by
the speaker audio output.

Audio::configMicAGC

Description

Configure Automatic Gain Control algorithm for microphone audio input.

Syntax

void configMicAGC(uint8_t enable, uint8_t dBFS);

Parameters

enable: Enable or disable Automatic Gain Control algorithm.

level: Target reference level of gain control algorithm, default value
of 6. Valid values range from 0 to 30, corresponding to 0 dBFS to -30
dBFS.

Returns

NA

Example Code

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::configMicNS

Description

Configure Noise Suppression algorithm for microphone audio input.

Syntax

void configMicNS(uint8_t enable, uint8_t level);

Parameters

enable: Enable or disable Noise Suppression algorithm.

level: Strength of Noise Suppression effect, default value of 12. Valid
values range from 0 to 12.

Returns

NA

Example Code

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::configSpkAGC

Description

Configure Acoustic Echo Cancellation algorithm for speaker audio output.

Syntax

void configMicAGC(uint8_t enable, uint8_t dBFS);

Parameters

enable: Enable or disable Automatic Gain Control algorithm.

level: Target reference level of gain control algorithm, default value
of 6. Valid values range from 0 to 30, corresponding to 0 dBFS to -30
dBFS.

Returns

NA

Example Code

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::configSpkNS

Description

Configure Noise Suppression algorithm for speaker audio output.

Syntax

void configMicNS(uint8_t enable, uint8_t level);

Parameters

enable: Enable or disable Noise Suppression algorithm.

level: Strength of Noise Suppression effect, default value of 12. Valid
values range from 0 to 12.

Returns

NA

Example Code

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function. The
algorithm will only work when the audio sample rate is configured as
8kHz or 16kHz.

Audio::begin

Description

Start audio data streaming.

Syntax

void begin(void);

Parameters

NA

Returns

NA

Example Code

LoopbackTest

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/LoopbackTest/LoopbackTest.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::end

Description

Stop audio data streaming.

Syntax

void end(void);

Parameters

NA

Returns

NA

Example Code

NA

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::setAMicBoost

Description

Adjust input sensitivity boost for analog mic.

Syntax

void setAMicBoost(uint8_t amicBoost);

Parameters

amicBoost: Sensitivity boost for analog mic input. Default value of 0.
Valid values range from 0 to 3, corresponding to sensitivity boosts of
0dB, 20dB, 30dB, 40dB.

Returns

NA

Example Code

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::setDMicBoost

Description

Adjust input sensitivity boost for digital mic.

Syntax

void setDMicBoost(uint8_t dmicBoost);

Parameters

dmicBoost: Sensitivity boost for analog mic input. Default value of 0.
Valid values range from 0 to 3, corresponding to sensitivity boosts of
0dB, 12dB, 24dB, 36dB.

Returns

NA

Example Code

AudioEffect

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioEffect/AudioEffect.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::setMicGain

Description

Adjust microphone input volume.

Syntax

void setMicGain(uint8_t gain);

Parameters

gain: Volume level of microphone input. Valid values range from 0 to
100.

Returns

NA

Example Code

AudioVolumeAdjust

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioVolumeAdjust/AudioVolumeAdjust.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::setSpkGain

Description

Adjust speaker output volume.

Syntax

void setSpkGain(uint8_t gain);

Parameters

gain: Volume level of speaker output. Valid values range from 0 to 100.

Returns

NA

Example Code

AudioVolumeAdjust

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/AudioVolumeAdjust/AudioVolumeAdjust.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::muteMic

Description

Mute microphone input.

Syntax

void muteMic(uint8_t mute);

Parameters

mute: Mute or unmute microphone input.

Returns

NA

Example Code

NA

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::muteSpk

Description

Mute speaker output.

Syntax

void muteSpk(uint8_t mute);

Parameters

mute: Mute or unmute speaker output.

Returns

NA

Example Code

NA

Notes and Warnings

“AudioStream.h” must be included to use the class function.

Audio::printInfo

Description

Print out current configuration of audio channel.

Syntax

void printInfo(void);

Parameters

NA

Returns

NA

Example Code

SingleVideoWithAudio
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/StreamRTSP/SingleVideoWithAudio/SingleVideoWithAudio.ino)

Notes and Warnings

“AudioStream.h” must be included to use the class function.
