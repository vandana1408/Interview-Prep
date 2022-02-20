"""
GET_AUTHOR_TITLES.PY

Write an HTTP GET method to retrieve information from an articles' database. The query response is paginated and can be further accessed by appending to the query string &page=num where num is the page number.

"""
import requests 
import json 

def get_article_titles(author): 
    base_url = "https://jsonmock.hackerrank.com/api/articles?"
    
    page = 1 
    pages = 5
    titles = []
    
    while page <= pages: 
        
        search_request = f"author={author}&page={str(page)}"
        req = requests.get(base_url + search_request)
        
        data = json.loads(req.text) 
        
        for articles in data['data']: 
            if articles['title']: 
                titles.append(articles['title'])
            elif articles['story_title']: 
                titles.append(articles['story_title'])
                
        page += 1
                        
    return titles  

if __name__ == "__main__":
    print(get_article_titles("epaga"))   
    
    