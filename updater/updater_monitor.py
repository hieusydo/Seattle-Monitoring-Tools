'''

Author: Hieu Do 

Start Date: June 6, 2016

Description: 
Retrieves a list of all the files from `https://seattle.poly.edu/updatesite/` 
and returns the files as well as their last modified dates.

Usage: 
python updater_monitor.py

'''
import tempfile
import softwareupdater

# this is being done so that the resources accounting doesn't interfere with logging
from repyportability import *
_context = locals()
add_dy_support(_context)

signeddata = dy_import_module("signeddata.r2py")
advertise_monitor = dy_import_module("advertise_monitor.r2py")

updatereurl = "https://seattle.poly.edu/updatesite/"

updater_servername = "seattle.poly.edu"
updater_serverport = 443 # port obtain from `nmap 128.238.63.51`


def main():
  advertise_monitor.checkServerStatus(updater_servername, updater_serverport)

  tempdir = tempfile.mkdtemp()+"/"
  metainfo_downloaded = softwareupdater.safe_download(updatereurl, "metainfo", tempdir, 1024*32)
  if not metainfo_downloaded:
    print("Failed to download metainfo.")
    return
  print("Successfully downloaded metainfo")

  # read the file data into a string
  newmetafileobject = file(tempdir+"metainfo")
  newmetafiledata = newmetafileobject.read()
  newmetafileobject.close()

  if not signeddata.signeddata_issignedcorrectly(newmetafiledata, softwareupdater.softwareupdatepublickey):
    print("CRITICAL - Downloaded metainfo not signed correctly. The updater site is delivering the correct updates")
    return
  print("Downloaded metainfo signed correctly. The updater site is delivering the correct updates")
  

if __name__ == '__main__':
  main()