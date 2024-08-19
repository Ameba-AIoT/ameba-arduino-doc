VideoStreamOverlay Class 
=========================

Description
-----------

VideoStreamOverlay also known as On-Screen Display (OSD) that allows
contents such as texts and shapes to be displayed on video streams.
VideoStreamOverlay class is used to draw on video streams.

Syntax
------

Class VideoStreamOverlay

Members
-------

**Public Constructors**

+------------------------------------+---------------------------------+
| VideoStreamOverlay::               | Constructs a VideoStreamOverlay |
| VideoStreamOverlay                 | object.                         |
+====================================+=================================+
+------------------------------------+---------------------------------+

**Public Methods**

+-------------------------------------+--------------------------------+
| VideoStreamOverlay::configVideo     | Configure input video stream   |
|                                     | parameters.                    |
+=====================================+================================+
| VideoStreamOverlay:: configTextSize | Configure text width and       |
|                                     | height shown on OSD\ **.**     |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay:: createBitmap   | Create bitmap on video         |
|                                     | streams.                       |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::begin           | Enable OSD and start drawing   |
|                                     | on top of video streams.       |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::end             | Stop OSD drawing on all video  |
|                                     | streams.                       |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::endChannel      | Stop OSD drawing on specified  |
|                                     | video stream.                  |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::getTextHeight   | Get current configuration of   |
|                                     | OSD text height.               |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::getTextWidth    | Get current configuration of   |
|                                     | OSD text width.                |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::color           | Convert ARGB color values into |
|                                     | a format compatible for OSD    |
|                                     | use.                           |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::drawLine        | Draw a line in OSD frame       |
|                                     | buffer.                        |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::drawPoint       | Draw a point in OSD frame      |
|                                     | buffer.                        |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::drawRect        | Draw a rectangle on OSD frame  |
|                                     | buffer.                        |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::drawText        | Draw text on OSD frame buffer. |
+-------------------------------------+--------------------------------+
| VideoStreamOverlay::update          | Update OSD and display         |
|                                     | drawings on video streams.     |
+-------------------------------------+--------------------------------+
|                                     |                                |
+-------------------------------------+--------------------------------+

VideoStreamOverlay::configVideo
===============================

.. _description-1:

Description
-----------

Configure input video stream parameters.

.. _syntax-1:

Syntax
------

void configVideo(int ch, VideoSetting& config);

Paramet\ **er**\ s
~~~~~~~~~~~~~~~~~~

ch: Channel to configure (Valid value: 0,1,2)

config: VideoSetting object

Return\ **s**
~~~~~~~~~~~~~

NA

Example **Cod**\ e
~~~~~~~~~~~~~~~~~~

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

Notes and Warnings
~~~~~~~~~~~~~~~~~~

Note that OSD only supports channel 0, 1 and 2. “VideoStreamOverlay.h”
must be included to use the class function.

VideoStreamOverlay::configTextSize
==================================

.. _description-2:

Description
-----------

Configure text width and height shown on OSD\ **.**

.. _syntax-2:

Syntax
------

void configTextSize(int ch, int text_width, int text_height);

.. _parameters-1:

Parameters
----------

ch: Channel to configure (Valid value: 0,1,2)

text_width: Text width in pixels. Default text width is 16.

text_height: Text height in pixels. Default height width is 32.

.. _returns-1:

Returns
-------

NA

.. _example-code-1:

Example Code
------------

NA

.. _notes-and-warnings-1:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function. Text
size should be configured before OSD is started using begin().

VideoStreamOverlay::createBitmap
================================

.. _description-3:

Description
-----------

Create bitmap on video streams.

.. _syntax-3:

Syntax
------

void createBitmap (int ch, int idx = 0);

.. _parameters-2:

Parameters
----------

ch: Channel to configure (Valid value: 0,1,2)

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

.. _returns-2:

Returns
-------

NA

.. _example-code-2:

Example Code
------------

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-2:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::begin
=========================

.. _description-4:

Description
-----------

Enable OSD and start drawing on top of video streams.

.. _syntax-4:

Syntax
------

void begin(void);

.. _parameters-3:

Parameters
----------

NA

.. _returns-3:

Returns
-------

NA

.. _example-code-3:

Example Code
------------

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-3:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::end
=======================

.. _description-5:

Description
-----------

Stop OSD drawing on all video streams.

.. _syntax-5:

Syntax
------

void end(void);

.. _parameters-4:

Parameters
----------

NA

.. _returns-4:

Returns
-------

NA

.. _example-code-4:

Example Code
------------

NA

.. _notes-and-warnings-4:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::endChannel
==============================

.. _description-6:

Description
-----------

Stop OSD drawing on specified video stream.

.. _syntax-6:

Syntax
------

void endChannel(int ch);

.. _parameters-5:

Parameters
----------

ch: Channel to stop. (Valid value: 0,1,2)

.. _returns-5:

Returns
-------

NA

.. _example-code-5:

Example Code
------------

NA

.. _notes-and-warnings-5:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::getTextHeight
=================================

.. _description-7:

Description
-----------

Get current configuration of OSD text height.

.. _syntax-7:

Syntax
------

int getTextHeight(int ch);

.. _parameters-6:

Parameters
----------

ch: Channel to get the OSD text’s height. (Valid value: 0,1,2)

.. _returns-6:

Returns
-------

This function returns the OSD text’s height on selected channel.

