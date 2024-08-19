CameraSetting Class
===================

Description
-----------

A class used to configure parameters for the camera sensor.

Syntax
------

class CameraSetting

Members
-------

+----------------------------+-----------------------------------------+
| .. rubric:: Public         |                                         |
|    Constructors            |                                         |
|                            |                                         |
| :name: public-constructors |                                         |
+============================+=========================================+
| Ca                         | Constructs a CameraSetting object and   |
| meraSetting::CameraSetting | set the parameters needed for camera    |
|                            | sensor.                                 |
+----------------------------+-----------------------------------------+

**Public Methods**

+-------------------------------+--------------------------------------+
| CameraSetting::setBrightness  | Set the brightness value of the      |
|                               | image.                               |
+===============================+======================================+
| CameraSetting::getBrightness  | Get the current brightness value.    |
+-------------------------------+--------------------------------------+
| CameraSetting::setContrast    | Set the contrast value of the image. |
+-------------------------------+--------------------------------------+
| CameraSetting::getContrast    | Get the current contrast value.      |
+-------------------------------+--------------------------------------+
| CameraSetting::setSaturation  | Set the saturation value of the      |
|                               | image.                               |
+-------------------------------+--------------------------------------+
| CameraSetting::getSaturation  | Get the current saturation value.    |
+-------------------------------+--------------------------------------+
| CameraSetting::setSharpness   | Set the sharpness value of the       |
|                               | image.                               |
+-------------------------------+--------------------------------------+
| CameraSetting::getSharpness   | Get the current sharpness value.     |
+-------------------------------+--------------------------------------+
| CameraSetting::setLDC         | Enable or Disable Lens Distortion    |
|                               | Correction (LDC).                    |
+-------------------------------+--------------------------------------+
| CameraSetting::getLDC         | Get the current LDC value.           |
+-------------------------------+--------------------------------------+
| CameraSetting::setWDR         | Enable or Disable WDR mode.          |
+-------------------------------+--------------------------------------+
| CameraSetting::getWDR         | Get current WDR mode.                |
+-------------------------------+--------------------------------------+
| CameraSetting::setWDRLevel    | Set WDR level.                       |
+-------------------------------+--------------------------------------+
| CameraSetting::getWDRLevel    | Get current WDR level.               |
+-------------------------------+--------------------------------------+
| C                             | Set Exposure mode in Auto or Manual  |
| ameraSetting::setExposureMode | mode.                                |
+-------------------------------+--------------------------------------+
| C                             | Get current exposure mode.           |
| ameraSetting::getExposureMode |                                      |
+-------------------------------+--------------------------------------+
| C                             | Set exposure time.                   |
| ameraSetting::setExposureTime |                                      |
+-------------------------------+--------------------------------------+
| C                             | Get current exposure time.           |
| ameraSetting::getExposureTime |                                      |
+-------------------------------+--------------------------------------+
| CameraSetting::setAEGain      | Set exposure gain value.             |
+-------------------------------+--------------------------------------+
| CameraSetting::getAEGain      | Get current exposure gain value.     |
+-------------------------------+--------------------------------------+
| Ca                            | Enable or Disable Power Line         |
| meraSetting::setPowerLineFreq | Frequency (Anti-flicker mode).       |
+-------------------------------+--------------------------------------+
| Ca                            | Get current Power Line Frequency.    |
| meraSetting::getPowerLineFreq |                                      |
+-------------------------------+--------------------------------------+
| CameraSetting::setAWB         | Set White Balance mode in Auto or    |
|                               | Manual mode.                         |
+-------------------------------+--------------------------------------+
| CameraSetting::getAWB         | Get current White Balance mode.      |
+-------------------------------+--------------------------------------+
| CameraSetting::getWBTemp      | Get current White Balance            |
|                               | Temperature.                         |
+-------------------------------+--------------------------------------+
| CameraSetting::setRedBalance  | Set red balance value.               |
+-------------------------------+--------------------------------------+
| CameraSetting::getRedBalance  | Get red balance value.               |
+-------------------------------+--------------------------------------+
| CameraSetting::setBlueBalance | Set blue balance value.              |
+-------------------------------+--------------------------------------+
| CameraSetting::getBlueBalance | Get blue balance value.              |
+-------------------------------+--------------------------------------+
| CameraSetting::setGrayMode    | Set Gray mode.                       |
+-------------------------------+--------------------------------------+
| CameraSetting::getGrayMode    | Get current mode, gray or color.     |
+-------------------------------+--------------------------------------+
| C                             | Set Day or Night mode.               |
| ameraSetting::setDayNightMode |                                      |
+-------------------------------+--------------------------------------+
| C                             | Get current mode, day, or night.     |
| ameraSetting::getDayNightMode |                                      |
+-------------------------------+--------------------------------------+
| CameraSetting::reset          | Reset all the values to default      |
|                               | value.                               |
+-------------------------------+--------------------------------------+

