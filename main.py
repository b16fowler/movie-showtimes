from bs4 import BeautifulSoup
import requests
import pprint
import re

'''
#################### TODO ####################

Fix bug when organzing last movie's showtimes
Send text/email?
Take parameters from terminal?

##############################################
'''

def main():
    # Scrape method takes url of desired theater to pull showtimes
    scrape("https://www.amctheatres.com/movie-theatres/plainville/amc-southington-12/showtimes")


def scrape(url):
    # Pull theater's name from url
    theater = findTheaterName(url)

    # Get request to the theater's showtimes, then parse html
    response = requests.get(url)
    html = BeautifulSoup(response.text, "html.parser")
    
    # Final all 'a' tags in html
    a_tags = list(html.find_all("a"))

    # Convert 'a' tag html elements into list of strings containing inner text
    text_list = []
    for item in a_tags:
        text_list.append(item.get_text().strip())

    # Find lines that are just the theaters name, there's one after each movie title
    matches = [i for i, tag in enumerate(text_list) if tag == theater]
    # Decrement by 1 to make list of movie titles
    movie_indexes = [item - 1 for item in matches]
    
    dictionary = {}
    # Use titles and indices to locate all showtimes for each movie 
    for index, title_index in enumerate(movie_indexes):
        # Save titles and showtimes in dictionary
        try:
            # text_list[title_index] --> movie's title
            # text_list[title_index + 2:movie_indexes[index + 1]] --> slice of that movie's showtimes
            dictionary[text_list[title_index]] = text_list[title_index + 2:movie_indexes[index + 1]]
        # IndexError catches last movie title
        except IndexError:
            dictionary[text_list[title_index]] = text_list[title_index + 2: text_list.index(text_list[-1])] 

    pprint.pprint(dictionary)


def findTheaterName(url):
    # Use regex to pull theater's name from url, follows format 'amc-theatername-number'
    match = re.search("amc-\S+['\/]", url)
    # Match indices are the theater's name
    theater_raw = url[match.start():match.end() - 1]
    # Capitialize the 'AMC' and first letter of theater name
    theater_raw = theater_raw[:5].upper() + theater_raw[5:]
    # Replace dashes from url with spaces
    theater = theater_raw.replace('-', ' ')
    
    return theater

if __name__ == "__main__":
    main()