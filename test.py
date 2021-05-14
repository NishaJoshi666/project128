import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

star_data = []

def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for th_tag in soup.find_all("th", attrs={"class", "exoplanet"}):
            tr_tags = th_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tags.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

def scrapemoredata(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,'html.parser')
    new_star_data = []
    for tr_tag in soup.find_all('tr',attrs={'class':'fact_row'}):
        tdtags = tr_tag.find_all('td')
        templist = []
        for td in tdtags:
            try:
                templist.append(td.find_all('div',attrs={'class':'value'})[0].content[0])
            except:
                templist.append('')
        new_star_data.append(templist)
    pass

scrape()
for index,data in enumerate(star_data):
    scrapemoredata(data[5])
    