+----------------------------+-----------------------------------------+
+----------------------------+-----------------------------------------+

CameraSetting::setBrightness 
=============================

.. _description-1:

Description
-----------

Set the brightness value of the image.

.. _syntax-1:

Syntax
------

void setBrightness (int value);

Parameters
----------

value: Preferred brightness value. Valid values range from -64 to 64.
Default value: 0.

Returns
-------

NA

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getBrightness
============================

.. _description-2:

Description
-----------

Get the current brightness value.

.. _syntax-2:

Syntax
------

void setBrightness (void);

.. _parameters-1:

Parameters
----------

NA

.. _returns-1:

Returns
-------

NA

.. _example-code-1:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-1:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setContrast 
===========================

.. _description-3:

Description
-----------

Set the contrast value of the image.

.. _syntax-3:

Syntax
------

void setContrast (int value);

.. _parameters-2:

Parameters
----------

value: Preferred contrast value. Valid values range from 0 to 100.
Default value: 50.

.. _returns-2:

Returns
-------

NA

.. _example-code-2:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-2:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getContrast 
===========================

.. _description-4:

Description
-----------

Get the current contrast value.

.. _syntax-4:

Syntax
------

void getContrast (void);

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

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-3:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setSaturation
============================

.. _description-5:

Description
-----------

Set the saturation value of the image.

.. _syntax-5:

Syntax
------

void setSaturation (int value);

.. _parameters-4:

Parameters
----------

value: Preferred saturation value. Valid values range from 0 to 100.
Default value: 50.

.. _returns-4:

Returns
-------

NA

.. _example-code-4:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-4:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getSaturation 
=============================

.. _description-6:

Description
-----------

Get the current saturation value.

.. _syntax-6:

Syntax
------

void getSaturation (void);

.. _parameters-5:

Parameters
----------

NA

.. _returns-5:

Returns
-------

NA

.. _example-code-5:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-5:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setSharpness 
============================

.. _description-7:

Description
-----------

Set the sharpness value of the image.

.. _syntax-7:

Syntax
------

void setSharpness (int value);

.. _parameters-6:

Parameters
----------

value: Preferred sharpness value. Valid values range from 0 to 100.
Default value: 50.

.. _returns-6:

Returns
-------

NA

.. _example-code-6:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-6:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getSharpness 
============================

.. _description-8:

Description
-----------

Get the current sharpness value.

.. _syntax-8:

Syntax
------

void getSharpness (void);

.. _parameters-7:

Parameters
----------

NA

.. _returns-7:

Returns
-------

NA

.. _example-code-7:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-7:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setLDC 
======================

.. _description-9:

Description
-----------

Enable or Disable Lens Distortion Correction (LDC).

.. _syntax-9:

Syntax
------

void setLDC (int enable);

.. _parameters-8:

Parameters
----------

enable: Enable or Disable LDC. Valid values: 0 (Disabled) and
1(Enabled). Default value: 0 (Disabled).

