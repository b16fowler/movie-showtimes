from bs4 import BeautifulSoup
import requests

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
        # print(item.get_text())
        text_list.append(item.get_text())

    # Find lines that are just the theaters name, there's one after each movie title
    matches = [i for i, tag in enumerate(text_list) if tag == theater]
    # Decrement by 1 to make list of movie titles
    movie_indexes = [item - 1 for item in matches]
    
    dictionary = {}
    # Use titles and indices to locate all showtimes for each movie 
    for index, title_index in enumerate(movie_indexes):
        try:
            dictionary[text_list[title_index]] = text_list[title_index + 2:movie_indexes[index + 1]] 
        except IndexError:
            dictionary[text_list[title_index]] = text_list[title_index + 2: text_list.index(text_list[-1])] 

    print(dictionary)

if __name__ == "__main__":
    main()