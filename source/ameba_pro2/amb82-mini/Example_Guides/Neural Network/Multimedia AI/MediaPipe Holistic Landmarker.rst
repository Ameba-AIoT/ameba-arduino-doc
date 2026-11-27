MediaPipe Holistic Landmarker
=============================

.. rubric:: Acknowledgments

.. list-table::
   :widths: 1 9
   :width: 100%

   * - .. image:: ../../../../../_static/3rd_party_logo.png
          :width: 40px
     - "Generative AI Speech" is jointly developed by RTKSG SD3 and `ChungYi Fu (Kaohsiung, Taiwan) <https://github.com/fustyles>`_.

   * - .. image:: ../../../../../_static/ameba_iot_logo.png
          :width: 40px
     - Special thanks to all developers for their contributions.

Materials
---------

- `AMB82-mini <https://www.amebaiot.com/en/where-to-buy-link/#buy_amb82_mini>`__ x 1

Example
-------

In this example, we will be using Ameba Pro2 development board to stream JPEG using HTTP and apply MediaPipe Holistic Landmarker on the streaming page.

Open MediaPipe Holistic Landmarker example in :guilabel:`File -> Examples -> AmebaNN -> MultimediaAI -> MediaPipe_Holistic_Landmarker`

|image01|

In the highlighted code snippet fill in the "ssid" with your WiFi network SSID and "pass" with the network password.

|image02|

Compile and upload the example.

Open the serial monitor to view the logs.

|image03|

Please copy the IP address for "Main page" printed on the log and paste it on your browser to view the stream.

Resources
---------

| MediaPipe Holistic Overview
| https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/holistic.md

| MediaPipe Tasks Vision Package
| https://www.jsdelivr.com/package/npm/@mediapipe/tasks-vision

.. |image01| image:: ../../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_MediaPipe_Holistic_Landmarker/image01.png
   :width:  918 px
   :height:  918 px
   :scale: 80%

.. |image02| image:: ../../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_MediaPipe_Holistic_Landmarker/image02.png
   :width:  768 px
   :height:  502 px

.. |image03| image:: ../../../../../_static/amebapro2/Example_Guides/Neural_Network/Neural_Network_-_MediaPipe_Holistic_Landmarker/image03.png
   :width:  378 px
   :height:  130 px
