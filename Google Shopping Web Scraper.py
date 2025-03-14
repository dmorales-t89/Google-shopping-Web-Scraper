#Diego A Morales Torres


# Imported the needed libraries. I did some research on Selenium and watched some tutorials for the specifics.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Basic function that converts reviews to a numerical value. 
def convert_reviews(review_text):
    try:
        if 'K' in review_text:
            return int(float(review_text.replace('K', '').strip()) * 1000)
        else:
            return int(review_text.strip())
    except ValueError:
        return 0  # Return 0 if the value cannot be converted

# Ask the user for the search term
search_term = input("Enter the search term you want to look up: ")

# Specify the path to your chromedriver executable
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Maximize the window so nothing is obstructed
driver.maximize_window()

try:
    # Open Google Shopping
    driver.get("https://shopping.google.com/")

    # Wait for the search input field to load and search for the term
    #Chatgpt helped me learn a bit more about the selectors
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)

    # Wait for product elements to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.njFjte"))
    )

    # Extract product elements
    products = driver.find_elements(By.CSS_SELECTOR, "div.njFjte")

    # Store product information
    product_list = []

    # Parse product details and extract links
    for index in range(len(products[:10])):  # Limit to top 10 products
        try:
            # Re-locate products due to potential changes; this helped me get the links in the right order
            products = driver.find_elements(By.CSS_SELECTOR, "div.njFjte")
            product = products[index]

            # Extract product details from the aria-label
            aria_label = product.get_attribute('aria-label')
            if aria_label:
                title = aria_label.split("Current Price:")[0].strip()
                price = aria_label.split("Current Price:")[1].split(".")[0].strip().replace("$", "").replace(",", "")
                condition = "Refurbished" if "Refurbished" in aria_label else "New"
                rating = (
                    float(aria_label.split("Rated")[1].split("out of")[0].strip())
                    if "Rated" in aria_label else 0.0
                )
                reviews_text = (
                    aria_label.split("reviews")[0].split()[-1]
                    if "reviews" in aria_label else "0"
                )

                # Convert reviews to integer
                reviews = convert_reviews(reviews_text)

                # Click product to open the detail panel
                product.click()

                # Wait a second for the link to be visible
                time.sleep(1)

                try:
                    # Try to find the link
                    link_element = driver.find_element(By.CSS_SELECTOR, "a.uchJRc")
                    product_link = link_element.get_attribute("href")
                except:
                    product_link = "NA"  # If no link is found, set as "NA"

                # Append product details along with the extracted link
                product_list.append({
                    'title': title,
                    'price': float(price) if price else float('inf'),
                    'condition': condition,
                    'rating': rating,
                    'reviews': reviews,
                    'link': product_link
                })

                # Output progress for debugging
                print(f"Processed Product: {title}")

            # Wait a second to ensure all elements are fully loaded before clicking the next product
            time.sleep(1)

        except Exception as e:
            print(f"Error processing product: {e}")

    # Sort a copy of the product list by price (ascending), condition, and rating
    #Chat gpt helped me better understand this key and how it worked
    sorted_product_list = sorted(
        product_list,
        key=lambda x: (x['price'], x['condition'] == "Refurbished", -x['rating'])
    )

    # Output the sorted results
    if sorted_product_list:
        print("\nTop Deals (Sorted by Price, Condition, and Rating):\n")
        for idx, detail in enumerate(sorted_product_list, 1):
            print(f"Product {idx}:")
            print(f"  Title: {detail['title']}")
            print(f"  Price: ${detail['price']:.2f}")
            print(f"  Condition: {detail['condition']}")
            print(f"  Rating: {detail['rating']}")
            print(f"  Reviews: {detail['reviews']}")
            print(f"  Link: {detail['link']}\n")
    else:
        print("No products found or extracted.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
