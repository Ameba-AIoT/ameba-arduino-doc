Class VideoStreamOverlay
========================

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
| VideoStreamOverlay::drawPlus           | Draw "+" on OSD frame buffer.   |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::update             | Update OSD and display drawings |
|                                        | on video streams.               |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::initOSDBitmapPos   | Set image position on video     |
|                                        | stream.                         |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::initOSDBitmapBlk   | Set block index of image        |
|                                        | on video stream.                |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::initOSDBitmapBuf   | Set buffer containing image data|
|                                        | and its length                  |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::resizeWidth        | Get resized width of image for  |
|                                        | overlaying on a video stream.   |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::resizeHeight       | Get resized height of image for |
|                                        | overlaying on a video stream.   |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::heapsizeCal        | Get heapsize for an image       |
|                                        | overlay given its resized       |
|                                        | dimensions and color format.    |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::drawImage          | Draw image on OSD frame buffer. |
+----------------------------------------+---------------------------------+
| VideoStreamOverlay::displayImage       | Update OSD and display images   |
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

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: OSD only supports channel 0, 1 and 2. "VideoStreamOverlay.h" must be included to use the class function.

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

.. note :: "VideoStreamOverlay.h" must be included to use the class function. Text size should be configured before OSD is started using begin().

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::begin**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Enable OSD and start drawing on top of video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(void);
    void begin(VideoSetting &config, int ch, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to enable OSD.

- 0

- 1

- 2

config: VideoSetting object.

idx: Layer index of OSD.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

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

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

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

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

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

ch: Channel to get the OSD text's height.

- 0

- 1

- 2

**Returns**
~~~~~~~~~~~

This function returns the OSD text's height on selected channel.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RTSPFaceDetection <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

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

ch: Channel to get the OSD text's width.

- 0

- 1

- 2

**Returns**
~~~~~~~~~~~

This function returns the OSD text's width on the selected channel.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

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

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

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

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. "VideoStreamOverlay.h" must be included to use the class function.

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

Example: `RTSPFaceDetection <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/RTSPFaceDetection/RTSPFaceDetection.ino>`_

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. "VideoStreamOverlay.h" must be included to use the class function.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. "VideoStreamOverlay.h" must be included to use the class function.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::drawPlus**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw "+" on OSD frame buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawPlus(int ch, int x_center, int y_center, int L, int line_width, uint32_t color, int idx = 0);

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to draw text on.

- 0

- 1

- 2

xmin: x coordinate of the center of the plus symbol.

ymin: y coordinate of the center of the plus symbol.

L:  Length of each arm of the plus symbol.

line width: Thickness of the lines of the plus symbol.

color: Color of the text.

idx: Layer index of OSD.

- 0 to 5 (Default value is 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: VideoStreamOverlay::update() needs to be called for drawings to be shown on the video streams. "VideoStreamOverlay.h" must be included to use the class function.

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

Example: `MotionDetection/LoopPostProcessing <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::initOSDBitmapPos**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set image position on video stream.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void initOSDBitmapPos(osd_pict_st *bmp_info, int chn_id, uint32_t start_x, uint32_t start_y, uint32_t width, uint32_t height);

**Parameters**
~~~~~~~~~~~~~~

bmp_info: Pointer to osd_pict_st structure which contains information about an OSD image.

chn_id: Channel used.

start_x: x-coordinate for the starting position of the image on the video stream.

start_y: y-coordinate for the starting position of the bitmap on the video stream.

width: Width of the image

height: Height of the image

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::initOSDBitmapBlk**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set block index of image on video stream.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void initOSDBitmapBlk(osd_pict_st *bmp_info, int blk_idx, enum rts_osd2_blk_fmt blk_fmt, uint32_t clr_1bpp);

**Parameters**
~~~~~~~~~~~~~~

bmp_info: Pointer to osd_pict_st structure which contains information about an OSD image.

blk_idx: Block index for each image (Valid value 0-23).

blk_fmt: Specifies the format of the block.

clr_1bpp: Set the RGB color when format is RTS_OSD2_BLK_FMT_1BP.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStreamOverlay.h" must be included to use the class function. Each image requires setting a new block index.

**VideoStreamOverlay::initOSDBitmapBuf**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Set buffer containing image data and its length.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void initOSDBitmapBuf(osd_pict_st *bmp_info, uint8_t *buf, uint32_t buf_len);

**Parameters**
~~~~~~~~~~~~~~

bmp_info: Pointer to osd_pict_st structure which contains information about an OSD image.

buf: pointer to a buffer containing the raw image data

buf_len: The length of buffer, specifying the size of the data buffer in bytes.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::resizeWidth**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get resized width of image for overlaying on a video stream.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int resizeWidth(int pict_width, int pict_scaling_up_factor, int pict_scaling_down_factor);

**Parameters**
~~~~~~~~~~~~~~

pict_width: The original width of the image.

pict_scaling_up_factor: The factor by which to scale up the width.

pict_scaling_down_factor: The factor by which to scale down the width.

**Returns**
~~~~~~~~~~~

This function returns the calculated resized width.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `VideoOSDImage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/VideoOSDImage/VideoOSDImage.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::resizeHeight**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get resized height of image for overlaying on a video stream.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int resizeHeight(int pict_height, int pict_scaling_up_factor, int pict_scaling_down_factor);

**Parameters**
~~~~~~~~~~~~~~

pict_height: The original height of the image.

pict_scaling_up_factor: The factor by which to scale up the height.

pict_scaling_down_factor: The factor by which to scale down the height.

**Returns**
~~~~~~~~~~~

This function returns the calculated resized height.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `VideoOSDImage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/VideoOSDImage/VideoOSDImage.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::heapsizeCal**
--------------------------------------

**Description**
~~~~~~~~~~~~~~~

Get heapsize of an image given its resized dimensions and color format.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    unsigned int heapsizeCal(int resize_width, int resize_height, rts_osd2_blk_fmt image_format);

**Parameters**
~~~~~~~~~~~~~~

resize_width: The resized width of an image.

resize_height: The height width of an image.

image_format: The color format of an image.

**Returns**
~~~~~~~~~~~

This function returns the calculated heapsize as an unsigned int.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `VideoOSDImage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/VideoOSDImage/VideoOSDImage.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::drawImage**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Draw image on OSD frame buffer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void drawImage(int ch, unsigned char *osd_array[], osd_pict_st pict_osd_buffer, unsigned int heapsize, void *pict_name, int pict_width, int pict_height, rts_osd2_blk_fmt pict_format, int resize_width, int resize_height, int start_x, int start_y, int pict_blk_idx)

**Parameters**
~~~~~~~~~~~~~~

ch: Channel used to draw image on.

osd_array: A pointer array that use to hold overlay data for the image that will be drawn.

pict_osd_buffer: A structure contains metadata associated with the image.

heapsize: Calculated heap size necessary to store the image data.

pict_name: A  pointer that reference a name or identifier for the image.

pict_width: Original width of image.

pict_height: Original height of image.

pict_format: Color format of image.

resize_width: Resized width of image.

resize_height: Resized height of image.

start_x: starting x coordinate on the video stream where the image should be displayed.

start_y: starting y coordinate on the video stream where the image should be displayed.

pict_blk_idx: Block index for the image. (Valid value: 0-23)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `VideoOSDImage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/VideoOSDImage/VideoOSDImage.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function.

**VideoStreamOverlay::displayImage**
-------------------------------------

**Description**
~~~~~~~~~~~~~~~

Update OSD and display images on video streams.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void displayImage(int ch)

**Parameters**
~~~~~~~~~~~~~~

ch: Channel to display image.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `VideoOSDImage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/VideoOSDImage/VideoOSDImage.ino>`_

.. note :: "VideoStreamOverlay.h" must be included to use the class function. Each image requires setting a new block index.

