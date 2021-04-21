


def parseUrl(url):
    if ("cik=" in url and "accession_number=" in url):
        cikind = url.find("cik=", 0)
        amp = url.find("&", cikind)
        cik = url[cikind+4:amp]

        accind = url.find("accession_number=", 0)
        amp = url.find("&", accind)
        acc = url[accind+17:amp]
        acc = acc.replace("-", "")
        urlformat = "https://www.sec.gov/Archives/edgar/data/{}/{}/Financial_Report.xlsx"
        return urlformat.format(cik, acc)
    else:
        raise ValueError