.. _returns-8:

Returns
-------

NA

.. _example-code-8:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-8:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getLDC 
======================

.. _description-10:

Description
-----------

Get the current LDC value.

.. _syntax-10:

Syntax
------

void getLDC (void);

.. _parameters-9:

Parameters
----------

NA

.. _returns-9:

Returns
-------

NA

.. _example-code-9:

Example Code
------------

ImageTuning
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/ImageTuning/ImageTuning.ino)

.. _notes-and-warnings-9:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setWDR 
======================

.. _description-11:

Description
-----------

Enable or Disable WDR mode.

.. _syntax-11:

Syntax
------

void setWDR (int enable);

.. _parameters-10:

Parameters
----------

enable: Preferred WDR mode. If WDR mode is enabled, Manual or Auto mode
can be chosen. Valid values: 0 (Disabled), 1 (Manual) and 2 (Auto).
Default value: 0 (Disabled).

.. _returns-10:

Returns
-------

NA

.. _example-code-10:

Example Code
------------

WideDynamicRange
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino)

.. _notes-and-warnings-10:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getWDR 
======================

.. _description-12:

Description
-----------

Get current WDR mode.

.. _syntax-12:

Syntax
------

void getWDR (void);

.. _parameters-11:

Parameters
----------

NA

.. _returns-11:

Returns
-------

NA

.. _example-code-11:

Example Code
------------

WideDynamicRange
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino)

.. _notes-and-warnings-11:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setWDRLevel 
===========================

.. _description-13:

Description
-----------

Set WDR level.

.. _syntax-13:

Syntax
------

void setWDRLevel (int value);

.. _parameters-12:

Parameters
----------

value: Preferred WDR level. Valid values range from 50 -100. Default
value: 50.

.. _returns-12:

Returns
-------

NA

.. _example-code-12:

Example Code
------------

WideDynamicRange
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino)

.. _notes-and-warnings-12:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

WDR level can only be modified, and changes can be seen on image if WDR
mode is set to manual mode before calling setWDRLevel() function.

CameraSetting::getWDRLevel
==========================

.. _description-14:

Description
-----------

Get current WDR level.

.. _syntax-14:

Syntax
------

void getWDRLevel (void);

.. _parameters-13:

Parameters
----------

NA

.. _returns-13:

Returns
-------

NA

.. _example-code-13:

Example Code
------------

WideDynamicRange
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WideDynamicRange/WideDynamicRange.ino)

.. _notes-and-warnings-13:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setExposureMode
==============================

.. _description-15:

Description
-----------

Set Exposure mode in Auto or Manual mode.

.. _syntax-15:

Syntax
------

void setExposureMode (int enable);

.. _parameters-14:

Parameters
----------

enable: Enable exposure mode in Manual or Auto mode. Valid values: 0
(Manual), 1 (Auto). Default value: 1 (Auto).

.. _returns-14:

Returns
-------

NA

.. _example-code-14:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-14:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getExposureMode
==============================

.. _description-16:

Description
-----------

Get current exposure mode.

.. _syntax-16:

Syntax
------

void getExposureMode (void);

.. _parameters-15:

Parameters
----------

NA

.. _returns-15:

Returns
-------

NA

.. _example-code-15:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-15:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setExposureTime
==============================

.. _description-17:

Description
-----------

Set exposure time.

.. _syntax-17:

Syntax
------

void setExposureTime (int time);

.. _parameters-16:

Parameters
----------

time: Preferred exposure time. Valid value must be less than or equal to
33333us.

.. _returns-16:

Returns
-------

NA

.. _example-code-16:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-16:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getExposureTime
==============================

.. _description-18:

Description
-----------

Get current exposure time.

.. _syntax-18:

Syntax
------

void getExposureTime (void);

.. _parameters-17:

Parameters
----------

NA

.. _returns-17:

Returns
-------

NA

