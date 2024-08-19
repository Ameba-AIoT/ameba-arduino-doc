Materials
=========

-  AmebaPro2 [AMB82 MINI] x 1

-  MicroSD card

Example
=======

Procedure
---------

Insert a MicroSD card into the SD card slot of the AMB82 MINI board.

Example 01 CreateFolder

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“CreateFolder”.

|Graphical user interface, application Description automatically
generated|

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first creates a folder named “testdir”, a text file
named “test.txt” is next created, and the text “hello world!” is saved
into the file. After that, the contents of the file are retrieved and
printed to the serial monitor.

|Graphical user interface, text, application Description automatically
generated|

Using a card reader, connect the SD card to a computer, open the folder
and the file to verify that the contents are as expected.

|Graphical user interface Description automatically generated|

Example 02 FileReadWrite

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“FileReadWrite”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code first creates a text file named “test.txt”, then the
text “hello world!” is saved into the file. After that, the contents of
the file are retrieved and printed to the serial monitor.

|Graphical user interface, text, application, email Description
automatically generated|

Using a card reader, connect the SD card to a computer, open the file to
verify that the contents are as expected.

|A screenshot of a computer Description automatically generated with
medium confidence|

Example 03 GetFileAttribute

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“GetFileAttribute”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code reads the contents of a directory and determines if each
item is a file or folder.

|image1|

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

|image2|

Using a card reader, connect the SD card to a computer and verify that
the last modified time of the file are as expected.

|image3|

Example 05 ListRootFiles

Open the example, "Files" -> "Examples" -> “AmebaFileSystem” ->
“ListRootFiles”.

Upload the code and press the reset button on the board once the upload
is finished.

The sample code will print out the names of all files and folders in the
root directory to the serial monitor.

|image4|

Using a card reader, connect the SD card to a computer and verify that
the contents are as expected.

.. |Graphical user interface, application Description automatically generated| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image01.png
   :width: 3.26042in
   :height: 5.56835in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image02.png
   :width: 4.125in
   :height: 1.96059in
.. |Graphical user interface Description automatically generated| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image03.png
   :width: 4.08333in
   :height: 3.35237in
.. |Graphical user interface, text, application, email Description automatically generated| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image04.png
   :width: 5.19792in
   :height: 2.47054in
.. |A screenshot of a computer Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image05.png
   :width: 3.53125in
   :height: 2.91328in
.. |image1| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image06.png
   :width: 6.26806in
   :height: 2.97917in
.. |image2| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image07.png
   :width: 6.26806in
   :height: 2.97917in
.. |image3| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image08.png
   :width: 3.71875in
   :height: 3.96433in
.. |image4| image:: ../../_static/Example_Guides/File_System_-_Simple_applications_with_SD_card/File_System_-_Simple_applications_with_SD_card_images/image09.png
   :width: 6.26806in
   :height: 2.97917in
