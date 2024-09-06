Class RTP
=========

.. contents::
  :local:
  :depth: 2

**RTP Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used to receive an audio data stream over a network using the Real-time Transport Protocol (RTP). This allows streaming of an audio stream from a computer to the development board.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class RTP

**Members**
~~~~~~~~~~~

+---------------------------+------------------------------------------+
| **Public Constructors**                                              |
+===========================+==========================================+
| RTP::RTP                  | Constructs a RTP object.                 |
+---------------------------+------------------------------------------+
| **Public Methods**                                                   |
+---------------------------+------------------------------------------+
| RTP::configPort           | Configure RTP network port.              |
+---------------------------+------------------------------------------+
| RTP::begin                | Start RTP streaming.                     |
+---------------------------+------------------------------------------+
| RTP::end                  | Stop RTP streaming.                      |
+---------------------------+------------------------------------------+
| RTP::getPort              | Get RTP network port value.              |
+---------------------------+------------------------------------------+

**RTP::configPort**
-------------------

**Description**
~~~~~~~~~~~~~~~

Configure RTP network port.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configPort(uint16_t port);

**Parameters**
~~~~~~~~~~~~~~

port: Desired network port for RTP.

- 5004 (Default value)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “RTP.h” must be included to use the class function.

**RTP::begin**
--------------

**Description**
~~~~~~~~~~~~~~~

Start RTP streaming.

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

Example: `Audio/RTPAudioStream <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/Audio/RTPAudioStream/RTPAudioStream.ino>`_

.. note :: “RTP.h” must be included to use the class function.

**RTP::end**
------------

**Description**
~~~~~~~~~~~~~~~

Stop RTP streaming.

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

.. note :: “RTP.h” must be included to use the class function.

**RTP::getPort**
----------------

**Description**
~~~~~~~~~~~~~~~

Get RTP stream network port.

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

.. note :: “RTP.h” must be included to use the class function.
