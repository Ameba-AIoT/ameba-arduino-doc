FatfsSDIO - Read And Open HTML File From SD Card
================================================

Materials
---------

- AmebaD [AMB25] x 1
- MicroSD card

Example
-------

Insert the MicroSD card into your computer and copy the HTML file to your SD card (Note: put the file at outside and do not put it inside of any folder in the SD card). Here is a HTML sample for testing, “Web_test.html”.

|image01|

| Then insert the MicroSD card into the onboard SD card reader of RTL8722DM MINI board.
| Open the example, ``“Files” → “Examples” → “AmebaFatfsSDIO” → “read_html_from_SD_card”``
| Upload the code and press the reset button on Ameba once the upload is finished. When the connection is established, you should be able to see the message “To see this page in action, open a browser to http://xxx.xxx.xxx.xxx” in the serial monitor as shown in the figure:

|image02|

Next, open the address stated in serial monitor in the browser of your laptop or cell phone under the same WiFi domain. 
You will see the following display in your browser:

|image03|

Now you have successfully read and opened the html file saved in your SD card.

.. |image01| image:: ../../../../_static/amebad/Example_Guides/FatfsSDIO/FatfsSDIO_Read_And_Open_HTML_File_From_SD_Card/image01.png
    :width: 1040
    :height: 360
    :scale: 80 %
.. |image02| image:: ../../../../_static/amebad/Example_Guides/FatfsSDIO/FatfsSDIO_Read_And_Open_HTML_File_From_SD_Card/image02.png
    :width: 1168
    :height: 630
    :scale: 70 %
.. |image03| image:: ../../../../_static/amebad/Example_Guides/FatfsSDIO/FatfsSDIO_Read_And_Open_HTML_File_From_SD_Card/image03.png
    :width: 3895
    :height: 1235
    :scale: 15 %