Materials
=========

-  AmebaPro2 [AMB82 MINI] x1

-  3.5mm TRS/TRRS breakout x 1 (e.g., Adafruit 2791 / Sparkfun 11570)

-  Adafruit PDM Microphone Breakout x 1 [Optional]

-  Potentiometer x 1

Example 
========

Introduction
------------

This example shows how to use the Automatic Gain Control (AGC) and Noise
Suppression (NS) audio effects of the Ameba board.

Procedure
---------

Connect the audio jack and potentiometers to the Ameba board as shown in
the diagram.

|image1|

Alternatively, connect the audio jack, potentiometers, and PDM
Microphone as shown in the diagram below if you would like to use a
digital microphone.

|A circuit board with wires Description automatically generated|

Open the example in “File” -> “Examples” -> “AmebaMultimedia” -> “Audio”
-> “AudioEffect”.

|image2|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|Graphical user interface, text, application Description automatically
generated|

Compile the code and upload it to Ameba.

Plug in a pair of wired earbuds into the audio jack. After pressing the
Reset button, you should be able to hear sounds picked up by the onboard
microphone replayed through the earbuds.

In this example, turning the potentiometers will adjust the microphone
sensitivity. Increasing the sensitivity will allow the microphone to
pick up softer sounds but will also increase the background noise.

Modify the highlighted lines of code to enable or disable the NS and AGC
audio effect algorithms on the microphone audio input or the speaker
audio output. Recompile and reupload the code to hear the effects.

|image3|

Code Reference
--------------

Both the NS and AGC algorithm are limited to 8 kHz and 16 kHz sample
rates.

The NS algorithm can reduce the loudness of background noise and is able
to significantly reduce the backgound noise introduced due to increasing
the microphone sensitivity. However, a side effect is that it adds an
echo like effect to the audio. The strength level of the NS effect can
be adjusted with the second argument of configMicNS and configSpkNS,
with 0 being the weakest and 12 being the strongest.

The AGC algorithm can dynamically adjust the gain and sensitivity to
maintain the audio signal at a target loudness level. The target
reference level of the AGC can be adjusted with the second argument of
configMicAGC and configSpkAGC, with 0 representing 0 dBFS the loudest
level, and 30 representing -30 dBFS the softest level.

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Effects/Multimedia_-_Audio_Effects_images/image01.png
   :width: 4.56065in
   :height: 3.62353in
.. |A circuit board with wires Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Effects/Multimedia_-_Audio_Effects_images/image02.png
   :width: 6.26042in
   :height: 3.47917in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Effects/Multimedia_-_Audio_Effects_images/image03.png
   :width: 4.01802in
   :height: 4.35359in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Effects/Multimedia_-_Audio_Effects_images/image04.png
   :width: 4.53125in
   :height: 5.4123in
.. |image3| image:: ../../_static/Example_Guides/Multimedia_-_Audio_Effects/Multimedia_-_Audio_Effects_images/image05.png
   :width: 4.55235in
   :height: 5.4375in
