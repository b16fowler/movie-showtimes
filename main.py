from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amctheatres.com/movie-theatres/plainville/amc-southington-12/showtimes")
html = BeautifulSoup(response.text, 'html.parser')
title = html.find('title').text

# print(html.prettify())
# print(html.find_all('a'))
print(html.get_text())