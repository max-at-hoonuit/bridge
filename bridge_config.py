#bridge_config.py

import json
## Change the instant_client_folder
INSTANT_CLIENT_FOLDER = r"c:\oracle\instantclient_19_8"

"""
{
	"basepath" : "C:\\work\\CICS_PS",
	"archiveSize" : 15,
    "database": {
        "hostname" : "localhost",
        "port" : "1521",
        "username" : "scott",
        "password": "tiger"
    },
    "ftp": {
        "address" : "co-ftp01.cps.k12.il.us",
        "username": "charter_data_bridge",
        "password": "1D3hht8e3huu02hYIpysGK/9b4YcoFHFwRrGKrbKxBY=",
        "remotePath": "/ftprootnew/charter_data_bridge/CICS_PS" ,
        "filePattern":".*dat"
    }
}

"""

def read_configuration(file_name):
    with open(file_name) as configuration_file:
        data = json.load(configuration_file)
    return data

def check_configuration(configuration_data):
    errors=[]
    if "basepath" not in configuration_data:
        errors.append('Missing basepath')
    if "archiveSize" not in configuration_data:
        errors.append('Missing archiveSize')
    if "database" not in configuration_data:
        errors.append('Missing database')
    else:
        database = configuration_data["database"]
        if "hostname" not in database:
            errors.append('Missing database hostname')
        if "port" not in database:
            errors.append('Missing database port')
        if "username" not in database:
            errors.append('Missing database username')
        if "password" not in database:
            errors.append('Missing database password')

    if "ftp" not in configuration_data:
        errors.append('Missing ftp')
    return errors

