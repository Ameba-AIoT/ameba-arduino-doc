Class Wiring OS API
===================

.. contents::
  :local:
  :depth: 2

**Wiring OS API Class**
-----------------------

**Description**
~~~~~~~~~~~~~~~

A wrapper to CMSIS (Cortex Microcontroller Software Interface Standard) OS API which serve as a RTOS to create multi-threaded application with real-time behaviour.

**Syntax**
~~~~~~~~~~

NA

**Members**
~~~~~~~~~~~

+--------------------------------+------------------------------------+
| **Public Methods**                                                  |
+================================+====================================+
| os_thread_create_arduino       | Create a thread and add it to      |
|                                | Active Threads and set it to state |
|                                | READY                              |
+--------------------------------+------------------------------------+
| os_thread_get_id_arduino       | Return the thread ID of the        |
|                                | current running thread             |
+--------------------------------+------------------------------------+
| os_thread_terminate_arduino    | Terminate execution of a thread    |
|                                | and remove it from Active Threads  |
+--------------------------------+------------------------------------+
| os_thread_yield_arduino        | Pass control to next thread that   |
|                                | is in state READY                  |
+--------------------------------+------------------------------------+
| os_thread_set_priority_arduino | Change priority of an active       |
|                                | thread                             |
+--------------------------------+------------------------------------+
| os_thread_get_priority_arduino | Get current priority of an active  |
|                                | thread                             |
+--------------------------------+------------------------------------+
| os_signal_set_arduino          | Set the specified Signal Flags of  |
|                                | an active thread                   |
+--------------------------------+------------------------------------+
| os_signal_clear_arduino        | Clear the specified Signal Flags   |
|                                | of an active thread                |
+--------------------------------+------------------------------------+
| os_signal_wait_arduino         | Wait for one or more Signal Flags  |
|                                | to become signaled for the current |
|                                | RUNNING thread                     |
+--------------------------------+------------------------------------+
| os_timer_create_arduino        | Create a timer                     |
+--------------------------------+------------------------------------+
| os_timer_start_arduino         | Start or restart a timer           |
+--------------------------------+------------------------------------+
| os_timer_stop_arduino          | Stop the timer                     |
+--------------------------------+------------------------------------+
| os_timer_delete_arduino        | Delete a timer that was created by |
|                                | os_timer_create                    |
+--------------------------------+------------------------------------+
| os_semaphore_create_arduino    | Create and Initialize a Semaphore  |
|                                | object used for managing resources |
+--------------------------------+------------------------------------+
| os_semaphore_wait_arduino      | Wait until a Semaphore token       |
|                                | becomes available                  |
+--------------------------------+------------------------------------+
| os_semaphore_release_arduino   | Release a Semaphore token          |
+--------------------------------+------------------------------------+
| os_semaphore_delete_arduino    | Delete a Semaphore that was        |
|                                | created by os_semaphore_create     |
+--------------------------------+------------------------------------+
| os_get_free_heap_size_arduino  | Return the available heap memory   |
|                                | space when called                  |
+--------------------------------+------------------------------------+

**os_thread_create_arduino**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Create a thread and add it to Active Threads and set it to state READY.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_thread_create_arduino (void (*task)(const void *argument), void *argument, int priority, uint32_t stack_size);

**Parameters**
~~~~~~~~~~~~~~

``task``: task Function pointer which is the thread body. It should not run into the end of function unless os_thread_terminate is invoked

``argument``: The pointer that is passed to the thread function as start argument.

``priority``: The underlying os is FreeRTOS. It executes tasks with highest priority which are not in idle state.

``stack_size``: The stack_size is used as memory heap only for this task.

**Returns**
~~~~~~~~~~~

This function returns the thread ID in 32-bit which is used in thread operation for reference by other functions or NULL in case of error.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

------------------------------------

