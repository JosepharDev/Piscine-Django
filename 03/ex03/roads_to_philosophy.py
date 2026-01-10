from bs4 import BeautifulSoup
import requests, sys

class WikiWalker:
    def __init__(self):
        self.visited_pages = dict()
        self.base_url = "https://en.wikipedia.org"
        self.search_url = "https://en.wikipedia.org/w/index.php?fulltext=1&search="
        self.session = requests.session()
        self.session.headers.update({'User-Agent': 'RoadsToPhilosophy/1.0'})
        self.excluded_namespaces = [
            '/wiki/Wikipedia:', '/wiki/File:', '/wiki/Help:',
            '/wiki/Special:', '/wiki/Category:', '/wiki/Talk:',
            '/wiki/Template:', '/wiki/Portal:'
        ]
    
    
    def _get_correct_query(self, term):
        search = self.search_url + term
        response = self.session.get(search)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            sys.exit(1)
        def parse_search(soup):
            search_results = soup.find_all('div', class_='mw-search-result-heading')
            if not search_results:
                return None
            first_result = search_results[0].find('a')
            if first_result:
                return first_result['href']
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        correct_path = parse_search(soup)    
        if correct_path:
            print(f"Redirected to: {correct_path}")
            return str(correct_path).replace("/wiki/", "")
        return None
    
    def _get_soup(self, url):
        """Fetches the URL and returns a BeautifulSoup object."""
        try:
            response = self.session.get(url)
            if response.status_code == 404:
                print("It leads to a dead end !")
                sys.exit(0)
            elif response.status_code != 200:
                print(f"Error: Received status code {response.status_code}")
                sys.exit(0)
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Network error: {e}")
            sys.exit(1)


    def _get_next_link(self, soup):
        """Scans the main content of the soup for the first valid link."""
        content = soup.find(id="mw-content-text")
        if not content:
            return None

        links = soup.select("p > a")
        for link in links:
            if link.get('href') is not None:
                href = link['href']
                if any(href.startswith(ns) for ns in self.excluded_namespaces):
                    continue
                return href
        return None

    def walk(self, search_term):
        """Main execution loop."""
        correct_search_term = self._get_correct_query(search_term)
        if correct_search_term is None:
            print("No article Found using this search term!")
            sys.exit(0)
        current_url = f"{self.base_url}/wiki/{correct_search_term}"
        print(f"Starting at: {current_url}")

        while True:
            soup = self._get_soup(current_url)
            
        
            title_node = soup.find(id="firstHeading")
            if not title_node:
                print("It leads to a dead end !")
                sys.exit(0)
            
            title = title_node.text
            print(title)

            if title == "Philosophy":
                print(f"{len(self.visited_pages)} roads from {list(self.visited_pages.values())[0]} to philosophy")
                sys.exit(0)

            if title in self.visited_pages.values():
                print("It leads to an infinite loop !")
                sys.exit(0)

            self.visited_pages[current_url] = title

            next_path = self._get_next_link(soup)
            if not next_path:
                print("It leads to a dead end !")
                sys.exit(0)

            current_url = self.base_url + next_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./roads_to_philosophy.py \"search_term\"")
        sys.exit(1)

    walker = WikiWalker()
   
    try:
        walker.walk(sys.argv[1])
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
