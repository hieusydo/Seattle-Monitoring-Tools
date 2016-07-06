'''

Author: Hieu Do 

Start Date: June 6, 2016

Description: 
Check the status of the software updater server

Usage: 
python softwareupdater_monitor.py

'''

import urllib2 
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://seattle.poly.edu/updatesite/").read()
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")

# The first tr contains the field names
headings = [th.get_text() for th in table.find("tr").find_all("th")]

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

# print datasets
print "{0:<35} {1}".format("FILES","LAST MODIFIED")
for dataset in datasets[2:]:
  if (len(dataset) > 2):
    print "{0:<35}: {1}".format(dataset[1][1], dataset[2][1])