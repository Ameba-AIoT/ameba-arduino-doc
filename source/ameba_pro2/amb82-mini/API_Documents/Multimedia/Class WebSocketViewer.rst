Class WebSocketViewer
======================

.. contents::
  :local:
  :depth: 2

**WebSocketViewer Class**
--------------------------

**Description**
~~~~~~~~~~~~~~~

A class for streaming live camera video from the AMB82 Mini to a web browser using WebSocket.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class WebSocketViewer

**Members**
~~~~~~~~~~~

+------------------------------------------------+--------------------------------------------------------+
| **Public Constructors**                                                                                 |
+================================================+========================================================+
| WebSocketViewer::WebSocketViewer               | Constructs a WebSocketViewer object.                   |
+------------------------------------------------+--------------------------------------------------------+
| **Public Methods**                                                                                      |
+------------------------------------------------+--------------------------------------------------------+
| WebSocketViewer::loadWebResourcesFromSD        | Load htdocs.bin from the SD card.                      |
+------------------------------------------------+--------------------------------------------------------+
| WebSocketViewer::loadWebResources              | Load WebSocket Viewer web resources.                   |
+------------------------------------------------+--------------------------------------------------------+
| WebSocketViewer::init                          | Initialize the WebSocket Viewer module.                |
+------------------------------------------------+--------------------------------------------------------+
| WebSocketViewer::begin                         | Start the WebSocket Viewer service.                    |
+------------------------------------------------+--------------------------------------------------------+
| WebSocketViewer::deinit                        | Deinitialize the WebSocket Viewer service.             |
+------------------------------------------------+--------------------------------------------------------+

**WebSocketViewer::loadWebResourcesFromSD**
--------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Load htdocs.bin from the SD card.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int loadWebResourcesFromSD(unsigned char **buf, int *len);

**Parameters**
~~~~~~~~~~~~~~

buf: Pointer to the buffer containing the loaded web resources.

len: Length of the loaded data in bytes.

**Returns**
~~~~~~~~~~~

0 on success, -1 on failure.

**Example Code**
~~~~~~~~~~~~~~~~~

NA

.. note :: "WebSocketViewer.h" must be included to use the class function.

**WebSocketViewer::loadWebResources**
----------------------------------------

**Description**
~~~~~~~~~~~~~~~

Load WebSocket Viewer web resources.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void loadWebResources(int websocket_from_sd);

**Parameters**
~~~~~~~~~~~~~~

websocket_from_sd: 1 to load web resources (htdocs.bin) from the SD card, 0 to load web resources from htdocs.h as an array.


**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WebSocketViewer <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/WebSocketViewer/WebSocketViewer.ino>`_

.. note :: "WebSocketViewer.h" must be included to use the class function.

**WebSocketViewer::init**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize the WebSocket Viewer module.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void init(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WebSocketViewer <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/WebSocketViewer/WebSocketViewer.ino>`_

.. note :: "WebSocketViewer.h" must be included to use the class function.

**WebSocketViewer::begin**
---------------------------

**Description**
~~~~~~~~~~~~~~~

Start the WebSocket Viewer service. 

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void begin(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `WebSocketViewer <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/Multimedia/examples/WebSocketViewer/WebSocketViewer.ino>`_

.. note :: "WebSocketViewer.h" must be included to use the class function.

**WebSocketViewer::deinit**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Deinitialize the WebSocket Viewer service.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    mm_context_t *deinit(mm_context_t *p);

**Parameters**
~~~~~~~~~~~~~~

p:  pointer to the mm_context_t to be deinitialized.

**Returns**
~~~~~~~~~~~

Pointer to the deinitialized mm_context_t.

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "WebSocketViewer.h" must be included to use the class function.
