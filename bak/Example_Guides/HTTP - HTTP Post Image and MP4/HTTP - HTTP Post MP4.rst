Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  PushButton x1

-  220 ohm resistor x1

Example

These examples illustrate how to send HTTP Post request of MP4 audio
file to a HTTP server.

This guide will be relevant to 2 examples:

1) HTTP_Post_MP4_Whisper_Server

2) RecordMP4_HTTP_Post_Whisper_Server

The difference between these 2 examples is that for
HTTP_Post_MP4_Whisper_Server.ino, one is expected to have an MP4 file
already saved inside the SD card. Whereas for the
RecordMP4_HTTP_Post_Whisper_Server.ino, it is not necessary to have a
MP4 file inside the SD card.

This is the block diagram for the example flow.

|image1|

Connect the pushbutton and resistor to AMB82 Mini as shown below.

|image2|

Open “File”-> “Examples” -> “AmebaHTTP” ->
“HTTP_Post_MP4_Whisper_Server” OR “RecordMP4_HTTP_Post_Whisper_Server”.

|image3|

Compile and run the code.

Set up the http server by locating the python script called
“whisper_llm_server.py” in src folder. Go to command prompt and go to
the src folder and execute this command: python3 whisper_llm_server.py.
Follow the readme in the python script.

Press the push button for 2s to trigger the recording. Speak into the
microphone to ask the AI. This should be the expected output on the
terminal that was running the python script. Please note that if you are
to use a more powerful model such as MediaTek 7B model, you will need a
PC with a powerful GPU to test. Purely CPU will not be able to run that
model.

Please note that this server can only be run on **Linux OS**. Mac OS and
Windows have not been supported yet.

|image4|

.. |image1| image:: ../../_static/Example_Guides/HTTP_-_HTTP_Post_MP4/HTTP_-_HTTP_Post_MP4_images/image01.png
   :width: 6.26806in
   :height: 2.21319in
.. |image2| image:: ../../_static/Example_Guides/HTTP_-_HTTP_Post_MP4/HTTP_-_HTTP_Post_MP4_images/image02.png
   :width: 4.41458in
   :height: 3.58264in
.. |image3| image:: ../../_static/Example_Guides/HTTP_-_HTTP_Post_MP4/HTTP_-_HTTP_Post_MP4_images/image03.png
   :width: 5.55972in
   :height: 3.47361in
.. |image4| image:: ../../_static/Example_Guides/HTTP_-_HTTP_Post_MP4/HTTP_-_HTTP_Post_MP4_images/image04.png
   :width: 6.26806in
   :height: 1.26736in
