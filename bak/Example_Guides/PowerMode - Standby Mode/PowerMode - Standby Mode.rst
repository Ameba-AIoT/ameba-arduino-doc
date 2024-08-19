Materials
=========

-  Ameba Pro2 [AMB82-Mini] x 1

..

   Optional

-  Push button x 1

-  Register 220 ohms x 1

-  USB to ttl serial cable x 1

Example 
========

Introduction
------------

In this example, the development board will demo the Standby Mode for
power save. There are 6 wake-up sources The system will count down 5s
then go to Stand By mode. Upon the wake-up source being tiggered, the
system will be reboot and wake up again.

The module and board power consumption report under Deep Sleep mode are
listed in these two tables below. For further information about how to
measure the module’s power consumption, please refer to *Ameba FAQ*.

+-----------------------+----------------------------------------------+
| **Wake-up source**    | **Module power consumption**                 |
|                       |                                              |
|                       | **(uA)**                                     |
+=======================+==============================================+
|                       | Stand By Mode (measure at 3V3)               |
+-----------------------+----------------------------------------------+
| AON timer             | 41.22                                        |
+-----------------------+----------------------------------------------+
| AON GPIO              | 41.28                                        |
+-----------------------+----------------------------------------------+
| RTC                   | 41.46                                        |
+-----------------------+----------------------------------------------+
| PON GPIO              | 41.07                                        |
+-----------------------+----------------------------------------------+
| UART/Serial1          | 41.32                                        |
+-----------------------+----------------------------------------------+
| Gtimer0               | 41.48                                        |
+-----------------------+----------------------------------------------+

**RTL8735B module power consumption test results**

+-----------------------+-----------------------+----------------------+
| **Wake-up source**    | **Development board   |                      |
|                       | power consumption**   |                      |
|                       |                       |                      |
|                       | **Approximate         |                      |
|                       | measurement (mA)**    |                      |
+=======================+=======================+======================+
|                       | Normal Mode           | Standby Mode         |
+-----------------------+-----------------------+----------------------+
| AON timer             | 53.15                 | 4.79                 |
+-----------------------+-----------------------+----------------------+
| AON GPIO              | 53.12                 | 4.81                 |
+-----------------------+-----------------------+----------------------+
| RTC                   | 53.11                 | 4.75                 |
+-----------------------+-----------------------+----------------------+
| PON GPIO              | 55.09                 | 4.87                 |
+-----------------------+-----------------------+----------------------+
| UART/Serial1          | 55.61                 | 4.79                 |
+-----------------------+-----------------------+----------------------+
| Gtimer0               | 55.59                 | 4.83                 |
+-----------------------+-----------------------+----------------------+

**AMB82-MINI board Power Consumption**

Procedure
---------

Open example in “File” -> “Examples” -> “AmebaPowerMode” ->
“StandbyMode”.

|Graphical user interface Description automatically generated|

Next is setting up the system and entering the power mode. Please refer
to the following steps for entering Standby mode.

Step 1. Set up the “WAKEUP_SOURCE”, AON timer: 0; AON GPIO: 1; RTC: 2,
PON GPIO: 3, UART/Serial1: 4, Gtimer0: 5.

Step 2. Set up the wake-up source setting. There are 6 wake-up sources,
each one has its own settings.

For AON timer, at section ”#if (WAKEUP_SOURCE == 0)”, set value to
“CLOCK” and “SLEEP_DURATION”. “CLOCK” can be 4MHz or 100kHz.
“SLEEP_DURATION” unit is in seconds.

For AON GPIO, at section “#elif (WAKEUP_SOURCE == 1)”, set value to
“WAKUPE_SETTING”. “WAKUPE_SETTING” in this case is the Pin number, that
can be 21 or 22. The GPIO pin is set to active high, please refer to the
following connection.

|image1|

For RTC, at section “#elif (WAKEUP_SOURCE == 2)”, set value to
“ALARM_DAY”, “ALARM_HOUR”, “ALARM_MIN”, or “ALARM_SEC”. All alarm values
set the duration of RTC wake-up. The range is “1day, 0h, 0m, 0s” to
“365day, 23h, 59min, 59s”.

For PON GPIO, at section “#elif (WAKEUP_SOURCE == 3)”, set value to
“WAKUPE_SETTING”. “WAKUPE_SETTING” in this case is the Pin number, that
can be 0 to 11. The GPIO pin is set to active high, please refer to the
following connection.

|image2|

For UART/Serial1, there is no setting required. However, USB to ttl
serial cable Tx(green) and Rx(white) pin needs to connect to Serial1 Rx
and Tx pin. Refer to the following connection. (Power 5V/3.3V Red,
Ground Black)

|A picture containing diagram Description automatically generated|

For Gtimer0, at section “#elif (WAKEUP_SOURCE == 5)”, set value to
“SLEEP_DURATION”. “SLEEP_DURATION” is the timer sleep duration in
seconds.

Step 3. Start the Standby mode. There is only 1 optional setting for
this step. When the wake-up source is set to RTC, use
“PowerMode.start(1970, 1, 1, 0, 0, 0);” to replace “PowerMode.start();”
for setting the start time. (Default is 1970.1.1 00:00:00).

|Graphical user interface Description automatically generated with
medium confidence|

To wake up, all timers will automatically wake up when the duration is
finished, all GPIO pins must active high by pressing the push button,
UART needs to give input by Serial1 though USB-ttl cable.

The correct boot, enter Standby, and reboot cycle will be same as
following picture.

|Table Description automatically generated with medium confidence|

Code Reference

NA

.. |Graphical user interface Description automatically generated| image:: ../../_static/Example_Guides/PowerMode_-_Standby_Mode/PowerMode_-_Standby_Mode_images/image01.png
   :width: 3.66422in
   :height: 5.41667in
.. |image1| image:: ../../_static/Example_Guides/PowerMode_-_Standby_Mode/PowerMode_-_Standby_Mode_images/image02.png
   :width: 4.32941in
   :height: 3.60417in
.. |image2| image:: ../../_static/Example_Guides/PowerMode_-_Standby_Mode/PowerMode_-_Standby_Mode_images/image03.png
   :width: 4.42671in
   :height: 3.69792in
.. |A picture containing diagram Description automatically generated| image:: ../../_static/Example_Guides/PowerMode_-_Standby_Mode/PowerMode_-_Standby_Mode_images/image04.png
   :width: 4.40625in
   :height: 6.0877in
.. |Graphical user interface Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/PowerMode_-_Standby_Mode/PowerMode_-_Standby_Mode_images/image05.png
   :width: 4.78125in
   :height: 5.71561in
.. |Table Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/PowerMode_-_Standby_Mode/PowerMode_-_Standby_Mode_images/image06.png
   :width: 4.39583in
   :height: 7.30006in
