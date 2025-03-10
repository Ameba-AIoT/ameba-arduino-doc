Simple applications with SD card
================================

.. contents::
  :local:
  :depth: 2

Materials
---------

-  `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`_ x 1

-  MicroSD card

Example
-------

Procedure
~~~~~~~~~

Insert a MicroSD card into the SD card slot of the AMB82 MINI board.

Example 01 CreateFolder
~~~~~~~~~~~~~~~~~~~~~~~

Open the example, "Files" -> "Examples" -> "AmebaFileSystem" ->
"CreateFolder".

|image01|

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first creates a folder named "testdir", a text file
named "test.txt" is next created, and the text "hello world!" is saved
into the file. After that, the contents of the file are retrieved and
printed to the serial monitor.

|image02|

Using a card reader, connect the SD card to a computer, open the folder
and the file to verify that the contents are as expected.

|image03|

Example 02 FileReadWrite
~~~~~~~~~~~~~~~~~~~~~~~~

Open the example, "Files" -> "Examples" -> "AmebaFileSystem" ->
"FileReadWrite".

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first creates a text file named "test.txt", then the
text "hello world!" is saved into the file. After that, the contents of
the file are retrieved and printed to the serial monitor.

|image04|

Using a card reader, connect the SD card to a computer, open the file to
verify that the contents are as expected.

|image05|

Example 03 GetFileAttribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the example, "Files" -> "Examples" -> "AmebaFileSystem" ->
"GetFileAttribute".

Upload the code and press the reset button on the board once the upload
is finished.

The sample code reads the contents of a directory and determines if each
item is a file or folder.

|image06|

Using a card reader, connect the SD card to a computer and verify that
the contents are as expected.

Example 04 LastModifiedTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the example, "Files" -> "Examples" -> "AmebaFileSystem" ->
"LastModifiedTime".

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first opens the text file named "test.txt". After that,
the last modified date and time of the file are changed and then printed
to the serial monitor.

|image07|

Using a card reader, connect the SD card to a computer and verify that
the last modified time of the file are as expected.

|image08|

Example 05 ListRootFiles
~~~~~~~~~~~~~~~~~~~~~~~~

Open the example, "Files" -> "Examples" -> "AmebaFileSystem" ->
"ListRootFiles".

Upload the code and press the reset button on the board once the upload
is finished.

The sample code will print out the names of all files and folders in the
root directory to the serial monitor.

|image09|

Using a card reader, connect the SD card to a computer and verify that
the contents are as expected.

.. |image01| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image01.png
   :width: 555 px
   :height: 950 px
.. |image02| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image02.png
   :width: 667 px
   :height: 317 px
.. |image03| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image03.png
   :width: 505 px
   :height: 415 px
.. |image04| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image04.png
   :width: 667 px
   :height: 317 px
.. |image05| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image05.png
   :width: 499 px
   :height: 414 px
.. |image06| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image06.png
   :width: 667 px
   :height: 317 px
.. |image07| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image07.png
   :width: 667 px
   :height: 317 px
.. |image08| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image08.png
   :width: 661 px
   :height: 707 px
.. |image09| image:: ../../../../_static/amebapro2/Example_Guides/File_System/Simple_applications_with_SD_card/image09.png
   :width: 667 px
   :height: 317 px