**os_thread_get_id_arduino**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Get the thread ID of the current running thread.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_thread_get_id_arduino (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns current thread id in 32-bit which calls os_thread_get_id_arduino.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

---------------------------------------

**os_thread_terminate_arduino**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Terminate execution of a thread and remove it from Active Threads.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_thread_terminate_arduino (uint32_t thread_id);

**Parameters**
~~~~~~~~~~~~~~

``thread_id``: Terminate the thread with specific thread_id

**Returns**
~~~~~~~~~~~

This function returns the os_status code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: Thread should not end without terminate first.

.. note :: “wiring_os.h” must be included to use the class function.

------------------------------------

**os_thread_yield_arduino**
---------------------------

**Description**
~~~~~~~~~~~~~~~
Pass control to next thread that is in READY state

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_thread_yield_arduino (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the os_status code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: The smallest execution unit by default is one millisecond. When a thread with a lower priority wants to instantly give execution rights to a thread with a higher priority rather than waiting for the current 1 millisecond to expire, calling os_thread yield can transfer execution rights to the OS's idle task and determine which thread will execute next.

.. note :: “wiring_os.h” must be included to use the class function.

-----------------------------------------

**os_thread_set_priority_arduino**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Change priority of an active thread.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_thread_set_priority_arduino (uint32_t thread_id, int priority);

**Parameters**
~~~~~~~~~~~~~~

``thread_id``: Thread ID identifies the thread (pointer to a thread control block). 

``priority``: The updated priority

**Returns**
~~~~~~~~~~~

This function returns os_status code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

--------------------------------------

**os_thread_get_priority_arduino**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get current priority of an active thread.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_thread_get_priority_arduino (uint32_t thread_id);

**Parameters**
~~~~~~~~~~~~~~

``thread_id``: The target thread with the thread id to be searched

**Returns**
~~~~~~~~~~~

This function returns os_priority.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

------------------------------

**os_signal_set_arduino**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Set the specified Signal Flags of an active thread.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  int32_t os_signal_set_arduino (uint32_t thread_id, int32_t signals);

**Parameters**
~~~~~~~~~~~~~~

``thread_id``: Thread ID obtained by os_thread_create_arduino or 

``os_thread_get_id_arduino.signals``: The signal flags of the thread that should be set.

**Returns**
~~~~~~~~~~~

This function returns previous signal flags of the specified thread or 0x80000000 in case of incorrect parameters.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

------------------------------------

**os_signal_clear_arduino**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Clear the specified Signal Flags of an active thread.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  int32_t os_signal_clear_arduino (uint32_t thread_id, int32_t signals);

**Parameters**
~~~~~~~~~~~~~~

``thread_id``: Clear signal to a thread with the thread_id

``signals``: The signal flags of the thread that shall be cleared.

**Returns**
~~~~~~~~~~~

This function returns previous signal flags of the specified thread or 0x80000000 in case of incorrect parameters.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

----------------------------------

**os_signal_wait_arduino**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Wait for one or more Signal Flags to become signalled for the current RUNNING thread.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  os_event_t os_signal_wait_arduino (int32_t signals, uint32_t millisec);

**Parameters**
~~~~~~~~~~~~~~

``signals``: the signals to be wait

``millisec``: the timeout value if no signal comes in (in ms). (Acceptable range: 0 - 0xFFFFFFFF, 0 indicates no timeout, 0xFFFFFFFF indicates infinite timeout)

**Returns**
~~~~~~~~~~~

This function returns event flag information or error code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

---------------------------------

**os_timer_create_arduino**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Create a timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_timer_create_arduino (void (*callback)(void const *argument), uint8_t isPeriodic, void *argument);

**Parameters**
~~~~~~~~~~~~~~

``callback``: The function to be invoke when timer timeout

``isPeriodic``: OS_TIMER_ONCE or OS_TIMER_PERIODIC

``argument``: The argument that is brought into callback function

**Returns**
~~~~~~~~~~~

This function returns the timer id.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

-------------------------------

**os_timer_start_arduino**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Start or restart a timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_timer_start_arduino (uint32_t timer_id, uint32_t millisec);

**Parameters**
~~~~~~~~~~~~~~

``timer_id``: The timer id obtained from os_timer_create

``millisec``: The delay after timer starts (in ms) (Acceptable range: 0 - 0xFFFFFFFF, 0 indicates no timeout, 0xFFFFFFFF indicates infinite timeout)

**Returns**
~~~~~~~~~~~

This function returns os_status code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

-----------------------------

**os_timer_stop_arduino**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Stop the timer.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_timer_stop_arduino (uint32_t timer_id);

**Parameters**
~~~~~~~~~~~~~~

``timer_id``: The timer id obtained from os_timer_create

**Returns**
~~~~~~~~~~~

This function returns os_status code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

**os_timer_delete_arduino**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Delete a timer that was created by “os_timer_create_arduino”.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_timer_delete_arduino(uint32_t timer_id);

**Parameters**
~~~~~~~~~~~~~~

``timer_id``: The timer id obtained from os_timer_create

**Returns**
~~~~~~~~~~~

This function returns os_status code.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

--------------------------------

**os_semaphore_create_arduino**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Create and initialize a Semaphore object used for managing resources.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_semaphore_create_arduino (int32_t count);

**Parameters**
~~~~~~~~~~~~~~

``count``: The number of available resources

**Returns**
~~~~~~~~~~~

This function returns semaphore ID.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

-------------------------------

**os_semaphore_wait_arduino**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Wait until a Semaphore token becomes available.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  int32_t os_semaphore_wait_arduino (uint32_t semaphore_id, uint32_t millisec);

**Parameters**
~~~~~~~~~~~~~~

``semaphore_id``: semaphore id obtained from os_semaphore_create

``millisec``: timeout value (in ms). (Acceptable range: 0 - 0xFFFFFFFF, 0 indicates no timeout, 0xFFFFFFFF indicates infinite timeout)

**Returns**
~~~~~~~~~~~

This function returns “1” if “os_semaphoe_wait_arduino” gets the available semaphore token, otherwise returns “0”.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

----------------------------------

**os_semaphore_release_arduino**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Release a Semaphore token.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_semaphore_release_arduino (uint32_t semaphore_id);

**Parameters**
~~~~~~~~~~~~~~

``semaphore_id``: semaphore id obtained from os_semaphore_create

**Returns**
~~~~~~~~~~~

This function returns os_status code that indicates the execution status of the function.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.

--------------------------------

**os_semaphore_delete_arduino**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Delete a Semaphore that was created by os_semaphore_create

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  uint32_t os_semaphore_delete_arduino (uint32_t semaphore_id);

**Parameters**
~~~~~~~~~~~~~~

``semaphore_id``: semaphore id obtained from os_semaphore_create

**Returns**
~~~~~~~~~~~

This function returns os_status code that indicates the execution status of the function.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. important :: “os_semaphore_delete_arduino” shall be consistent in every CMSIS_RTOS. 

.. note :: “wiring_os.h” must be included to use the class function.

-----------------------------------

**os_get_free_heap_size_arduino**
---------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the available heap memory space when called.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

  size_t os_get_free_heap_size_arduino (void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the current free heap size as unsigned integer.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: “wiring_os.h” must be included to use the class function.
