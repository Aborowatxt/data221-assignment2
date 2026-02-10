import requests
from bs4 import BeautifulSoup

wikipedia_link = "https://en.wikipedia.org/wiki/Data_science"

#Storing the webpage HTML into a variable
data_science_page = requests.get(wikipedia_link, headers={"User-Agent": "Mozilla/5.0"}).text

#Parsing the webpage HTML using beautifulsoup
data_science_page = BeautifulSoup(data_science_page, "html.parser")

# Find the main article content
content_div = data_science_page.find("div", id="mw-content-text")

#Find all <h2> headings inside the content area
section_headings = content_div.find_all("h2")

filtered_headings = []
excluded_sections = ["References", "External links", "See also", "Notes"]

for headings in section_headings:
    headings_text = headings.get_text(strip=True)

    # Remove [edit] text
    headings_text = headings_text.replace("[edit]", "")

    # Check if heading should be skipped
    skip_heading = False
    for word in excluded_sections:
        if word in headings_text:
            skip_heading = True

    if skip_heading:
        continue

    filtered_headings.append(headings_text)  #add filtered headings to a new list

print(filtered_headings)

# Saving the headings to headings.txt
file = open("headings.txt", "w")
for heading in filtered_headings:
    file.write(heading + "\n")
file.close()
