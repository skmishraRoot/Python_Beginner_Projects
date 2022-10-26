# Importing Module
from bs4 import BeautifulSoup
import requests

# setting up user agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Writing function to retrive data from google
def weather(city):
    city=city.replace(" ","+")
    # Making request
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0. i635i39l2j0l4j46j690.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)  
    print("Searching in google......\n")
    # Passing html raw page to soup
    soup = BeautifulSoup(res.text,'html.parser')

    # retriving data
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    # Printing
    print(location)
    print(time)
    print(info)
    print(weather+"°C")


# Getting user input
print("enter the city name")
city=input()
city=city+" weather"
weather(city)