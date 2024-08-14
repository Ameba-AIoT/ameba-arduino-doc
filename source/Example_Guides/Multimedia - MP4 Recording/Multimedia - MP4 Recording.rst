Materials

AmebaPro2 [AMB82 MINI] x 1

SD card x 1

Example

Introduction

In this example, we will use the Ameba Pro2 development board to record
video and audio data from the on-board camera sensor (JX-F37P) and audio
codec to an MP4 file on the SD card.

The following examples shows different use cases for MP4 recording.

AudioOnly

VideoOnly

SingleVideoWithAudio

DoubleVideoWithAudio

Procedure

Open one of the RecordMP4 examples in “File” -> “Examples” ->
“AmebaMultimedia”-> “RecordMP4”.

Compile the code and upload it to Ameba. After pressing the Reset
button, the Ameba Pro 2 board will start recording MP4 to SD card.

After the recording duration has passed, the MP4 file will stop
recording.

Disconnect power from the Ameba Pro 2 board, remove the SD card and
connect it to a computer to view the contents. Depending on the compiled
example, there will be either one or two MP4 videos. Using VLC to open
the MP4 file, detailed information about the MP4 files can be obtained
in “Tools” -> “Codec Information”.

There are 4 additional examples that has been integrated with NTPClient.
These examples complement the original examples, by being able to set
the last modified time of the recordings to the actual time and date
automatically.

They are:

AudioOnlyWithNTPClient

VideoOnlyWithNTPClient

SingleVideoWithAudioAndNTPClient

DoubleVideoWithAudioAndNTPClient

Code Reference

NA

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.png| |image08.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image03.png
.. |image04.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image04.png
.. |image05.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image05.png
.. |image06.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image06.png
.. |image07.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image07.png
.. |image08.png| image:: ../../../_static/_Example_Guides/_Multimedia%20-%20MP4%20Recording/image08.png
