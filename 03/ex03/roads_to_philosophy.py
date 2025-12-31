from bs4 import BeautifulSoup, NavigableString, Tag
import requests

class WikiWalker:
    def __init__(self, search_query):
        self.search_query = search_query
        self.visited_pages = dict()
        self.base_url = "https://en.wikipedia.org/wiki/"
        self.search_urk = "https://en.wikipedia.org/w/index.php?fulltext=1&search="
        self.session = requests.session()
        self.session.update({'User-Agent': 'RoadsToPhilosophy/1.0'})
        self.excluded_namespaces = [
            '/wiki/Wikipedia:', '/wiki/File:', '/wiki/Help:',
            '/wiki/Special:', '/wiki/Category:', '/wiki/Talk:',
            '/wiki/Template:', '/wiki/Portal:'
        ]
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
    def _find_link_in_paragraph(self, paragraph):
        """
        Recursively searches a paragraph for a valid link, ignoring content 
        in parentheses or italics.
        """
        # Dictionary to track parenthesis depth (mutable so it persists in recursion)
        state = {'parens': 0}
        def traverse(element):
            for child in element.children:
                if isinstance(child, NavigableString):
                    text = str(child)
                    state['parens'] += text.count('(')
                    state['parens'] -= text.count(')')
                
                elif isinstance(child, Tag):
                    # Skip italics
                    if child.name in ['i', 'em']:
                        continue
                    
                    # Check anchor tags
                    if child.name == 'a':
                        if state['parens'] == 0:
                            href = child.get('href')
                            if self._is_valid_wiki_link(href):
                                return href
                    
                    # Recurse deeper (e.g., into <b> tags)
                    result = traverse(child)
                    if result:
                        return result
            return None

        return traverse(paragraph)
    def_get_next_link(self, soup):
        """Scans the main content of the soup for the first valid link."""
        content = soup.find(id="mw-content-text")
        if not content:
            return None
        
        parser_output = content.find(class_="mw-parser-output")
        if not parser_output:
            return None

        # Check direct paragraph children only
        for p in parser_output.find_all('p', recursive=False):
            link = self._find_link_in_paragraph(p)
            if link:
                return link
        return None

    def walk(self, search_term):
        """Main execution loop."""
        current_url = f"{self.base_url}/wiki/{search_term}"

        while True:
            soup = self._get_soup(current_url)
            
            # Extract and validate title
            title_node = soup.find(id="firstHeading")
            if not title_node:
                print("It leads to a dead end !")
                sys.exit(0)
            
            title = title_node.text
            print(title)

            # 1. Success Condition
            if title == "Philosophy":
                print(f"{len(self.visited_titles)} roads from {self.visited_titles[0]} to philosophy")
                sys.exit(0)

            # 2. Infinite Loop Condition
            if title in self.visited_titles:
                print("It leads to an infinite loop !")
                sys.exit(0)

            # Record visit
            self.visited_titles.append(title)
            self.visited_urls.append(current_url)

            # 3. Find Next Link
            next_path = self._get_next_link(soup)
            if not next_path:
                print("It leads to a dead end !")
                sys.exit(0)

            current_url = self.base_url + next_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./roads_to_philosophy.py \"search_term\"")
        sys.exit(1)
    
    # Initialize and run
    walker = WikiWalker()
    try:
        walker.walk(sys.argv[1])
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
