#bridge_data.py
"""



"""
import os
import logging
import zipfile
import bridge_date


no_hostkey_error_message = """

To use this program you need to make sure the sftp server's key is registered on the machine.


If you get an error that looks like this 
paramiko.ssh_exception.SSHException: No hostkey for host co-ftp01.cps.k12.il.us found.

"""
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def get_zipped_file_name(basepath):
    date_path = bridge_date.get_date_path()
    return os.path.join(basepath,"export","extract"+date_path+".dat")

def get_data_path(basepath):
    date_path = bridge_date.get_date_path()
    return     os.path.join(basepath,"export","tmp",date_path)

def create_zip_file(basepath):
    """
    Create a file called extractYYYYMMDD.dat that is a zipped file
    of data extracted.
    """
    logging.info("create zip file")
    data_path =  get_data_path(basepath)
    zipped_file = get_zipped_file_name(basepath)

    zipf = zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED)
    zipdir(data_path, zipf)
    zipf.close()

def send_zip_file_to_ftp(basepath, ftp_configuration):
    """
    Create a file called extractYYYYMMDD.dat that is a zipped file
    of data extracted.
    """
    logging.info("sending zip file to ftp")

    import pysftp
    from paramiko import ssh_exception
    try:
        with pysftp.Connection(ftp_configuration['address']
            , username=ftp_configuration['username']
            , password=ftp_configuration['password']) as sftp:

            with sftp.cd(ftp_configuration['remotePath']):
                sftp.put(get_zipped_file_name(basepath))
    except ssh_exception.SSHException  as err:
        error_string = err.__str__()
        if error_string.find("No hostkey for host") !=-1:
            logging.error("To run bridge to connect to an ftp server with SSH, please setup the host")
        else:
            raise(err)
def send(configuration):
    """
    """
    create_zip_file(configuration['basepath'])
    send_zip_file_to_ftp(configuration['basepath'],configuration['ftp'])