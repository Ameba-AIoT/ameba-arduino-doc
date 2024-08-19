**AmebaFatFS Class**

**Description**

A class for file management using FatFS File system.

| **Syntax**
| class AmebaFatFS

**Members**

**Public Constructors**

+---------------------------+------------------------------------------+
| AmebaFatFS::AmebaFatFS    | Constructs a AmebaFatFS object           |
+===========================+==========================================+
+---------------------------+------------------------------------------+

**Public Methods**

+---------------------------+------------------------------------------+
| AmebaFatFS::begin         | Initialize file system                   |
+===========================+==========================================+
| AmebaFatFS::end           | Deinitialize file system                 |
+---------------------------+------------------------------------------+
| AmebaFatFS::open          | Open a file                              |
+---------------------------+------------------------------------------+
| AmebaFatFS::exists        | Check if a file or folder exists         |
+---------------------------+------------------------------------------+
| AmebaFatFS::remove        | Delete a file or folder                  |
+---------------------------+------------------------------------------+
| AmebaFatFS::rename        | Rename a file or folder                  |
+---------------------------+------------------------------------------+
| AmebaFatFS::mkdir         | Create a new folder                      |
+---------------------------+------------------------------------------+
| AmebaFatFS::rmdir         | Delete a file or folder                  |
+---------------------------+------------------------------------------+
| AmebaFatFS::getRootPath   | Get the file system root path            |
+---------------------------+------------------------------------------+
| AmebaFatFS::readDir       | List files and folders in a directory    |
+---------------------------+------------------------------------------+
| AmebaFatFS::isDir         | Check if a path is a folder              |
+---------------------------+------------------------------------------+
| AmebaFatFS::isFile        | Check if a path is a file                |
+---------------------------+------------------------------------------+
| A                         | Retrieve last modified timestamp of a    |
| mebaFatFS::getLastModTime | file or folder                           |
+---------------------------+------------------------------------------+
| A                         | Set last modified timestamp of a file or |
| mebaFatFS::setLastModTime | folder                                   |
+---------------------------+------------------------------------------+
| AmebaFatFS::status        | Check if the file system is initialized  |
+---------------------------+------------------------------------------+


**AmebaFatFS::AmebaFatFS**

| **Description**
| Constructs a AmebaFatFS object.

**Syntax**

