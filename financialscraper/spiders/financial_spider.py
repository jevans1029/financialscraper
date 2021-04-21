import scrapy
from financialscraper.items import FinancialscraperItem
from financialscraper.urlparser import parseUrl

tickers = ["AAPL", "MSFT", "AMZN", "T", "TSLA", "NFLX", "CAT", "MMM", "AXP", "BA", "CSCO", "KO", "DIS", "DWDP", "XOM", "GE", "GS", "HD", "IBM",
           "INTC", "JNJ", "JPM", "MCD", "MRK", "NKE", "PFE", "PG", "TRV", "UTX", "UNH", "VZ", "V", "WMT"]
sec = "https://www.sec.gov"

class FinancialSpider(scrapy.Spider):
    name = "financial"
    start_urls = [

    ]
    def start_requests(self):
        baseurl = "https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&owner=exclude&action=getcompany"

        for ticker in tickers:
            url = baseurl.format(ticker)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.xpath("//*[@id='seriesDiv']/table")

        for row in table.xpath(".//tr"):
            text = row.xpath(".//td[1]/text()").get()
            if (text=="10-Q"):
                print(text)
                href = row.xpath(".//a[2]/@href").get()
                print(href)
                return FinancialscraperItem(file_urls=[parseUrl(sec + href)])
                #yield scrapy.Request(url=sec + href, callback=self.parseXBRL)
            #print(row.xpath(".//td[1]/text()").get())

            # entries = row.xpath(".//td")
            # html = entries.getall()
            # print(type(html))
            # print(html[0])


        # result = table.get()
        #
        # with open("result.html", "a") as f:
        #     f.write(result)
        #     f.close()

    # def parseXBRL(self, xbrl):
    #     return FinancialscraperItem(file_urls=)
        # return FinancialscraperItem(file_urls=sec + href)
        #print(response.xpath("//p"))

        #
        # href = index.xpath("//tr[2]/td[3]/a/@href").get()
        #
        # return scrapy.Request(url=sec + href, callback=self.parseReport)

    # def parseReport(self, report):
        # stateofops= report.xpath("//font[contains(., 'Consolidated Statements of Operations')]/text()")
        # print(len(stateofops.getall()))
        # for state in stateofops.getall():
        #     print(state)

        # with open("result.html", "ab") as f:
        #     for table in report.xpath("//table").getall():
        #         f.write(table.encode("utf-8"))
        #     f.close()


