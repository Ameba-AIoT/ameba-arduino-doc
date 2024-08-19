**PMClass Class**

| **Description**
| A class used for PowerMode control.

**Syntax**

class PMClass

**Members**

+-----------------------------------+-----------------------------------+
| **Public Constructors**           |                                   |
+===================================+===================================+
| PMClass::PMClass                  | Constructs an PMClass object.     |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
| **Public Methods**                |                                   |
+-----------------------------------+-----------------------------------+
| PMClass::begin                    | Initializes the PowerMode         |
|                                   | settings for device, include type |
|                                   | of the mode, wake up sources and  |
|                                   | related source settings.          |
+-----------------------------------+-----------------------------------+
| PMClass::start                    | Start the PowerMode of device.    |
+-----------------------------------+-----------------------------------+


**PMClass::begin**

| **Description**
| Initializes the PowerMode settings for device, include type of the
  mode, wake up sources and related source settings.

| **Syntax**
| void begin(uint32_t sleep_mode, int wakeup_source, uint32_t
  wakeup_setting = 0);

| **Parameters**
| sleep_mode: Power Mode selection. Deepsleep mode: DEEPSLEEP_MODE;
  Standby mode: STANDBY_MODE

wakeup_source: Wake up source selection. AON timer, AON GPIO, RTC, PON
GPIO, UART/Serial1, and Gtimer0 set by 0 to 5.

wakeup_setting: Settings for different wakeup sources and default is 0.

For AON time, it is a pointer to an array that stores clock(1:4MHz;
0:100kHz) and duration(by seconds).

For AON GPIO, it is pin number 21 or 22.

For RTC, it is a pointer to an array that stores time duration as day,
hour, min and sec(0, 0:0:0, to 365, 23:59:59).

For PON GPIO, it is pin number 0 to 11.

For Gtimer0, it is time duration in seconds. (start from 1s)

| **Returns**
| NA

| **Example Code**
| Example: DeepSleepMode, StandbyMode

| **Notes and Warnings**
| “PowerMode.h” must be included to use the class function.\ **

**PMClass::start**

| **Description**
| Start the PowerMode of device.

| **Syntax**
| void start(void);

void start(int year, int month, int day, int hour, int min, int sec);

| **Parameters**
| Optional when wake up source is RTC. Default start time is 1970.1.1
  00:00:00.

year: Start time by year. Starts from 1900.

month: Start time by month. 0 to 11.

day: Start time by day. 1 to 365.

hour: Start time by hour. 0 to 23.

min: Start time by min. 0 to 59.

sec: Start time by sec. 0 to 59.

| **Returns**
| NA

| **Example Code**
| Example: DeepSleepMode, StandbyMode

| **Notes and Warnings**
| “PowerMode.h” must be included to use the class function.
