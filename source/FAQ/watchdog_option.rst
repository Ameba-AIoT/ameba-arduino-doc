.. tags:: amb82-mini, watchdog timer

Can the system automatically reset if the program hangs?
========================================================

**Answer**

The system can automatically reset using the watchdog timer (WDT).

When enabled, the watchdog continuously monitors the main loop and ensures it remains responsive.

You can enable or disable the watchdog in the Arduino IDE under **Tools → Watchdog**.

Please refer to `AMB82 Mini Getting Started - Selection Ameba Modes <https://ameba-doc-arduino-sdk.readthedocs-hosted.com/en/latest/ameba_pro2/amb82-mini/Getting_Started/Getting%20Started%20with%20Ameba.html#step-1-selection-ameba-modes>`_

If the program hangs and stops updating for too long (beyond **LOOP_TIMEOUT_MS**, e.g. 1.5 s), the watchdog stops refreshing.
After the set timeout period (**WDT_TIMEOUT_MS**, e.g. 10 s), the watchdog triggers a system reset.

Watchdog timing parameters can be modified in: cores/ambpro2/Arduino.h

- WDT_TIMEOUT_MS: Time before system reset if not refreshed.

- WDT_PERIOD_MS: How often the watchdog checks system health.

- LOOP_TIMEOUT_MS: Max time allowed since last loop update.
