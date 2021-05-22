# Financial Data Scraper to scrape data from the SEC Edgar database

The SEC Edgar database contains the quartery, annual, and other financial reports and statements for public companies. It includes income, balance, and cash flow tables that are parseable. 

This turned out to not be very feasible. There is no standard table format for the financial statements. For example, the table columns for revenue have several different possible names such as Sales, Net Sales, Total Sales, Revenue, Total Revenue, Total Yearly Sales, Goods Sold, etc. I looked into NLP but there is no out of the box solution to identify which table columns are the ones you are looking for. NLP seems to be more about finding meaning in full sentences or extracting the subject of a sentence. The best solution I found was to use NLP features that are similar to regular expressions to get close enough. 
