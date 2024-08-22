Materials
=========

-  AmebaPro2 [AMB82 MINI] x 1

-  SD card x 1

Example 
========

Introduction
------------

In this example, we will use the Ameba Pro2 development board to record
video and audio data from the on-board camera sensor (JX-F37P) and audio
codec to an MP4 file on the SD card.

The following examples shows different use cases for MP4 recording.

1. AudioOnly

2. VideoOnly

3. SingleVideoWithAudio

4. DoubleVideoWithAudio

Procedure
---------

Open one of the RecordMP4 examples in “File” -> “Examples” ->
“AmebaMultimedia”-> “RecordMP4”.

|image1|

Compile the code and upload it to Ameba. After pressing the Reset
button, the Ameba Pro 2 board will start recording MP4 to SD card.

|Graphical user interface, text, application, email Description
automatically generated|

After the recording duration has passed, the MP4 file will stop
recording.

|Graphical user interface, text, application Description automatically
generated|

Disconnect power from the Ameba Pro 2 board, remove the SD card and
connect it to a computer to view the contents. Depending on the compiled
example, there will be either one or two MP4 videos. Using VLC to open
the MP4 file, detailed information about the MP4 files can be obtained
in “Tools” -> “Codec Information”.

+-----------------------------------+-----------------------------------+
| Example                           | MP4 file details                  |
+===================================+===================================+
| RecordMP4AudioOnly                | Single 30 second MP4 file with    |
|                                   | audio only                        |
|                                   |                                   |
|                                   | |image2|                          |
+-----------------------------------+-----------------------------------+
| RecordMP4VideoOnly                | Single 30 second MP4 file with    |
|                                   | video only                        |
|                                   |                                   |
|                                   | |image3|                          |
+-----------------------------------+-----------------------------------+
| RecordMP4SingleVideoWithAudio     | Single 30 second MP4 file with    |
|                                   | audio and video                   |
|                                   |                                   |
|                                   | |image4|                          |
+-----------------------------------+-----------------------------------+
| RecordMP4DoubleVideoWithAudio     | One 30 second and one 15 second   |
|                                   | MP4 file                          |
|                                   |                                   |
|                                   | Both files with audio and video   |
|                                   |                                   |
|                                   | |image5|                          |
|                                   |                                   |
|                                   | |image6|                          |
+-----------------------------------+-----------------------------------+

There are 4 additional examples that has been integrated with NTPClient.
These examples complement the original examples, by being able to set
the last modified time of the recordings to the actual time and date
automatically.

They are:

1) AudioOnlyWithNTPClient

2) VideoOnlyWithNTPClient

3) SingleVideoWithAudioAndNTPClient

4) DoubleVideoWithAudioAndNTPClient

Code Reference

NA

.. |image1| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image01.png
   :width: 4.09736in
   :height: 4.43802in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image02.png
   :width: 3.86458in
   :height: 2.51716in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image03.png
   :width: 3.80208in
   :height: 2.47645in
.. |image2| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image04.png
   :width: 2.15625in
   :height: 1.92375in
.. |image3| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image05.png
   :width: 2.11458in
   :height: 1.88658in
.. |image4| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image06.png
   :width: 2.36458in
   :height: 2.10962in
.. |image5| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image07.png
   :width: 2.72041in
   :height: 2.42708in
.. |image6| image:: ../../_static/Example_Guides/Multimedia_-_MP4_Recording/Multimedia_-_MP4_Recording_images/image08.png
   :width: 2.66667in
   :height: 2.37913in