.. _example-code-17:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-17:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setAEGain
========================

.. _description-19:

Description
-----------

Set exposure gain value.

.. _syntax-19:

Syntax
------

void setAEGain (int value);

.. _parameters-18:

Parameters
----------

value: Preferred exposure gain. Valid values between 256 to 32768.

.. _returns-18:

Returns
-------

NA

.. _example-code-18:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-18:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

AE gain can only be modified, and changes can be seen on image if
Exposure mode is set to manual mode before calling setAEGain() function.

CameraSetting::getAEGain 
=========================

.. _description-20:

Description
-----------

Get current exposure gain value.

.. _syntax-20:

Syntax
------

void getAEGain (void);

.. _parameters-19:

Parameters
----------

NA

.. _returns-19:

Returns
-------

NA

.. _example-code-19:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-19:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setPowerLineFreq 
================================

.. _description-21:

Description
-----------

Enable or Disable Power Line Frequency (Anti-flicker mode).

.. _syntax-21:

Syntax
------

void setPowerLineFreq (int enable);

.. _parameters-20:

Parameters
----------

enable: Enable or disable power line frequency. If power line frequency
is enabled, power line frequency can be set as auto or choose from
different frequencies (50Hz, 60Hz). Valid values: 0 (Disable), 1 (50Hz),
2: (60Hz), 3 (Auto). Default value: 3 (Auto).

.. _returns-20:

Returns
-------

NA

.. _example-code-20:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-20:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getPowerLineFreq 
================================

.. _description-22:

Description
-----------

Get current Power Line Frequency.

.. _syntax-22:

Syntax
------

void getPowerLineFreq (void);

.. _parameters-21:

Parameters
----------

NA

.. _returns-21:

Returns
-------

NA

.. _example-code-21:

Example Code
------------

Exposure
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Exposure/Exposure.ino)

.. _notes-and-warnings-21:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setAWB 
======================

.. _description-23:

Description
-----------

Set White Balance mode in Auto or Manual mode.

.. _syntax-23:

Syntax
------

void setAWB (int enable);

.. _parameters-22:

Parameters
----------

enable: Enable white balance mode in Manual or Auto mode. Valid value: 0
(Manual Temperature), 1 (Auto). Default value: 1 (Auto).

.. _returns-22:

Returns
-------

NA

.. _example-code-22:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-22:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getAWB 
======================

.. _description-24:

Description
-----------

Get current White Balance mode.

.. _syntax-24:

Syntax
------

void getAWB (void);

.. _parameters-23:

Parameters
----------

NA

.. _returns-23:

Returns
-------

NA

.. _example-code-23:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-23:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getWBTemp 
=========================

.. _description-25:

Description
-----------

Get current White Balance Temperature.

.. _syntax-25:

Syntax
------

void getWBTemp (void);

.. _parameters-24:

Parameters
----------

NA

.. _returns-24:

Returns
-------

NA

.. _example-code-24:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-24:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setRedBalance 
=============================

.. _description-26:

Description
-----------

Set red balance value.

.. _syntax-26:

Syntax
------

void setRedBalance (int value);

.. _parameters-25:

Parameters
----------

value: Preferred red balance value based on 256. Valid value ranges from
256 to 2047.

.. _returns-25:

Returns
-------

NA

.. _example-code-25:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-25:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Red Balance value can only be modified, and changes can be seen on image
if white balance mode is set to manual mode before calling setRedBalance
() function.

CameraSetting::getRedBalance
============================

.. _description-27:

Description
-----------

Get current red balance value.

.. _syntax-27:

Syntax
------

void getRedBalance (void);

.. _parameters-26:

Parameters
----------

NA

.. _returns-26:

Returns
-------

NA

.. _example-code-26:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-26:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setBlueBalance 
==============================

.. _description-28:

Description
-----------

Set blue balance value.

.. _syntax-28:

Syntax
------

void setBlueBalance (int value);

.. _parameters-27:

