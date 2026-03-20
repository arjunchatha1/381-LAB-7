import requests 
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
total_h = len(soup.find_all(['h1','h2','h3','h4', 'h5', 'h6']))
print(total_h)

total_a = len(soup.find_all('a'))
print(total_a)

total_p = len(soup.find_all('p'))
print(total_p)


"""
Analyze the webpage's content to identify the most frequently used words. To achieve this:
• Extract all the text content from the web page using soup.get_text().
• Convert the text to lowercase.
• Split the text into individual words using the findall method of Python's re (regular expressions) module.
• Count the frequency of each word.
• Display the top 5 most frequently occurring words with their counts.
"""
