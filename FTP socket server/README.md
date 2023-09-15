# FTP File Server 
To run the server/client, call the appropriate program from the terminal. Each program will display a short message on startup:
```
> python server.py

Welcome to the FTP server.

To get started, connect a client.
```
```
> python client.py

Welcome to the FTP client.

Call one of the following functions:
CONN           : Connect to server
UPLD file_path : Upload file
LIST           : List files
DWLD file_path : Download file
DELF file_path : Delete file
QUIT           : Exit

Enter a command:
```
As indicated, the first thing that needs to be done is to connect the client to the server. To do this, just enter the command CONN:
```
Enter a command: CONN
```
The client will then attempt a connection. If successful a message will appear:
```
Enter a command: Connect

Sending a server request...
Connection successful
```
After that, all other commands can be entered through the client. Messages will display the progress of the request on both the client and server end. For example, to upload a file 'filename.xyz', use the following command:
```
Enter a command: UPLD filename.xyz
```
All standard file paths also work:
```
Enter a command: UPLD C:\Users\...\folder\filename.xyz
```

When the server receives a file, it puts it in the same folder that it is in. Likewise, when the LIST command is used the server searches for files in the same folder that it is located in.
