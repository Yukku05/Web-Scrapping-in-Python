
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set search term and headers
search_term = "headphones"
url = f"https://www.amazon.in/s?k={search_term}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Initialize lists
product_names = []
product_prices = []
product_ratings = []

# Extract data
for product in soup.find_all("div", {"data-component-type": "s-search-result"}):
    name_tag = product.h2
    name = name_tag.text.strip() if name_tag else "N/A"

    price_tag = product.find("span", class_="a-price-whole")
    price = price_tag.text.strip() if price_tag else "N/A"

    rating_tag = product.find("span", class_="a-icon-alt")
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    product_names.append(name)
    product_prices.append(price)
    product_ratings.append(rating)

# Save to CSV
data = pd.DataFrame({
    "Product Name": product_names,
    "Price": product_prices,
    "Rating": product_ratings
})

data.to_csv("amazon_products.csv", index=False)
print("Scraping completed. Data saved to 'amazon_products.csv'.")
