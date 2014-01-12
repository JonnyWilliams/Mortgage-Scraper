'''
Created on Jan 11, 2014

@author: Jonny
'''
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup          # For processing HTML
import urllib2
from mortgage import mortgage
import time
import re

class scrapeMortgage:

    page = ""
    soup = ""

    def scrape(self,mortgageURL):

        # give it a bit of time so gumtree doesn't
        # ban us
        time.sleep(2)

        url = mortgageURL
        print "-- scraping "+url+" --"
        page = urllib2.urlopen(url)
        self.soup = BeautifulSoup(page)

        self.aMor = mortgage()
        #the basics
        self.aMor.url = url
        self.aMor.lender = self.extractLender()
        self.aMor.typeOfMortgage = self.extractTypeOfMortgage()
        self.aMor.initialRate = self.extractInitialRate()
        self.aMor.revertRate = self.extractRevertRate()
        self.aMor.maxLTV = self.extractMaxLTV()
        self.aMor.initialPeriod = self.extractInitialPeriod()
        self.aMor.minMaxMortgageAmount = self.extractMinMaxMortgageAmount()
        self.aMor.minimumAge = self.extractMinimumAge()
        
        #the repayments
        self.aMor.initialMonthlyRepayments = self.extractInitialMonthlyRepayments()
        self.aMor.monthlyRepaymentsAfter = self.extractMonthlyRepaymentsAfter()
        self.aMor.totalAmountToRepay = self.extractTotalAmountToRepay()
        self.aMor.TotalAmountOfInterest = self.extractTotalAmountOfInterest()
        
        #mortgage features
        self.aMor.overpayments = self.extractOverpayments()
        self.aMor.paymentHolidays = self.extractPaymentHolidays()
        self.aMor.portable = self.extractPortable()
        self.aMor.cashback = self.extractCashback()
        
        #product cost and fees
        self.aMor.booking = self.extractBooking()
        self.aMor.completion = self.extractCompletion()
        
        #survey fees
        self.aMor.valuationReport = self.extractValuationReport()
        self.aMor.homebuyerSurvey = self.extractHomebuyerSurvey()
        
    def extractLender(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "brandName"})
        lender = str.contents[0]
        return lender

    def extractTypeOfMortgage(self):
        str = self.soup.find('span',attrs={"data-productattribute" : "rateType"})
        type = str.contents[0]
        return type

    def extractInitialRate(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "initialRate"})
        initRate = str.contents[0]
        return initRate
    
    def extractRevertRate(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "lenderSVR"})
        revRate = str.contents[0]
        return revRate
    
    def extractMaxLTV(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "maxLTV"})
        maxLTV = str.contents[0]
        return maxLTV
    
    def extractInitialPeriod(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "schemeDuration"})
        initPeriod = str.contents[0]
        return initPeriod
            
    def extractMinMaxMortgageAmount(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "minMaxMortgageAmount"})
        minMaxMort = str.contents[0]
        return minMaxMort
    
    def extractMinimumAge(self):

        str = self.soup.find('span',attrs={"data-productattribute" : "minMaxAge"})
        minMaxAge = str.contents[0]
        return minMaxAge
    
    def extractInitialMonthlyRepayments(self):
        
        sec = self.soup.findAll("div", { "class" : "info-panel" })[1]
        table = sec.find("table", { "class" : "dash-table" })
        initMonRepay = table.findAll("span")[0].contents[0]
        return initMonRepay

    def extractMonthlyRepaymentsAfter(self):

        sec = self.soup.findAll("div", { "class" : "info-panel" })[1]
        table = sec.find("table", { "class" : "dash-table" })
        initMonRepayAft = table.findAll("span")[1].contents[0]
        return initMonRepayAft

    def extractTotalAmountToRepay(self):

        sec = self.soup.findAll("div", { "class" : "info-panel" })[1]
        table = sec.find("table", { "class" : "dash-table" })
        totAmount = table.findAll("span")[2].contents[0]
        
        non_decimal = re.compile(r'[^\d.]+')
        totAmount2 = non_decimal.sub('', totAmount)
        return totAmount2

    def extractTotalAmountOfInterest(self):

        sec = self.soup.findAll("div", { "class" : "info-panel" })[1]
        table = sec.find("table", { "class" : "dash-table" })
        interest = table.findAll("span")[3].contents[0]
        return interest

    def extractOverpayments(self):
        
        sec = self.soup.findAll("ul", { "class" : "pro-con-list" })[0]
        table = sec.findAll("li")[0]
        overpayments = table.get("class")[0]
        return overpayments
        
    def extractPaymentHolidays(self):
        
        sec = self.soup.findAll("ul", { "class" : "pro-con-list" })[0]
        table = sec.findAll("li")[1]
        paymentHolidays = table.get("class")[0]
        return paymentHolidays

    def extractPortable(self):
         
        sec = self.soup.findAll("ul", { "class" : "pro-con-list" })[0]
        table = sec.findAll("li")[2]
        portable = table.get("class")[0]
        return portable       

    def extractCashback(self):
        
        sec = self.soup.findAll("ul", { "class" : "pro-con-list" })[0]
        table = sec.findAll("li")[3]
        cashback = table.get("class")[0]
        return cashback

    def extractBooking(self):
        
        try:
            str = self.soup.find('span',attrs={"data-productattribute" : "BOOKING"})
            booking = str.contents[0]
            return booking
        except:
            try:
                str = self.soup.find('span',attrs={"data-productattribute" : "ARRANGEMENT"})
                booking = str.contents[0]
                return booking
            except:
                return ""
        
    def extractCompletion(self):
        
        try:
            str = self.soup.find('span',attrs={"data-productattribute" : "COMPLETION"})
            completion = str.contents[0]
            return completion
        except:
            return ""
                
    def extractValuationReport(self):

        try:
            str = self.soup.find('span',attrs={"data-productattribute" : "Valuation"})
            valuation = str.contents[0]
            return valuation
        except:
            return ""
        
    def extractHomebuyerSurvey(self):
        
        try:
            str = self.soup.find('span',attrs={"data-productattribute" : "Homebuyer"})
            homebuyer = str.contents[0]
            return homebuyer
        except:
            return ""