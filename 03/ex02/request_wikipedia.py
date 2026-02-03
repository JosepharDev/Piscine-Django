import requests, json, sys
from dewiki import from_string

def write_to_file(cleaned_article: str, title: str)-> None:
    filename = title.replace(" ", "_") + ".wiki"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(cleaned_article)
    print(f"✔ Result saved in {filename}")

def get_correct_name(requested_string: str)-> str:
    HEADERS = {
    "User-Agent": "WikiRequester/1.0 (school-project)"
    }
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": requested_string
    }
    try:
        response = requests.get(url=base_url, params=params, headers=HEADERS)
        print("requested url: ", response.url)
    except requests.RequestException as e:
        print("Unable to connect to wikipedia:  ", e)
        sys.exit(1)
    if response.status_code != 200:
        print("Wikipedia api error")
        sys.exit(1)
    data = response.json()
    if "query" not in data or not data["query"]["search"]:
        print("No result found for this query.")
        exit(1)
    page_title = data["query"]["search"][0]["title"]
    return page_title


def get_article(title: str)-> str:
    HEADERS = {
    "User-Agent": "WikiRequester/1.0 (school-project)"
    }
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
            "action": "query",
            "format": "json",
            "prop": "revisions",
            "rvprop": "content",
            "rvslots": "main",
            "titles":title
        }
    try:
        response = requests.get(base_url, params=params, headers=HEADERS)
        print("requested url: ", response.url)
    except requests.exceptions.RequestException as e:
        print("Unable to connect to wikipedia:  ", e)
        sys.exit(1)

    if response.status_code != 200:
        print("Wikipedia api error")
        sys.exit(1)
    data = response.json()

    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    if "revisions" not in page:
        print("No content found.")
        sys.exit(1)
    
    wiki_text = page["revisions"][0]["slots"]["main"]["*"]
    clean_text = from_string(wiki_text)
    return clean_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of argument")
        sys.exit(1)
    title = get_correct_name(sys.argv[1].strip())
    article = get_article(title)
    write_to_file(article, title)
    print(title)