AmebaFatFS::AmebaFatFS(void)

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: CreateFolder
(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::begin**

| **Description**
| Initialize the file system.

**Syntax**

bool begin(void);

**Parameters**

NA

**Returns**

This function returns true if file system initialization is successful,
otherwise false.

**Example Code**

Example: CreateFolder
(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::end**

| **Description**
| Deinitialize the file system.

**Syntax**

void end(void);

**Parameters**

NA

**Returns**

NA

**Example Code**

Example: CreateFolder
(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.\ **

**AmebaFatFS::open**

| **Description**
| Open a file. The file will be created if it does not already exist.

**Syntax**

File open(const String& path);

File open(const char\* path);

| **Parameters**
| path: The full path of the file to open. Expressed as a String class
  object or a pointer to a char array.

**Returns**

This function returns a File class object corresponding to the opened
file.

| **Example Code**
| Example: CreateFolder
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::exists**

**Description**

Check if a file or folder exists.

**Syntax**

bool exists(const String& path);

bool exists(const char\* path);

**Parameters**

path: The full path of the file or folder to check. Expressed as a
String class object or a pointer to a char array.

**Returns**

This function returns true if the path exists, otherwise false.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::remove**

| **Description**
| Delete a file or folder.

**Syntax**

bool remove(const String& path);

bool remove(const char\* path);

**Parameters**

path: The full path of the file or folder to remove. Expressed as a
String class object or a pointer to a char array.

**Returns**

This function returns true if the file or folder is deleted
successfully, otherwise false.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::rename**

| **Description**
| Rename a file or folder.

**Syntax**

bool rename(const String& pathFrom, const String& pathTo);

bool rename(const char\* pathFrom, const char\* pathTo);

**Parameters**

pathFrom: The full path of the file or folder to rename. Expressed as a
String class object or a pointer to a char array.

pathTo: The new path of the file or folder. Expressed as a String class
object or a pointer to a char array.

**Returns**

This function returns true if the file or folder is deleted
successfully, otherwise false.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::mkdir**

| **Description**
| Create a new folder.

**Syntax**

File mkdir(const String& path);

File mkdir(const char\* path);

| **Parameters**
| path: The full path of the folder to create. Expressed as a String
  class object or a pointer to a char array.

**Returns**

This function returns true if the folder is created successfully,
otherwise false.

| **Example Code**
| Example: CreateFolder
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::rmdir**

| **Description**
| Delete a file or folder.

**Syntax**

bool rmdir(const String& path);

bool rmdir(const char\* path);

**Parameters**

path: The full path of the file or folder to remove. Expressed as a
String class object or a pointer to a char array.

**Returns**

This function returns true if the file or folder is deleted
successfully, otherwise false.

| **Example Code**
| NA

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::getRootPath**

| **Description**
| Get the file system root path.

**Syntax**

char\* getRootPath(void);

| **Parameters**
| NA

| **Returns**
| This function a pointer to a character array containing the base root
  path of the current file system drive.

| **Example Code**
| Example: CreateFolder
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/CreateFolder/CreateFolder.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function. Mounted
logical volumes have names starting from ‘0’, thus the corresponding
root path would be “0:/”.


**AmebaFatFS::readDir**

**Description**

List files and folders in a directory.

**Syntax**

int readDir(char\* path, char\* result_buf, unsigned int bufsize);

**Parameters**

path: The full path of the directory to list. Expressed as a pointer to
a char array.

result_buf: Pointer to a char array buffer used to store results.

bufsize: Size of result buffer. Results exceeding the buffer size are
discarded.

**Returns**

This function returns “0” if completed successfully, otherwise it
returns a negative error code.

| **Example Code**
| Example: ListRootFiles
  (https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/ListRootFiles/ListRootFiles.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function. The names of
files and folders found in the target directory are returned in the
result buffer, separated by a null character ‘\\0’.


**AmebaFatFS::isDir**

| **Description**
| Check if a path is a folder.

**Syntax**

bool isDir(char\* path);

| **Parameters**
| path: The full path of the file or folder to check. Expressed as a
  pointer to a char array.

**Returns**

This function returns true if the path points to a folder, false
otherwise.

**Example Code**

Example: GetFileAttribute

(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/GetFileAttribute/GetFileAttribute.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::isFile**

| **Description**
| Check if a path is a file.

**Syntax**

bool isFile(char\* path);

| **Parameters**
| path: The full path of the file or folder to check. Expressed as a
  pointer to a char array.

**Returns**

This function returns true if the path points to a file, false
otherwise.

**Example Code**

Example: GetFileAttribute

(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/GetFileAttribute/GetFileAttribute.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::getLastModTime**

| **Description**
| Retrieve last modified timestamp of a file or folder.

**Syntax**

int getLastModTime(char\* path, uint16_t\* year, uint16_t\* month,
uint16_t\* date, uint16_t\* hour, uint16_t\* minute, uint16_t\* second);

| **Parameters**
| path: The full path of the file or folder to check. Expressed as a
  pointer to a char array.

year: Pointer to a uint16_t variable to store the year value of the last
modified time.

month: Pointer to a uint16_t variable to store the month value of the
last modified time.

date: Pointer to a uint16_t variable to store the date value of the last
modified time.

hour: Pointer to a uint16_t variable to store the hour value of the last
modified time.

minute: Pointer to a uint16_t variable to store the minute value of the
last modified time.

second: Pointer to a uint16_t variable to store the second value of the
last modified time.

**Returns**

This function returns “0” if completed successfully, otherwise it
returns a negative error code.

**Example Code**

Example: LastModifiedTime

(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/LastModifiedTime/LastModifiedTime.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::setLastModTime**

| **Description**
| Set last modified timestamp of a file or folder.

**Syntax**

int setLastModTime(char\* path, uint16_t year, uint16_t month, uint16_t
date, uint16_t hour, uint16_t minute, uint16_t second);

| **Parameters**
| path: The full path of the file or folder to check. Expressed as a
  pointer to a char array.

year: A uint16_t variable containing the year value of the last modified
time.

month: A uint16_t variable containing the month value of the last
modified time.

date: A uint16_t variable containing the date value of the last modified
time.

hour: A uint16_t variable containing the hour value of the last modified
time.

minute: A uint16_t variable containing the minute value of the last
modified time.

second: A uint16_t variable containing the second value of the last
modified time.

**Returns**

This function returns “0” if completed successfully, otherwise it
returns a negative error code.

**Example Code**

Example: LastModifiedTime

(https://github.com/ambiot/ambpro2_arduino/tree/dev/Arduino_package/hardware/libraries/FileSystem/examples/LastModifiedTime/LastModifiedTime.ino)

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.


**AmebaFatFS::status**

| **Description**
| Check if the file system is initialized.

**Syntax**

Int status(void);

| **Parameters**
| NA

**Returns**

This function returns 1 if the file system is initialized, 0 otherwise.

**Example Code**

NA

**Notes and Warnings**

“AmebaFatFS.h” must be included to use the class function.
