.. tags:: gpio, voltage, output

Why am I not getting 3.3V from my GPIO pins?
============================================

**Answer**

Kindly verify that:

1. You are measuring the correct GPIO pin,
2. GPIO pin is configured to produce OUTPUT HIGH signal,
3. No large load is connected to any of the GPIO pin,
4. GPIO pin is not configured to output PWM wave,
5. GPIO pin is not set to push-pull HIGH internally,
6. Your multimeter is set to correct range for DC voltage measurement (ensure that you are in DC voltage measurement not BATT mode).

If possible, measure with an oscilloscope for a more accurate and reliable reading.
