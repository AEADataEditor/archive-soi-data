#!/usr/bin/env python
# coding: utf-8

# # Get county level income from tax returns
#
# Public facing website:
# - https://www.irs.gov/statistics/soi-tax-stats-county-data
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


# ## Download zipped county files from IRS website
#
# - WARNING: only download data from website once!
# - Don't want to call IRS site too many times, or will get blocked

years   = list(range(2004,2017))
irs_url = 'https://www.irs.gov/pub/irs-soi/'

for yy in years:

        # Random pause to prevent bombarding website
        sleep(randint(1,5))

        # File name
        if yy < 2010:
            filename = (str(yy) + 'countyincome.zip')
        elif (yy>=2010)&(yy<2013):
            filename = (str(yy) + 'countydata.zip')
        elif (yy>=2013):
            filename = ('county' + str(yy) + '.zip')

        # Get full URL (needs to include the file name)
        url = irs_url + filename

        # Download data from URL
        urllib.request.urlretrieve(url, filename = datadir + str(yy) + 'countyincome.zip')

        print('Finished: ' + filename)


