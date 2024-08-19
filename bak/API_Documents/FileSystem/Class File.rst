**File Class**

**Description**

A class for data manipulation of files in a file system.

| **Syntax**
| class File

**Members**

**Public Constructors**

+---------------------------+------------------------------------------+
| File::File                | Constructs a File object                 |
+===========================+==========================================+
+---------------------------+------------------------------------------+

**Public Methods**

+---------------------------+------------------------------------------+
| File::open                | Open a file from the filesystem          |
+===========================+==========================================+
| File::close               | Close a previously opened file           |
+---------------------------+------------------------------------------+
| File::write               | Write data to the currently open file    |
+---------------------------+------------------------------------------+
| File::read                | Read data from the currently open file   |
+---------------------------+------------------------------------------+
| File::peek                | Peek at the next data byte from the      |
|                           | currently open file                      |
+---------------------------+------------------------------------------+
| File::available           | Check number of bytes remaining till end |
|                           | of file                                  |
+---------------------------+------------------------------------------+
| File::flush               | Flush cached data                        |
+---------------------------+------------------------------------------+
| File::seek                | Move read write pointer                  |
+---------------------------+------------------------------------------+
| File::position            | Get current read write pointer           |
+---------------------------+------------------------------------------+
| File::size                | Get file size                            |
+---------------------------+------------------------------------------+
| File::isOpen              | Check if a file is currently open        |
+---------------------------+------------------------------------------+
| File::name                | Get currently open file name             |
+---------------------------+------------------------------------------+

**File::File**

**Description**

Constructs a File object.

**Syntax**

File::File(void);

File::File(const char\* filename);

| **Parameters**
| filename: pointer to a char array containing the path of the file to
  open

| **Returns**
| NA

| **Example Code**
| Example: CreateFolder
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.


**File::open**

**Description**

Open a file from the file system.

**Syntax**

bool open(const char\* filename);

| **Parameters**
| filename: pointer to a char array containing the path of the file to
  open

**Returns**

This function returns true if the file is opened successfully, false
otherwise.

**Example Code**

NA\ [STRIKEOUT:
]

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.


**File::close**

| **Description**
| Close a previously opened file.

**Syntax**

void close(void);

**Parameters**

NA

| **Returns**
| NA

| **Example Code**
| Example: CreateFolder
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function. Opened
files need to be closed to ensure that any pending data is saved
correctly.


**File::write**

| **Description**
| Write data to the currently open file.

**Syntax**

size_t write(uint8_t c);

size_t write(const uint8_t\* buf, size_t size);

size_t write(const char\* str;

size_t write(const char\* buf, size_t size);

**Parameters**

c: single data byte to write

str: pointer to char array containing data to write, expressed as a null
terminated string

buf: pointer to array containing data to write

size: number of bytes to write

| **Returns**
| This function returns the number of data bytes written to file.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.


**File::read**

| **Description**
| Read data from the currently open file.

**Syntax**

int read(void);

int read(void\* buf, size_t size);

| **Parameters**
| buf: pointer to buffer to store read data.

size: number of data bytes to read.

**Returns**

When a buffer pointer is not used, this function returns the data byte
read if successful, otherwise it returns -1.

When a buffer pointer is used, this function returns the number of bytes
read.

| **Example Code**
| Example: CreateFolder
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.


**File::peek**

| **Description**
| Peek at the next data byte from the currently open file.

**Syntax**

int peek(void);

**Parameters**

NA

**Returns**

This function returns the next data byte if successful, otherwise it
returns -1.

**Example Code**

NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.


**File::available**

| **Description**
| Check number of bytes remaining till end of file.

**Syntax**

int available(void);

| **Parameters**
| NA

**Returns**

This function returns the number of bytes available to read until the
end of file.

| **Example Code**
| Example: ReadHTMLFile

(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/ReadHTMLFile/ReadHTMLFile.ino)

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.

**File::flush**

| **Description**
| Flush cached data.

**Syntax**

void flush(void);

| **Parameters**
| NA

**Returns**

This function flushes any cached data and writes all pending data into
file.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.

**File::seek**

| **Description**
| Move the file read/write pointer of the currently open file.

**Syntax**

bool seek(uint32_t pos);

| **Parameters**
| pos: file position to move to

**Returns**

This function returns true if the file pointer is move successfully,
false otherwise.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function. If the
target position is larger than the size of the currently open file, the
file size will be increased as required.

**File::position**

| **Description**
| Get the read/write pointer of the currently open file.

**Syntax**

uint32_t position(void);

| **Parameters**
| NA

**Returns**

This function returns the current file read/write position.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.

**File::size**

| **Description**
| Get the size of the currently open file.

**Syntax**

uint32_t size(void);

| **Parameters**
| NA

**Returns**

This function returns the size of the currently open file.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.

**File::isOpen**

| **Description**
| Check if a file is currently open.

**Syntax**

bool isOpen(void);

| **Parameters**
| NA

**Returns**

This function returns true if a file is currently open, false otherwise.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.

**File::name**

| **Description**
| Get the filename of the currently open file.

**Syntax**

const char\* name(void);

| **Parameters**
| NA

**Returns**

This function returns a pointer to a character array containing the
filename of the currently open file. If no file is open, it returns
NULL.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFSFile.h” must be included to use the class function.
