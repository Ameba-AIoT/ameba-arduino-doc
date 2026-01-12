Class HttpClient
================

**HttpClient Class**
--------------------

**Description**
~~~~~~~~~~~~~~~

A class to use HttpClient

**Syntax**
~~~~~~~~~~

.. code:: c++

  class HttpClient

**Members**
~~~~~~~~~~~

+---------------------------------+-----------------------------------+
| **Public Constructors**         |                                   |
+=================================+===================================+
| HttpClient::HttpClient          | Constructs a HttpClient object    |
+---------------------------------+-----------------------------------+
| **Public Methods**              |                                   |
+---------------------------------+-----------------------------------+
| HttpClient::stop                | Disconnect from the server        |
+---------------------------------+-----------------------------------+
| HttpClient::beginRequest        | Start a more complex request      |
+---------------------------------+-----------------------------------+
| HttpClient::startRequest        | Connect to the server and start   |
|                                 | to send the request               |
+---------------------------------+-----------------------------------+
| HttpClient::sendHeader          | Send an additional header line    |
+---------------------------------+-----------------------------------+
| HttpClient::sendBasicAuth       | Send a basic authentication header|
+---------------------------------+-----------------------------------+
| HttpClient::finishHeaders       | Let the server know that we've    |
|                                 | reached the end of the headers    |
+---------------------------------+-----------------------------------+
| HttpClient::endRequest          | End a more complex request        |
+---------------------------------+-----------------------------------+
| HttpClient::responseStatusCode  | Get the HTTP status code          |
|                                 | contained in the response         |
+---------------------------------+-----------------------------------+
| HttpClient::get                 | Connect to the server and start   |
|                                 | to send a GET request             |
+---------------------------------+-----------------------------------+
| HttpClient::post                | Connect to the server and start   |
|                                 | to send a POST request            |
+---------------------------------+-----------------------------------+
| HttpClient::put                 | Connect to the server and start   |
|                                 | to send a PUT request             |
+---------------------------------+-----------------------------------+
| HttpClient::skipResponseHeaders | Skip any response headers to get  |
|                                 | to the body                       |
+---------------------------------+-----------------------------------+
| HttpClient::endOfBodyReached    | Check whether the end of the body |
|                                 | has been reached                  |
+---------------------------------+-----------------------------------+
| HttpClient::read                | Returns the incoming byte from the|
|                                 | server that the client is         |
|                                 | connected to                      |
+---------------------------------+-----------------------------------+
| HttpClient::readHeader          | Read the next character of the    |
|                                 | response headers                  |
+---------------------------------+-----------------------------------+
| HttpClient::finishRequest       | Finish sending the HTTP request   |
+---------------------------------+-----------------------------------+
| HttpClient::endOfHeadersReached | The function reads the next       |
|                                 | character of the response headers |
+---------------------------------+-----------------------------------+
| HttpClient::endOfStream         | Check whether the end of the body |
|                                 | has been reached                  |
+---------------------------------+-----------------------------------+
| HttpClient::completed           | Check whether the end of the body |
|                                 | has been reached                  |
+---------------------------------+-----------------------------------+
| HttpClient::contentLength       | This function returns the length  |
|                                 | of the body                       |
+---------------------------------+-----------------------------------+
| HttpClient::available           | Get the number of bytes available |
|                                 | for reading                       |
+---------------------------------+-----------------------------------+
| HttpClient::connected           | Check if client is connected      |
+---------------------------------+-----------------------------------+

--------------------------------------------------

**HttpClient::HttpClient**
--------------------------

**Description**
~~~~~~~~~~~~~~~

Constructs a HttpClient object. The Marco "PROXY_ENABLED" is defined and currently disabled as introduces a dependency on DNS.h in Ethernet.

**Syntax**
~~~~~~~~~~

.. code:: c++

  HttpClient(Client& aClient, const char* aProxy = NULL, uint16_t aProxyPort);

.. code:: c++

  HttpClient(Client& aClient);

**Parameters**
~~~~~~~~~~~~~~

``aClient``: The object of class WiFiClient.

