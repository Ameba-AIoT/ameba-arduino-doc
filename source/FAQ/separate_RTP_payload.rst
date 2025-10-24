.. tags:: rtp, h264, rtsp, nalu

How to separate the NALU info of each H264 frame into individual RTP payload?
=============================================================================

We have been having issues with using some receivers to handle the rtsp h264 stream from the Ameba RTOS Pro2. We dug into the issues and it seems the RTP payloading process is grouping the SPS, PPS, and IDR into a single Fragment Unit A (FU-A) NALU for each IDR frame. This seems to not be decoded correctly by some receivers since a FU-A should only be encapsulating a single NALU, not 3 (SPS, PPS, and IDR).

**Answer**

Kindly go to "ameba-rtos-pro2\\component\\media\\mmfv2\\module_rtsp2.c" in FreeRTOS SDK and uncomment line 15, `#define SEPERATE_VIDEO_NALU_PAYLOAD`. This will ensure that each RTP payload consists of only one NAL unit.
