Retention Standby Mode
======================

.. contents::
  :local:
  :depth: 2

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  Optional: Push button x 1

-  Optional: Register 220 ohms x 1

Example
-------

In this example, the development board will demo the retention Standby Mode for power save. There are 4 wake-up retention sources. The system will count down 5s then go to Stand By mode. Upon the wake-up source being tiggered, the system will be reboot and wake up again without losing the retention value.

The module and board power consumption report under Standby mode are listed in these two tables below.

**RTL8735B module power consumption test results**

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
| PON GPIO              | 41.07                                        |
+-----------------------+----------------------------------------------+
| Gtimer0               | 41.48                                        |
+-----------------------+----------------------------------------------+

**AMB82-MINI board Power Consumption**

+-----------------------+-----------------------+----------------------+
| **Wake-up source**    | **Development board                          |
|                       | power consumption**                          |
|                       |                                              |
|                       | **Approximate                                |
|                       | measurement (mA)**                           |
+=======================+=======================+======================+
|                       | Normal Mode           | Standby Mode         |
+-----------------------+-----------------------+----------------------+
| AON timer             | 53.15                 | 4.79                 |
+-----------------------+-----------------------+----------------------+
| AON GPIO              | 53.12                 | 4.81                 |
+-----------------------+-----------------------+----------------------+
| PON GPIO              | 55.09                 | 4.87                 |
+-----------------------+-----------------------+----------------------+
| Gtimer0               | 55.59                 | 4.83                 |
+-----------------------+-----------------------+----------------------+

Open example in “File” -> “Examples” -> “AmebaPowerMode” -> “RetentionStandbyMode”.

|Image01|

| Next is setting up the system and entering the power mode. Please refer to the following steps for entering Standby mode.
| Step 1. Ensure RETENTION is "#define RETENTION 1" in this example.
| Step 2. Set up the “WAKEUP_SOURCE”, AON timer: 0; AON GPIO: 1; PON GPIO: 2, Gtimer0: 3.
| Step 3. Set up the wake-up source setting. There are 4 wake-up sources, each one has its own settings.
| For AON timer, at section ”#if (WAKEUP_SOURCE == 0)”, set value to “CLOCK” and “SLEEP_DURATION”. “CLOCK” can be 4MHz or 100kHz. “SLEEP_DURATION” unit is in seconds.
| For AON GPIO, at section “#elif (WAKEUP_SOURCE == 1)”, set value to “WAKUPE_SETTING”. “WAKUPE_SETTING” in this case is the Pin number, that can be 21 or 22. The GPIO pin is set to active high, please refer to the following connection.

|image02|

| For PON GPIO, at section “#elif (WAKEUP_SOURCE == 2)”, set value to “WAKUPE_SETTING”. “WAKUPE_SETTING” in this case is the Pin number, that can be 0 to 11. The GPIO pin is set to active high, please refer to the following connection.

|image03|

| For Gtimer0, at section “#elif (WAKEUP_SOURCE == 3)”, set value to “SLEEP_DURATION”. “SLEEP_DURATION” is the timer sleep duration in seconds.
| Step 4. Start the Deep Sleep mode. There is only 1 optional setting for this step. 

|image04|

| Step 5. Define retention variables.

|image05|

| To wake up, all timers will automatically wake up when the duration is finished, all GPIO pins must active high by pressing the push button.
| The correct boot, enter Standby, reboot cycle, and printed retention data will be same as following picture.

|image06|

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/PowerMode/Retention_Standby_Mode/image01.png
   :width:  1919 px
   :height:  1029 px
   :scale: 40%
.. |image02| image:: ../../../_static/amebapro2/Example_Guides/PowerMode/Retention_Standby_Mode/image02.png
   :width:  621 px
   :height:  517 px

.. |image03| image:: ../../../_static/amebapro2/Example_Guides/PowerMode/Retention_Standby_Mode/image03.png
   :width:  741 px
   :height:  619 px

.. |image04| image:: ../../../_static/amebapro2/Example_Guides/PowerMode/Retention_Standby_Mode/image04.png
   :width:  828 px
   :height:  703 px

.. |image05| image:: ../../../_static/amebapro2/Example_Guides/PowerMode/Retention_Standby_Mode/image05.png
   :width:  1310 px
   :height:  746 px
   :scale: 60%
.. |image06| image:: ../../../_static/amebapro2/Example_Guides/PowerMode/Retention_Standby_Mode/image06.png
   :width:  368 px
   :height:  777 px