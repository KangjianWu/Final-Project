import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize

def extract_locations(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    ne_tree = ne_chunk(tagged_words)

    locations = []
    for subtree in ne_tree.subtrees():
        if subtree.label() == "GPE":
            locations.append(" ".join([leaf[0] for leaf in subtree.leaves()]))
    return locations

# text = "Fungal infection outbreak affects 90+ workers at Michigan paper mill"
# locations = extract_locations(text)
# print(locations)


# import spacy

# def extract_locations2(text):
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(text)

#     locations = []
#     for ent in doc.ents:
#         if ent.label_ == "GPE":
#             locations.append(ent.text)
#     return locations


# text = "How kids in MA territories 'bear the burden' of neglected tropical disease"
# locations = extract_locations2(text)
# print(locations)

import requests
from bs4 import BeautifulSoup

def get_soup(url):
# URL of USA Today's Health section
# url = 'https://www.cnn.com/health'

    # Retrieve the HTML content of the page
    response = requests.get(url)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

america_states = ["Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"Rhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming",]

crawling_links = ["https://www.cnn.com/health", "https://www.nytimes.com/section/health", \
                  "https://www.nbcnews.com/health", "https://www.washingtonpost.com/health/", "https://www.usatoday.com/news/health/", \
                  "https://www.webmd.com/news/default.htm", "https://abcnews.go.com/health", "https://www.cbsnews.com/health/", 
                  "https://www.foxnews.com/category/health", "https://www.wsj.com/news/life-work/health-wellness"]

import collections
Res = []
Location_map = collections.defaultdict(list)

def getNewsFromUrl(url, classname):
    soup = get_soup(url)
    # Find all the article titles on the page
    articles = soup.find_all('a',)
    print("len",len(articles))

    news_res = []
    for article in articles:
        # get locations name and justify
        title = article.text
        locations = extract_locations(title)
        if len(locations) > 0 and len(locations[0]) > 1:
            news_title = title.lstrip().rstrip()

            if len(news_title) > 10:
                link = article.get('href')
                print('\n', news_title)
                # print(url + link)
                for loc in locations:
                    if loc in america_states:
                        # if url == "https://www.usatoday.com/news/health/":
                        #     new_url = "https://www.usatoday.com"
                        # if url == "https://www.cnn.com/health":
                        #   if "https" in link:
                        #     new_url = ""
                        #   else:
                        #     new_url = "https://www.cnn.com"
                        # if url == "https://www.nytimes.com/section/health":
                        #     new_url = "https://www.nytimes.com"
                        # if url == "https://www.washingtonpost.com/health/":
                        #     new_url = "https://www.washingtonpost.com"
                        # if url == "https://www.nbcnews.com/health":
                        #     new_url = "https://www.nbcnews.com"
                        # if url == "https://www.webmd.com/news/default.htm":
                        #     new_url = "https://www.webmd.com"
                        # if url == "https://abcnews.go.com/health":
                        #     new_url = url
                        # if url == "https://www.cbsnews.com/health/":
                        #     new_url = "https://www.cbsnews.com"
                        # if url == "https://www.foxnews.com/category/health":
                        #     new_url = "https://www.foxnews.com"
                        # if url == "https://www.wsj.com/news/life-work/health-wellness":
                        #     new_url = "https://www.wsj.com"
                        if "https" == link[5]:
                            Location_map[loc].append((news_title, link))
                        else:
                            newlink = '/'.join(url.split('/')[:3])
                            Location_map[loc].append((news_title, newlink))
                news_res.append(news_title)
                print("locations", locations)
    return len(news_res)

for link in crawling_links:
    print(link)
    getNewsFromUrl(link, 0)

print("--------------------")
# print(Location_map)
for key in Location_map:
    print(key)
    print(len(Location_map[key]))
    for news, link in Location_map[key]:
        print("   " + news + " :" + link)

