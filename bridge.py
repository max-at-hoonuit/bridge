#
# data bridge II



"""
open configuration
    find location of export sql scripts
    find the intermediate directories
    connect to the database
    test connection to the ftp server

open database connection
    open the connect to the database
    
for_each_sql
package_zip_file
    collect up the files into a single zip file

send
    send the zipped file to an ftp location

"""
import click
import logging
import bridge_config
import bridge_extract
import bridge_send

def bridge_data(configuration_data):
    bridge_extract.extract(configuration_data)
    bridge_send.send(configuration_data)

@click.command()
@click.option('--configuration_file', default='config.json', help='Bridge configuration file.')
def run(configuration_file):
    """
    read the configuration file
    connect to the database, run sql and send data
    """
    configuration_data = bridge_config.read_configuration(configuration_file)
    configuration_errors = bridge_config.check_configuration(configuration_data)
    if (len(configuration_errors)==0):
        bridge_data(configuration_data)
    else:
        logging.error("Errors found in the configuration file "+ configuration_file)
        for error_message in configuration_errors:
            logging.error(error_message)


if __name__ == '__main__':
    run()