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

years   = list(range(1989,2020))
irs_url = 'https://www.irs.gov/pub/irs-soi/'

for yy in years:


        # File name
        if yy < 2010:
            filename = (str(yy) + 'countyincome.zip')
        elif (yy>=2010)&(yy<2013):
            filename = (str(yy) + 'countydata.zip')
        elif (yy>=2013):
            filename = ('county' + str(yy) + '.zip')

        # Get full URL (needs to include the file name)
        url = irs_url + filename
        savename = datadir + str(yy) + 'countyincome.zip'

        # Download data from URL
        if os.path.exists(savename):
            print("File already exists: " + filename)
        else:
            # Random pause to prevent bombarding website
            sleep(randint(1,5))
            urllib.request.urlretrieve(url, filename = savename)
            print('Downloaded: ' + filename)


