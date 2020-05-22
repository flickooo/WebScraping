import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import openpyxl
import os

#excel file
filename = 'pahrmacy.csv'
f = open(filename, 'w')
headers = 'Pharmacy_Name, email\n'
f.write(headers)


myUrl = 'https://www.healthdirect.gov.au/australian-health-services/results/hughesdale-3166/tihcs-aht-11222/gp-general-practice?pageIndex=1&tab=SITE_VISIT'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

page_soup = bs(page_html, 'html.parser')
main_div = page_soup.findAll('div',{'class':'hsf-search_results-item-tiles'})
main_div_a = main_div[0].findAll('a')

#treba da iteriras kroz svaki href
# main_href = main_div_a[0]['href']
counter = 0
for main_href in main_div_a:
    if main_href.has_attr('href'):

        counter= counter + 1
        second_pageUrl = 'https://www.healthdirect.gov.au' + main_href['href']

        uClient_secondPage = uReq(second_pageUrl)
        secondPage_html = uClient_secondPage.read()
        uClient_secondPage.close()

        secondPage_soup = bs(secondPage_html, 'html.parser')
        pharmacy_name = secondPage_soup.findAll('h1',{'data-ng-cloak':''})
        pharmacy_email = secondPage_soup.findAll('div',{'class':'veyron-hsf-contact-details'})

        pharmacy_email_format = pharmacy_email[0]['data-email']



        pharmacy_name_format = pharmacy_name[1].text
        real_pharmacy_name = pharmacy_name_format.split()
        real_pharmacy_name.pop(0)
        real_pharmacy_name.pop(0)
        full_name = ' '.join(word for word in real_pharmacy_name)
        print(full_name)
        print(pharmacy_email_format)
        
        
        f.write(full_name + ',' + pharmacy_email_format + '\n')

print(counter)