import json # Change here
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the JSON file
with open("JSON/articles.json", "r", encoding="utf-8") as file:
    articles = json.load(file)

# Initialize an empty list to store article content
scraped_data = []

# Iterate through each article
for article in articles:
    try:
        # Open the article's link
        driver.get(article["Link"])
        time.sleep(3)  # Wait for the page to load
        
        # Extract content from the specified div
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.editor-box p")
        content = " ".join([paragraph.text for paragraph in paragraphs])
        
        # Append the extracted content to the data
        scraped_data.append({
            "title": article["Title"],
            "link": article["Link"],
            "content": content
        })

        print(f"Scraped: {article['Title']}")
    except Exception as e:
        print(f"Error scraping {article['Title']}: {e}")

# Save the scraped data to a new JSON file
with open("JSON/scraped_articles.json", "w", encoding="utf-8") as outfile:
    json.dump(scraped_data, outfile, ensure_ascii=False, indent=4)


# Close the driver
driver.quit()