import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """Fetch a webpage using requests and return the page content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return None

def parse_webpage(html):
    """Parse the webpage and extract relevant information using BeautifulSoup."""
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    paragraphs = [p.text for p in soup.find_all('p')]
    return title, paragraphs

def main():
    url = "https://www.example.com"
    print(f"Fetching webpage: {url}")
    
    html = fetch_webpage(url)
    if html:
        title, paragraphs = parse_webpage(html)
        
        print(f"\nWebpage Title: {title}")
        print("\nFirst few paragraphs:")
        for i, p in enumerate(paragraphs[:3], 1):
            print(f"{i}. {p[:100]}...")
    else:
        print("Failed to fetch the webpage.")

if __name__ == "__main__":
    main()