Parameters
----------

value: Preferred blue balance value based on 256. Valid value ranges
from 256 to 2047.

.. _returns-27:

Returns
-------

NA

.. _example-code-27:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-27:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Blue Balance value can only be modified, and changes can be seen on
image if white balance mode is set to manual mode before calling
setBlueBalance() function.

CameraSetting::getBlueBalance 
==============================

.. _description-29:

Description
-----------

Get current blue balance value.

.. _syntax-29:

Syntax
------

void getBlueBalance (void);

.. _parameters-28:

Parameters
----------

NA

.. _returns-28:

Returns
-------

NA

.. _example-code-28:

Example Code
------------

WhiteBalance
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/WhiteBalance/WhiteBalance.ino)

.. _notes-and-warnings-28:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setGrayMode 
===========================

.. _description-30:

Description
-----------

Set Gray mode.

.. _syntax-30:

Syntax
------

void setGrayMode (int enable);

.. _parameters-29:

Parameters
----------

enable: Enable gray mode. Valid value: 0 (Color mode), 1 (Gray mode).
Default value: 0 (Color mode).

.. _returns-29:

Returns
-------

NA

.. _example-code-29:

Example Code
------------

Mode
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino)

.. _notes-and-warnings-29:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getGrayMode 
===========================

.. _description-31:

Description
-----------

Get current mode, gray or color.

.. _syntax-31:

Syntax
------

void getGrayMode (void);

.. _parameters-30:

Parameters
----------

NA

.. _returns-30:

Returns
-------

NA

.. _example-code-30:

Example Code
------------

Mode
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino)

.. _notes-and-warnings-30:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::setDayNightMode 
===============================

.. _description-32:

Description
-----------

Set Day or Night mode.

.. _syntax-32:

Syntax
------

void setDayNightMode (int enable);

.. _parameters-31:

Parameters
----------

enable: Enable day or night mode. Valid value: 0 (Day mode), 1 (Night
mode). Default value: 0 (Day mode).

.. _returns-31:

Returns
-------

NA

.. _example-code-31:

Example Code
------------

Mode
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino)

.. _notes-and-warnings-31:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::getDayNightMode 
===============================

.. _description-33:

Description
-----------

Get current mode, day or night.

.. _syntax-33:

Syntax
------

void getDayNightMode (void);

.. _parameters-32:

Parameters
----------

NA

.. _returns-32:

Returns
-------

NA

.. _example-code-32:

Example Code
------------

Mode
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino)

.. _notes-and-warnings-32:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

CameraSetting::reset 
=====================

.. _description-34:

Description
-----------

Reset all the values to default value.

.. _syntax-34:

Syntax
------

void reset (void);

.. _parameters-33:

Parameters
----------

NA

.. _returns-33:

Returns
-------

NA

.. _example-code-33:

Example Code
------------

Mode
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/ISPControl/Mode/Mode.ino)

.. _notes-and-warnings-33:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

VideoSetting Class
==================

.. _description-35:

Description
-----------

A class used to configure parameters for video streams.

.. _syntax-35:

Syntax
------

class VideoSetting

.. _members-1:

Members
-------

**Public Constructors**

+----------------------------+-----------------------------------------+
| VideoSetting::VideoSetting | Constructs a VideoSetting object and    |
|                            | set the parameters needed for video     |
|                            | streams.                                |
+============================+=========================================+
+----------------------------+-----------------------------------------+

**Public Methods**

+----------------------------+-----------------------------------------+
| VideoSetting::setBitrate   | Configure bitrate for H264 and H265     |
|                            | video encoder.                          |
+============================+=========================================+
| Vi                         | Configure quality level for JPEG        |
| deoSetting::setJpegQuality | snapshots.                              |
+----------------------------+-----------------------------------------+
| VideoSetting::setRotation  | Configure orientation for H264, H265    |
|                            | video and JPEG encoders.                |
+----------------------------+-----------------------------------------+
| VideoSetting::width        | Get current configured video stream     |
|                            | width.                                  |
+----------------------------+-----------------------------------------+
| VideoSetting::height       | Get current configured video stream     |
|                            | height.                                 |
+----------------------------+-----------------------------------------+
| VideoSetting::fps          | Get current configured video stream fps |
|                            | (frame per second).                     |
+----------------------------+-----------------------------------------+

