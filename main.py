from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    """Set up and return a Chrome WebDriver instance."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def fetch_webpage(url, driver):
    """Fetch a webpage using Selenium and return the page source."""
    try:
        driver.get(url)
        return driver.page_source
    except Exception as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return None

def parse_webpage(driver):
    """Parse the webpage and extract relevant information using Selenium."""
    try:
        title = driver.title
        paragraphs = [element.text for element in WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "p"))
        )]
        return title, paragraphs
    except Exception as e:
        print(f"An error occurred while parsing the webpage: {e}")
        return "No title found", []

def main():
    url = "https://www.example.com"
    print(f"Fetching webpage: {url}")
    
    driver = setup_driver()
    
    try:
        fetch_webpage(url, driver)
        title, paragraphs = parse_webpage(driver)
        
        print(f"\nWebpage Title: {title}")
        print("\nFirst few paragraphs:")
        for i, p in enumerate(paragraphs[:3], 1):
            print(f"{i}. {p[:100]}...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
