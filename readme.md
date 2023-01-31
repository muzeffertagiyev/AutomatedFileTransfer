# Automated Email Sender

## About the project
It is used for a company to  automatically to transfer files from ftp server into their internal network. 

## Tech stack
- Backend technologies : 
    - Python v3.10.x or higher
    - Libraries
        - schedule
        - ftplib
        - shutil
        - time
        - os
        - logging

## About application
The project is divided to : 
   
- logging.py : Which deals with logging of transferring files. We create Class of LoggingService by using library of logging . it keeps track of the files that have been transferred and any errors that may have occurred during the transfer process.following details:
    
    - firstly we create file ,message format and date format by using basic.Config function from logging.
    - then we create tow functions one for success message another for error message,we will use them in the main.py. 

- main.py : It will transfer the transfer files from test ftp server which we have used.Please be informed that it is a test ftp server(https://dlptest.com/ftp-test/) and our uploaded files disappears after some time from the server,that is why we created a upload_files.py file in upload_files folder  for uploading test files into our test ftp server .following details:
    - We imported ftplib library for making connection with our ftp server:
    - We imported os library for working on directories in our pc.
    - We imported shutil library for transferring our downloaded files from local directory to internal network directory.
    - We used schedule library for running our app every day on specific date.

    - we created some variables which contains data about our ftp server.
    - we created some variables for our directories.

    - we made a logger variable for LoggingService.
    - we used FTP class for connection to our server
    - we used ftp.login for log in into our account in ftp server.
    - we wanted our app enter into specific folder inside ftp server in name "BrainnestC5"
    - then we made a variable which contains list of all documents inside "BrainnestC5" folder by using ftp.nlst().
    -we checked if our local directory exist or not ,if it is not we used os.makedirs() function for creating our local directory.

    - then we iterated all the files from our files list by using for loop.Then we used os.path.join method for making a direction for our files to be downloaded.Then we used ftp.retrbinary method for downloading the files.

    - we used shutil.move method for moving our all files from local directory to internal network directory.

    - then we just started using logger file for showing info in our log file ,if it is successful it will show success message ,if it is not in except section it will show our error.
    - We used schedule to send a message at a specific time"23:17"every day.
    - We used While true to make our app to work all the time.
        


