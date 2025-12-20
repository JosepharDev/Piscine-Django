import requests, json
 #dewiki, sys

URL = "https://en.wikipedia.org/w/api.php"
query = "chocolate"
params = {
        "action": "opensearch",
        "search": query,
        "limit": 10,
        "namespace": 0, # Search only articles, ignoring Talk, Mediawiki, etc.
        "format": "json"
    }
try:
    response = requests.get(URL, params=params)
    response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

    search_results = response.json()
    # The structure is typically [search_term, [titles], [descriptions], [urls]]
    titles = search_results[1]
    print(titles)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    
print(response.status_code)