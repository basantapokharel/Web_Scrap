import json
from nltk.tokenize import word_tokenize

# Load the JSON file
with open("JSON/scraped_articles.json", 'r', encoding='utf-8') as file:
    articles = json.load(file)

# Tokenize the content of each article
tokenized_articles = []
for index, article in enumerate(articles, start=1):
    tokens = word_tokenize(article['content'])
    
    tokenized_articles.append(
        {
            'number': index,  # New key for number before title
            'title': article['title'],
            'tokens': tokens  # Tokens in one line
        }
    )

# Save the tokenized articles to a JSON file
output_file = 'JSON/tokenized_articles.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(tokenized_articles, file, ensure_ascii=False, indent=4)

print(f"Tokenized articles have been saved to {output_file}")