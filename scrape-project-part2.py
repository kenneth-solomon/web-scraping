from csv import DictReader, DictWriter, reader, writer
import requests
from time import sleep
from random import choice
from bs4 import BeautifulSoup

BASE_URL = ("http://quotes.toscrape.com/")

def read_quotes(filename):
	with open(filename, "r") as f: 
		csv_read = DictReader(f)
		return list(csv_read)

read_quotes("scrape-project.csv")
	
	
def start_game(kquotes):		
	kchoice = choice(kquotes)
	remaining_guesses = 4
	print("Here's a quote")
	print(kchoice["author"])



	guess = ""

	while guess.lower() != kchoice["author"].lower() and remaining_guesses > 0:
		guess = input(f"who said this : you have {remaining_guesses} remaining_guesses \n")
		if guess == kchoice['author']:
			print("you are correct")
			break
		remaining_guesses -= 1
		
		if remaining_guesses == 3:
			print("incorrect")
			print("here's a hint for you")
			link = requests.get(f"{BASE_URL}{kchoice['bio-link']}")
			html = link.text
			soup = BeautifulSoup(html,"html.parser")
			author_dob = soup.find(class_ = "author-born-location").get_text()
			author_birth_location = soup.find(class_ = "author-born-date").get_text()
			print(f"author was born {author_birth_location} on {author_dob}")
			
		elif remaining_guesses == 2:
			print("incorrect")
			print("here's a hint for you")
			print(f"author's intial of the first name is {kchoice['author'][0]}")
		
		elif remaining_guesses == 1:
			print("incorrect")
			print("here's a hint for you")
			last_name_initial = kchoice["author"].split(" ")
			print(f"author's intial of the first name is{last_name_initial[1][0]}")
		
	again = ' ' 
	while again.lower() not in ("y", "yes", "n", "no"):
		again = input("press 'y' to play and 'n' to exit \n")
		if again in ("n", "no"):
			print("Good Bye Buddy")
			break
		elif again in ("y", "yes"):
			return start_game(kquotes)
		else :
			print("press 'y' or 'n'")
				
			
kquotes = read_quotes("scrape-project.csv")
start_game(kquotes)