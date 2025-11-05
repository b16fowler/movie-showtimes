from bs4 import BeautifulSoup
import requests

def main():
    '''
    BeautifulSoup notes:

    title = html.find("title").text

    print(html.prettify())
    print(html.find_all("a"))
    print(html.get_text())
    '''

    # Get request to the AMC Southington showtimes, then parse html
    response_south = requests.get("https://www.amctheatres.com/movie-theatres/plainville/amc-southington-12/showtimes")
    html_south = BeautifulSoup(response_south.text, "html.parser")
    
    # Finds and prints inner text for all 'a' tags for Southington theater
    for tag in html_south.find_all("a"):
        print(tag.get_text())

    # Get request to the AMC Plainville showtimes, then parse html
    response_plain = requests.get("https://www.amctheatres.com/movie-theatres/plainville/amc-plainville-20/showtimes")
    html_plain = BeautifulSoup(response_plain.text, "htmlparser")

    # Finds and prints inner text for all 'a' tags for Plainville theater
    for tag in html_plain.find_all("a"):
        print(tag.get_text())
        

if __name__ == "__main__":
    main()