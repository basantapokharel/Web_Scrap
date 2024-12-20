import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
sum = 0
all_articles = []  # List to store all article details

for i in range(1, 2):
    # Open the Setopati website
    url = f"https://www.setopati.com/sports/cricket?page={i}"
    driver.get(url)

    # Wait for the page to load
    time.sleep(3)

    # Select all divs with the class 'items col-md-4'
    articles = driver.find_elements(By.CSS_SELECTOR, 'div.items.col-md-4')

    # Iterate through each article and extract details
    count = 0
    for article in articles:
        try:
            if count == 2:  # In md-4 run up to 18, in md-6 up to 12
                break
            count += 1

            # Extract the link
            link = article.find_element(By.TAG_NAME, 'a').get_attribute('href')

            # Extract the title
            title = article.find_element(By.CLASS_NAME, 'main-title').text

            # Extract the category (tag)
            tag = article.find_element(By.CLASS_NAME, 'tags').text

            # Extract the author
            author = article.find_element(By.CLASS_NAME, 'author-title').text

            # Extract the publication date
            date = article.find_element(By.CLASS_NAME, 'time-stamp').text

            # Add article details to the list
            article_data = {
                "Title": title,
                "Tag": tag,
                "Author": author,
                "Date": date,
                "Link": link
            }
            all_articles.append(article_data)

            print(f"Title: {title,count}")
            print(f"Tag: {tag}")
            print(f"Author: {author}")
            print(f"Date: {date}")
            print(f"Link: {link}")
            print("-" * 80)
        except Exception as e:
            print("Error extracting article:", e)

    sum += len(articles)
    print("Total articles found:", len(articles))

# Save all articles to a JSON file
with open("JSON/articles.json", "w", encoding="utf-8") as json_file:
    json.dump(all_articles, json_file, ensure_ascii=False, indent=4)

print("Total articles found:", sum)
print("Data saved to JSON/articles.json")
# Close the driver after scraping
driver.quit()