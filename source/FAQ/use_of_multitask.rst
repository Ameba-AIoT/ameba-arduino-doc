.. tags:: multitask, thread, task

How to enable/use the multitask
===============================

In embedded systems, multitasking enables multiple tasks—like sensor reading, data processing, and communication—to run concurrently. It improves CPU utilization, responsiveness, and modularity while reducing idle time. With an RTOS managing task priorities, multitasking ensures efficient, real-time performance essential for applications in automotive, IoT, and industrial control systems.

**Answer**

Yes, Ameba Arduino has multitask feature.

.. code-block:: c++

    xTaskCreate(Taskfunc, "Taskname", (8 * 1024), NULL, 1, NULL);

+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| Parameter       | Example Value  | Description                                                                                                   |
+=================+================+===============================================================================================================+
| ``pvTaskCode``  | ``Taskfunc``   | The function to run as the task (task entry function).                                                        |
+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| ``pcName``      | ``"Taskname"`` | A human-readable task name (useful for debugging).                                                            |
+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| ``usStackDepth``| ``(8 * 1024)`` | Stack size (in words, not bytes on some systems) allocated for this task — here, 8 KB of stack space.         |
+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| ``pvParameters``| ``NULL``       | Optional parameter passed into the task function (can be used to give input data).                            |
+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| ``uxPriority``  | ``1``          | Task priority — higher numbers mean higher priority. The scheduler decides which task runs first based on this.|
+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| ``pxCreatedTask``| ``NULL``      | Optional pointer to store the **task handle** (used to manage or delete the task later).                      |
+-----------------+----------------+---------------------------------------------------------------------------------------------------------------+

Refer to the following basic test code.

.. code-block:: c++

    void blinkTask(void *param) {
        pinMode(LED_BUILTIN, OUTPUT);
        while (true) {
            digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
            vTaskDelay(500 / portTICK_PERIOD_MS);
        }
    }

    void setup() {
        xTaskCreate(blinkTask, "BlinkTask", 1024, NULL, 1, NULL); // new multitask
    }