VideoSetting::VideoSetting 
===========================

.. _description-36:

Description
-----------

Constructs a VideoSetting object and sets the parameters needed for
video streams, such as resolution, frame rate per second (fps), bit rate
per second (bps), encoder type.

.. _syntax-36:

Syntax
------

VideoSetting(uint8_t preset);

VideoSetting(uint8_t resolution, uint8_t fps, uint8_t encoder, uint8_t
snapshot);

VideoSetting(uint16_t w, uint16_t h, uint8_t fps, uint8_t encoder,
uint8_t snapshot);

.. _parameters-34:

Parameters
----------

preset: Select one out of 3 preset video stream settings. Default
preset: 0.

resolution: Video resolution (Valid value: VIDEO_HD, VIDEO_FHD)

fps: Frame rate in frames per second.

encoder: Video encoder format to use. (Valid value: VIDEO_HEVC,
VIDEO_H264, VIDEO_JPEG)

snapshot: Enable or disable snapshot function.

w: Width in pixels.

h: Height in pixels.

.. _returns-34:

Returns
-------

NA

.. _example-code-34:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-34:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Preset configurations:

**Preset 0:**

resolution: VIDEO_FHD

fps: 30

bps: 2*1024*1024

encoder: VIDEO_H264

snapshot: 0

**Preset 1:**

resolution: VIDEO_HD

fps: 30

bps: 2*1024*1024

encoder: VIDEO_H264

snapshot: 0

**Preset 2:**

resolution: VIDEO_FHD

fps: 30

bps: 2*1024*1024

encoder: VIDEO_JPEG

snapshot: 0

VideoSetting::setBitrate
========================

.. _description-37:

Description
-----------

Configure bitrate for H264 and H265 video encoder.

.. _syntax-37:

Syntax
------

void setBitrate(uint32_t bitrate);

.. _parameters-35:

Parameters
----------

bitrate: desired video encoder bitrate. Valid values range from 1Mbps
(1024 \* 1024) to 50Mbps (50 \* 1024 \* 1024). Default value of 4Mbps.

.. _returns-35:

Returns
-------

NA

.. _example-code-35:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-35:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function. The default
value of 4Mbps is a suitable balance of video quality and file size. For
RTSP streaming, it is recommended that the bitrate is lowered to 2Mbps
to account for possible network congestion.

VideoSetting::setJpegQuality
============================

.. _description-38:

Description
-----------

Configure quality level for JPEG snapshots.

.. _syntax-38:

Syntax
------

void setJpegQuality(uint8_t quality);

.. _parameters-36:

Parameters
----------

quality: desired JPEG image quality level. Valid values range from 1
(worst) to 9 (best). Default value of 5.

.. _returns-36:

Returns
-------

NA

.. _example-code-36:

Example Code
------------

NA

.. _notes-and-warnings-36:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function. A lower
quality results in a reduced file size, while a quality level of 9 may
result in large file sizes without a significant improvements in image
quality.

VideoSetting::setRotation
=========================

.. _description-39:

Description
-----------

Configure orientation for H264, H265 video and JPEG encoders.

.. _syntax-39:

Syntax
------

void setRotation(int angle);

.. _parameters-37:

Parameters
----------

angle: desired rotation angle represented by numerical values. Valid
values: 0, 1, 2, 3. Default value of 0.

0: No rotation

1: 90 degree to right

2. 90 degree to left

3: 180 degree

.. _returns-37:

Returns
-------

NA

.. _example-code-37:

Example Code
------------

