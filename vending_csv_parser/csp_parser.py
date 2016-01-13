#!/usr/local/bin/python

##########
## TODO:
##     - find the proper number of items per sale.  sometimes
##       prices are included, sometimes not.
##     - if a price was included in the item, list it.
##     - output to excel csv.
##########

import sys
import csv
import re

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['Location'])
        delimiters = ",", "("
        items = split(delimiters, row['Items'])
        #print items
        for thing in items:
            if not '$' in thing:
                thing = thing.translate(None, ' )')
                print(row['Location'], row['Date'], row['Amount'], len(items), thing)


