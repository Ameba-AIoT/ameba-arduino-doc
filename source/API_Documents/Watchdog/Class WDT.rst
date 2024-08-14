WDT Class

Description A class used for initializing, starting, stopping watchdog
timer.

Syntax

class WDT

Members

WDT::init

Description Initialize the watchdog, including time setting, and mode
register.

Syntax void init(uint32_t timeout_ms);

Parameters timeout_ms: the watch-dog timer timeout value in millisecond
(ms). The default action after watchdog timer timeout is to reset the
whole system.

Returns NA

Example Code Example: SimpleWDT

Notes and Warnings “WDT.h” must be included to use the class function.

WDT::start

Description Start the watchdog timer by enabling the WDG state.

Syntax void start(void);

Parameters NA

Returns NA

Example Code Example: SimpleWDT

Notes and Warnings “WDT.h” must be included to use the class function.

WDT::stop

Description Stop the watchdog timer by disabling the WDG state.

Syntax void stop(void);

Parameters NA

Returns NA

Example Code Example: SimpleWDT

Notes and Warnings “WDT.h” must be included to use the class function.

WDT::refresh

Description Clear WDG Timer and refresh the watchdog timer to prevent
WDT timeout.

Syntax void refresh(void);

Parameters NA

Returns NA

Example Code Example: SimpleWDT

Notes and Warnings “WDT.h” must be included to use the class function.

WDT::init_irq

Description Switch the watchdog timer to interrupt mode and register a
watchdog timer timeout interrupt handler. The interrupt handler will be
called when the watchdog timer is timeout.

Syntax void init_irq(wdt_irq_handler handler, uint32_t id);

Parameters handler: the callback function for WDT timeout interrupt. id:
the parameter for the callback function

Returns NA

Example Code Example: SimpleWDT

Notes and Warnings “WDT.h” must be included to use the class function.
