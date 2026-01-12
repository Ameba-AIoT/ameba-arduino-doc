Ameba Over-the-Air Firmware Update
==================================

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1
- Set up of Web UI in a PC

Example
-------

In this example, we use a web UI to upload firmware to one or more AMB82 Mini.

For the instructions to set up web UI for AmebaPro2 OTA: Web UI, please click into the link below and perform the steps as shown in the ``README.md``. [https://github.com/Ameba-AioT/ameba-OTA-UI]

If Ameba OTA Web UI is set up successfully in your PC, you will see the webpage on [http://localhost:3000/], figure below shows the rendering of webpage with no device connected:

|image01|

To begin, open the OTA example in Arduino IDE. "File" -> "Examples" -> "AmebaOTA" -> "OTA".

|image02|

Before compiling and upload the example, please complete the following steps:

1. Set NN Model Load From SD Card. "Tools" -> "NN Model Load From" -> "SD Card"

|image03|

2.	Enable the OTA mode. "Tools" -> "OTA Mode" -> "Enable"

|image04|

3.	Modify the SSID and password according to your AP. Your PC and AMB82 Mini should be connecting to the same local area network.

|image05|

4. Modify the port number and IP address according to your HTTP server.

|image06|

Now, compile and upload this example into each and every board that you have. It can be one board or multiple boards (we will be using two AMB82 Mini boards in this example guide).

This set up must be done at least once to allow the OTA thread API to be called for the first time. For subsequent firmware updates, as long as ``OTA.h`` is included and ``start_ota_threads`` API is called in the setup function, you do not need to re-upload the code manually.

Once uploaded, press reset button and get the IP address of the individual AMB82 Mini on serial monitor.

Board 1 IP address: 192.168.3.26

|image07|

Board 2 IP address: 192.168.3.65

|image08|

Then, go to Ameba OTA Web UI [http://localhost:3000/] to view the connected device(s).

|image09|

If you can see the IP address(es) of your AMB82 Mini board(s) on the OTA webpage, it shows that the connection is successful.

For the steps below, you may disconnect AMB82 Mini from your PC and power up the board with any stable 5V DC power source. The overall connection map of this example guide is shown in the figure below.

|image10|

In this tutorial, we will be uploading a NTPClient sketch via OTA.  Open the NTPClient example. "File"-> "Examples" -> "NTPClient" -> "Basic". Include the header file ``OTA.h`` and at the end of setup function, add in the API ``start_OTA_threads`` and define the port number and ip address according to your HTTP server. Also modify the SSID and password according to your AP. Refer to the picture below for the modified NTPClient sketch.

|image11|

Before compiling, remember to set NN Model to load from SD card and enable OTA mode.

Compile the modified NTPClient sketch, DO NOT upload after compilation.

.. note :: Priority matters:  Kindly take note that AMB82 Mini will only boot with the latest compiled firmware.

Once compilation is done, look for ``ota.bin`` file in C:\\Users\\<username>\\AppData\\Local\\Arduino15\\packages\\realtek\\tools\\ameba_pro2_tools\\x.x.x

Upload ``ota.bin`` (or renamed ``ota.bin``) to the webpage UI for OTA transfer to AMB82, as shown in the figure below:

|image12|

Once uploaded, select the device(s) to perform OTA transfer:

|image13|

Click "Start OTA" to begin OTA transfer. You will see the change of OTA state while the firmware is being updated on the board(s), as shown in the figure below.

|image14|

The board will automatically reboot with the OTA transferred firmware (i.e. modified NTPClient in this example) once download progress is completed.

You will see the output generated on serial monitor after reboot.

**Board 1:**

|image15|

**Board 2:**

|image16|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image01.png
   :width:  602 px
   :height:  348 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image02.png
   :width:  601 px
   :height:  533 px
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image03.png
   :width:  654 px
   :height:  661 px
.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image04.png
   :width:  662 px
   :height:  662 px
.. |image05| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image05.png
   :width:  576 px
   :height:  692 px
.. |image06| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image06.png
   :width:  575 px
   :height:  691 px
.. |image07| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image07.png
   :width:  813 px
   :height:  557 px
.. |image08| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image08.png
   :width:  817 px
   :height:  568 px
.. |image09| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image09.png
   :width:  603 px
   :height:  336 px
.. |image10| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image10.png
   :width:  896 px
   :height:  504 px
.. |image11| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image11.png
   :width:  533 px
   :height:  722 px
.. |image12| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image12.png
   :width:  519 px
   :height:  518 px
.. |image13| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image13.png
   :width:  969 px
   :height:  590 px
.. |image14| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image14.png
   :width:  755 px
   :height:  449 px
.. |image15| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image15.png
   :width:  526 px
   :height:  560 px
.. |image16| image:: ../../../../_static/amebapro2/Example_Guides/OTA/Ameba_Over-the-Air_Firmware_Update/image16.png
   :width:  526 px
   :height:  560 px

Code Reference
--------------

**Multithreading:**

Two threads are written in ``start_OTA_threads()`` to ensure successful OTA update.

Thread 1: For the purpose of connectivity check, the OTA state is sent to the server from AMB82 Mini board. Once received, the OTA state of the board will be shown on the Web UI.

.. code-block:: c++

  thread1_id = os_thread_create_arduino(thread1_task, NULL, priority1, stack_size1);

  // First thread is to do keep alive connectivity check (post requests every 5s)
  if (thread1_id) {
      Serial.println("[OTA] Keep-alive connectivity thread created success-fully.");
  } else {
      Serial.println("[OTA] Failed to create keep-alive connectivity thread.");
  }

Thread 2: To listen for the OTA begin signal from server, once ``start_ota`` signal is received, AMB82 Mini will request for the firmware to be downloaded via OTA.

.. code-block:: c++

  thread2_id = os_thread_create_arduino(thread2_task, NULL, priority1, stack_size2);

  // Second thread is to get the signal to start OTA process.
  if (thread2_id) {
      Serial.println("[OTA] Start OTA process thread created successfully.");
  } else {
      Serial.println("[OTA] Failed to create Start OTA process thread.");
  }
