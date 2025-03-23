
# Selenium Web Scraper

This project demonstrates web scraping using Selenium WebDriver with Chrome in a headless mode. The application is configured to run in a Replit environment and handles the necessary setup for ChromeDriver and Chromium.

## Features

- Automated web page scraping using Selenium
- Headless Chrome browser configuration
- Automatic detection of ChromeDriver and Chromium binaries
- Extraction of webpage title and paragraphs
- Error handling and logging

## Main Components

### `setup_driver()`
- Configures Chrome options for headless operation
- Locates ChromeDriver and Chromium binaries
- Initializes and returns a Chrome WebDriver instance

### `fetch_webpage(url, driver)`
- Takes a URL and WebDriver instance
- Retrieves the webpage content
- Handles potential errors during fetching

### `parse_webpage(driver)`
- Extracts the webpage title
- Collects all paragraph texts
- Returns structured data from the webpage

### `main()`
- Orchestrates the scraping process
- Demonstrates usage with example.com
- Prints extracted information to console

## Dependencies
- selenium: WebDriver for browser automation
- Other dependencies are managed through Poetry (see pyproject.toml)

## Usage
To run the scraper:
1. Click the "Run" button in Replit
2. The script will fetch example.com and display its title and first few paragraphs

## Error Handling
The script includes comprehensive error handling for:
- Missing ChromeDriver/Chromium binaries
- Failed webpage fetching
- General exceptions during execution
