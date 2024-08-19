Materials
=========

-  AmebaPro2 [AMB82 MINI] x1

-  3.5mm TRS/TRRS breakout x 1 (e.g., Adafruit 2791 /)

-  Adafruit PDM Microphone Breakout x 1 [Optional]

-  Potentiometer x 2

Example 
========

Introduction
------------

In this example, we will use the Ameba Pro2 board to playback audio
recorded by the onboard analogue microphone or an external PDM (Pulse
Density Modulation) microphone.

The following examples are relevant to this guide.

1. LoopbackTest

2. AudioVolumeAdjust

Procedure
---------

Connect the audio jack and potentiometers to the Ameba board as shown in
the diagram.

|Diagram Description automatically generated|

Alternatively, connect the audio jack, potentiometers, and PDM
Microphone as shown in the diagram below if you would like to use a
digital microphone.

|image1|

Open one of the Audio examples in “File” -> “Examples” ->
“AmebaMultimedia” -> “Audio”.

|image2|

Compile the code and upload it to Ameba.

Plug in a pair of wired earbuds into the audio jack. After pressing the
Reset button, you should be able to hear sounds picked up by the onboard
microphone replayed through the earbuds.

In the “AudioVolumeAdjust” example, turning the potentiometers will
adjust either the input volume of the microphone or the output volume of
the audio jack.

.. |Diagram Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Basic/Multimedia_-_Audio_Basic_images/image01.png
   :width: 4.55208in
   :height: 3.64782in
.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Basic/Multimedia_-_Audio_Basic_images/image02.png
   :width: 6.26042in
   :height: 3.65625in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Basic/Multimedia_-_Audio_Basic_images/image03.png
   :width: 4.53145in
   :height: 4.90991in
