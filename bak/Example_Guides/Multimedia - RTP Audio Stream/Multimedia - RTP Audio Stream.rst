Materials
=========

-  AmebaPro2 [AMB82 MINI] x1

-  3.5mm TRS/TRRS breakout x 1 (e.g., Adafruit 2791 / Sparkfun 11570)

Example 
========

Introduction
------------

This example shows how to stream audio from a computer to the Ameba Pro
2 board.

Procedure
---------

Connect the audio jack to the Ameba board as shown in the diagram.

|image1|

Open the example in “File” -> “Examples” -> “AmebaMultimedia” -> “Audio”
-> “RTPAudioStream”.

|image2|

In the highlighted code snippet, fill in the “ssid” with your WiFi
network SSID and “pass” with the network password.

|image3|

Compile the code and upload it to Ameba.

After pressing the Reset button, wait for the Ameba Pro 2 board to
connect to the WiFi network.

On a computer connected to the same WiFi network, open VLC media player,
and go to “Media” -> “Stream”.

|Graphical user interface, application Description automatically
generated|

Using the add button, add the audio file you would like to stream to the
Ameba board, and click the stream button.

|Graphical user interface, text, application, email Description
automatically generated|

In the new window that appears, click on next to move to the destination
setup page. In the dropdown menu, select “RTP Audio/Video Profile” and
click on the add button next to it.

|image4|

In the new tab that appears, enter the IP address of the Ameba Pro 2
board in the address field. Ensure that the base port uses the default
value of 5004. Click on the next button.

|image5|

For transcoding options, ensure that “Activate Transcoding” is checked.
If you already have a profile created for the Ameba Pro 2, select the
existing profile, and skip the next section showing how to create a
profile. Otherwise, click on the highlighted button to create a new
profile for the Ameba Pro 2 Board.

|Graphical user interface, text, application, Word Description
automatically generated|

In the new window that appears, give a suitable name for the new
transcoding profile. Ensure that “RAW” is selected in the
“Encapsulation” tab.

|image6|

Ensure that “Video” and “Subtitle” are disabled in the “Video codec” and
“Subtitles” tabs.

|image7|

|Graphical user interface, text, application Description automatically
generated|

In the “Audio codec” tab, ensure that “Audio” is enabled. Select “MPEG 4
Audio (AAC)” for the codec, and 1 for the number of channels. For the
sample rate, this value should be the same as the AudioSetting
configuration for the Ameba Pro 2, which is 8000 Hz by default for this
example. Click on the create button, ensure that the new profile is
selected, and click on the next button.

|image8|

In the next window, click on the stream button, and VLC will begin
streaming the audio file to Ameba Pro 2 using RTP.

Plug in a pair of wired earbuds into the audio jack, and you should hear
the audio streamed from the computer. You can use the buttons in VLC to
control the playback.

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image01.png
   :width: 3.47631in
   :height: 3.62353in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image02.png
   :width: 4.59797in
   :height: 4.98198in
.. |image3| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image03.png
   :width: 4.53403in
   :height: 5.41565in
.. |Graphical user interface, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image04.png
   :width: 2.53125in
   :height: 2.58709in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image05.png
   :width: 4.67708in
   :height: 3.45045in
.. |image4| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image06.png
   :width: 4.70833in
   :height: 3.08916in
.. |image5| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image07.png
   :width: 5.36627in
   :height: 3.52083in
.. |Graphical user interface, text, application, Word Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image08.png
   :width: 5.62029in
   :height: 3.6875in
.. |image6| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image09.png
   :width: 6.10417in
   :height: 5.23958in
.. |image7| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image10.png
   :width: 4.04113in
   :height: 3.46875in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image11.png
   :width: 4.59936in
   :height: 3.94792in
.. |image8| image:: ../../_static/Example_Guides/Multimedia_-_RTP_Audio_Stream/Multimedia_-_RTP_Audio_Stream_images/image12.png
   :width: 4.56296in
   :height: 3.91667in
