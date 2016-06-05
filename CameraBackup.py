#!/usr/bin/env python

import subprocess


#do dry run to get files
status = subprocess.check_output("find /media/3063-3361/DCIM/ |grep DSC", shell=True)

for this_line in status.splitlines():
    if (this_line[-3:] == 'JPG'):
        status= subprocess.check_output("exiftool " + this_line + " | grep 'Sony Date Time'", shell=True)
        print(status)
        #status = subprocess.check_output("convert /media/Synology/Pictures/A6000/100MSDCF/" + this_line + " -resize 25% /media/Synology/Pictures/A6000/100MSDCF/Small/" +this_line[:-4] + "_sml.JPG",shell=True)
#        status = subprocess.check_output("convert /media/3063-3361/DCIM/100MSDCF/" + this_line + " -resize 25% /media/Synology/Pictures/A6000/100MSDCF/")


