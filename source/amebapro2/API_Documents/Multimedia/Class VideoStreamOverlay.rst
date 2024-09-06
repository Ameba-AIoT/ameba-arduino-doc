Class VideoStreamOverlay
========================

.. contents::
  :local:
  :depth: 2

**VideoStreamOverlay Class**
----------------------------

**Description**
~~~~~~~~~~~~~~~

VideoStreamOverlay also known as On-Screen Display (OSD) that allows contents such as texts and shapes to be displayed on video streams. VideoStreamOverlay class is used to draw on video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class VideoStreamOverlay

**Members**
~~~~~~~~~~~

+----------------------------------------+---------------------------------+
| **Public Constructors**                                                  |
+========================================+=================================+
| VideoStreamOverlay::VideoStreamOverlay | Constructs a VideoStreamOverlay |
|                                        | object.                         |
+----------------------------------------+---------------------------------+
| **Public Methods**                                                       |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::configVideo        | Configure input video stream    |
|                                        | parameters.                     |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay:: configTextSize    | Configure text width and height |
|                                        | shown on OSD.                   |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay:: createBitmap      | Create bitmap on video streams. |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::begin              | Enable OSD and start drawing on |
|                                        | top of video streams.           |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::end                | Stop OSD drawing on all video   |
|                                        | streams.                        |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::endChannel         | Stop OSD drawing on specified   |
|                                        | video stream.                   |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::getTextHeight      | Get current configuration of    |
|                                        | OSD text height.                |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::getTextWidth       | Get current configuration of    |
|                                        | OSD text width.                 |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::color              | Convert ARGB color values into  |
|                                        | a format compatible for OSD     |
|                                        | use.                            |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::drawLine           | Draw a line in OSD frame        |
|                                        | buffer.                         |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::drawPoint          | Draw a point in OSD frame       |
|                                        | buffer.                         |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::drawRect           | Draw a rectangle on OSD frame   |
|                                        | buffer.                         |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::drawText           | Draw text on OSD frame buffer.  |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::update             | Update OSD and display drawings |
|                                        | on video streams.               |
+----------------------------------------+---------------------------------+

**VideoStreamOverlay::configVideo**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure input video stream parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideo(int ch, VideoSetting& config);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to configure.

- 0

- 1

- 2

config: VideoSetting object.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: OSD only supports channel 0, 1 and 2. “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::configTextSize**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Configure text width and height shown on OSD.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configTextSize(int ch, int text_width, int text_height);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to configure.

- 0

- 1

- 2

text_width: Text width in pixels. (Default value is 16)

text_height: Text height in pixels (Default value is 32)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “VideoStreamOverlay.h” must be included to use the class function. Text size should be configured before OSD is started using begin().

**VideoStreamOverlay::createBitmap**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Create bitmap on video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void createBitmap (int ch, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to configure.

- 0

- 1

- 2

idx: Layer index of OSD.

- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::begin**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Enable OSD and start drawing on top of video streams.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::end**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Stop OSD drawing on all video streams.

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

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::endChannel**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Stop OSD drawing on specified video stream.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void endChannel(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to stop.

- 0

- 1

- 2

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::getTextHeight**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current configuration of OSD text height.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int getTextHeight(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to get the OSD text’s height.

- 0

- 1

- 2

**Returns**
~~~~~~~~~~~

This function returns the OSD text’s height on selected channel.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::getTextWidth**
------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current configuration of OSD text width.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int getTextWidth(int ch);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to get the OSD text’s width.

- 0

- 1

- 2

**Returns**
~~~~~~~~~~~

This function returns the OSD text’s width on the selected channel.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::color**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Convert ARGB color values into a format compatible for OSD use.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    uint32_t color(uint8_t red, uint8_t green, uint8_t blue, uint8_t alpha = 0xff);

**Parameters**
~~~~~~~~~~~~~~

red: Intensity level of red color expressed as an 8-bit unsigned integer.

- 0 to 255

green: Intensity level of green color expressed as an 8-bit unsigned integer.
- 0 to 255

blue: Intensity level of blue color expressed as an 8-bit unsigned integer.
- 0 to 255

alpha: Transparency of color expressed as an 8-bit unsigned integer.
- 0 to 255 (Default value is 255. This value is optional)

Returns
~~~~~~~

This function returns the ARGB value in a format compatible for OSD use.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::drawLine**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a line in OSD frame buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawLine(int ch, int xmin, int ymin, int xmax, int ymax, int line_width, uint32_t color, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to draw on.

- 0

- 1

- 2

xmin: x coordinate of the top left corner.

ymin: y coordinate of the top left corner.

xmax: x coordinate of the bottom right corner.

ymax: y coordinate of bottom right corner.

line_width: Width of a line.

color: Color of the line.

idx: Layer index of OSD.

- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::drawPoint**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a point in OSD frame buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void VideoStreamOverlay::drawPoint(int ch, int xmin, int ymin, int point_width, uint32_t color, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to draw on.

- 0

- 1

- 2

xmin: x coordinate of the point

ymin: y coordinate of the point

point_width: size of the point.

color: Color of the point.

idx: Layer index of OSD.

- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_


.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::drawRect**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw a rectangle on OSD frame buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawRect(int ch, int xmin, int ymin, int xmax, int ymax, int line_width, uint32_t color, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to draw rectangle on.

- 0

- 1

- 2

xmin: x coordinate of the top left corner.

ymin: y coordinate of the top left corner.

xmax: x coordinate of the bottom right corner.

ymax: y coordinate of bottom right corner.

line_width: Width of a rectangle's border.

color: Color of the rectangle.

idx: Layer index of OSD.

- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::drawText**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw text on OSD frame buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawText(int ch, int xmin, int ymin, const char *text_string, uint32_t color, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to draw text on.

- 0

- 1

- 2

xmin: x coordinate of top left corner of text box.

ymin: y coordinate of top left corner of text box.

text_string: pointer to a character array containing the text to be displayed.

color: Color of the text.

idx: Layer index of OSD.

- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. “VideoStreamOverlay.h” must be included to use the class function.

**VideoStreamOverlay::update**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Update OSD and display drawings on video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void update(int ch, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to display drawings.

- 0

- 1

- 2

idx: Layer index of OSD.
- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: “VideoStreamOverlay.h” must be included to use the class function.
