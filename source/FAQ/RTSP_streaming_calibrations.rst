.. tags:: wifi, 2.4g, 5g, rtsp

Got "MMF ENC Queue full" when using 2.4G WiFi for RTSP streaming
================================================================

"MMF ENC Queue full" appearing only on 2.4 GHz Wi-Fi, suggests a network bandwidth or latency issue. The 2.4 GHz link is slower and more congested, causing encoder output data to queue up. Using 5 GHz or lowering video bitrate/frame rate can prevent the encoder queue from filling.

**Answer**

Yes, using a 2.4 GHz Wi-Fi connection is likely to cause this warning message when running RTSP streaming–related applications.

Some calibration suggestions:

- Switch to 5 GHz Wi-Fi – faster, less interference, more stable throughput.

- Lower video bitrate or resolution – reduces encoder output size.

- Reduce frame rate – less data per second.

- Improve network quality – avoid crowded 2.4 GHz channels.

- Check for background traffic – other devices might be saturating the 2.4 GHz band.

- Using multi-task structure for application - Wi-Fi and streaming by 2 tasks.

- Increase the queue length - using "Video::setQLen(int ch, int len)".

Refer to the following code for the basic use of "Video::setQLen(int ch, int len)".

.. code-block:: c++

    Camera.configVideoChannel(CHANNEL, config);
    Camera.videoInit();

    rtsp.configVideo(config);
    rtsp.begin();

    videoStreamer.registerInput(Camera.getStream(CHANNEL));
    videoStreamer.registerOutput(rtsp);
    if (videoStreamer.begin() != 0) {
        Serial.println("StreamIO link start failed");
    }

    Camera.setQLen(CHANNEL, 30 * 3);
    Camera.channelBegin(CHANNEL);
