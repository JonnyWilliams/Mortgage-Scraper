MoneySupermarket.com Mortgage Scraper/h1>
MoneySupermarket.com Mortgage Scraper is written in Python. The code scrapes Mortgages from http://www.MoneySupermarket.com
 
<h2>The source files</h2>
mortgage.py – Stores all information about each mortgage offering, with a ‘save’ method that inserts the data into the mysql database<br />
results.py – Stores all the information on each results page, which is broken down into links for specific mortgages, and also the link to the more results page in the sequence (ie: the ‘show more’ link)<br />
scrapeMortgage.py – When given an mortgage URL, this creates and populates an mortgage object<br />
scrapeResults.py – When given a mortgage URL, this creates and populates a results object<br />
scrapeSequence.py – This walks through a series of mortgages, calling scrapeResults and scrapeMortgage for all of them,<br />