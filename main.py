import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    """Fetch a webpage and return its content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return None

def parse_webpage(html_content):
    """Parse the HTML content and extract relevant information."""
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    paragraphs = [p.text for p in soup.find_all('p')]
    return title, paragraphs

def main():
    url = "https://www.example.com"
    print(f"Fetching webpage: {url}")
    
    html_content = fetch_webpage(url)
    if html_content:
        title, paragraphs = parse_webpage(html_content)
        
        print(f"\nWebpage Title: {title}")
        print("\nFirst few paragraphs:")
        for i, p in enumerate(paragraphs[:3], 1):
            print(f"{i}. {p[:100]}...")
    else:
        print("Failed to fetch the webpage.")

if __name__ == "__main__":
    main()
