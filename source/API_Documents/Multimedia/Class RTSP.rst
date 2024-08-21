Class RTSP
==========

.. contents::
  :local:
  :depth: 2

**RTSP Class**
--------------

**Description**
~~~~~~~~~~~~~~~

A class used to send audio and video data streams over a network using the Real Time Streaming Protocol (RTSP). This allows viewing of a video stream on a computer using media players.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class RTSP

**Members**
~~~~~~~~~~~

+---------------------------+------------------------------------------+
| **Public Constructors**                                              |
+===========================+==========================================+
| RTSP::RTSP                | Constructs a RTSP object.                |
+---------------------------+------------------------------------------+
| **Public Methods**                                                   |
+---------------------------+------------------------------------------+
| RTSP::configVideo         | Configure RTSP module by setting up RTSP |
|                           | video parameters.                        |
+---------------------------+------------------------------------------+
| RTSP::configAudio         | Configure RTSP module by setting up RTSP |
|                           | audio parameters.                        |
+---------------------------+------------------------------------------+
| RTSP::begin               | Start RTSP streaming.                    |
+---------------------------+------------------------------------------+
| RTSP::end                 | Stop RTSP streaming.                     |
+---------------------------+------------------------------------------+
| RTSP::getPort             | Get RTSP port value.                     |
+---------------------------+------------------------------------------+
| RTSP:: printInfo          | Print out current configuration of RTSP. |
+---------------------------+------------------------------------------+

**RTSP::configVideo**
---------------------

**Description**
~~~~~~~~~~~~~~~

Configure RTSP module by setting up RTSP video parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideo(VideoSetting& config);

**Parameters**
~~~~~~~~~~~~~~

config: VideoSetting object

**Returns**
~~~~~~~~~~~

NA

*Example Code**
~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: “RTSP.h” must be included to use the class function.

**RTSP::configAudio**
---------------------

**Description**
~~~~~~~~~~~~~~~

Configure RTSP module by setting up RTSP audio parameters.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configAudio(AudioSetting& config, Audio_Codec_T codec);

**Parameters**
~~~~~~~~~~~~~~

config: AudioSetting object containing desired audio configuration

codec: Codec format of Audio stream input. Valid values: CODEC_AAC,
CODEC_G711_PCMU, CODEC_G711_PCMA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “RTSP.h” must be included to use the class function.

**RTSP::begin**
---------------

**Description**
~~~~~~~~~~~~~~~

Start RTSP streaming.

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

Example: `StreamRTSP/VideoOnly <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: “RTSP.h” must be included to use the class function.

**RTSP::end**
-------------

**Description**
~~~~~~~~~~~~~~~

Stop RTSP streaming.

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

.. note :: “RTSP.h” must be included to use the class function.

**RTSP::getPort**
-----------------

**Description**
~~~~~~~~~~~~~~~

Get RTSP stream network port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int getPort(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the port number as an integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RTSP.h” must be included to use the class function.

**RTSP::printInfo**
-------------------

**Description**
~~~~~~~~~~~~~~~

Print out current configuration of RTSP.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void printInfo(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/VideoOnly <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino>`_

.. note :: “RTSP.h” must be included to use the class function.
