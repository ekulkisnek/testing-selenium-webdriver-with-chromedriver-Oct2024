import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def setup_driver():
    """Set up and return a Chrome WebDriver instance."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    try:
        # Use the system-installed ChromeDriver
        chromedriver_path = "/nix/store/chromium-chromedriver/bin/chromedriver"
        if not os.path.exists(chromedriver_path):
            print(f"ChromeDriver not found at {chromedriver_path}")
            chromedriver_path = os.popen("which chromedriver").read().strip()
            if not chromedriver_path:
                print("ChromeDriver not found in PATH")
                return None
        print(f"ChromeDriver found at {chromedriver_path}")
        service = Service(chromedriver_path)

        # Set the path to the Chromium binary
        chromium_path = "/nix/store/chromium/bin/chromium"
        if not os.path.exists(chromium_path):
            print(f"Chromium not found at {chromium_path}")
            chromium_path = os.popen("which chromium").read().strip()
            if not chromium_path:
                print("Chromium not found in PATH")
                return None
        print(f"Chromium found at {chromium_path}")
        chrome_options.binary_location = chromium_path

        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("ChromeDriver initialized successfully")
        return driver
    except Exception as e:
        print(f"Error setting up ChromeDriver: {e}")
        return None

def fetch_webpage(url, driver):
    """Fetch a webpage using Selenium and return the page content."""
    try:
        driver.get(url)
        return driver.page_source
    except Exception as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return None

def parse_webpage(driver):
    """Parse the webpage and extract relevant information using Selenium."""
    title = driver.title
    paragraphs = [p.text for p in driver.find_elements(By.TAG_NAME, 'p')]
    return title, paragraphs

def main():
    url = "https://www.example.com"
    print(f"Fetching webpage: {url}")
    
    driver = setup_driver()
    if not driver:
        print("Failed to set up ChromeDriver. Exiting.")
        return

    html = fetch_webpage(url, driver)
    
    if html:
        title, paragraphs = parse_webpage(driver)
        
        print(f"\nWebpage Title: {title}")
        print("\nFirst few paragraphs:")
        for i, p in enumerate(paragraphs[:3], 1):
            print(f"{i}. {p[:100]}...")
    else:
        print("Failed to fetch the webpage.")
    
    driver.quit()

if __name__ == "__main__":
    main()
