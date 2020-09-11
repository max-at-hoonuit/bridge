Bridge
=====

The bridge tool runs SQL queries and sends the output to an sftp server.


How to Install
==============
1. Install Python
2. Install Python dependencies
3. Install Oracle Connection libraries
4. Setup Directories
5. Install scripts
6. Configure the conf.json file
6. Configure bridge_config.py file

Install Python
--------------------------
This installation requires Python 3.7 or higher

https://www.python.org/downloads/


Install scripts
---------------
Create a directory C:\Bridge\src

Place the python scripts into this directory 
```
bridge.py
bridge_config.py
bridge_date.py
bridge_extract.py
bridge_send.py
```

Install Python Dependencies
--------------------------
To install the dependencies run this:

```
pip install -r requirements.txt
```


Install Oracle Connection Libraries
--------------------------

Download the client zip file and then unzip the file to a directory

For more information see:
https://www.oracle.com/database/technologies/instant-client.html
https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html

For example if you unzip the file in c:\oracle it should  create "c:\oracle\instantclient_19_8\"

This is your instant_client_folder location. Note this for setting up the configuration.


Setup Directories
--------------------------

Create a base directory and three subdirectories following layout
```
C:\Bridge\base\
C:\Bridge\base\archive
C:\Bridge\base\export
C:\Bridge\base\sql
```



Configure the conf.json file
--------------------------

Edit a file called conf.json with this information
```
{
    "basepath": "C:\\Bridge\\base",
    "archiveSize": 15,
    "database": {
        "hostname": "localhost",
        "port": 1521,
        "service_name": "XEPDB1",
        "username": "scott",
        "password": "tiger"
    },
    "ftp": {
        "address": "co-ftp01.cps.k12.il.us",
        "username": "charter_data_bridge",
        "password": "xxxxxxxx",
        "remotePath": "/ftprootnew/charter_data_bridge/CICS_PS"
    }
}
```
Configure bridge_config.py file
------------------------------
Using the file editor, edit the file bridge_conf.py.  Set the field in the INSTANT_CLIENT_FOLDER

```
INSTANT_CLIENT_FOLDER = r"c:\oracle\instantclient_19_8"
```



Running the Process
====================
To run the process
Go to the directory and type
```
python bridge.py
```