NA

.. _notes-and-warnings-37:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

VideoSetting::width
===================

.. _description-40:

Description
-----------

Get current configured video stream width.

.. _syntax-40:

Syntax
------

uint16_t width(void);

.. _parameters-38:

Parameters
----------

NA

.. _returns-38:

Returns
-------

This function returns the current configured video stream width.

.. _example-code-38:

Example Code
------------

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino

.. _notes-and-warnings-38:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

VideoSetting::height
====================

.. _description-41:

Description
-----------

Get current configured video stream height.

.. _syntax-41:

Syntax
------

uint16_t height(void);

.. _parameters-39:

Parameters
----------

NA

.. _returns-39:

Returns
-------

This function returns the current configured video stream height.

.. _example-code-39:

Example Code
------------

LoopPostProcessing
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/MotionDetection/LoopPostProcessing/LoopPostProcessing.ino

.. _notes-and-warnings-39:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

VideoSetting::fps
=================

.. _description-42:

Description
-----------

Get current configured video stream fps (frame per second).

.. _syntax-42:

Syntax
------

uint16_t fps(void);

.. _parameters-40:

Parameters
----------

NA

.. _returns-40:

Returns
-------

This function returns the current configured video stream fps.

.. _example-code-40:

Example Code
------------

NA

.. _notes-and-warnings-40:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video Class
===========

.. _description-43:

Description
-----------

A class used to configure and initialize the camera to generate video
data streams.

.. _syntax-43:

Syntax
------

class Video

**Public Constructors**

+----------------------------+-----------------------------------------+
| Video::Video               | Construct a Video object.               |
+============================+=========================================+
+----------------------------+-----------------------------------------+

**Public Methods**

+----------------------------+-----------------------------------------+
| Video::configVideoChannel  | Configure video stream channel.         |
+----------------------------+-----------------------------------------+
| Video::camInit             | Initialization of camera sensor using   |
|                            | existing configurations.                |
+----------------------------+-----------------------------------------+
| Video::camDeinit           | Deinitialization of camera sensor       |
+----------------------------+-----------------------------------------+
| Video::videoInit           | Initialization of video streams using   |
|                            | existing configurations.                |
+----------------------------+-----------------------------------------+
| Video::videoDeinit         | Deinitialization of video stream module |
|                            | for a specific channel.                 |
+----------------------------+-----------------------------------------+
| Video::channelBegin        | Start video streaming on a specific     |
|                            | channel.                                |
+----------------------------+-----------------------------------------+
| Video::channelEnd          | Stop video streaming on a specific      |
|                            | channel.                                |
+----------------------------+-----------------------------------------+
| Video::getStream           | Get video data stream to provide as an  |
|                            | input for other data stream consumers.  |
+----------------------------+-----------------------------------------+
| Video::getImage            | Enable snapshot function.               |
+----------------------------+-----------------------------------------+
| Video::setFPS              | Set camera video max FPS.               |
+----------------------------+-----------------------------------------+
| Video::printInfo           | Print out current configuration of      |
|                            | video channels.                         |
+----------------------------+-----------------------------------------+

Video::configVideoChannel
=========================

.. _description-44:

Description
-----------

Configure video stream channel parameters using VideoSetting class object. 
---------------------------------------------------------------------------

.. _syntax-44:

Syntax
------

void configVideoChannel(int ch, VideoSetting& config);

.. _parameters-41:

Parameters
----------

ch: Channel to configure (Valid value: 0,1,2)

config: VideoSetting object

.. _returns-41:

Returns
-------

NA

.. _example-code-41:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-41:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::camInit
==============

.. _description-45:

Description
-----------

Initialize camera sensor using configuration from CameraSetting object.

.. _syntax-45:

Syntax
------

void cameraInit(CameraSetting& config);

.. _parameters-42:

Parameters
----------

config: CameraSetting object

.. _returns-42:

Returns
-------

NA

.. _example-code-42:

