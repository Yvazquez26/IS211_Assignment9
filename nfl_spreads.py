#!/usr/bin/env python
# coding: utf-8

# Assignment 9 - Part II NFL
# This script outputs the favorite NFL teams, the underdog and the spread of a given game.

import urllib.request
import sys
from bs4 import BeautifulSoup

url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")

find_table = soup.find_all('table', attrs = {'cols': '4', 'width': 
                                             '580', 'cellspacing': '6', 'cellpadding': '3', 'border': '0'})

for i in find_table:
    table = i

tRows = table.find_all('tr')

for i in tRows:
    tData = i.find_all('td')
    timedat = str(tData[0].get_text())
    favo = str(tData[1].get_text())
    spr = str(tData[2].get_text())
    udog = str(tData[3].get_text())

print('Date & Time:{}, Favorite:{}, Spread:{}, Underdog:{}'.format(timedat, favo, spr, udog))
