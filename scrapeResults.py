'''
Created on Jan 11, 2014

@author: Jonny
'''
from bs4 import BeautifulSoup
import urllib2
from results import result
import mechanize

class scrapeResult:
    
    
    soup = ""    
    url = ""
    aMortgage = ""

    def scrape(self,url):

        print "scraping url = "+str(url)

        br = mechanize.Browser()

        # User-Agent (this is cheating, ok?)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
        
        response = br.open(url)
            
        br.select_form("questionForm")         # works when form has a name
        
        form = br.form
         
        form['goalId'] = ['MOR_FTB'] #dropdown box must be a list so enclose with []
        form["houseValue"] = '190000'
        form["borrowAmount"] = '110000'
        form["term"] = '25'
         
        form["repaymentType"] = ['capitalandinterest'] #dropdown box must be a list so enclose with []
        
        br.find_control("typeFixed").items[0].selected=True
        br.find_control("typeTracker").items[0].selected=False
        br.find_control("typeDiscountedVariable").items[0].selected=False
        br.find_control("typeStandardVariable").items[0].selected=False
        br.find_control("typeCapped").items[0].selected=False
        
        br.find_control("camOffset").items[0].selected=False
        
        br.find_control("initialPeriod2Years").items[0].selected=True
        br.find_control("initialPeriod3Years").items[0].selected=True
        br.find_control("initialPeriod4Years").items[0].selected=True
        br.find_control("initialPeriod5Years").items[0].selected=True
        br.find_control("initialPeriod5YearsPlus").items[0].selected=True
        br.find_control("noInitialPeriod").items[0].selected=True
         
        response = br.submit()
        #print response.read()
        
        page = response.read()
        self.soup = BeautifulSoup(page)

        self.aMortgage = result()
        self.aMortgage.url = url
        self.aMortgage.resulturls = self.extractResultURLs()
        self.aMortgage.moreLink = self.extractMoreLink()

    def extractResultURLs(self):
    
        resultpages = []
        temp = []

        for results_wrapper in self.soup.find_all("ul", class_="results-table"):
            for result in results_wrapper.find_all("li", class_="actions"):
                for a in result.find_all('a', href=True):
                    temp.append(a['href'])
                
        for link in temp:
            if link.startswith("/mortgages/details/"):
                resultpages.append("http://www.moneysupermarket.com"+link)
        
        print resultpages
        print len(resultpages)
        return resultpages

    def extractMoreLink(self): #to-do - make code click the more link, but don't really need it for now

        try:
            links = self.soup.find("li", class_=" pag-next").find("a").get("href")
        except:
            return ""
        
        return links