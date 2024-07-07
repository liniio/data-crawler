import requests
from bs4 import BeautifulSoup

url = ''

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product links in the page
    product_links = [item.get('href') for item in soup.find_all('a', class_='woocommerce-LoopProduct-link')]

    # Print the product links
    for link in product_links:
        print(link)
else:
    print(f'Failed to load the page: {response.status_code}')