.. _example-code-6:

Example Code
------------

RTSPFaceDetection
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino)

.. _notes-and-warnings-6:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::getTextWidth
================================

.. _description-8:

Description
-----------

Get current configuration of OSD text width.

.. _syntax-8:

Syntax
------

int getTextWidth(int ch);

.. _parameters-7:

Parameters
----------

ch: Channel to get the OSD text’s width. (Valid value: 0,1,2)

.. _returns-7:

Returns
-------

This function returns the OSD text’s width on the selected channel.

.. _example-code-7:

Example Code
------------

NA

.. _notes-and-warnings-7:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::color
=========================

.. _description-9:

Description
-----------

Convert ARGB color values into a format compatible for OSD use.

.. _syntax-9:

Syntax
------

uint32_t color(uint8_t red, uint8_t green, uint8_t blue, uint8_t alpha =
0xff);

.. _parameters-8:

Parameters
----------

red: Intensity level of red color expressed as an 8-bit unsigned integer
from 0 to 255.

green: Intensity level of green color expressed as an 8-bit unsigned
integer from 0 to 255.

blue: Intensity level of blue color expressed as an 8-bit unsigned
integer from 0 to 255.

alpha: Transparency of color expressed as an 8-bit unsigned integer from
0 to 255. Default value of 255. This value is optional.

.. _returns-8:

Returns
~~~~~~~

This function returns the ARGB value in a format compatible for OSD use.

.. _example-code-8:

Example Code
------------

NA

.. _notes-and-warnings-8:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.

VideoStreamOverlay::drawLine
============================

.. _description-10:

Description
-----------

Draw a line in OSD frame buffer.

.. _syntax-10:

Syntax
------

void drawLine(int ch, int xmin, int ymin, int xmax, int ymax, int
line_width, uint32_t color, int idx = 0);

.. _parameters-9:

Parameters
----------

ch: Channel to draw on. (Valid value: 0,1,2)

xmin: x coordinate of the top left corner.

ymin: y coordinate of the top left corner.

xmax: x coordinate of the bottom right corner.

ymax: y coordinate of bottom right corner.

line_width: Width of a line.

color: Color of the line.

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

.. _returns-9:

Returns
-------

NA

.. _example-code-9:

Example Code
------------

NA

.. _notes-and-warnings-9:

Notes and Warnings
------------------

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::drawPoint
=============================

.. _description-11:

Description
-----------

Draw a point in OSD frame buffer.

.. _syntax-11:

Syntax
------

void VideoStreamOverlay::drawPoint(int ch, int xmin, int ymin, int
point_width, uint32_t color, int idx = 0);

.. _parameters-10:

Parameters
----------

ch: Channel to draw on. (Valid value: 0,1,2)

xmin: x coordinate of the point

ymin: y coordinate of the point

point_width: size of the point.

color: Color of the point.

[STRIKEOUT:idx: Block index of OSD]

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

.. _returns-10:

Returns
-------

NA

.. _example-code-10:

Example Code
------------

RTSPFaceDetection
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino)

.. _notes-and-warnings-10:

Notes and Warnings
------------------

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::drawRect
============================

.. _description-12:

Description
-----------

Draw a rectangle on OSD frame buffer.

.. _syntax-12:

Syntax
------

void drawRect(int ch, int xmin, int ymin, int xmax, int ymax, int
line_width, uint32_t color, int idx = 0);

.. _parameters-11:

Parameters
----------

ch: Channel to draw rectangle on. (Valid value: 0,1,2)

xmin: x coordinate of the top left corner.

ymin: y coordinate of the top left corner.

xmax: x coordinate of the bottom right corner.

ymax: y coordinate of bottom right corner.

line_width: Width of a rectangle's border.

color: Color of the rectangle.

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

.. _returns-11:

Returns
-------

NA

.. _example-code-11:

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-11:

Notes and Warnings
------------------

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.

VideoStreamOverlay::drawText
============================

.. _description-13:

Description
-----------

Draw text on OSD frame buffer.

.. _syntax-13:

Syntax
------

void drawText(int ch, int xmin, int ymin, const char \*text_string,
uint32_t color, int idx = 0);

.. _parameters-12:

Parameters
----------

ch: Channel to draw text on. (Valid value: 0,1,2)

xmin: x coordinate of top left corner of text box.

ymin: y coordinate of top left corner of text box.

text_string: pointer to a character array containing the text to be
displayed.

color: Color of the text.

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

.. _returns-12:

Returns
-------

NA

.. _example-code-12:

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-12:

Notes and Warnings
------------------

VideoStreamOverlay::update() needs to be called for drawings to be shown
on the video streams. “VideoStreamOverlay.h” must be included to use the
class function.\ **

VideoStreamOverlay::update
==========================

.. _description-14:

Description
-----------

Update OSD and display drawings on video streams.

.. _syntax-14:

Syntax
------

void update(int ch, int idx = 0);

.. _parameters-13:

Parameters
----------

ch: Channel to display drawings. (Valid value: 0,1,2)

idx: Layer index of OSD. The default value is 0. (Valid value: 0 to 5)

.. _returns-13:

Returns
-------

NA

.. _example-code-13:

Example Code
------------

Example: LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino)

.. _notes-and-warnings-13:

Notes and Warnings
------------------

“VideoStreamOverlay.h” must be included to use the class function.
