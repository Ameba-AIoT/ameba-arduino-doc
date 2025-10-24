.. tags:: isp control, amb82-mini

Is day/night detection supported?
=================================

**Answer**

| Yes, you could refer to “sensor_service.c” for this feature, ALS_TYPE = SW_ALS (https://github.com/Ameba-AIoT/ameba-rtos-pro2/blob/main/component/media/framework/sensor_service.c)
| It's using ISP information for automatic day/night mode changing.
| You could check for video example `mmf2_video_example_v1_day_night_change_init <https://github.com/Ameba-AIoT/ameba-rtos-pro2/blob/main/project/realtek_amebapro2_v0_example/src/mmfv2_video_example/mmf2_video_example_v1_day_night_change_init.c>`_ -> day_night_mode_change()
