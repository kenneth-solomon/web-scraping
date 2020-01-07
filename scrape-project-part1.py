#A small game to guess the name of the author of the quote
from csv import DictReader, DictWriter
import requests
from time import sleep
from random import choice
from bs4 import BeautifulSoup


BASE_URL = ("http://quotes.toscrape.com/")

#function to scrape all the quotes and its author's details from the website
def scrape_quotes():
	url = "/page/1"
	k_list = []
	while url:
		response = requests.get(f"{BASE_URL}{url}")
		ktml = response.text
		ksoup = BeautifulSoup(ktml, "html.parser")
		quotes = ksoup.find_all(class_ = "quote")
			
		for k in quotes:
			k_list.append({"quote": k.find(class_ = "text").get_text(),
			"author": k.find(class_ = "author").get_text(),
			"bio-link": k.find("a")["href"]
			})
		#create these variable to scrape data from all the pages from the website	
		next_button = ksoup.find(class_ = "next")
		url = next_button.find("a")["href"] if next_button else None
		sleep(2)
		
	return k_list
	
kquotes = scrape_quotes()

#wrote all the data in a CSV file, so that we dont have to scrape all over again when we execute the code	
with open("scrape-project.csv", "w") as f:
	headers = ["quote", "author", "bio-link"]
	csv_write = DictWriter(f, fieldnames = headers)
	csv_write.writeheader()
	for k_write in kquotes:
		csv_write.writerow(k_write)
	
	
	
	