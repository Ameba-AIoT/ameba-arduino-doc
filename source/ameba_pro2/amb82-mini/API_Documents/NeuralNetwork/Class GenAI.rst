Class GenAI
===========

.. contents::
  :local:
  :depth: 2

**GenAI Class**
---------------

**Description**
~~~~~~~~~~~~~~~

A class used to call online GenAI API to perform various tasks.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    class GenAI

**Members**
~~~~~~~~~~~

+------------------------------------+--------------------------------------------------------------+
| **Public Constructors**                                                                           |
+====================================+==============================================================+
| GenAI::GenAI                       | Constructs a GenAI object.                                   |
+------------------------------------+--------------------------------------------------------------+
| **Public Methods**                                                                                |
+------------------------------------+--------------------------------------------------------------+
| GenAI::openaivision                | Send image to OpenAI server and receive response             |
+------------------------------------+--------------------------------------------------------------+
| GenAI::geminivision                | Send image to Gemini server and receive response             |
+------------------------------------+--------------------------------------------------------------+
| GenAI::llamavision                 | Send image to Groq server and receive response               |
+------------------------------------+--------------------------------------------------------------+
| GenAI::whisperaudio                | Send audio to openAI or groq server and receive response     |
+------------------------------------+--------------------------------------------------------------+
| GenAI::googletts                   | Perform TTS using Google TTS API and save audio to           |
|                                    | SD card as MP3 file                                          |
+------------------------------------+--------------------------------------------------------------+

**GenAI::openaivision**
-----------------------
**Description**
~~~~~~~~~~~~~~~

Send image to OpenAI server and receive response.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    String openaivision(String key, String model, String message, uint32_t img_addr, uint32_t img_len, WiFiSSLClient client);

**Parameters**
~~~~~~~~~~~~~~

| key: OpenAI API key
| model: LLM model
| message: Prompt message
| img_addr: Captured image address
| img_len: Size of the captured image
| client: WiFi SSL Client object

**Returns**
~~~~~~~~~~~

Response from LLM model

**Example Code**
~~~~~~~~~~~~~~~~

Example: `GenAIVision <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/MultimediaAI/GenAIVision/GenAIVision.ino>`_

**GenAI::geminivision**
-----------------------
**Description**
~~~~~~~~~~~~~~~

Send image to Gemini server and receive response.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    String geminivision(String key, String model, String message, uint32_t img_addr, uint32_t img_len, WiFiSSLClient client);

**Parameters**
~~~~~~~~~~~~~~

| key: Gemini API key
| model: LLM model
| message: Prompt message
| img_addr: Captured image address
| img_len: Size of the captured image
| client: WiFi SSL Client object

**Returns**
~~~~~~~~~~~

Response from LLM model

**Example Code**
~~~~~~~~~~~~~~~~

Example: `GenAIVision <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/MultimediaAI/GenAIVision/GenAIVision.ino>`_

**GenAI::llamavision**
-----------------------
**Description**
~~~~~~~~~~~~~~~

Send image to OpenAI server and receive response.

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    String llamavision(String key, String model, String message, uint32_t img_addr, uint32_t img_len, WiFiSSLClient client);

**Parameters**
~~~~~~~~~~~~~~

| key: Groq API key
| model: LLM model
| message: Prompt message
| img_addr: Captured image address
| img_len: Size of the captured image
| client: WiFi SSL Client object

**Returns**
~~~~~~~~~~~

Response from LLM model

**Example Code**
~~~~~~~~~~~~~~~~

Example: `GenAIVision <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/MultimediaAI/GenAIVision/GenAIVision.ino>`_

**GenAI::whisperaudio**
-----------------------
**Description**
~~~~~~~~~~~~~~~

Send audio to openAI or groq server and receive response 

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    String whisperaudio(String api_key, char* api_server, String api_path, String model, String filename, WiFiSSLClient client);

**Parameters**
~~~~~~~~~~~~~~

| api_key: OpenAI or Groq API key
| api_server: Online LLM API server 
| api_path: API endpoint
| model: LLM model
| filename: audio filename
| client: WiFi SSL Client object

**Returns**
~~~~~~~~~~~

Response from LLM model

**Example Code**
~~~~~~~~~~~~~~~~

Example: `GenAISpeech <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/MultimediaAI/GenAISpeech/GenAISpeech.ino>`_

**GenAI::googletts**
-----------------------
**Description**
~~~~~~~~~~~~~~~

Perform TTS using Google TTS API and save audio to SD card as MP3 file

**Syntax**
~~~~~~~~~~

.. code-block:: c++

    void googletts(String filename_mp3, String message, String lang);

**Parameters**
~~~~~~~~~~~~~~

| filename_mp3: Speech audio filename
| message: Text message to perform TTS
| lang: Language code

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `Text-to-Speech <https://github.com/Ameba-AIoT/ameba-arduino-pro2/blob/dev/Arduino_package/hardware/libraries/NeuralNetwork/examples/MultimediaAI/Text-to-Speech/Text-to-Speech.ino>`_
