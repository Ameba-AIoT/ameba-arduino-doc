**RTCClass Class**

| **Description**
| A class used for initializing, starting, stopping, and setting alarm
  with RTC.

**Syntax**

class WDT

**Members**

+-----------------------------------+-----------------------------------+
| **Public Constructors**           |                                   |
+===================================+===================================+
| RTCClass:: RTCClass               | Constructs an RTC object.         |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
| **Public Methods**                |                                   |
+-----------------------------------+-----------------------------------+
| RTCClass::Init                    | Initializes the RTC device,       |
|                                   | include clock, RTC registers and  |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+
| RTCClass::DeInit                  | Deinitializes the RTC device.     |
+-----------------------------------+-----------------------------------+
| RTCClass::Write                   | Set the specified timestamp in    |
|                                   | seconds to RTC.                   |
+-----------------------------------+-----------------------------------+
| RTCClass::Read                    | Get current timestamp in seconds  |
|                                   | from RTC.                         |
+-----------------------------------+-----------------------------------+
| RTCClass::Wait                    | Wait for seconds. A delay         |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+
| RTCClass::SetEpoch                | Convert human readable time to    |
|                                   | epoch time.                       |
+-----------------------------------+-----------------------------------+
| RTCClass::EnableAlarm             | Enable the RTC alarm.             |
+-----------------------------------+-----------------------------------+
| RTCClass::DisableAlarm            | Disable the RTC alarm.            |
+-----------------------------------+-----------------------------------+


**RTCClass::Init**

| **Description**
| Initializes the RTC device, include clock, RTC registers and function.

**Syntax**

void Init(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.\ **

**RTCClass::DeInit**

| **Description**
| Deinitializes the RTC device.

| **Syntax**
| void DeInit(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.\ **

**RTCClass::Write**

| **Description**
| Set the specified timestamp in seconds to RTC.

| **Syntax**
| void Write(long long t);

| **Parameters**
| t: Seconds from 1970.1.1 00:00:00 to specified data and time which is
  to be set.

| **Returns**
| NA

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.\ **

**RTCClass::Read**

| **Description**
| Get current timestamp in seconds from RTC.

| **Syntax**
| long long Read(void);

| **Parameters**
| NA

| **Returns**
| The current timestamp in seconds which is calculated from 1970.1.1
  00:00:00.

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.\ **

**RTCClass::Wait**

| **Description**
| Wait for seconds. A delay function.

**Syntax**

void Wait(int s);

| **Parameters**
| s: delay time in seconds.

| **Returns**
| NA

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.

**RTCClass::SetEpoch**

| **Description**
| Convert human readable time to epoch time.

**Syntax**

long long SetEpoch(int year, int month, int day, int hour, int min, int
sec);

| **Parameters**
| year: Input time in year. Start from 1900.

month: Input time in month. 0 to 11

day: Input time unit in day. 1 to 31.

hour: Input time unit in hour. 0 to 23.

min: Input time unit in min. 0 to 59.

sec: Input time unit in sec. 0 to 59.

| **Returns**
| The epoch time of the input date.

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.

**RTCClass::EnableAlarm**

| **Description**
| Enable the RTC alarm.

**Syntax**

void EnableAlarm(int day, int hour, int min, int sec, void
(\*rtc_handler)(void));

| **Parameters**
| day: Alarm time unit in day. 1 to 31.

hour: Alarm time unit in hour. 0 to 23.

min: Alarm time unit in min. 0 to 59.

sec: Alarm time unit in sec. 0 to 59.

rtc_handler: the callback function for rtc alarm interrupt.

| **Returns**
| NA

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.

**RTCClass::DisableAlarm**

| **Description**
| Disable the RTC alarm.

**Syntax**

void DisableAlarm(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| Example: Simple_RTC, Simple_RTC_Alarm

| **Notes and Warnings**
| “rtc.h” must be included to use the class function.
