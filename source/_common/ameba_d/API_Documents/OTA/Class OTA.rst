Class OTA
=========

**OTA Class**
-------------

**Description**
~~~~~~~~~~~~~~~

A class used for updating firmware Over the Air (OTA) in local area network.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class OTA

**Members**
~~~~~~~~~~~

+------------------------------------------+-------------------------------------------------+
| **Public Constructors**                                                                    |
+==========================================+=================================================+
| A public constructor should not be used as this class is intended to be a singleton class. |
| Access member functions using the object instance named OTA.                               |
+------------------------------------------+-------------------------------------------------+
| **Public Methods**                                                                         |
+------------------------------------------+-------------------------------------------------+
| OTA::beginOTA                            | Starts to connect to MDNS OTA server            |
|                                          | and receive the new firmware.                   |
|                                          |                                                 |
+------------------------------------------+-------------------------------------------------+
| OTA::start_OTA_threads                   | Starts multithreading tasks to connect          |
|                                          | to HTTP OTA server and receive new firmware     |
|                                          | upon triggered.                                 |
+------------------------------------------+-------------------------------------------------+

**OTA::beginOTA**
-----------------

**Description**
~~~~~~~~~~~~~~~

Starts the connect of OTA server and waiting to receive the new OTA firmware sending from the OTA client via TCP socket.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void beginOTA(int port);

**Parameters**
~~~~~~~~~~~~~~

port: port number for the OTA MDNS IP address, default port address is 8082.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `OTA_Basic <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/OTA/examples/OTA_Basic/OTA_Basic.ino>`_

.. note :: Configures and registers the MDNS service required for the Arduino IDE to discover and recognize Ameba OTA. "OTA.h" must be included to use the class function.

**OTA::start_OTA_threads**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Starts the connect of OTA server and waiting to receive the new OTA firmware sending from the OTA client via TCP socket.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void start_OTA_threads(int port, char *server);

**Parameters**
~~~~~~~~~~~~~~

port: port number for the OTA HTTP server IP address, default port address is 3000.

\*server: pointer for OTA HTTP server IP address.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `OTA_Http <https://github.com/Ameba-AIoT/ameba-arduino-d/blob/dev/Arduino_package/hardware/libraries/OTA/examples/OTA_Http/OTA_Http.ino>`_

