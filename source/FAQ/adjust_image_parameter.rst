.. tags:: isp control, amb82-mini

Are there APIs to adjust image parameters (brightness, contrast, sharpness, white balance) at runtime?
======================================================================================================

**Answer**

| To know more about the API, you may refer to https://ameba-doc-rtos-pro2-sdk.readthedocs-hosted.com/en/latest/application_note/15_ISP.html#isp-control-api.
| 2 methods are supported for these API (before stream / after stream).
| Functions defined in `isp_ctrl_api.h <https://github.com/Ameba-AIoT/ameba-rtos-pro2/blob/main/component/video/driver/RTL8735B/isp_ctrl_api.h>`__ are all supported at runtime.
| It can also be adjusted using AT Commands.
| You may find all the AT commands in `atcmd_isp.c <https://github.com/Ameba-AIoT/ameba-rtos-pro2/blob/main/component/at_cmd/atcmd_isp.c>`_.
