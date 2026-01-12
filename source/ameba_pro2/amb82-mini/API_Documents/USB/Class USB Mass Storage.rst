Class USB Mass Storage
=======================

**USB Mass Storage Class**
---------------------------

**Description**
~~~~~~~~~~~~~~~

A class for USB Mass Storage API.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class USBMassStorage

**Members**
~~~~~~~~~~~

+------------------------------------------+-------------------------------------+
| **Public Constructors**                                                        |
+==========================================+=====================================+
| USBMassStorage::USBMassStorage           | Constructs a USBMassStorage object. |
|                                          | Initialize/Re-initialize of         |
|                                          | using USB Mass Storage device.      |
+------------------------------------------+-------------------------------------+
| **Public Methods**                                                             |
+------------------------------------------+-------------------------------------+
| USBMassStorage::USBInit                  | Initialize the USB hardware.        |
+------------------------------------------+-------------------------------------+
| USBMassStorage::SDIOInit                 | Initialize the SDIO and related     |
|                                          | GPIOs for SD card access.           |
+------------------------------------------+-------------------------------------+
| USBMassStorage::USBStatus                | Check the USB connection and        |
|                                          | initialization status.              |
+------------------------------------------+-------------------------------------+
| USBMassStorage::initializeDisk           | Initialize disk operations for USB  |
|                                          | Mass Storage.                       |
+------------------------------------------+-------------------------------------+
| USBMassStorage::loadUSBMassStorageDriver | Load and initialize the USB         |
|                                          | Mass Storage Class (MSC) driver.    |
+------------------------------------------+-------------------------------------+
| USBMassStorage::USBDeinit                | Deinitialize the USB MSC driver     |
|                                          | and free allocated resources.       |
+------------------------------------------+-------------------------------------+
| USBMassStorage::isConnected              | Check whether a USB host is         |
|                                          | connected.                          |
+------------------------------------------+-------------------------------------+

**USBMassStorage::USBMassStorage**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a USBMassStorage object. Initialize/Re-initialize of using USB Mass Storage device.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    USBMassStorage(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::USBInit**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize the USB hardware.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void USBInit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::SDIOInit**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize the SDIO and related GPIOs for SD card access.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void SDIOInit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::USBStatus**
-------------------------------

**Description**
~~~~~~~~~~~~~~~

Check the USB connection and initialization status.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    int USBStatus(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the USB status.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::initializeDisk**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Initialize disk operations for USB Mass Storage.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void initializeDisk(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::loadUSBMassStorageDriver**
---------------------------------------------

**Description**
~~~~~~~~~~~~~~~

Load and initialize the USB Mass Storage Class (MSC) driver

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void loadUSBMassStorageDriver(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::USBDeinit**
------------------------------

**Description**
~~~~~~~~~~~~~~~

Deinitialize the USB MSC driver and free allocated resources.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void USBDeinit(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "USBMassStorage.h" must be included to use the class function.

**USBMassStorage::isConnected**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Check whether a USB host is connected.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void isConnected(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the USB attach status, indicating whether a USB device is currently connected (attached) or not.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `USB_Mass_Storage <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/USB/examples/USB_Mass_Storage/USB_Mass_Storage.ino>`_

.. note :: "USBMassStorage.h" must be included to use the class function.
