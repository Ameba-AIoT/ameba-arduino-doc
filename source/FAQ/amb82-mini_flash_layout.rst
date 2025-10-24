.. tags:: layout, flash, nor-flash, amb82-mini

What is the flash layout of amb82-mini and the size for user to use?
====================================================================

**Answer**

For amb82-mini, the hardware is 16M nor-flash. And the `NOR Flash Layout overview <https://ameba-doc-rtos-pro2-sdk.readthedocs-hosted.com/en/latest/application_note/08_FLASHLAYOUT.html#nor-flash-layout-overview>`_
For Arduino SDK, there are flash reserved for user to use under following conditions.
- Without OTA, refer to `amebapro2_partitiontable.json <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/ameba_pro2_tools_windows/misc/sys_img/amebapro2_partitiontable.json>`_ OTA firmware is limited as 64KB and NN model as 10MB. User-reserved flash are from 0xFC0000 to 0x1000000 that is 256KB.
- With OTA, refer to `amebapro2_partitiontable_OTA.json <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/ameba_pro2_tools_windows/misc/sys_img/amebapro2_partitiontable_OTA.json>`_ OTA firmware is limited as 4MB and NN model as 5MB. User-reserved flash are from 0xF00000 to 0x1000000 that is 1023KB.
