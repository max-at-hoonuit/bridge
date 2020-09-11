# bridge_extract.py
"""

"""
import path
from datetime import date
from os import listdir
from os.path import isfile, join
import csv
import cx_Oracle
import logging
import bridge_date
import bridge_config
cx_Oracle.init_oracle_client(lib_dir=bridge_config.INSTANT_CLIENT_FOLDER)

"""
https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#wininstall

https://www.oracle.com/database/technologies/instant-client.html
https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
"""


def get_sql_file(sql_directory):
    return_file = []
    for file in listdir(sql_directory):
        if file.endswith("extract.sql"):
            return_file.append(file)
    return return_file


def get_output_file_name(sql_file_name, base_path):
    """
    Create output path and file name based on the date
    and the sql file name 
    """
    date_path = bridge_date.get_date_path()
    import os

    if os.path.exists(join(base_path, "export")) == False:
        os.mkdir(join(base_path, "export"))
    if os.path.exists(join(base_path, "export", "tmp")) == False:
        os.mkdir(join(base_path, "export", "tmp"))
    if os.path.exists(join(base_path, "export", "tmp", date_path)) == False:
        os.mkdir(join(base_path, "export", "tmp", date_path))

    file_name = (
        sql_file_name.replace("extract.sql", "")
        .replace("_", " ")
        .strip()
        .replace(" ", "_")
        .upper()
    )
    return join(base_path, "export", "tmp", date_path, file_name)


def execute_sql(sql_file, database, base_path, write_header=False):
    """
    Extract the contents of a SQL file and save the output
    as tab delimited file to a temporary directory with the 
    output file named after the sql file.
    """
    logging.info("executing " + sql_file)

    dsn = cx_Oracle.makedsn(
        database["hostname"], database["port"], service_name=database["service_name"]
    )
    connection = cx_Oracle.connect(
        database["username"], database["password"], dsn, encoding="UTF-8"
    )
    cursor = connection.cursor()
    sql = ""
    with open(join(base_path, "sql", sql_file), "r") as opened_sql_file:
        for x in opened_sql_file:
            sql = sql + x
    cursor.execute(sql)
    out_file = get_output_file_name(sql_file, base_path)
    with open(out_file, "w", newline="") as file_out:
        writer = csv.writer(file_out, dialect="excel", delimiter="\t")
        if write_header:
            writer.writerow([i[0] for i in cursor.description])  # heading row
        writer.writerows(cursor.fetchall())


def extract(configuration):
    base_path = configuration["basepath"]
    database = configuration["database"]
    sql_files = get_sql_file(join(base_path, "sql"))
    for sql_file in sql_files:
        execute_sql(sql_file, database, base_path)
