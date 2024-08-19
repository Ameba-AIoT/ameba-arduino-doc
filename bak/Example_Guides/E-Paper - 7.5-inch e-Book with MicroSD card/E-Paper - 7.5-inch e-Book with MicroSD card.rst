Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Waveshare E-Paper [7.5-inch E-Ink display HAT] x1

-  Button x 1

-  MicroSD card x 1

-  330 Ohm resistor x1

Introduction

In this example, we will be connecting Ameba Pro2 board to Waveshare
7.5-inch e-Paper module to be used as an e-Book. The 7.5” active area
contains 800 x 480 pixels and has 1-bit white/black full display
capabilities. An integrated circuit contains gate buffer, source buffer,
interface, timing control logic, oscillator, etc. are supplied with each
panel. You may refer to [7.5inch-e-paper-specification]
(https://www.waveshare.com/w/upload/6/60/7.5inch_e-Paper_V2_Specification.pdf)
for more information about this e-Paper module.

Procedure

**AMB82-Mini wiring diagram:**

Do note that Display Config should be set to B and Interface Config
should be set to 0.

|image1|

|image2|

| Next, download the Eink zip library, AmebaEink.zip,
  at https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_zip_libraries
| Then install the AmebaEink.zip by navigating to “Sketch” -> “Include
  Library” -> “Add .ZIP Library…”.

After AmebaEink.zip is installed, Open the “Eink_7in5_Ebook” example by
selecting “File” -> “Examples” -> “AmebaEink” -> “EPD_7in5” ->
“Eink_7in5_Ebook”.

|image3|

Next, insert the MicroSD card into your computer and create a new text
file named “User_Ebook.txt”. Then, save the content that you would like
to display in the text file (Note: do only include words). The content
of “User_Ebook.txt” shown below is for illustration purposes only.

|image4|

|image5|

Alternatively, if you prefer another filename for your text file, you
can modify the highlighted code snippet in the sketch with the new
filename.

|image6|

Once the file is created, insert the MicroSD card into the onboard SD
card reader on AMB82 Mini. Upload the code and press the reset button
once the uploading is done. When the reset button is pressed, the
e-Paper display will refresh and display a cover page.

|image7|

By pressing the button, the content in the selected text file saved in
MicroSD card will be read and displayed onto the e-Paper display. The
content will be split into pages.

To proceed to the next page, press the button once more. The page number
will be shown at the bottom right-hand corner as the page changes. You
will see the following in either portrait or landscape mode based on
your orientation choice after button is pressed:

|image8| |image9|

You can modify the highlighted code snippet to change the font size or
orientation of the displayed text.

| Supported font size: 16, 20, 24
| Supported orientation: 0 degree – 0 (landscape), 90 degree – 1
  (portrait), 180 degree- 2 (landscape), 270 degree – 3 (portrait)

|image10|

Code Reference

| [1] We use waveshare 7.5-inch e-Paper display module/ 800×480
  Resolution driver code to get e-Paper successfully display:
| https://github.com/waveshare/e-Paper/tree/master/Arduino/epd7in5_V2

[2] EPD libraries can be obtained from:
https://github.com/waveshare/e-Paper

| [3] Text Wrap function was written reference to:
| https://www.cprogramming.com/snippets/source-code/word-wrap-in-c

.. |image1| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image01.png
   :width: 3.63575in
   :height: 4.66995in
.. |image2| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image02.png
   :width: 6.25347in
   :height: 3.36389in
.. |image3| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image03.png
   :width: 3.696in
   :height: 4.00332in
.. |image4| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image04.png
   :width: 4.09722in
   :height: 1.06292in
.. |image5| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image05.png
   :width: 4.32639in
   :height: 0.92571in
.. |image6| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image06.png
   :width: 4.11435in
   :height: 4.456in
.. |image7| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image7.jpeg
   :width: 2.6495in
   :height: 3.536in
.. |image8| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image8.jpeg
   :width: 2.64931in
   :height: 3.53574in
.. |image9| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image9.jpeg
   :width: 3.368in
   :height: 2.7056in
.. |image10| image:: ../../_static/Example_Guides/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card/E-Paper_-_7.5-inch_e-Book_with_MicroSD_card_images/image10.png
   :width: 4.12913in
   :height: 4.472in
