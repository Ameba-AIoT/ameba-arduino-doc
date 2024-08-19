Preparation

-  AmebaPro2 [`AMB82
   Mini <https://www.amebaiot.com/en/amebapro2-amb82-mini-arduino-getting-started/>`__]
   x 1

Example

In this example, we use an NTP client to sync with NTP servers using UDP
and keep track of time locally.Open the example. “File” -> “Examples” ->
“NTPClient” -> “Advanced”

|image1|\ Modify the highlighted code section (ssid, password) to
connect to your WiFi network.

|image2|

Compile the code and upload it to Ameba. After pressing the Reset
button, Ameba connects to WiFi, gets the UTC time from the NTP server,
and prints out the current time with time zone offset to the serial
monitor.

|image3|

Code Reference

| Configure NTP client:
| The NTPClient needs to use a UDP client for communications. A WiFiUDP
  client is declared and passed to the NTPClient constructor, along with
  an NTP server address, time zone offset in seconds, and update
  interval in milliseconds. If detailed configuration is not needed,
  just passing in the UDP client is also sufficient, refer to the
  “NTPClient” -> “Basic” example.

WiFiUDP ntpUDP;

NTPClient timeClient(ntpUDP, “europe.pool.ntp.org”, 3600, 60000);

| Start NTP client:
| After connecting to WiFi, the NTPClient is started using the begin()
  function, which causes the client to sync with the NTP server and get
  the UTC time.

WiFiUDP ntpUDP;

timeClient.begin();

| Get local time:
| getFormattedTime() is used to format the received UTC time into the
  local time zone.
| update() is called every loop so that the NTPClient will sync with the
  NTP server once every update interval.

timeClient.update();

timeClient.getFormattedTime();

.. |image1| image:: ../../_static/Example_Guides/NTP_-_Retrieve_Universal_Time_(UTC)_by_NTPClient_library/NTP_-_Retrieve_Universal_Time_(UTC)_by_NTPClient_library_images/image01.png
   :width: 6.26806in
   :height: 3.32222in
.. |image2| image:: ../../_static/Example_Guides/NTP_-_Retrieve_Universal_Time_(UTC)_by_NTPClient_library/NTP_-_Retrieve_Universal_Time_(UTC)_by_NTPClient_library_images/image02.png
   :width: 3.76042in
   :height: 3.88056in
.. |image3| image:: ../../_static/Example_Guides/NTP_-_Retrieve_Universal_Time_(UTC)_by_NTPClient_library/NTP_-_Retrieve_Universal_Time_(UTC)_by_NTPClient_library_images/image03.png
   :width: 6.26806in
   :height: 6.57083in
