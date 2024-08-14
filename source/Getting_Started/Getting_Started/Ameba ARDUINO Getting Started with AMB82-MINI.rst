Ameba ARDUINO: Getting Started with AMB82 MINI (RTL8735B)

Introduction

Ameba is an easy-to-program platform for developing all kinds of IoT
applications. AMB82 MINI is equipped with various peripheral interfaces,
including WiFi, BLE, GPIO INT, I2C, UART, SPI, PWM, ADC. Through these
interfaces, AMB82 MINI can connect with electronic components such as
LED, switches, manometer, hygrometer, PM2.5 dust sensors, …etc. Besides,
AMB82 MINI has 3 key features, Audio codec, Video codec and NN (build in
NPU for AIoT). The collected data can be uploaded via WiFi and be
utilized by applications on smart devices to realize IoT implementation.

AMB82 mini is connected to the open-source world by one of the widest
development environments, Arduino. For more information, HDK, SDK, API
documents, Example Guides and so on, refer to the following Ameba
Arduino SDK page https://www.amebaiot.com/en/ameba-arduino-summary/ .

AMB82 MINI uses Micro USB to supply power, which is common in many smart
devices. Please refer to the following figure and table for the pin
diagram and functions.

Set up developing environment

Step 1. OS environment

AMB82 MINI board currently supports Windows OS 64-bits (Windows 10 and
above), Linux OS (Ubuntu22 and above) and MacOS (Intel and Apple
Silicon). To have the best experiences, please use the latest version of
OS.

For any Linux OS (Ubuntu) related issues, refer to
https://forum.amebaiot.com/t/ubuntu-linux-environment/2259.

For any macOS related issues, refer to
https://forum.amebaiot.com/t/macos-environment/2260.

Step 2. Installing the Driver

First, connect AMB82 MINI to the computer via Micro USB:

If this is the first time connects board to computer, the USB driver for
board will be automatic installed. If you have driver issue of connect
board to computer please go
to http://www.wch-ic.com/downloads/CH341SER_ZIP.html for USB driver.
Check the COM port number in Device Manager of computer:

Step 3. Set up Arduino IDE

From version 1.6.5, Arduino IDE supports third-party hardware.
Therefore, we can use Arduino IDE to develop applications, and the
Arduino basic examples are supported. Arduino IDE can be downloaded in
the Arduino website: https://www.arduino.cc/en/Main/Software

When the installation is finished, open Arduino IDE. To set up correctly
in Arduino IDE, go to “File” -> “Preferences”

And paste the following URL into “Additional Boards Manager URLs” field:
https://github.com/ambiot/ambpro2_arduino/raw/main/Arduino_package/package_realtek.com_amebapro2_index.json

Next, go to “Tools” -> “Board” -> “Boards Manager”:

The “Boards Manager” requires about 10~20 seconds to refresh all
hardware files (if the network is in bad condition, it may take longer).
Every time the new hardware is connected, we need to reopen the Board
Manager. Find “Realtek Ameba Boards” in the list, click “Install”, then
the Arduino IDE starts to download required files.

After the installation tool running successfully, you may open Arduino
IDE and proceed to “tools” -> “Board“ -> “Boards Manager…”. Try to find
“Realtek Ameba Boards” in the list, click “Install”, then the Arduino
IDE starts to download required files.

Finally, we select board in “tools” -> “Board” -> “AmebaPro2 ARM
(32-bits) Boards” -> “AMB82-MINI”

Try the First Example

Step 1. Selection Ameba Modes

There are many different Modes for user to select for different settings
of compile and upload. Please refer to the following picture and table.

Step 2. Compile

Arduino IDE provides many built-in examples, which can be compiled,
uploaded, and run directly on the boards. Here, we take the “Blink”
example as the first try. Open “File” -> “Examples” -> “01.Basics” ->
“Blink”:

Arduino IDE opens a new window with the complete sample code.

Next, we compile the sample code directly; click “Sketch” ->
“Verify/Compile”

Arduino IDE prints the compiling messages in the bottom area of the IDE
window. When the compilation is finished, you will get the message as
following.

Afterwards, we will upload the compiled code to board.

Step 3. Upload

Please make sure board is connected to computer, then click “Sketch” ->
“Upload”.

The Arduino IDE will compile first then upload. Users are required to
enter the upload mode of the board. To enter upload mode, first press
and hold the UART_DOWNLOAD button, then press and release the RESET
button, lastly release the UART_DOWNLOAD button.

Additionally, if the board has the hardware updates and enabled “Auto
Flash Mode”, please ignore above instruction.

It is optional for users to check if the board entered the upload mode.
Open serial monitor/terminal and check the following information,.

When upload completed, the “Done uploading” message is printed.

Step 2. Run the Blink example

In each example, Arduino not only provides sample code, but also
detailed documentation, including wiring diagram, sample code
explanation, technical details, …etc. Please refer the detailed
information of the Blink example:
https://www.arduino.cc/en/Tutorial/Blink

In short, this example makes on-board LED blinks.

Video Tutorials and Demos

YouTube Channel:

AMB82 Mini - Getting Started: https://youtu.be/\_rLiih5RkXY .

AMB82 Mini tutorials list:
https://youtube.com/playlist?list=PLEQfNjOZQRyPnmXCuRqE1f5au2HT4E9CP .

AMB82 Mini - 入門教學: https://youtu.be/-jQDpDFX2ao .

AMB82 Mini 教程 list:
https://youtube.com/playlist?list=PLEQfNjOZQRyOxXFV7X_2fIcnd_J6VBmyM .

BiliBili Channel: https://space.bilibili.com/457777430 .

Useful Links

Ameba Arduino SDK page:
https://www.amebaiot.com/en/ameba-arduino-summary/ .

FAQ: https://forum.amebaiot.com/t/welcome-to-ameba-faq/1748

Forum: https://forum.amebaiot.com/ .

Facebook Group Chinese: https://www.facebook.com/groups/AmebaIoT .

Facebook Group English: https://www.facebook.com/groups/amebaioten .

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.png| |image08.png| |image09.png| |image10.png|
|image11.png| |image12.png| |image13.png| |image14.png|

.. |image01.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image01.png
.. |image02.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image02.png
.. |image03.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image03.png
.. |image04.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image04.png
.. |image05.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image05.png
.. |image06.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image06.png
.. |image07.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image07.png
.. |image08.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image08.png
.. |image09.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image09.png
.. |image10.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image10.png
.. |image11.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image11.png
.. |image12.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image12.png
.. |image13.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image13.png
.. |image14.png| image:: ../../../_static/_Getting_Started/_Getting_Started/image14.png
