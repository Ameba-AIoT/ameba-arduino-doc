Materials

AmebaPro2 [AMB82 MINI] x 1

MicroSD card

Example

Procedure

Insert a MicroSD card into the SD card slot of the AMB82 MINI board.

Example 01 CreateFolder

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“CreateFolder”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first creates a folder named “testdir”, a text file
named “test.txt” is next created, and the text “hello world!” is saved
into the file. After that, the contents of the file are retrieved and
printed to the serial monitor.

Using a card reader, connect the SD card to a computer, open the folder
and the file to verify that the contents are as expected.

Example 02 FileReadWrite

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“FileReadWrite”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first creates a text file named “test.txt”, then the
text “hello world!” is saved into the file. After that, the contents of
the file are retrieved and printed to the serial monitor.

Using a card reader, connect the SD card to a computer, open the file to
verify that the contents are as expected.

Example 03 GetFileAttribute

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“GetFileAttribute”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code reads the contents of a directory and determines if each
item is a file or folder.

Using a card reader, connect the SD card to a computer and verify that
the contents are as expected.

Example 04 LastModifiedTime

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“LastModifiedTime”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first opens the text file named “test.txt”. After that,
the last modified date and time of the file are changed and then printed
to the serial monitor.

Using a card reader, connect the SD card to a computer and verify that
the last modified time of the file are as expected.

Example 05 ListRootFiles

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“ListRootFiles”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code will print out the names of all files and folders in the
root directory to the serial monitor.

Using a card reader, connect the SD card to a computer and verify that
the contents are as expected.

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.png| |image08.png| |image09.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image03.png
.. |image04.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image04.png
.. |image05.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image05.png
.. |image06.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image06.png
.. |image07.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image07.png
.. |image08.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image08.png
.. |image09.png| image:: ../../../_static/_Example_Guides/_File%20System%20-%20Simple%20applications%20with%20SD%20card/image09.png
