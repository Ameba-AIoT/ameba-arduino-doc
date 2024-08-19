Materials
=========

-  AmebaPro2 [AMB82 MINI] x 1

Example
=======

AmebaPro2 ISP can support compressed (H264 / H265 / JPG) and
uncompressed (NV16 / NV12) image through UVC (wired transmission), and
user can check video on pc with PC applications (eg. Potplayer).

Connect the “Micro USB” into Arduino IDE device. Open the sample code in
“File” -> “Examples” -> “AmebaUSB” -> “UVC_Device”. Compile and upload
to Ameba, then press the reset button. Connect the “USB OTG” via
micro-USB cable to the target device such as PC, then use the Ameba
device as a USB cam.

|A black circuit board with blue arrows Description automatically
generated|

Review the USB cam driver as following picture.

|A screenshot of a computer Description automatically generated|

It is optional to open the Serial Monitor, review the processing log. At
this stage “Micro USB” can be disconnected.

|image1|

.. |A black circuit board with blue arrows Description automatically generated| image:: ../../_static/Example_Guides/USB_-_UVC_Device/USB_-_UVC_Device_images/image01.png
   :width: 3.3209in
   :height: 3.24437in
.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/USB_-_UVC_Device/USB_-_UVC_Device_images/image02.png
   :width: 3.76861in
   :height: 4.19629in
.. |image1| image:: ../../_static/Example_Guides/USB_-_UVC_Device/USB_-_UVC_Device_images/image03.png
   :width: 4.15289in
   :height: 3.8115in
