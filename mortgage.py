'''
Created on Jan 11, 2014

@author: Jonny
'''
import MySQLdb
import chardet
import sys

class mortgage:

    #the basics
    url = ""
    lender = ""
    typeOfMortgage = ""
    initialRate = ""
    revertRate = ""
    maxLTV = ""
    initialPeriod = ""
    minMaxMortgageAmount = ""
    minimumAge = ""
    
    #the repayments
    initialMonthlyRepayments = ""
    monthlyRepaymentsAfter = ""
    totalAmountToRepay = ""
    TotalAmountOfInterest = ""
    
    #mortgage features
    overpayments = ""
    paymentHolidays = ""
    portable = ""
    cashback = ""
    
    #product cost and fees
    booking = ""
    
    #survey fees
    valuationReport = ""
    homebuyerSurvey = ""

    def save(self):
        db=MySQLdb.connect(host="127.0.0.1", user="root", db="JonnyTest")
        c=db.cursor()

        #self.description = unicode(self.description, errors='replace')
        #self.description = self.description.encode('ascii','ignore')
        #self.title = self.title.encode('ascii','ignore')
        # TODO: might need to convert the other strings in the advert if there are any unicode conversetion errors

        sql = "INSERT INTO mortgages (url,lender,typeOfMortgage,initialRate,revertRate,maxLTV,initialPeriod,minMaxMortgageAmount,minimumAge,initialMonthlyRepayments,monthlyRepaymentsAfter,totalAmountToRepay,TotalAmountOfInterest,overpayments,paymentHolidays,portable,cashback,booking,valuationReport,homebuyerSurvey) VALUES('"+self.url+"','"+self.lender+"','"+self.typeOfMortgage+"','"+self.initialRate+"','"+self.revertRate+"','"+self.maxLTV+"','"+self.initialPeriod+"','"+self.minMaxMortgageAmount+"','"+self.minimumAge+"','"+self.initialMonthlyRepayments+"','"+self.monthlyRepaymentsAfter+"','"+self.totalAmountToRepay+"','"+self.TotalAmountOfInterest+"','"+self.overpayments+"','"+self.paymentHolidays+"','"+self.portable+"','"+self.cashback+"','"+self.booking+"','"+self.valuationReport+"','"+self.homebuyerSurvey+"' )"
        print sql
        c.execute(sql)
