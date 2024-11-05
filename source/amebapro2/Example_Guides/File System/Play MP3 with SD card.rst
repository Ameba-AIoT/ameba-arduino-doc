Play MP3 with SD card
=====================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  MicroSD card

- 3.5mm TRS/TRRS breakout x 1 (e.g., Adafruit 2791 / Sparkfun 11570)

Example
-------

In this example, we will use the Ameba Pro2 board to play MP3 audio from SD card.

Procedure
~~~~~~~~~

Using a card reader, connect the SD card to a computer and copy the MP3 file into the SD card. Take note to place the MP3 file in the root directory
and not in any folder.

Connect the audio jack to the Ameba board as shown in the diagram.

|image01|

|image02|

Insert the MicroSD card into the SD card slot of the AMB82 MINI board.

Open the example in “File” -> “Examples” -> “AmebaFileSystem” -> “SDCardPlayMP3”.

|image03|

In the highlighted code snippet, fill in the MP3 file name which was store on the MicroSD card.

|image04|

Plug in a pair of wired earbuds or a wired speaker into the audio jack. Upload the code and press the reset button on the board, now you can hear the MP3 audio through the earbuds. 

.. |image01| image:: ../../../_static/amebapro2/Example_Guides/File_System/Play_MP3_with_SD_card/image01.png
   :width:  900 px
   :height: 550 px

.. |image02| image:: ../../../_static/amebapro2/Example_Guides/File_System/Play_MP3_with_SD_card/image02.png
   :width:  586 px
   :height: 610 px

.. |image03| image:: ../../../_static/amebapro2/Example_Guides/File_System/Play_MP3_with_SD_card/image03.png
   :width:  1000 px
   :height:  550 px

.. |image04| image:: ../../../_static/amebapro2/Example_Guides/File_System/Play_MP3_with_SD_card/image04.png
   :width:  1000 px
   :height:  550 px
   