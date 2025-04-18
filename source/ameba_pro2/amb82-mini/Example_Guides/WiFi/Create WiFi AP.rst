Create WiFi AP
==============

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

Example
-------

Introduction
~~~~~~~~~~~~

In AP mode, Ameba can accept at most 3 station connections, and can be
set to open mode or WPA2 mode.

In this example, we turn on the AP mode of Ameba and connect station to
Ameba.

Procedure
~~~~~~~~~

Open example, "File" -> "Examples" -> "WiFi" -> "CreateWiFiAP"

|image01|

In the highlighted code snippet, fill in your SSID, PASSWORD and
CHANNEL.

If you prefer to enter your SSID & password in the Serial monitor
while the program is running, uncomment ``#define MANUAL_INPUT`` at the top
of the file.

|image02|

Note: If you enabled ``MANUAL_INPUT``, after uploading the sample
code and pressing the reset button on Ameba, input your SSID in the
Serial monitor and press enter. Next, input your password and press
enter. AP mode should start after that.

|image03|

The code highlighted is the API we used to turn on the AP mode in
security mode.

If you want to turn on the AP mode in open mode, please modify the code
to ``status = WiFi.apbegin(ssid, channel);``

Then upload the sample code and press reset, and you can see related
information shown in serial monitor.

|image04|

In the figure below, we show the messages shown in serial monitor when
two stations connect to Ameba AP in open mode:

|image05|

In the figure below, we show the messages shown in serial monitor when a
station connects to Ameba AP in security mode:

|image06|

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/Create_WiFi_AP/image01.png
   :width: 822 px
   :height: 886 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/Create_WiFi_AP/image02.png
   :width: 817 px
   :height: 882 px
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/Create_WiFi_AP/image03.png
   :width: 826 px
   :height: 997 px
   :scale: 80%
.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/Create_WiFi_AP/image04.png
   :width: 663 px
   :height: 775 px
.. |image05| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/Create_WiFi_AP/image05.png
   :width: 478 px
   :height: 560 px
.. |image06| image:: ../../../../_static/amebapro2/Example_Guides/WiFi/Create_WiFi_AP/image06.png
   :width: 561 px
   :height: 712 px
