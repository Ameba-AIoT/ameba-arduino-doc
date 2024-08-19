Materials

-  AmebaPro2 [AMB82 MINI] x 1

-  Android / iOS mobile phone

Example

**Introduction**

This example configures the Ameba as a Bluetooth central device, uses
the scan functionality to scan for other Bluetooth devices, and prints
out the results to the serial monitor.

**Procedure**

Open the example, “Files” -> “Examples” -> “AmebaBLE” -> “BLEScan”

|image1|

| Upload the code and press the reset button on Ameba once the upload is
  finished.
| Open the Arduino serial monitor, and you should see the scan results
  of nearby Bluetooth devices formatted and printed out.

|3|

If you have the Bluetooth app nRF Connect installed, you can also use it
to send out Bluetooth advertisements for the Ameba to pick up.

Code Reference

setScanMode(GAP_SCAN_MODE_ACTIVE) is used to set the scan mode. Active
scanning will request for an additional scan response data packet from a
device when it is found. Passive scanning will only look at the
advertisement data, and not request for additional data.

setScanInterval() and setScanWindow() are used to set the frequency and
duration of scans in milliseconds. A scan will start every interval
duration, and each scan will last for the scan window duration. The scan
window duration should be lesser or equal to the scan interval. Set a
short interval to discover devices rapidly, set a long interval to
conserve power.

setScanCallback(scanFunction) is used to register a function to be
called when scan results are received. This can be used to set a user
function for additional processing of scan data, such as looking for a
specific device. If no function is registered, the scan results are
formatted and printed to the serial monitor by default.

beginCentral(0) is used to start the Bluetooth stack in Central mode.
The argument 0 is used to indicate that no clients will be operating in
central mode.

startScan(5000) is used to start the scanning process for a specified
duration of 5000 milliseconds. The scan will repeat according to the set
scan interval and scan window values. After 5000 milliseconds, the scan
process will stop, and will be ready to be started again.

.. |image1| image:: ../../_static/Example_Guides/BLE_-_Scan/BLE_-_Scan_images/image01.png
   :width: 3.02117in
   :height: 4.2536in
.. |3| image:: ../../_static/Example_Guides/BLE_-_Scan/BLE_-_Scan_images/image02.png
   :width: 4.49514in
   :height: 5.38261in