``aProxy``: The proxy name. (The default proxy name is set to "NULL")

``aProxyPort``: The proxy port. (Default value: 0)

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included must be included to use the class function.

----------------------------------------------------

**HttpClient::stop**
--------------------

**Description**
~~~~~~~~~~~~~~~

Disconnect from the server and reset the status.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void stop(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "HttpClient.h" must be included to use the class function.

-----------------------------------------------------------------

**HttpClient::beginRequest**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Start a more complex request. Use this when you need to send additional headers in the request, but you will also need to call endRequest() when you are finished.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void beginRequest(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------------------------------------

**HttpClient::startRequest**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Connect to the server and start to send the request.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int startRequest(const char* aServerName,uint16_t    aServerPort,const char* aURLPath, const char* aHttpMethod, const char* aUserAgent);

.. code:: c++

  int startRequest(const IPAddress& aServerAddress, const char* aServerName, uint16_t    aServerPort, const char* aURLPath, const char* aHttpMethod, const char* aUserAgent);

**Parameters**
~~~~~~~~~~~~~~

``aServerAddress``: IP address of the server to connect to.

``aServerName``: Name of the server being connected to. If NULL, the "Host" header line won't be sent.

``aServerPort``: Port to connect to on the server.

``aURLPath``: Url to request.

``aHttpMethod``: Type of HTTP request to make, e.g. "GET", "POST", etc.

``aUserAgent``: User-Agent string to send. If NULL the default user-agent kUserAgent will be sent.

**Returns**
~~~~~~~~~~~

This function returns 0 if successful, else returns error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

---------------------------------------------------------

**HttpClient::sendHeader**
--------------------------

**Description**
~~~~~~~~~~~~~~~

The function sends an additional header line.
The function can only be called in between startRequest and finishRequest functions.

The other 2 functions,
void sendHeader(const char* aHeaderName, const char* aHeaderValue);
void sendHeader(const char* aHeaderName, const int aHeaderValue);
are alternate form from the void HttpClient::sendHeader(const char* aHeader); which takes the header name and content as separate strings. The call will add the ":" in the log to separate different header in the case of multiple headers.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void sendHeader(const char* aHeader);

.. code:: c++

  void sendHeader(const char* aHeaderName, const char* aHeaderValue);

.. code:: c++

  void sendHeader(const char* aHeaderName, const int aHeaderValue);

**Parameters**
~~~~~~~~~~~~~~

``aHeader`` : Header line to send, in its entirety (but without the trailing CRLF. E.g. "Authorization: Basic YQDDCAIGES".

``aHeaderName`` : Type of header being sent.

``aHeaderValue`` : Value for that header.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

-----------------------------

**HttpClient::sendBasicAuth**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

The function sends a basic authentication header which will encode the given username and password, and send them in a suitable header line for doing Basic Authentication.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void sendBasicAuth(const char* aUser, const char* aPassword);

**Parameters**
~~~~~~~~~~~~~~

``aUser``: Username for the authorization.

``aPassword`` : Password for the user aUser.

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::finishHeaders**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Let the server know that we've reached the end of the headers

**Syntax**
~~~~~~~~~~

.. code:: c++

  void finishHeaders(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::get**
-------------------

**Description**
~~~~~~~~~~~~~~~

Connect to the server and start to send a "GET" request. If the input parameter contains "aServerAddress", DNS lookup will not be performed and just purely connect to the given IP address.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int get(const char* aServerName, uint16_t aServerPort, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int get(const char* aServerName, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int get(const IPAddress& aServerAddress, const char* aServerName, uint16_t aServerPort, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int get(const IPAddress& aServerAddress, const char* aServerName, const char* aURLPath, const char* aUserAgent = NULL);

**Parameters**
~~~~~~~~~~~~~~

``aServerName``: The name of the server being connected to. If aServerName is "NULL", the "Host" header line will not be sent.

``aServerPort``: The port on which server connected.

``aURLPath``: The URL to request.

``aUserAgent``: User-Agent string to be sent. If aUserAgent indicated as "NULL", the default user-agent kUserAgent will be sent.

``aServerAddress``: IP address of the server to connect to.

**Returns**
~~~~~~~~~~~

This function returns 0 if successful, else returns an error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

----------------------------------------------------------------

**HttpClient::post**
--------------------

**Description**
~~~~~~~~~~~~~~~

Connect to the server and start to send a "POST" request. If the input parameter has "aServerAddress", DNS lookup will not be performed and just purely connect to the given IP address.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int post(const char* aServerName, uint16_t aServerPort, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int post(const char* aServerName, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int post(const IPAddress& aServerAddress, const char* aServerName, uint16_t aServerPort, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int post(const IPAddress& aServerAddress,const char* aServerName,  const char* aURLPath, const char* aUserAgent = NULL);

**Parameters**
~~~~~~~~~~~~~~

``aServerName``: Name of the server being connected to. If NULL, the "Host" header line won't be sent.

``aServerPort``: Port to connect to on the server.

``aURLPath``: Url to request.

``aUserAgent``: User-Agent string to be sent. If aUserAgent indicated as "NULL", the default user-agent kUserAgent will be sent. Default value: NULL.

``aServerAddress``: IP address of the server to connect to.

**Returns**
~~~~~~~~~~~

This function returns 0 if successful, else returns error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

----------------------------------------------------------------

**HttpClient::put**
-------------------

**Description**
~~~~~~~~~~~~~~~

Connect to the server and start to send a PUT request. If the input parameter has "aServerAddress", DNS lookup will not be performed and just connect to the given IP address.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int put(const char* aServerName, uint16_t aServerPort,const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int put(const char* aServerName, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int put(const IPAddress& aServerAddress,const char* aServerName, uint16_t aServerPort, const char* aURLPath, const char* aUserAgent = NULL);

.. code:: c++

  int put(const IPAddress& aServerAddress,const char* aServerName, const char* aURLPath, const char* aUserAgent = NULL);

**Parameters**
~~~~~~~~~~~~~~

``aServerName``: Name of the server being connected to. If NULL, the "Host" header line won't be sent.

``aServerPort``: Port to connect to on the server.

``aURLPath``: Url to request.

``aUserAgent``: User-Agent string to be sent. If aUserAgent indicated as "NULL", the default user-agent kUserAgent will be sent. Default value: NULL.

``aServerAddress``: IP address of the server to connect to.

**Returns**
~~~~~~~~~~~

This function returns 0 if successful, else returns error.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

----------------------------------------------------------------

**HttpClient::endOfHeadersReached**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Check whether the end of the headers have been reached. Test whether all of the response headers have been consumed.

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool endOfHeadersReached(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "true" if the end of response header has reached and we are now processing the response body, else returns "false".

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------

**HttpClient::endRequest**
--------------------------

**Description**
~~~~~~~~~~~~~~~

End a more complex request. Use this when you need to have sent additional headers in the request, but you will also need to call beginRequest() at the start.

**Syntax**
~~~~~~~~~~

.. code:: c++

  void endRequest(void);;

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

NA

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

---------------------------------------------------------------

**HttpClient::responseStatusCode**
----------------------------------

**Description**
~~~~~~~~~~~~~~~

Get the HTTP status code contained in the response. For example, "200" for successful requests, "404" for file not found, etc.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int responseStatusCode(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns 0 indicates "HTTP_SUCCESS", else returns other negative error codes.

  1. HTTP_ERROR_CONNECTION_FAILED
  2. HTTP_ERROR_API
  3. HTTP_ERROR_TIMED_OUT
  4. HTTP_ERROR_INVALID_RESPONSE

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

---------------------------------------

**HttpClient::skipResponseHeaders**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

Skip any response headers to get to the body. Use this if you don't want to do any special processing of the headers returned in the response. You can also use it after you've found all of the headers you're interested in, and just want to get on with processing the body.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int skipResponseHeaders();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns 0 indicates "HTTP_SUCCESS", else returns other negative error codes.

  1. HTTP_ERROR_CONNECTION_FAILED
  2. HTTP_ERROR_API
  3. HTTP_ERROR_TIMED_OUT
  4. HTTP_ERROR_INVALID_RESPONSE

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

-----------------------------------------------------

**HttpClient::endOfBodyReached**
--------------------------------

**Description**
~~~~~~~~~~~~~~~

Check whether the end of the body has been reached. It only works if the Content-Length header was returned by the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool endOfBodyReached(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if the end of the body has been reached, else false.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::read**
--------------------

**Description**
~~~~~~~~~~~~~~~

Returns the incoming byte recving from the server that the client is connected to.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int read ();

.. code:: c++

  int read(uint8_t *buf, size_t size);

**Parameters**
~~~~~~~~~~~~~~

``buf``: buffer to hold incoming byte

``size``: maximum size of the buffer

**Returns**
~~~~~~~~~~~

Returns the incoming byte from the server that the client is connected to.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

-------------------------------------------------

**HttpClient::readHeader**
--------------------------

**Description**
~~~~~~~~~~~~~~~

The function reads the next character of the response headers. This function is the same as read() but to be used when reading through the headers which are slightly less efficient. The user might check whether the end of the headers has been reached by calling endOfHeadersReached(), although after endOfHeadersReached() is called, data return will be the same as read().

**Syntax**
~~~~~~~~~~

.. code:: c++

  int readHeader(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the next character of the response headers.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

-------------------------------------------------

**HttpClient::finishRequest**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

Finish sending the HTTP request.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int finishRequest(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the blank line to signify the end of the request

**Example Code**
~~~~~~~~~~~~~~~~

NA

.. note :: "HttpClient.h" must be included to use the class function.

--------------------------------

**HttpClient::endOfHeadersReached**
-----------------------------------

**Description**
~~~~~~~~~~~~~~~

The function reads the next character of the response headers. This function is the same as read() but to be used when reading through the headers which are slightly less efficient. The user might check whether the end of the headers has been reached by calling endOfHeadersReached(), although after endOfHeadersReached() is called, data return will be the same as read().

**Syntax**
~~~~~~~~~~

.. code:: c++

  int endOfHeadersReached();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if we are at the end of the header, else false.

**Example Code**
~~~~~~~~~~~~~~~~

.. note :: "HttpClient.h" must be included to use the class function.

----------------------------------

**HttpClient::endOfStream**
----------------------------

**Description**
~~~~~~~~~~~~~~~

Check whether the end of the body has been reached. It only works if the Content-Length header was returned by the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool endOfStream(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if the end of the body has been reached, else false.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::completed**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Check whether the end of the body has been reached. It only works if the Content-Length header was returned by the server.

**Syntax**
~~~~~~~~~~

.. code:: c++

  bool completed(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns true if the end of the body has been reached, else false.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::contentLength**
-----------------------------

**Description**
~~~~~~~~~~~~~~~

This function returns the length of the body.

**Syntax**
~~~~~~~~~~

.. code:: c++

  int contentLength(void);

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns the length of the body (in bytes) or kNoContentLengthHeader if no Content-Length header was returned by the server.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::available**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Get the number of bytes available for reading

**Syntax**
~~~~~~~~~~

.. code:: c++

  int available();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns 1 and number of bytes available for reading if there are available data, else returns 0.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.

------------------------------------

**HttpClient::connected**
-------------------------

**Description**
~~~~~~~~~~~~~~~

Check if the client is connected

**Syntax**
~~~~~~~~~~

.. code:: c++

  Uint_8 connected();

**Parameters**
~~~~~~~~~~~~~~

NA

**Returns**
~~~~~~~~~~~

This function returns "1" if connected, returns "0" if not connected.

**Example Code**
~~~~~~~~~~~~~~~~

Example: `SimpleHttpExample <https://github.com/ambiot/ambd_arduino/blob/dev/Arduino_package/hardware/libraries/Http/examples/SimpleHttpExample/SimpleHttpExample.ino>`_

.. note :: "HttpClient.h" must be included to use the class function.
