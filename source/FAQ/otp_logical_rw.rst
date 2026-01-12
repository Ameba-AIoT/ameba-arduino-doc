.. tags:: otp, log system, amb82-mini

How do I disable the log UART by writing OTP?
=============================================

**Answer**

You can program the **logical OTP** to control the ROM log messages:

- To **disable** log UART:

  .. code-block:: c

     int otp_rom_log_message_disable(void);

- To **enable** log UART:

  .. code-block:: c

     int otp_rom_log_message_enable(void);

Make sure to include the header file:

.. code-block:: c

   #include "otp_api_ext.h"

**Notes & cautions**

- OTP has a **limited number of writes**. Avoid repeatedly toggling between enable and disable.
- It is **recommended to call these functions only after the firmware is finalized** and no further changes will be made.
