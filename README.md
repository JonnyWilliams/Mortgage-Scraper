<h1>MoneySupermarket.com Mortgage Scraper</h1>
MoneySupermarket.com Mortgage Scraper is written in Python. The code scrapes Mortgages from http://www.MoneySupermarket.com and inserts the mortage details into a SQL database.

I created this code as I wanted to buy my first house. I wanted to keep an eye on the mortgage offerings so I could keep an eye on the market trends. I could then easily run some queries to compare mortgages to find the best deal.
 
<h2>The source files</h2>
<b>mortgage.py</b> – Stores all information about each mortgage offering, with a ‘save’ method that inserts the data into the sql database.<br />
<b>results.py</b> – Stores all the information on each results page, which is broken down into links for specific mortgages, and also the link to the more results page in the sequence (ie: the ‘show more’ link).<br />
<b>scrapeMortgage.py</b> – When given an mortgage URL, this creates and populates an mortgage object.<br />
<b>scrapeResults.py</b> – When given a mortgage URL, this creates and populates a results object.<br />
<b>scrapeSequence.py</b> – This walks through a series of mortgages, calling scrapeResults and scrapeMortgage for all of them.<br />

<h2>Instructions for use</h2>
These are some instructions to get you started:
<h3>SQL Database</h3>
In your SQL database run the following query to create the table<br />

```sql
CREATE TABLE `mortgages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rundate` date NOT NULL,
  `url` varchar(500) NOT NULL DEFAULT '',
  `lender` text NOT NULL,
  `typeOfMortgage` text NOT NULL,
  `borrowAmount` decimal(10,2) NOT NULL,
  `houseValue` decimal(10,2) NOT NULL,
  `term` int(2) NOT NULL,
  `initialRate` text NOT NULL,
  `revertRate` text NOT NULL,
  `maxLTV` text NOT NULL,
  `initialPeriod` text NOT NULL,
  `minMaxMortgageAmount` text NOT NULL,
  `minimumAge` text NOT NULL,
  `initialMonthlyRepayments` text NOT NULL,
  `monthlyRepaymentsAfter` text NOT NULL,
  `totalAmountToRepay` decimal(10,2) NOT NULL,
  `TotalAmountOfInterest` decimal(10,2) NOT NULL,
  `overpayments` text NOT NULL,
  `paymentHolidays` text NOT NULL,
  `portable` text NOT NULL,
  `cashback` text NOT NULL,
  `fees` decimal(10,2) NOT NULL,
  `valuationReport` text NOT NULL,
  `homebuyerSurvey` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
```

Edit the SQL connection details in the mortgage.py file to point it to your SQL database.

<h3>Setting "Borrow Amount", "House Value", and "Mortgage Term" values</h3>
You can change the "Borrow Amount", "House Value", and "Mortgage Term" parameters in the scrapeSequence.py file.

<h3>Running the scraper</h3>
To run, run the scrapeSequence.py file