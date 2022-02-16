#!/usr/bin/env python
# coding: utf-8

# # Get zipcode level income from tax returns
#
# Public facing website
# - https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi
#
# Parent directory:
# - https://www.irs.gov/downloads/irs-soi

import requests
import urllib
from random import randint
from time import sleep

# Data directory
import os
absdirname = os.path.dirname(__file__)
datadir = os.path.join(absdirname, './data/')
try:
    (os.mkdir(datadir))
except OSError as error:
    print(error)



# ## Download zipped Zipcode files from IRS website
#
# - WARNING: only download data from website once!
# - Don't want to call IRS site too many times, or will get blocked
years   = list(range(2004,2017))
irs_url = 'https://www.irs.gov/pub/irs-soi/'

for yy in years:

        # Random pause to prevent bombarding website
        sleep(randint(1,5))

        # File name
        if (yy<2013):
            filename = (str(yy) + 'zipcode.zip')
        else:
            filename = ('zipcode' + str(yy) + '.zip')

        # Get full URL (needs to include the file name)
        url = irs_url + filename

        # Download data from URL
        urllib.request.urlretrieve(url, filename = datadir + str(yy) + 'zipcodeincome.zip')

        print('Finished: ' + filename)

