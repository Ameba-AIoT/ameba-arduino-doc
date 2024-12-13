Preparation

-  AMB82-Mini x 1

-  SEGGER debug probe x 1

Example

Using the debugging feature available in the Arduino 2.0 IDE to debug
your board. In this example, we will use SEGGER’s debug probe with
Arduino IDE’s debug interface. Begin by installing the SEGGER debugging
software. This can be found on SEGGER’s official website:
https://www.segger.com/downloads/jlink/.

Before debugging, ensure that the code is optimized for debugging.
Enable it by navigating to Sketch -> Optimize for Debugging.

|image1|

Open the Debug example, “File” -> “Examples” -> “Debugging” ->
“ExampleDebug”

|image2|

Two files will open in the IDE; ExampleDebug.ino and debug_custom.json.
Click on debug_custom.json. Under “serverArgs”, insert the directory
path to Arduino15 folder, as well as the current version number of the
tools folder.

|image3|

Connect the JLink Debug Probe and AMB82 Mini board to the computer.
Refer to the table below for the wiring connection between JLink Debug
Probe and AMB82 Mini board. For more information, please refer to:
https://www.segger.com/products/debug-probes/j-link/technology/interface-description/

+-----------------------------------+-----------------------------------+
| **JLink Debug Probe**             | **AMB82 Mini Board**              |
+===================================+===================================+
| VTref                             | 3.3V                              |
+-----------------------------------+-----------------------------------+
| GND                               | GND                               |
+-----------------------------------+-----------------------------------+
| SWDIO                             | SWDIO                             |
+-----------------------------------+-----------------------------------+
| SWCLK                             | SWCLK                             |
+-----------------------------------+-----------------------------------+

|image4| |image5|

[STRIKEOUT:Note that, VTref (Pin 1) is indicate by the blue/red wire on
the cable depending on the JLink Debug Probe that you are using.]

AMB82 Mini boards have 4 hardware breakpoints. Hardware breakpoints can
be set at the left of the code and are indicated by a red dot shown in
line 42. Setting more than 4 hardware breakpoints will cause debugging
to fail. You will need to stop debugging and reset if this happens.

If 4 hardware breakpoint is not enough, software breakpoint can be used.
Either of the instructions (\__BKPT() or \__asm\_\_("BKPT")) can be used
to add a software breakpoint in the program execution.

|image6|

Upload the code and press the reset button on Ameba once the upload is
finished.

Once uploading is completed, reset the board. Start debugging by
selecting the Debug button. This is located to the right of the upload
button. Arduino will proceed with opening a gdb-server tab in the same
window as the output window if all connections were connected correctly
between JLink and board. This can sometimes take up to 10 seconds to set
up.

|image7|

The line highlighted in yellow indicates which line of code the program
is currently halted at. Debug console will appear to show the debugging
information.

|image8|

To continue running the code after the breakpoint, use any of the
single-stepping functions highlighted in the red box (continue, step
over, step into, step out, restart, stop).

|image9|

.. |image1| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image01.png
   :width: 5.93023in
   :height: 2.54068in
.. |image2| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image02.png
   :width: 5.71875in
   :height: 4.7006in
.. |image3| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image03.png
   :width: 6.25in
   :height: 1.57292in
.. |image4| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image04.png
   :width: 2.02326in
   :height: 2.5703in
.. |image5| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image5.jpeg
   :width: 3.18657in
   :height: 2.39178in
.. |image6| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image06.png
   :width: 6.26389in
   :height: 4.11111in
.. |image7| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image07.png
   :width: 5.74799in
   :height: 3.25in
.. |image8| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image08.png
   :width: 6.25694in
   :height: 3.33333in
.. |image9| image:: ../../_static/Example_Guides/Debugging_-_Using_the_Debug_Interface/Debugging_-_Using_the_Debug_Interface_images/image09.png
   :width: 5.34328in
   :height: 3.96943in
