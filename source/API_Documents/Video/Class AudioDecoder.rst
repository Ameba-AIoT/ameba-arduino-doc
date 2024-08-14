AAD Class

Description

A class used to decode an audio data stream using AAC (Advanced Audio
Codec) standard.

Syntax

class AAD

Members

Public Constructors

Public Methods

AAD::configAudio

Description

Configure AAD module by setting up audio configuration parameters.

Syntax

void configAudio(AudioSetting& config);

Parameters

config: AudioSetting object containing desired audio configuration.

Returns

NA

Example Code

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

Notes and Warnings

“AudioDecoder.h” must be included to use the class function.

AAD::begin

Description

Start AAD audio decoder.

Syntax

void begin(void);

Parameters

NA

Returns

NA

Example Code

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

Notes and Warnings

“AudioDecoder.h” must be included to use the class function.

AAD::end

Description

Stop AAD audio decoder.

Syntax

void end(void);

Parameters

NA

Returns

NA

Example Code

NA

Notes and Warnings

“AudioDecoder.h” must be included to use the class function.

G711D Class

Description

A class used to decode an audio data stream using ITU-T G.711 standard.

Syntax

class G711D

Members

Public Constructors

Public Methods

G711D::configAudio

Description

Configure G711D module by setting up audio configuration parameters.

Syntax

void configAudio(AudioSetting& config);

Parameters

config: AudioSetting object containing desired audio configuration.

Returns

NA

Example Code

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

Notes and Warnings

“AudioDecoder.h” must be included to use the class function. The G711D
audio decoder will only work when the audio sample rate is configured as
8kHz or 16kHz.

G711D::configCodec

Description

Configure G711D module companding algorithm.

Syntax

void configCodec(Audio_Codec_T codec);

Parameters

codec: Codec format of audio stream. Valid values: CODEC_G711_PCMU,
CODEC_G711_PCMA. Default value of CODEC_G711_PCMU.

Returns

NA

Example Code

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

Notes and Warnings

“AudioDecoder.h” must be included to use the class function. The G711D
audio decoder will only work when the audio sample rate is configured as
8kHz or 16kHz.

G711D::begin

Description

Start G711D audio decoder.

Syntax

void begin(void);

Parameters

NA

Returns

NA

Example Code

RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

Notes and Warnings

“AudioDecoder.h” must be included to use the class function.

G711D::end

Description

Stop G711D audio decoder.

Syntax

void end(void);

Parameters

NA

Returns

NA

Example Code

NA

Notes and Warnings

“AudioDecoder.h” must be included to use the class function.