Example Code
------------

NA

.. _notes-and-warnings-42:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::camDeinit
================

.. _description-46:

Description
-----------

Deinitialize camera sensor.

.. _syntax-46:

Syntax
------

void cameraDeinit(void);

.. _parameters-43:

Parameters
----------

NA

.. _returns-43:

Returns
-------

NA

.. _example-code-43:

Example Code
------------

NA

.. _notes-and-warnings-43:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::videoInit
================

.. _description-47:

Description
-----------

Initialization of video streams from camera using existing
configurations.

.. _syntax-47:

Syntax
------

void videoInit(void);

.. _parameters-44:

Parameters
----------

NA

.. _returns-44:

Returns
-------

NA

.. _example-code-44:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-44:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::videoDeinit
==================

.. _description-48:

Description
-----------

Deinitialization of all video streams.

.. _syntax-48:

Syntax
------

void videoDeinit(void);
-----------------------

.. _parameters-45:

Parameters
----------

NA

.. _returns-45:

Returns
-------

NA

.. _example-code-45:

Example Code
------------

NA

.. _notes-and-warnings-45:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::channelBegin
===================

.. _description-49:

Description
-----------

Start video streaming on a specific channel.

.. _syntax-49:

Syntax
------

void channelBegin(int ch);

.. _section-1:

.. _parameters-46:

Parameters
----------

ch: channel to start streaming. Default channel is 0.

.. _returns-46:

Returns
-------

NA

.. _example-code-46:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-46:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::channelEnd
=================

.. _description-50:

Description
-----------

Stop video streaming on a specific channel.

.. _syntax-50:

Syntax
------

void channelEnd(int ch);

.. _parameters-47:

Parameters
----------

ch: channel to stop streaming. Default channel is 0.

.. _returns-47:

Returns
-------

NA

.. _example-code-47:

Example Code
------------

NA

.. _notes-and-warnings-47:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::getStream
================

.. _description-51:

Description
-----------

Get video data stream to provide as an input for other data stream
consumers.

.. _syntax-51:

Syntax
------

MMFModule getStream(int ch);
----------------------------

.. _parameters-48:

Parameters
----------

ch: channel to get data stream of. Default channel is 0.

.. _returns-48:

Returns
-------

This function returns the video data stream.

.. _example-code-48:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-48:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::getImage
===============

.. _description-52:

Description
-----------

Take a snapshot.

.. _syntax-52:

Syntax
------

void getImage(int ch, uint32_t\* addr, uint32_t\* len);

.. _parameters-49:

Parameters
----------

ch: Video stream channel to take a snapshot from.

addr: A pointer to a 32-bit unsigned integer to store the image address.

len: A pointer to a 32-bit unsigned integer to store the image length.

.. _returns-49:

Returns
-------

NA

.. _example-code-49:

Example Code
------------

HTTPDisplayJPEG
(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/CaptureJPEG/HTTPDisplayJPEG/HTTPDisplayJPEG.ino

.. _notes-and-warnings-49:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::setFPS 
==============

.. _description-53:

Description
-----------

Set camera video max FPS.

.. _syntax-53:

Syntax
------

void setFPS(int fps);

.. _parameters-50:

Parameters
----------

fps: max frame rate in frames per second for camera.

.. _returns-50:

Returns
-------

NA

.. _example-code-50:

Example Code
------------

NA

.. _notes-and-warnings-50:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.

Video::printInfo
================

.. _description-54:

Description
-----------

Print out current configuration of video channels.

.. _syntax-54:

Syntax
------

void printInfo(void);

.. _parameters-51:

Parameters
----------

NA

.. _returns-51:

Returns
-------

NA

.. _example-code-51:

Example Code
------------

VideoOnly

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/StreamRTSP/VideoOnly/VideoOnly.ino)

.. _notes-and-warnings-51:

Notes and Warnings
------------------

“VideoStream.h” must be included to use the class function.
