import ftplib
import os
import sys

#Get ARM files from a ftp server

if __name__ == "__main__":
    arm_user = sys.argv[1]
    order_number = sys.argv[2]
    odir = sys.argv[3]
    print('odir '+odir)
    print('user'+arm_user)
    print('order_number'+order_number)
    try:
        os.makedirs(odir)
    except FileExistsError:
        print('dir exists, ignoring')

    ftp = ftplib.FTP('ftp.archive.arm.gov')
    ftp.login()
    ftp.cwd(arm_user+'/'+order_number)
    lst = ftp.nlst()
    for item in lst:
        if len(item) > 4:
            ofile = open(os.path.join(odir,item), 'wb')
            ftp.retrbinary('RETR ' + item, ofile.write)
            ofile.close()
            print('Done '+item)
    ftp.close()



