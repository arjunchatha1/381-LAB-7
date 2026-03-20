import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt



url = "https://en.wikipedia.org/wiki/University_of_Calgary"


headers = {
    "User-Agent": "lab07-web-analyzer"
}
try:
    response = requests.get(url, headers = headers)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")


    # Part 2

    print(soup.prettify())

    # Part 3

    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    headings_count = len(headings)

   
    links = soup.find_all('a')
    links_count = len(links)

    
    paragraphs = soup.find_all('p')
    paragraphs_count = len(paragraphs)

    
    print(f"Total Headings: {headings_count}")
    print(f"Total Links: {links_count}")
    print(f"Total Paragraphs: {paragraphs_count}")



    # Part 4

    # Using the hint givenn in part 5
    all_text = soup.get_text().lower() 


    words = re.findall(r'\b\w+\b', all_text) 


    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1



    print("\nTop 5 Most Frequent Words: \n")

    for i in range(5):
        highest_count = -1
        top_word = ""

        
        for word in word_counts:
            
            if word_counts[word] > highest_count:
                highest_count = word_counts[word]
                top_word = word

        
        
        print(f"{top_word}: {highest_count}")

        
        del word_counts[top_word]


    # Part 5

    # Using the all_text variable from part 4 still 

    search_keyword = input("Enter a keyword to search for: ").lower()

    all_text = soup.get_text().lower()


    keyword_matches = re.findall(rf'\b{search_keyword}\b', all_text)

    count = len(keyword_matches)

    print(f"The keyword '{search_keyword}' appears {count} times in the webpage content.")
    
    # Part 6

    longest_p_text = ""
    max_word_count = 0


    paragraphs = soup.find_all('p')


    for p in paragraphs:
    
    
        p_text = p.get_text().strip()
        words_in_p = p_text.split()
        word_count = len(words_in_p)
        


        if word_count >= 5:
        
            if word_count > max_word_count:
                max_word_count = word_count
                longest_p_text = p_text


    print("\nLongest Paragraph:\n")
    print(f"\nWord Count: {max_word_count}")
    print(f"\nText in paragraph:\n {longest_p_text}")

except Exception as e:
    print(f"Error fetching content: {e}")



# Part 7

labels = ['Headings', 'Links', 'Paragraphs']
values = [headings_count, links_count, paragraphs_count]
plt.bar(labels, values)
plt.title('14')
plt.ylabel('Count')
#plt.savefig('web_analysis_results.png') # Save the figure as an image file
plt.show()










