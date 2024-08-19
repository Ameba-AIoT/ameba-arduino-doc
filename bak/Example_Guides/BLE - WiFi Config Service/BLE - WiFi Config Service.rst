Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Android / iOS mobile phone

Example

Introduction
============

In this example, a WiFi configuration service is set up on the Ameba
Bluetooth stack. A mobile phone with the configuration app connects to
the Ameba device using BLE and configures the Ameba to connect to the
correct WiFi access point.

Procedure
=========

Ensure that the Realtek WiFi configuration app is installed on your
mobile phone, it is available at:

-  Google Play Store:
   https://play.google.com/store/apps/details?id=com.rtk.btconfig

-  Apple App Store:
   https://apps.apple.com/sg/app/easy-wifi-config/id1194919510

Open the example, "Files" -> "Examples" -> “AmebaBLE” ->
“BLEWifiConfigService”.

|image1|

Upload the code and press the reset button on Ameba once the upload is
finished.

On your mobile phone, open the Realtek WiFiConfig app and tap the round
button to scan for Ameba boards.

|image2|

Select the correct Ameba board from the scan results. The app will
connect to the Ameba board and ask the board to scan for WiFi networks
and send the scan results back to the app using BLE.

|image3|\ |image4|\ |image5|

If your phone is currently connected to a WiFi network, the app will ask
for the WiFi password to connect the Ameba board to the same WiFi
network. Tap “Select AP” to choose another WiFi network, or enter the
password and tap continue to connect Ameba to the selected WiFi network.

|image6|

After the Ameba board connects to the WiFi network, the following
message will be shown. Tap “Try another AP” to connect to another WiFi
network or tap “Confirm” to keep the current WiFi network and disconnect
BLE from the Ameba board.

|image7|

Code Reference

*BLEWifiConfigService* is used to create an instance of the WiFi
configuration service to run on the Bluetooth device.

*BLE.configAdvert()->setAdvType(configService.advData())* is used to set
the correct advertisement data necessary for the phone app to find the
Ameba Bluetooth device.

.. |image1| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image01.png
   :width: 2.4657in
   :height: 3.47153in
.. |image2| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image02.png
   :width: 1.84375in
   :height: 3.6875in
.. |image3| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image03.png
   :width: 1.55309in
   :height: 3.10617in
.. |image4| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image04.png
   :width: 1.55729in
   :height: 3.11458in
.. |image5| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image5.jpeg
   :width: 1.55208in
   :height: 3.10417in
.. |image6| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image06.png
   :width: 1.71875in
   :height: 3.4375in
.. |image7| image:: ../../_static/Example_Guides/BLE_-_WiFi_Config_Service/BLE_-_WiFi_Config_Service_images/image07.png
   :width: 2.17188in
   :height: 4.34375in
