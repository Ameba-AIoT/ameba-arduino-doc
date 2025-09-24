.. tags:: multimedia, neural network, log system, amb82-mini

How can I control debug logs?
===============================

**Answer**

**Multimedia Logs**

Navigate to "Tools" -> "[Logs] Multimedia". It is set to "Enable all" by default.

|image01|

You can choose from the following, 

1. Video/OSD logs only
    - Activates logging for Video and OSD components only.

2. NN/OSD logs only
    - Activates logging for Neural Network (NN) and OSD components only.

3. Disable all (Soft Mute)
    - Turns off NN, Video, and OSD logs.
    - You can add your own custom debug logs if needed.

4. Disable all (Hard Mute)
    - Completely disables all logs, including printf.
    - Not recommended if you still need debugging capabilities.

.. |image01| image:: ../_static/FAQ/disable_logs/image01.png
   :width:  1936 px
   :height:  1048 px
   :scale: 50%