Materials

AmebaPro2 [AMB82 MINI] x 1

Example

AmebaPro2 ISP can support compressed (H264 / H265 / JPG) and
uncompressed (NV16 / NV12) image through UVC (wired transmission), and
user can check video on pc with PC applications (eg. Potplayer).

Connect the “Micro USB” into Arduino IDE device. Open the sample code in
“File” -> “Examples” -> “AmebaUSB” -> “UVC_Device”. Compile and upload
to Ameba, then press the reset button. Connect the “USB OTG” via
micro-USB cable to the target device such as PC, then use the Ameba
device as a USB cam.

Review the USB cam driver as following picture.

It is optional to open the Serial Monitor, review the processing log. At
this stage “Micro USB” can be disconnected.

|image01.png| |image02.png| |image03.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_USB%20-%20UVC%20Device/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_USB%20-%20UVC%20Device/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_USB%20-%20UVC%20Device/image03.png
