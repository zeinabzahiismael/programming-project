from ftplib import FTP
def uploadFile(ftp):
   filename = '1212.png'
   ftp.storbinary('STOR '+filename, open(filename, 'rb'))
   ftp.quit()
with FTP() as ftp:
   ftp.connect('192.168.43.109',2121)
   ftp.login('zienab',"12345")
   ftp.getwelcome()
   ftp.dir()
   uploadFile(ftp)
