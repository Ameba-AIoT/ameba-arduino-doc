.. tags:: SD card, SDIO, GPIO

SD_D1 and SD_CD can be used as GPIO, when not usring SDIO
=========================================================

With GPIOS_1 and GPIOS_4 we refer to serial GPIO to control LEDs (pin 9 (SD_D1) and 11 (SD_CD) of the QFN128 RTL8735BDM).

**Answer**

GPIOS_1 and GPIOS_4: If you are not using SDIO, these pins are free to use as GPIO.

Refer to the following test code.

.. code-block:: c++

    #include "gpio_api.h"
    #include "us_ticker_api.h"
    #include "wait_api.h"

    #define GPIO_LED_S1       PS_1
    #define GPIO_LED_S4       PS_4

    int main(void)
    {
        gpio_t gpio_led_s1;
        gpio_t gpio_led_s4;

        dbg_printf("\r\n   GPIO DEMO Michael  \r\n");

        // Init LED control pin
        gpio_init(&gpio_led_s1, GPIO_LED_S1);
        gpio_dir(&gpio_led_s1, PIN_OUTPUT);        // Direction: Output
        gpio_mode(&gpio_led_s1, PullNone);         // No pull

        gpio_init(&gpio_led_s4, GPIO_LED_S4);
        gpio_dir(&gpio_led_s4, PIN_OUTPUT);        // Direction: Output
        gpio_mode(&gpio_led_s4, PullNone);         // No pull

        while (1) {
            if (gpio_read(&gpio_led_s1)) {
                // turn off LED
                gpio_write(&gpio_led_s1, 0);
            } else {
                // turn on LED
                gpio_write(&gpio_led_s1, 1);
            }

            if (gpio_read(&gpio_led_s4)) {
                // turn off LED
                gpio_write(&gpio_led_s4, 0);
            } else {
                // turn on LED
                gpio_write(&gpio_led_s4, 1);
            }

            wait_ms(2000);
        }
    }
