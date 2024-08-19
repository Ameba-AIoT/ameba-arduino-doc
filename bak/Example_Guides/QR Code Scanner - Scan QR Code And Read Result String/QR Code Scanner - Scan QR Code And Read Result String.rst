Materials

-  AmebaPro2 [AMB82 MINI] x 1

Example

**Introduction**

This example will demonstrate how to retrieve the result string and
length when QR code is placed in front of the camera of AMB82-Mini.

**Procedure**

Open the QR Code Scanner example “File” -> “Examples” -> “AmebaQR” ->
“QRCodeScanner”

|A screenshot of a computer Description automatically generated|

You can start the scanner by calling the method StartScanning(). Please
note that this should be in the setup() and not in the loop().

You can retrieve the result string and result length by calling the
method GetResultString() and GetResultLength().

Please note that users are to modify their conditional checks in the
loop(). This is just an illustration on how to get the result string and
length. Currently, 3\ :sup:`rd` successful scan onwards will be able to
retrieve the result string and length reliably. Strongly encourage more
people to try out and improve the performance of this example. This
example may not be the most optimised version.

To optimise the performance for your application, one can modify the
qr_code_scanner_config_map in qrcode_drv.c as shown in the picture
below. For now, there is no API exposed on the Arduino level, but this
can be done in future if there is a huge demand for it.

|A screenshot of a computer program Description automatically generated|

To test this example, compile and run the example. Place a QR code in
from the camera of AMB82-Mini. If there is no QR code detected, you will
be able to see this in Serial Monitor.

|image1|

If QR Code is detected after 3 successful times, you will observe this
log on the Serial Monitor.

|A screen shot of a computer code Description automatically generated|

.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String_images/image01.png
   :width: 6.26806in
   :height: 5.69375in
.. |A screenshot of a computer program Description automatically generated| image:: ../../_static/Example_Guides/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String_images/image02.png
   :width: 5.21875in
   :height: 1.51042in
.. |image1| image:: ../../_static/Example_Guides/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String_images/image03.png
   :width: 6.26806in
   :height: 1.41389in
.. |A screen shot of a computer code Description automatically generated| image:: ../../_static/Example_Guides/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String/QR_Code_Scanner_-_Scan_QR_Code_And_Read_Result_String_images/image04.png
   :width: 6.26806in
   :height: 1.13889in
