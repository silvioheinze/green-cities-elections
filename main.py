import requests
from html_table_parser import HTMLTableParser
import pandas as pd


def url_get_contents(url): 
	req = request.Request(url=url) 
	f = request.urlopen(req) 
  
	return f.read() 
  
url = 'https://greeningthecities.wordpress.com/election-results/election-results-cities/'
html = url_get_contents(url).decode('utf-8') 

p = HTMLTableParser() 
p.feed(html) 
  
print(p.tables[1]) 
 
print(pd.DataFrame(p.tables[1]))
