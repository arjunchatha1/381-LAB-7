import requests
import re
from bs4 import BeautifulSoup 

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

headers = { 
    "User-Agent": "lab07-web-analyzer" 
}

try: 
    response = requests.get(url, headers=headers) 
    response.raise_for_status() # Ensures the request was successful 
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    
except Exception as e:
    print(f"Error fetching content: {e}")
    

print(soup.prettify())


"""
In web_analyzer.py, write Python code that counts and displays:
• The number of headings (<h1> to <h6>) in the HTML content. This should be a total count of all heading tags, rather than a count for each individual heading level.
• The number of links (<a> tags).
• The number of paragraphs (<p> tags). Hint: You can use Beautiful Soup's find_all method.
"""

headings_count = len(soup.find_all(['h1','h2','h3','h4', 'h5', 'h6']))
print(headings_count)

links_count = len(soup.find_all('a'))
print(links_count)

paragraphs_count = len(soup.find_all('p'))
print(paragraphs_count)

print("\n")

"""
Analyze the webpage's content to identify the most frequently used words. To achieve this:
• Extract all the text content from the web page using soup.get_text().
• Convert the text to lowercase.
• Split the text into individual words using the findall method of Python's re (regular expressions) module.
• Count the frequency of each word.
• Display the top 5 most frequently occurring words with their counts.
"""
lowercase_content = soup.getText().casefold()

words = re.findall(r'\b\w+\b', lowercase_content)

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

top_five_values = [0] * 5
top_five_keys = [None] * 5

for key in word_count:
    count = word_count[key]
    index = 0
    while index < 5:
        if top_five_values[index] < count:
            top_five_keys.insert(index, key)
            top_five_values.insert(index, count)
            break
        index += 1

# print top 5
for i in range(0, 5):
    print(top_five_keys[i] + ": " + str(top_five_values[i]))

print("\n")

"""
Write Python code that asks the user for a keyword and counts how many times it appears in the webpage content, ignoring case.
Then print the result clearly.
"""
plain_text = soup.get_text().casefold()
search_text = input("Enter a search term: ").casefold()

search_count = plain_text.count(search_text)
print('"'+ search_text + '" appears ' + str(search_count) + " times")

print("\n")

"""
Write Python code to find and display the longest paragraph in the webpage, and the number of words it contains.
Ignore empty paragraphs or paragraphs with fewer than 5 words.
"""
p_elements = soup.find_all('p')

max_length = 0
max_text = ""

for p in p_elements:
    innerSoup = BeautifulSoup(str(p), 'html.parser')
    plain_p = innerSoup.get_text()
    length = len(plain_p.split())
    if length > max_length:
        max_length = length
        max_text = plain_p

print("The longest paragraph has " + str(max_length) + " words:")
print(max_text)




import matplotlib.pyplot as plt 
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings_count, links_count, paragraphs_count] 
plt.bar(labels, values)
plt.title('Put your Group# Here')
plt.ylabel('Count')
#plt.savefig('web_analysis_results.png') # Save the figure as an image file
plt.show()