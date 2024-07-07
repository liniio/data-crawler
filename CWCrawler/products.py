import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

# Define the URL of the website to scrape
url = "#"

# Send an HTTP request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the fetched webpage content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product containers in the webpage
    product_containers = soup.find_all(class_="product-container")

    # Create an empty list to store product information
    products = []

    # Loop through the product containers
    for product_container in product_containers:
        # Extract product information
        product_image = product_container.find(class_="product-image")["src"]
        product_name = product_container.find(class_="product-name").text
        product_price = product_container.find(class_="product-price").text
        product_description = product_container.find(class_="product-description").text

        # Append the product information to the list
        products.append({
            "image": product_image,
            "name": product_name,
            "price": product_price,
            "description": product_description
        })

    # Print the scraped product information
    print(products)
else:
    print("Failed to fetch the webpage")