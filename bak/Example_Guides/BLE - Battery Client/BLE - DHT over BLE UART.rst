Materials

-  AmebaPro2 [AMB82 MINI] x1

-  DHT11 or DHT22 or DHT21

-  Android / iOS smartphoned

Example

**Introduction**

In this example, the data obtained from a DHT temperature and humidity
sensor are transmitted over a BLE UART service to a smartphone. Refer to
the other examples for detailed explanations of using the DHT sensor and
the BLE UART service.

**Procedure**

Take note that if you are using a DHT sensor that is not mounted on a
PCB, you will have to add in a 10K Ohm pull up resistor.

Connect the DHT sensor to the Ameba board following the diagram.

**AMB82 MINI:**

*DHT sensor not mounted on a PCB* *board*

|image1|

*DHT sensor mounted on a PCB* *board*

|image2|

| Ensure that a compatible BLE UART app is installed on your smartphone,
  it is available at:
| – Google Play Store:
| `https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connecta>
   <https://play.google.com/store/apps/details?id=com.adafruit.bluefruit.le.connect>`__\ https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal

| – Apple App Store:
| https://apps.apple.com/us/app/bluefruit-connect/id830125974

Open the example, “Files” -> “Examples” -> “AmebaBLE” ->
“DHT_over_BLEUart”.

|Table Description automatically generated with medium confidence|

| Upload the code and press the reset button on Ameba once the upload is
  finished.
| Open the app on your smartphone, scan and connect to the Ameba board
  shown as “AMEBA_BLE_DEV” and choose the UART function in the app.

|1|

|image3|

After starting the UART function, notifications should be received every
5 seconds containing the measured temperature and humidity.

|image4|

.. |image1| image:: ../../_static/Example_Guides/BLE_-_DHT_over_BLE_UART/BLE_-_DHT_over_BLE_UART_images/image01.png
   :width: 6.26111in
   :height: 3.13678in
.. |image2| image:: ../../_static/Example_Guides/BLE_-_DHT_over_BLE_UART/BLE_-_DHT_over_BLE_UART_images/image02.png
   :width: 2.71718in
   :height: 2.21601in
.. |Table Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/BLE_-_DHT_over_BLE_UART/BLE_-_DHT_over_BLE_UART_images/image03.png
   :width: 2.69635in
   :height: 4.20793in
.. |1| image:: ../../_static/Example_Guides/BLE_-_DHT_over_BLE_UART/BLE_-_DHT_over_BLE_UART_images/image04.png
   :width: 3.79851in
   :height: 7.59701in
.. |image3| image:: ../../_static/Example_Guides/BLE_-_DHT_over_BLE_UART/BLE_-_DHT_over_BLE_UART_images/image05.png
   :width: 3.46269in
   :height: 6.92537in
.. |image4| image:: ../../_static/Example_Guides/BLE_-_DHT_over_BLE_UART/BLE_-_DHT_over_BLE_UART_images/image06.png
   :width: 3.73134in
   :height: 7.46269in
