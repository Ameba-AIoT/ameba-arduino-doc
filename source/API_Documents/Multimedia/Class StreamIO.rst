Class StreamIO
==============

.. contents::
  :local:
  :depth: 2

**StreamIO Class**
------------------

**Description**
~~~~~~~~~~~~~~~

A class used to connect streaming data from data stream producers (e.g., video, audio) to data stream consumers (e.g., RTSP, MP4 recording). Can be configured to duplicate a single data stream to multiple consumers, or to combine several data streams into a single consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class StreamIO

**Members**
~~~~~~~~~~~

+---------------------------+-------------------------------------------+
| **Public Constructors**                                               |
+===========================+===========================================+
| StreamIO::StreamIO        | Constructs a StreamIO object              |
+---------------------------+-------------------------------------------+
| **Public Methods**                                                    |
+---------------------------+-------------------------------------------+
| StreamIO::begin           | Start streaming data from data producer   |
|                           | to data consumer.                         |
+---------------------------+-------------------------------------------+
| StreamIO::end             | Stop streaming data from data producer to |
|                           | data consumer.                            |
+---------------------------+-------------------------------------------+
| StreamIO::pause           | Pause streaming data from data producer   |
|                           | to data consumer.                         |
+---------------------------+-------------------------------------------+
| StreamIO::resume          | Resume streaming data from data producer  |
|                           | to data consumer.                         |
+---------------------------+-------------------------------------------+
| StreamIO::registerInput   | Register input data stream from a data    |
|                           | producer.                                 |
+---------------------------+-------------------------------------------+
| StreamIO::registerInput1  | Register first input data stream from a   |
|                           | data producer.                            |
+---------------------------+-------------------------------------------+
| StreamIO::registerInput2  | Register second input data stream from a  |
|                           | data producer.                            |
+---------------------------+-------------------------------------------+
| StreamIO::registerInput3  | Register third input data stream from a   |
|                           | data producer.                            |
+---------------------------+-------------------------------------------+
| StreamIO::registerOutput  | Register output data stream to a data     |
|                           | consumer.                                 |
+---------------------------+-------------------------------------------+
| StreamIO::registerOutput1 | Register first output data stream to a    |
|                           | data consumer.                            |
+---------------------------+-------------------------------------------+
| StreamIO::registerOutput2 | Register second output data stream to a   |
|                           | data consumer.                            |
+---------------------------+-------------------------------------------+
| StreamIO::setStackSize    | Configure memory stack size available to  |
|                           | StreamIO data processing task.            |
+---------------------------+-------------------------------------------+
| StreamIO::setTaskPriority | Configure priority of StreamIO data       |
|                           | processing task.                          |
+---------------------------+-------------------------------------------+

**StreamIO::StreamIO**
----------------------

**Description**
~~~~~~~~~~~~~~~

A class used to connect streaming data from data stream producers (e.g., video, audio) to data stream consumers (e.g., RTSP, MP4 recording). Can be configured to duplicate a single data stream to multiple consumers, or to combine several data streams into a single consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    StreamIO::StreamIO(uint8_t numInput, uint8_t numOutput)

**Parameters**
~~~~~~~~~~~~~~

numInput: number of input data streams.

numOutput: number of output data streams.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `StreamRTSP/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: “StreamIO.h” must be included to use the class function.

**StreamIO::begin**
-------------------

**Description**
~~~~~~~~~~~~~~~

Start streaming data from data producer to data consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

Function returns 0 for success, -1 for fail to start the data streaming task.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: This function should only be called after configuration of input and output data streams. “StreamIO.h” must be included to use the class function.

**StreamIO::end**
-----------------

**Description**
~~~~~~~~~~~~~~~

Stop streaming data from data producer to data consumer.

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

.. note :: “StreamIO.h” must be included to use the class function.

**StreamIO::pause**
-------------------

**Description**
~~~~~~~~~~~~~~~

Pause streaming data from data producer to data consumer.

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

NA

.. note :: “StreamIO.h” must be included to use the class function.

**StreamIO::resume**
--------------------

**Description**
~~~~~~~~~~~~~~~

Resume streaming data from data producer to data consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void resume(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “StreamIO.h” must be included to use the class function.

**StreamIO::registerInput**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Register input data stream from a data producer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerInput(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream producer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a multi-input StreamIO class, this has the same effect as calling registerInput1. “StreamIO.h” must be included to use the class function.

**StreamIO::registerInput1**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Register first input data stream from a data producer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerInput1(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream producer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a single-input StreamIO class, this has the same effect as calling registerInput. “StreamIO.h” must be included to use the class function.

**StreamIO::registerInput2**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Register second input data stream from a data producer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerInput2(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream producer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a single-input StreamIO class, this has the same effect as calling registerInput. “StreamIO.h” must be included to use the class function.

**StreamIO::registerInput3**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Register third input data stream from a data producer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerInput3(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream producer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a single-input StreamIO class, this has the same effect as calling registerInput. “StreamIO.h” must be included to use the class function.

**StreamIO::registerOutput**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Register output data stream to a data consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerOutput(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream consumer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a multi-output StreamIO class, this has the same effect as calling registerOutput1. “StreamIO.h” must be included to use the class function.

**StreamIO::registerOutput1**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Register first output data stream to a data consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerOutput1(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream consumer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a single-output StreamIO class, this has the same effect as calling registerOutput. “StreamIO.h” must be included to use the class function.

**StreamIO::registerOutput2**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Register second output data stream to a data consumer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void registerOutput2(const MMFModule& module);

**Parameters**
~~~~~~~~~~~~~~

module: data stream consumer module.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `RecordMP4/SingleVideoWithAudio <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/RecordMP4/SingleVideoWithAudio/SingleVideoWithAudio.ino>`_

.. note :: When used on a single-output StreamIO class, this has the same effect as calling registerOutput. “StreamIO.h” must be included to use the class function.

**StreamIO::setStackSize**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Configure memory stack size available to StreamIO data processing task.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setStackSize(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “StreamIO.h” must be included to use the class function.

**StreamIO::setTaskPriority**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Configure priority of StreamIO data processing task.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void setTaskPriority(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “StreamIO.h” must be included to use the class function.
