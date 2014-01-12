'''
Created on Jan 12, 2014

@author: Jonny
'''
from scrapeResults import scrapeResult
from scrapeMortgage import scrapeMortgage
from results import result
from mortgage import mortgage
import MySQLdb
import _mysql_exceptions
import mechanize
from bs4 import BeautifulSoup
import urllib2

url = "http://www.moneysupermarket.com/mortgages/search/results/?goal=MOR_FTB"

while url != None:
    sl = ""
    sl = scrapeResult()
    sl.scrape(url)
    for mortgageURL in sl.aMortgage.resulturls:
        sa = ""
        sa = scrapeMortgage()
        sa.scrape(mortgageURL)
        try:
            sa.aMor.save()
        except _mysql_exceptions.IntegrityError:
            print "** Mortgage " + sa.aMor.url + " already saved **"
        sa.onAd = ""

    url = ""
    try:
        #to-do - make code click the more link, but don't really need it for now
        if sl.aMortgage.nextLink:
            print "nextLink = "+sl.aMortgage.nextLink
            url = sl.aMortgage.nextLink    
        else:
            print 'all done.'
            break
    except:
        print 'all done.'
        break

        
