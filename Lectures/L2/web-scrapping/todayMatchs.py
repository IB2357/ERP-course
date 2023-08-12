import requests
from bs4 import BeautifulSoup
import csv
# install lxml,BeautifulSoup,requests
from datetime import datetime


choice = input("Do you want to show today's matchs?  type y/n ") 
if choice == 'y':
    current_date = datetime.now()
    date  = current_date.strftime("%m/%d/%y")
else:
    date  = input("please enter the date with the following format MM/DD/YY: ")
print("wait...\n")

# date = '08/11/2023'
# date = '12/17/2022'
page  = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}")



def main(page):
    src = page.content
    soup = BeautifulSoup(src,'lxml')

    # matches_detailes = []
    championships = soup.find_all('div',{'class':'matchCard'})
    def get_match_info(championship):
        title = championship.contents[1].find('h2').text.strip()
        print(title)
    print(f"matchs in {date}: ")
    for match in championships:
        get_match_info(match)
        print("____________________\n")



if __name__ == "__main__":
    main(page)
# main(page)

