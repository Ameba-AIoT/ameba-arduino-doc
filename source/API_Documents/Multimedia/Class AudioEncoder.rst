AAC Class

Description

A class used to encode an audio data stream using AAC (Advanced Audio
Codec) standard.

Syntax

class AAC

Members

Public Constructors

Public Methods

AAC::configAudio

Description

Configure AAC module by setting up audio configuration parameters.

Syntax

void configAudio(AudioSetting& config);

Parameters

config: AudioSetting object containing desired audio configuration.

Returns

NA

Example Code

RTSPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino)

Notes and Warnings

“AudioEncoder.h” must be included to use the class function.

AAC::begin

Description

Start AAC audio encoder.

Syntax

void begin(void);

Parameters

NA

Returns

NA

Example Code

RTSPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino)

Notes and Warnings

“AudioEncoder.h” must be included to use the class function.

AAC::end

Description

Stop AAC audio encoder.

Syntax

void end(void);

Parameters

NA

Returns

NA

Example Code

NA

Notes and Warnings

“AudioEncoder.h” must be included to use the class function.

G711E Class

Description

A class used to encode an audio data stream using ITU-T G.711 standard.

Syntax

class G711E

Members

Public Constructors

Public Methods

G711E::configAudio

Description

Configure G711E module by setting up audio configuration parameters.

Syntax

void configAudio(AudioSetting& config);

Parameters

config: AudioSetting object containing desired audio configuration.

Returns

NA

Example Code

RTSPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino)

Notes and Warnings

“AudioEncoder.h” must be included to use the class function. The G711E
audio encoder will only work when the audio sample rate is configured as
8kHz or 16kHz.

G711E::configCodec

Description

Configure G711E module companding algorithm.

Syntax

void configCodec(Audio_Codec_T codec);

Parameters

codec: Codec format of audio stream. Valid values: CODEC_G711_PCMU,
CODEC_G711_PCMA. Default value of CODEC_G711_PCMU.

Returns

NA

Example Code

RTSPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino)

Notes and Warnings

“AudioEncoder.h” must be included to use the class function. The G711E
audio encoder will only work when the audio sample rate is configured as
8kHz or 16kHz.

G711E::begin

Description

Start G711E audio encoder.

Syntax

void begin(void);

Parameters

NA

Returns

NA

Example Code

RTSPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTSPAudioStream/RTSPAudioStream.ino)

Notes and Warnings

“AudioEncoder.h” must be included to use the class function.

G711E::end

Description

Stop G711E audio encoder.

Syntax

void end(void);

Parameters

NA

Returns

NA

Example Code

NA

Notes and Warnings

“AudioEncoder.h” must be included to use the class function.
