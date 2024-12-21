import json
import os

# List the JSON files you want to combine
json_files = ["JSON/Article_Content/sports_content_4.json", "JSON/Article_Content/sports_content_6.json", "JSON/Article_Content/politics_content_4.json", "JSON/Article_Content/politics_content_6.json", "JSON/Article_Content/kinmel_content_4.json", "JSON/Article_Content/kinmel_content_6.json"]  # Add your file names here

# List to store combined data
combined_data = []

# Loop through each JSON file and load the data
for file in json_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            combined_data.extend(data)  # Combine the data (assuming it's a list)
            print(f"Data from {file} loaded successfully.")
    except Exception as e:
        print(f"Error loading {file}: {e}")

# Save the combined data into a new JSON file
with open("JSON/Article_Content/combined_data.json", "w", encoding="utf-8") as outfile:
    json.dump(combined_data, outfile, ensure_ascii=False, indent=4)

print("Combined data saved to 'combined_data.json'.")
