from selenium import webdriver

def scrape_screen(url):
    # Create a ChromeDriver instance
    driver = webdriver.Chrome()

    # Navigate to the given URL
    driver.get(url)

    # Scrape the screen by accessing the page source
    page_source = driver.page_source

    # Close the ChromeDriver instance
    driver.close()

    return page_source

if __name__ == '__main__':
    # Read the URL from the user
    url = input("Enter the URL to scrape: ")

    # Scrape the screen of the given URL
    page_source = scrape_screen(url)

    # Print the page source
    print(page_source)
