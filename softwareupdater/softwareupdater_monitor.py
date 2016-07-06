'''

Author: Hieu Do 

Start Date: June 6, 2016

Description: 
Retrieves a list of all the files from `https://seattle.poly.edu/updatesite/` 
and returns the files as well as their last modified dates.

Usage: 
python softwareupdater_monitor.py

'''

import urllib2 
from bs4 import BeautifulSoup

# store the html raw content 
html = urllib2.urlopen("https://seattle.poly.edu/updatesite/").read()
# parse the html content using  Beautiful Soup
# to extract the tabl
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")

# get field names
headings = [th.get_text() for th in table.find("tr").find_all("th")]

# store each row as a list, each cell as a tuple
datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

# print datasets
print "{0:<34} {1}".format("-----FILES-----","---LAST MODIFIED---")
for dataset in datasets[2:]:
  if (len(dataset) > 2):
    print "{0:<35}: {1}".format(dataset[1][1], dataset[2][1])