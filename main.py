import requests

api_key = "298a5adfdf594ec4b7acac10fd3458bf"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-12-21&sortBy=publishedAt&" \
      "apiKey=298a5adfdf594ec4b7acac10fd3458bf"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
      print(article["title"])
