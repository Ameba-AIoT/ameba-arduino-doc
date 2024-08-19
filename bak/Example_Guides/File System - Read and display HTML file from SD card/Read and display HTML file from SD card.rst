Materials
=========

-  AmebaPro2 [AMB82 MINI] x 1

-  MicroSD card

Example
=======

Procedure
---------

Using a card reader, connect the SD card to a computer and copy the HTML
file into the SD card. Take note to place the file in the root directory
and not in any folder. The HTML sample file can be downloaded at
https://github.com/ambiot/ambpro2_arduino/tree/dev/Ameba_misc/Example_Samples/Web_test.html.

|A screenshot of a computer Description automatically generated|

Then insert the MicroSD card into the SD card slot of the AMB82 MINI
board.

Open the example, “Files” -> “Examples” -> “AmebaFileSystem” ->
“ReadHTMLFile”

In the sample code, modify “ssid” to the WiFi SSID to be connected to
and “pass” to the network password.

|Graphical user interface, text, application, email Description
automatically generated|

Upload the code and press the reset button on the board once the upload
is finished.

Wait for the board to connect to WiFi. When the connection is
established, the message “To see this page in action, open a browser to
http://xxx.xxx.xxx.xxx” will be printed in the serial monitor.

|image1|

Next, on a device connected to the same network, use a web browser to
open the address provided in the serial monitor. The following web page
will be displayed.

|Text Description automatically generated with medium confidence|

.. |A screenshot of a computer Description automatically generated| image:: ../../_static/Example_Guides/File_System_-_Read_and_display_HTML_file_from_SD_card/Read_and_display_HTML_file_from_SD_card_images/image01.png
   :width: 3.77083in
   :height: 2.39092in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/File_System_-_Read_and_display_HTML_file_from_SD_card/Read_and_display_HTML_file_from_SD_card_images/image02.png
   :width: 4.29111in
   :height: 5.11458in
.. |image1| image:: ../../_static/Example_Guides/File_System_-_Read_and_display_HTML_file_from_SD_card/Read_and_display_HTML_file_from_SD_card_images/image03.png
   :width: 5.20833in
   :height: 3.46684in
.. |Text Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/File_System_-_Read_and_display_HTML_file_from_SD_card/Read_and_display_HTML_file_from_SD_card_images/image04.png
   :width: 6.26806in
   :height: 1.9875in
