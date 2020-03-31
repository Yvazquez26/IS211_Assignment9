#!/usr/bin/env python
# coding: utf-8

# Assignment 9 - Part I CBS Football Stats
# This script output the list of top 20 players, player's position, team and total # of touchdowns.

import urllib
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://www.cbssports.com/nfl/stats/'
                       'playersort/nfl/year-2019-season-regular-category-touchdowns')

bsObj = BeautifulSoup(html)

td_table = bsObj.findAll("table", attrs={"class":"data"})[0].findAll('tr', attrs={"valign":"top"})

def main():
    """Function that returns list of top 20 players from the CBS webpage."""
    counter = 0
    print("The 20 players currently with the most touchdowns are:")
    for i in td_table:
        name = i.findAll('td')[0].findAll('a')[0].contents[0]
        position = i.findAll('td')[1].contents[0]
        team =  i.findAll('td')[2].findAll('a')[0].contents[0]
        tds = i.findAll('td')[6].contents[0]
        counter += 1
        print(("Player rank: {}, Player Name: {}, Position: {}, "
               "Team: {}, total # of touchdowns: {}").format(counter, name, position, team, tds))
        if counter >= 20:
            break

if __name__ == '__main__':
    main()
