**GTimerClass Class**

| **Description**
| A class used for initializing, starting, stopping Gtimer.

**Syntax**

class GTimerClass

**Members**

+-----------------------------------+-----------------------------------+
| **Public Constructors**           |                                   |
+===================================+===================================+
| GTimerClass:: GTimerClass         | Constructs a GTimerClass object.  |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
| **Public Methods**                |                                   |
+-----------------------------------+-----------------------------------+
| GTimerClass::begin                | Initialize a timer and start it   |
|                                   | immediately.                      |
+-----------------------------------+-----------------------------------+
| GTimerClass::stop                 | Stop a specific timer.            |
+-----------------------------------+-----------------------------------+
| GTimerClass::reload               | Reload a specific timer.          |
+-----------------------------------+-----------------------------------+
| GTimerClass::read_us              | Read current countdown value.     |
+-----------------------------------+-----------------------------------+


**GtimerCass::begin**

| **Description**
| Initialize a timer and start it immediately.

| **Syntax**
| void begin(uint32_t timerid, uint32_t duration_us, void
  (\*handler)(uint32_t), bool periodical = true, uint32_t userdata = 0,
  uint32_t timer0_clk_sel = 0);

| **Parameters**
| timerid: There are 5 valid GTimer with timer id 0 to 4.

duration_us: The duration of timer. The time unit is microsecond and the
precision is 32768Hz.

handler: As timer timeout, it would invoke this handler.

periodical: By default, the timer would keep periodically countdown and
reload which leads the handler periodically invoked.

userdata: The user data brings to the handler. Default value is 0.

timer0_clk_sel: Select the timer0 clock, 0 for 40MHz or 1 for 4MHz.
Default value is 0.

| **Returns**
| NA

| **Example Code**
| Example: TimerOneshot, TimerPeriodical

| **Notes and Warnings**
| “GTimer.h” must be included to use the class function.\ **

**GtimerCass::stop**

| **Description**
| Stop a specific timer.

| **Syntax**
| void stop(uint32_t timerid);

**Parameters**

timerid: Stop the timer with its timer id 0 to 4.

| **Returns**
| NA

| **Example Code**
| Example: TimerOneshot, TimerPeriodical

| **Notes and Warnings**
| “GTimer.h” must be included to use the class function.\ **

**GtimerCass::reload**

| **Description**
| Reload a specific timer. The GTimer is a countdown timer. Reload it
  would make it discard the current countdown value and restart
  countdown based on the duration.

| **Syntax**
| void refresh(uint32_t timerid, uint32_t duration_u);

| **Parameters**
| timerid: The timer to be modified with its timer id 0 to 4.

duration_us: The updated duration in unit of microseconds. (1 to 10000)

| **Returns**
| NA

| **Example Code**
| Example: TimerOneshot, TimerPeriodical

| **Notes and Warnings**
| “GTimer.h” must be included to use the class function.\ **

**GtimerCass::read_us**

| **Description**
| Read current countdown value.

| **Syntax**
| void reload(uint32_t timerid, uint32_t duration_us);

| **Parameters**
| timerid: The timer to be read with its timer id 0 to 4.

| **Returns**
| The current countdown value in microseconds.

| **Example Code**
| Example: TimerOneshot, TimerPeriodical

| **Notes and Warnings**
| “GTimer.h” must be included to use the class function.
