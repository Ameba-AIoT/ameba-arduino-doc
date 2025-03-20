RTC - Simple RTC
================

.. contents::
  :local:
  :depth: 2

Materials
---------

- AmebaD [AMB21 / AMB22 / AMB23 /  AMB25 / AMB26 / BW16 / AW-CU488 Thing Plus] x 1

Example
-------

This example demonstrates how to use the RTC library methods. This function describes how to use the RTC API. The RTC function is
implemented by an independent BCD timer/counter.

| Select the correct Ameba development board from the Arduino IDE: "Tools" → "Board". 
| Then open the “RTC” example from: "File" → "Examples" → "AmebaRTC" → "RTC":

|image01|

Upon successfully upload the sample code and press the reset button, this example will print out time information since the user initialized
time every second in the Serial Monitor.

|image02|

**Code Reference**

| [1] Simple RTC example from Arduino Tutorials:
| https://www.arduino.cc/en/Tutorial/SimpleRTC

.. |image01| image:: ../../../../_static/amebad/Example_Guides/RTC/RTC_Simple_RTC/image01.png
   :width: 549
   :height: 426

.. |image02| image:: ../../../../_static/amebad/Example_Guides/RTC/RTC_Simple_RTC/image02.png
   :width: 597
   :height: 324