
from bs4 import BeautifulSoup
import requests
import re
import json

def fetch_cookie():
    root_url = "https://country-leaders.onrender.com"
    endpoint="cookie"
    cookie_url=f"{root_url}/{endpoint}"
    # Query the enpoint, set the cookies variable and display it (2 lines)
    cookies1= requests.get(cookie_url)
    cookies1 =cookies1.cookies.get_dict() 
    return cookies1

    
# Regex pattern to detect bold text within <b>, <strong>, or <i> (italic) tags
pattern_2=  r"<(?:b|strong|i)[^>]*>.*?<\/(?:b|strong|i)>"
# Detects Wikipedia references
reference_pattern = r"\[\d+\]"  
# Removes content inside parentheses
parentheses_pattern = r"\([^)]*\)" 

#overwrite our function with new pattern 
def get_first_paragraph(wikipedia_url,session= None):
    #check the session firstly
    if session is None:
        #Create new session in case we have no one
        session = requests.Session()
        #update the cookie with new session
        session.cookies.update(fetch_cookie())
 

    # get the result of url
    session.get("https://country-leaders.onrender.com/cookie")
    result = session.get(wikipedia_url)
    # paring url's html content
    soup = BeautifulSoup(result.text, "html.parser")
    #finding all paragraphs .
    paragraphs1 = soup.find_all('p')
    #looping throup the ps 
    for paragraph in paragraphs1:
      first_paragraph = paragraph.get_text()
      #check if we have bolds  then thats my first paragraph
      if re.search(pattern_2 ,str(paragraph) ):
          return first_paragraph


import requests

def get_leaders(session):
    first_paragraph = ""
    leaders_per_country = {}

    # Define URLs
    root_url = "https://country-leaders.onrender.com"
    countries_url = f"{root_url}/countries"
    leaders_url = f"{root_url}/leaders"

    # Get initial cookies
    cookies = fetch_cookie()

    # Fetch countries list
    countries_response = session.get(countries_url, cookies=cookies)
    countries = countries_response.json()

    # Loop over countries to fetch leaders
    for country in countries:
        params = {"country": country}
        
        # Attempt to get leaders for the country
        result = session.get(leaders_url, cookies=cookies, params=params)

        # Retry fetching cookie if unauthorized
        if result.status_code in [401, 403]:  
            cookies = fetch_cookie()
            result = session.get(leaders_url, cookies=cookies, params=params)
        
        leaders_per_country[country] = result.json()

    # Loop through leaders and get first paragraph for each Wikipedia link
    for country in countries:
        for leader in leaders_per_country[country]:
            wikipedia_url = leader.get("wikipedia_url")
            print(wikipedia_url)
            if wikipedia_url:
                first_paragraph = get_first_paragraph(wikipedia_url, session)
                leader["first_paragraph"] = first_paragraph
    
    return leaders_per_country



#the same as above with puting in function
def save (leaders_per_country):
    with open("leaders_per_country.json", "w", encoding="utf-8") as f:
        json.dump(leaders_per_country, f, ensure_ascii=False, indent=4)
        return

# Last Calling !
save(get_leaders(requests.Session()))
