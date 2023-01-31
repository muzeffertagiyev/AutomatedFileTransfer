from ftplib import FTP
import os
import shutil
import schedule
import time
from logging_transfer import LoggingService

ftp_server = "ftp.dlptest.com"
ftp_user = "dlpuser"
ftp_pass = "rNrKYTX9g7z3RgJRmxWuGHbeu"

local_dir = "./local_directory/documents/files_from_ftp"
internal_network_dir = "./internal_network_directory/data_from_ftp"

def file_transfer():
    logger = LoggingService()
    try:
        with FTP(ftp_server) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_pass)

            ftp.cwd("BrainnestC5")
            files = ftp.nlst()

            if not os.path.exists(local_dir):
                os.makedirs(local_dir)
            
            for file in files:
                with open(os.path.join(local_dir,file), 'wb') as f:
                    ftp.retrbinary(f"RETR {file}", f.write)

                shutil.move(os.path.join(local_dir,file),internal_network_dir)
        logger.log_info("files were transferred from ftp into internal network successfully")
    except Exception as exception:
        logger.log_error(f"Error : {exception}")


schedule.every().day.at("23:17").do(file_transfer)

while True:
    schedule.run_pending()
    time.sleep(1)

