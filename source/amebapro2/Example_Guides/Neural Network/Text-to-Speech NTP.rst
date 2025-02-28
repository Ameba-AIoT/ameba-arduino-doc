Text-to-Speech NTP
==================

.. contents::
  :local:
  :depth: 2

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

Example 
-------

In this example, we will be using Ameba Pro2 development board to demonstrate audio time and date report using NTP Client and Google Translate API.

Open Text-to-Speech NTP example in "File" -> "Examples" -> "AmebaNN" -> "MultimediaAI" -> "Text-to-SpeechNTP".

|image01|

In the highlighted code snippet, fill in the "ssid" with your WiFi network SSID and "pass" with the network password.

|image02|

The default ``message`` is set for date reporting. You may modify the ``message`` according to NTP Client API for time reporting.

|image03|

Compile and upload the code to AMB82-mini. Please refer to the table below for language codes.

**Language Codes**

+--------------------------------------+---------------+
| **Language**                         | **Code**      |
+======================================+===============+
| English (US)                         | en            |
+--------------------------------------+---------------+
| English (UK)                         | en-GB         |
+--------------------------------------+---------------+
| Chinese (Taiwan)                     | zh-TW         |
+--------------------------------------+---------------+
| Chinese (PRC)                        | zh-CN         |
+--------------------------------------+---------------+
| Japanese                             | ja            |
+--------------------------------------+---------------+
| Korean                               | ko            |
+--------------------------------------+---------------+
| French                               | fr            |
+--------------------------------------+---------------+
| German                               | de            |
+--------------------------------------+---------------+
| Italian                              | it            |
+--------------------------------------+---------------+
| Russian                              | ru            |
+--------------------------------------+---------------+
| Spanish                              | es            |
+--------------------------------------+---------------+

Resources
---------

| Google Language Codes
| https://developers.google.com/admin-sdk/directory/v1/languages

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Text-to-Speech_NTP/image01.png
   :width:  826 px
   :height:  946 px

.. |image02| image:: ../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Text-to-Speech_NTP/image02.png
   :width:  839 px
   :height:  646 px

.. |image03| image:: ../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_Text-to-Speech_NTP/image03.png
   :width:  729 px
   :height:  344 px

.. |image_ameba_iot| image:: ../../../_static/ameba_iot_logo.png
   :scale: 40%

.. |image_3rd_party| image:: ../../../_static/3rd_party_logo.png
   :scale: 10%

