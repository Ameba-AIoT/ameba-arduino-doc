Materials

AmebaPro2 [AMB82 MINI] x 1

MicroSD card

Example

Procedure

Using a card reader, connect the SD card to a computer and copy the HTML
file into the SD card. Take note to place the file in the root directory
and not in any folder. The HTML sample file can be downloaded at
https://github.com/ambiot/ambpro2_arduino/tree/dev/Ameba_misc/Example_Samples/Web_test.html.

Then insert the MicroSD card into the SD card slot of the AMB82 MINI
board.

Open the example, “Files” -> “Examples” -> “AmebaFileSystem” ->
“ReadHTMLFile”

In the sample code, modify “ssid” to the WiFi SSID to be connected to
and “pass” to the network password.

Upload the code and press the reset button on the board once the upload
is finished.

Wait for the board to connect to WiFi. When the connection is
established, the message “To see this page in action, open a browser to
http://xxx.xxx.xxx.xxx” will be printed in the serial monitor.

Next, on a device connected to the same network, use a web browser to
open the address provided in the serial monitor. The following web page
will be displayed.

|image01.png| |image02.png| |image03.png| |image04.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Read%20and%20display%20HTML%20file%20from%20SD%20card/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Read%20and%20display%20HTML%20file%20from%20SD%20card/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Read%20and%20display%20HTML%20file%20from%20SD%20card/image03.png
.. |image04.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Read%20and%20display%20HTML%20file%20from%20SD%20card/image04.png
