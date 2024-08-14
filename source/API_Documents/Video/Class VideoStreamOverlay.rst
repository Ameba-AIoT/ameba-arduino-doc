VideoStreamOverlay Class

Description

VideoStreamOverlay also known as On-Screen Display (OSD) that allows
contents such as texts and shapes to be displayed on video streams.
VideoStreamOverlay class is used to draw on video streams.

Syntax

Class VideoStreamOverlay

Members

Public Constructors

Public Methods

VideoStreamOverlay::configVideo

Description

Configure input video stream parameters.

Syntax

void configVideo(int ch, VideoSetting& config);

Parameters

ch: Channel to configure (Valid value: 0,1,2)

config: VideoSetting object

Returns

NA

Example Code

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings

Note that OSD only supports channel 0, 1 and 2. “VideoStreamOverlay.h”
must be included to use the class function.

VideoStreamOverlay::configTextSize

Description

Configure text width and height shown on OSD.

Syntax

void configTextSize(int ch, int text_width, int text_height);

Parameters

ch: Channel to configure (Valid value: 0,1,2)

text_width: Text width in pixels. Default text width is 16.

text_height: Text height in pixels. Default height width is 32.

Returns

NA

Example Code

NA

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function. Text
size should be configured before OSD is started using begin().

VideoStreamOverlay::createBitmap

Description

Create bitmap on video streams.

Syntax

void createBitmap (int ch, int idx = 0);

Parameters

ch: Channel to configure (Valid value: 0,1,2)

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

Returns

NA

Example Code

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::begin

Description

Enable OSD and start drawing on top of video streams.

Syntax

void begin(void);

Parameters

NA

Returns

NA

Example Code

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::end

Description

Stop OSD drawing on all video streams.

Syntax

void end(void);

Parameters

NA

Returns

NA

Example Code

NA

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::endChannel

Description

Stop OSD drawing on specified video stream.

Syntax

void endChannel(int ch);

Parameters

ch: Channel to stop. (Valid value: 0,1,2)

Returns

NA

Example Code

NA

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::getTextHeight

Description

Get current configuration of OSD text height.

Syntax

int getTextHeight(int ch);

Parameters

ch: Channel to get the OSD text’s height. (Valid value: 0,1,2)

Returns

This function returns the OSD text’s height on selected channel.

Example Code

RTSPFaceDetection
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino)

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::getTextWidth

Description

Get current configuration of OSD text width.

Syntax

int getTextWidth(int ch);

Parameters

ch: Channel to get the OSD text’s width. (Valid value: 0,1,2)

Returns

This function returns the OSD text’s width on the selected channel.

Example Code

NA

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::color

Description

Convert ARGB color values into a format compatible for OSD use.

Syntax

uint32_t color(uint8_t red, uint8_t green, uint8_t blue, uint8_t alpha =
0xff);

Parameters

red: Intensity level of red color expressed as an 8-bit unsigned integer
from 0 to 255.

green: Intensity level of green color expressed as an 8-bit unsigned
integer from 0 to 255.

blue: Intensity level of blue color expressed as an 8-bit unsigned
integer from 0 to 255.

alpha: Transparency of color expressed as an 8-bit unsigned integer from
0 to 255. Default value of 255. This value is optional.

Returns

This function returns the ARGB value in a format compatible for OSD use.

Example Code

NA

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::drawLine

Description

Draw a line in OSD frame buffer.

Syntax

void drawLine(int ch, int xmin, int ymin, int xmax, int ymax, int
line_width, uint32_t color, int idx = 0);

Parameters

ch: Channel to draw on. (Valid value: 0,1,2)

xmin: x coordinate of the top left corner.

ymin: y coordinate of the top left corner.

xmax: x coordinate of the bottom right corner.

ymax: y coordinate of bottom right corner.

line_width: Width of a line.

color: Color of the line.

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

Returns

NA

Example Code

NA

Notes and Warnings

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::drawPoint

Description

Draw a point in OSD frame buffer.

Syntax

void VideoStreamOverlay::drawPoint(int ch, int xmin, int ymin, int
point_width, uint32_t color, int idx = 0);

Parameters

ch: Channel to draw on. (Valid value: 0,1,2)

xmin: x coordinate of the point

ymin: y coordinate of the point

point_width: size of the point.

color: Color of the point.

idx: Block index of OSD

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

Returns

NA

Example Code

RTSPFaceDetection
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino)

Notes and Warnings

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::drawRect

Description

Draw a rectangle on OSD frame buffer.

Syntax

void drawRect(int ch, int xmin, int ymin, int xmax, int ymax, int
line_width, uint32_t color, int idx = 0);

Parameters

ch: Channel to draw rectangle on. (Valid value: 0,1,2)

xmin: x coordinate of the top left corner.

ymin: y coordinate of the top left corner.

xmax: x coordinate of the bottom right corner.

ymax: y coordinate of bottom right corner.

line_width: Width of a rectangle's border.

color: Color of the rectangle.

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

Returns

NA

Example Code

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::drawText

Description

Draw text on OSD frame buffer.

Syntax

void drawText(int ch, int xmin, int ymin, const char \*text_string,
uint32_t color, int idx = 0);

Parameters

ch: Channel to draw text on. (Valid value: 0,1,2)

xmin: x coordinate of top left corner of text box.

ymin: y coordinate of top left corner of text box.

text_string: pointer to a character array containing the text to be
displayed.

color: Color of the text.

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

Returns

NA

Example Code

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::update

Description

Update OSD and display drawings on video streams.

Syntax

void update(int ch, int idx = 0);

Parameters

ch: Channel to display drawings. (Valid value: 0,1,2)

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

Returns

NA

Example Code

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings

“VideoStreamOverlay.h” must be included to use the class function.
