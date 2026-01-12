RTC - Simple RTC Alarm
======================

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 /  AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

Example
-------

This example demonstrates how to use the RTC library methods to create a RTC Alarm, so that to do some tasks when an alarm is matched. In particular, the RTC time is set at 16:00:00 and an alarm at 16:00:10. When the time matches, "Alarm Match"
information will be printed on the serial monitor.

First, select the correct Ameba development board from the Arduino IDE: "Tools" → "Board".

Then open the "RTCAlarm" example from: "File" → "Examples" → "RTC" → "RTCAlarm":

|image01|

| In the example, the RTC time is set at 16:00:00 and an alarm is set at 16:00:10.
| Upon successfully upload the sample code and press the reset button.
| When the alarm time (10 seconds) is reached the attached interrupt function will print the following information: "Alarm Matched!" showing in this figure below.

|image02|

.. |image01| image:: ../../../../_static/amebad/Example_Guides/RTC/RTC_Simple_RTC_Alarm/image01.png
   :width: 543
   :height: 489

.. |image02| image:: ../../../../_static/amebad/Example_Guides/RTC/RTC_Simple_RTC_Alarm/image02.png
   :width: 598
   :height: 318
