Class UVCD
==========

.. contents::
  :local:
  :depth: 2

**UVCD Class**
--------------

**Description**
~~~~~~~~~~~~~~~

A class for USB UVC device API.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class UVCD

**Members**
~~~~~~~~~~~

+-----------------------------------+----------------------------------+
| **Public Constructors**           |                                  |
+===================================+==================================+
| UVCD::UVCD                        | Constructs a UVCD object.        |
|                                   | Initialize/Re-initialize of      |
|                                   | using USB UVC device.            |
+-----------------------------------+----------------------------------+
| **Public Methods**                |                                  |
+-----------------------------------+----------------------------------+
| UVCD::configVideo                 | Start config video of using USB  |
|                                   | UVC device.                      |
+-----------------------------------+----------------------------------+
| UVCD::begin                       | Begin video streaming of using   |
|                                   | USB UVC device.                  |
+-----------------------------------+----------------------------------+

**UVCD::UVCD**
--------------

**Description**
~~~~~~~~~~~~~~~

Constructs a UVCD object. Initialize/Re-initialize of using USB UVC device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    UVCD(void);
    UVCD(const char *usb_uvcd_driver_name);

**Parameters**
~~~~~~~~~~~~~~

usb_uvcd_driver_name: A string of user defined USB UVC device driver name.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVC Device <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/UVC_Device/UVC_Device.ino>`_

.. note :: “UVCD.h”, "StreamIO.h" and "VideoStream.h" must be included to use the class function.

**UVCD::configVideo**
---------------------

**Description**
~~~~~~~~~~~~~~~

Start config video of using USB UVC device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void configVideo(VideoSetting &config);

**Parameters**
~~~~~~~~~~~~~~

config: pointer of VideoSetting

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVC Device <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/UVC_Device/UVC_Device.ino>`_

.. note :: “UVCD.h”, "StreamIO.h" and "VideoStream.h" must be included to use the class function.

**UVCD::begin**
---------------

**Description**
~~~~~~~~~~~~~~~

Begin video streaming of using USB UVC device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(const MMFModule &module_videocam, void *module_videolinker, int uvcd_channel);

**Parameters**
~~~~~~~~~~~~~~

module_videocam: stream data from camera video.

module_videolinker: StreamIO object for uvcd.

uvcd_channel: video channel.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `UVC Device <https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/USB/examples/UVC_Device/UVC_Device.ino>`_

.. note :: “UVCD.h”, "StreamIO.h" and "VideoStream.h" must be included to use the class function.
