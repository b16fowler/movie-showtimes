from bs4 import BeautifulSoup
import requests
import re

'''
BeautifulSoup notes:

title = html.find("title").text

print(html.prettify())
print(html.find_all("a"))
print(html.get_text())
'''

def main():
    # Set theater name
    theater = "AMC Southington 12"

    # Get request to the AMC Southington showtimes, then parse html
    response_south = requests.get("https://www.amctheatres.com/movie-theatres/plainville/amc-southington-12/showtimes")
    html_south = BeautifulSoup(response_south.text, "html.parser")
    
    # Final all 'a' tags in html
    a_tags = list(html_south.find_all("a"))

    # Convert 'a' tag html elements into list of strings containing inner text
    text_list = []
    for item in a_tags:
        text_list.append(item.get_text())


    matches = [i for i, tag in enumerate(text_list) if tag == theater]
    movie_indexes = [item - 1 for item in matches]
    print(movie_indexes)
    
    
    # TODO -> Later
    '''
    # Get request to the AMC Plainville showtimes, then parse html
    response_plain = requests.get("https://www.amctheatres.com/movie-theatres/plainville/amc-plainville-20/showtimes")
    html_plain = BeautifulSoup(response_plain.text, "html.parser")

    # Finds and prints inner text for all 'a' tags for Plainville theater
    for tag in html_plain.find_all("a"):
        print(tag.get_text())
    '''


if __name__ == "__main__":
    main()