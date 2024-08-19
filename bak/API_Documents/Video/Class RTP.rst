RTP Class 
==========

Description
-----------

A class used to receive an audio data stream over a network using the
Real-time Transport Protocol (RTP). This allows streaming of an audio
stream from a computer to the development board.

Syntax
------

class RTP

**Members**
-----------

**Public Constructors**

+---------------------------+------------------------------------------+
| RTP::RTP                  | Constructs a RTP object.                 |
+===========================+==========================================+
+---------------------------+------------------------------------------+

**Public Methods**

+---------------------------+------------------------------------------+
| RTP::configPort           | Configure RTP network port.              |
+===========================+==========================================+
| RTP::begin                | Start RTP streaming.                     |
+---------------------------+------------------------------------------+
| RTP::end                  | Stop RTP streaming.                      |
+---------------------------+------------------------------------------+
| RTP::getPort              | Get RTP network port value.              |
+---------------------------+------------------------------------------+

RTP::configPort
===============

| **Description**
| Configure RTP network port.

| **Syntax**
| void configPort(uint16_t port);

| **Parameters**
| port: Desired network port for RTP. Default value of 5004.

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “RTP.h” must be included to use the class function.

RTP::begin
==========

| **Description**
| Start RTP streaming.

| **Syntax**
| void begin(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| RTPAudioStream

(https://github.com/ambiot/ambpro2_arduino/blob/dev/Arduino_package/hardware/libraries/Video/examples/Audio/RTPAudioStream/RTPAudioStream.ino)

| **Notes and Warnings**
| “RTP.h” must be included to use the class function.

RTP::end
========

| **Description**
| Stop RTP streaming.

| **Syntax**
| void end(void);

| **Parameters**
| NA

| **Returns**
| NA

| **Example Code**
| NA

| **Notes and Warnings**
| “RTP.h” must be included to use the class function.

RTP::getPort
============

| **Description**
| Get RTP stream network port.

| **Syntax**
| int getPort(void);

| **Parameters**
| NA

| **Returns**
| This function returns the port number as an integer.

| **Example Code**
| NA

| **Notes and Warnings**
| “RTP.h” must be included to use the class function.
