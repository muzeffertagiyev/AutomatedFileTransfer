from ftplib import FTP
import os

ftp_server = "ftp.dlptest.com"
ftp_user = "dlpuser"
ftp_pass = "rNrKYTX9g7z3RgJRmxWuGHbeu"

with FTP(ftp_server) as ftp:
    ftp.login(user=ftp_user, passwd=ftp_pass)


    path = './files'
    files = os.listdir(path)
    folder_name = ftp.mkd("BrainnestC5")
    ftp.cwd(folder_name)
    
    for file in files:
        with open(os.path.join(path,file), 'rb') as f:
            ftp.storbinary(f"STOR {file}", f)