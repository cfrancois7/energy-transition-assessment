from ftplib import FTP
from getpass import getpass

def listFtp():
	"""Need password. Will list files in data folder on ftp if listed is True (default)."""
	passwd= getpass(prompt='FTP password?')
	ftp = FTP('u45610654.1and1-data.host')
	ftp.login(user='u45610654',passwd=passwd)
	ftp.cwd('/Energy_transition/data/')
	ftp.retrlines('LIST')
	ftp.quit()
    
def downloadFile(filename):
	passwd= getpass(prompt='FTP password?')
	"""Download in ../data/. """
	localfile = open('../data/'+filename, 'wb')
	ftp = FTP('u45610654.1and1-data.host')
	ftp.login(user='u45610654',passwd=passwd)
	ftp.cwd('/Energy_transition/data/')
	ftp.retrbinary('RETR ' + filename, localfile.write,1024)
	ftp.quit()
	localfile.close()
    
def uploadFile(filename):
	"""Upload files present in ../data/ to the correct folder on the ftp server (PLEASE DON'T CHANGE IT). Password required."""
	passwd= getpass(prompt='FTP password?')
	"""Upload files in ../data/: no need to specify it."""
	ftp = FTP('u45610654.1and1-data.host')
	ftp.login(user='u45610654',passwd=passwd)
	ftp.cwd('/Energy_transition/data/')
	ftp.storbinary('STOR '+filename, open('../data/'+filename, 'rb'))
	ftp.quit()
