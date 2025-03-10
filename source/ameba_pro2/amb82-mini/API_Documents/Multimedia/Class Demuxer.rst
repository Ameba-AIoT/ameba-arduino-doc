Class Demuxer
=============

.. contents::
  :local:
  :depth: 2

**Demuxer Class**
------------------

**Description**
~~~~~~~~~~~~~~~

A class used to handle MP4 file processing and extract audio and video streams from an MP4 file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class Demuxer

**Members**
~~~~~~~~~~~

+---------------------------+------------------------------------------+
| **Public Constructors**                                              |
+===========================+==========================================+
| Demuxer::Demuxer          | Constructs a Demuxer object.             |
+---------------------------+------------------------------------------+
| **Public Methods**                                                   |
+---------------------------+------------------------------------------+
| Demuxer::begin            | Begin initializes and starts the demuxer |
|                           | for processing an MP4 file.              |
+---------------------------+------------------------------------------+
| Demuxer::pause            | Pause the RTSP streaming.                |
+---------------------------+------------------------------------------+
| Demuxer::resume           | Resume the RTSP streaming.               |
+---------------------------+------------------------------------------+
| Demuxer::end              | Stop demuxer.                            |
+---------------------------+------------------------------------------+

**Demuxer::begin**
-------------------

**Description**
~~~~~~~~~~~~~~~

Begin initializes and starts the demuxer for processing an MP4 file.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(const char* MP4FileName, uint32_t loopMode, uint32_t startTime = 0);

**Parameters**
~~~~~~~~~~~~~~

MP4FileName: The name of the MP4 file to be processed.

loopMode: Determines whether the file should play in a loop. (Valid value: 0 (No looping) & 1 (looping))

startTime: The starting position (in milliseconds) from which playback begins. (Default: 0ms)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DemuxerRTSP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/DemuxerRTSP/DemuxerRTSP.ino>`_

.. note :: "Demuxer.h" must be included to use the class function.

**Demuxer::pause**
-------------------

**Description**
~~~~~~~~~~~~~~~

Pause the RTSP streaming.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void pause(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DemuxerRTSP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/DemuxerRTSP/DemuxerRTSP.ino>`_

.. note :: "Demuxer.h" must be included to use the class function.

**Demuxer::resume**
--------------------

**Description**
~~~~~~~~~~~~~~~

Resume the RTSP streaming.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void pause(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `DemuxerRTSP <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/DemuxerRTSP/DemuxerRTSP.ino>`_

.. note :: "Demuxer.h" must be included to use the class function.

**Demuxer::end**
-----------------

**Description**
~~~~~~~~~~~~~~~

Stop demuxer.

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

.. note :: "RTP.h" must be included to use the class function.

