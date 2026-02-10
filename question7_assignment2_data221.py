import requests
from bs4 import BeautifulSoup

wikipedia_link = "https://en.wikipedia.org/wiki/Data_science"

#Storing the webpage HTML into a variable
data_science_page = requests.get(wikipedia_link, headers={"User-Agent": "Mozilla/5.0"}).text

#Parsing the webpage HTML using beautifulsoup
data_science_page = BeautifulSoup(data_science_page, "html.parser")

#Finding and printing the page title from <title> tag
data_science_page_title = data_science_page.title.get_text(strip=True)
print("Page title:", data_science_page_title)

# Find the main article content
content_div = data_science_page.find("div", id="mw-content-text")


#Finding the first paragraph
first_paragraph = None
for p in content_div.find_all("p"):
    text = p.get_text(strip=True)  # Converts the paragraph tag into plain text (removes HTML tags) and removes extra whitespace
    if len(text) >= 50:  #Checks how many characters are in the paragraph.
        first_paragraph = text  #Save paragraph that is long enough to variable
        break

print(f"First paragraph: {first_paragraph}")
