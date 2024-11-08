
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
    #finding all paragraphs 
    paragraphs1 = soup.find_all('p')
    #looping throup the ps 
    for paragraph in paragraphs1:
      first_paragraph = paragraph.get_text()
      #check if we have bolds  then thats my first paragraph
      if re.search(pattern_2 ,str(paragraph) ):
          return first_paragraph


#add session to get_leaders
def get_leaders(session_):
    first_paragraph1=""
    leaders_per_country={}
    #1 defining urls and endpoints
    root_url = "https://country-leaders.onrender.com"
    countries_endpoint = "countries"
    leaders_endpoint = "leaders"
    countries_url=f"{root_url}/{countries_endpoint}"
    leaders_url=f"{root_url}/{leaders_endpoint}"
    #2 Getting cookie
    cookies1=fetch_cookie()
    #3 getting the countires
    countries= requests.get(countries_url,cookies=cookies1)
    # 4 looping over the countries and geting the reuslts 
    for country in countries.json():
        params= { "country": country}
        result= requests.get(leaders_url,cookies=cookies1,params=params)
    # check the status 
        if result.status_code in [401, 403]:  
            #fetch our cookie !
            cookies1 = fetch_cookie()
            #request again
            result = requests.get(leaders_url, cookies=cookies1, params=params)

        leaders_per_country[country]=result.json()
    for country in countries.json():
        for leader in leaders_per_country[country]:
            Wikipedia_url1=leader["wikipedia_url"]
            print(Wikipedia_url1)
            #pass the session to get_first_paragraph(()
            first_paragraph1= get_first_paragraph(Wikipedia_url1,session_)
            leader["first_paragraph"] = first_paragraph1
           
    return leaders_per_country



#the same as above with puting in function
def save (leaders_per_country):
    with open("leaders_per_country.json", "w", encoding="utf-8") as f:
        json.dump(leaders_per_country, f, ensure_ascii=False, indent=4)
        return

# Last Calling !
save(get_leaders(requests.Session()))
