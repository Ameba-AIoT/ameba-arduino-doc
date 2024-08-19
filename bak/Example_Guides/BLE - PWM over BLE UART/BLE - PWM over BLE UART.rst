Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  RGB LED

-  Android / iOS smartphone

Example

Introduction
============

In this example, a smartphone app is used to transmit commands over BLE
UART to control the PWM outputs and change the color of a RGB LED. Refer
to the other example guides for detailed explanations of the BLE UART
service.

Procedure
=========

Connect the RGB LED to the AmebaPro2 board following the diagram, the
common LED pin may need to connect to 3.3V or GND depending on the type
of LED (common anode / common cathode).

**AMB82** **MINI:**

|image1|

Ensure that the required app is installed on your smartphone, it is
available at:

-  Google Play Store:
   https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect

-  Apple App Store:
   https://apps.apple.com/us/app/bluefruit-connect/id830125974

Open the example, "Files" -> "Examples" -> “AmebaBLE” ->
“PWM_over_BLEUart”.

Upload the code and press the reset button on Ameba once the upload is
finished.

|Graphical user interface, table Description automatically generated|

Open the app on your smartphone, scan and connect to the board shown as
“AMEBA_BLE_DEV” and choose the controller -> color picker function in
the app.

|image2|\ |image3|\ |image4|

Using the color selection wheel, saturation, and brightness sliders,
choose a desired color and click select to send the RGB values to the
board. You should see the RGB LED change to the matching color.

|image5|

Code Reference

The RGB values are sent as three consecutive bytes prefixed by “!C”
characters. The “!” exclamation mark is used to indicate that the
following data is a command, and the “C” character is used to indicate
that the data is RGB values. The received UART message is checked in the
callback function for “!C” first, otherwise it is treated as a regular
message and printed to the serial terminal.

.. |image1| image:: ../../_static/Example_Guides/BLE_-_PWM_over_BLE_UART/BLE_-_PWM_over_BLE_UART_images/image01.png
   :width: 3.84712in
   :height: 2.74936in
.. |Graphical user interface, table Description automatically generated| image:: ../../_static/Example_Guides/BLE_-_PWM_over_BLE_UART/BLE_-_PWM_over_BLE_UART_images/image02.png
   :width: 2.48684in
   :height: 3.5013in
.. |image2| image:: ../../_static/Example_Guides/BLE_-_PWM_over_BLE_UART/BLE_-_PWM_over_BLE_UART_images/image03.png
   :width: 1.704in
   :height: 3.408in
.. |image3| image:: ../../_static/Example_Guides/BLE_-_PWM_over_BLE_UART/BLE_-_PWM_over_BLE_UART_images/image04.png
   :width: 1.704in
   :height: 3.408in
.. |image4| image:: ../../_static/Example_Guides/BLE_-_PWM_over_BLE_UART/BLE_-_PWM_over_BLE_UART_images/image05.png
   :width: 1.704in
   :height: 3.40605in
.. |image5| image:: ../../_static/Example_Guides/BLE_-_PWM_over_BLE_UART/BLE_-_PWM_over_BLE_UART_images/image06.png
   :width: 2.44in
   :height: 4.8772in
