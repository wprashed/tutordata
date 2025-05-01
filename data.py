import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import os


def get_page_data(url, writer):
    # Send the HTTP request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the relevant thread elements
    print(f"Scraping page: {url}")

    # Find all <li> elements with class 'bbp-topic-title'
    threads = soup.find_all('li', class_='bbp-topic-title')  # Threads are in <li class='bbp-topic-title'>
    if not threads:
        print("No threads found, check the page structure.")

    # Loop through each thread to extract the title
    for thread in threads:
        title_tag = thread.find('a', class_='bbp-topic-permalink')  # Find the <a> tag with the topic link
        if title_tag:
            title = title_tag.text.strip()  # Get the thread title
            print(f"Thread Title: {title}")  # Debug print to check the data
            writer.writerow([title])  # Write the thread title to the CSV

    # Look for the next page link (pagination)
    next_page = soup.find('a', class_='next page-numbers')  # Look for the 'next' link
    if next_page:
        next_url = urljoin(url, next_page['href'])  # Build the absolute URL for the next page
        return next_url  # Return the next page URL
    return None  # No next page found


def scrape_all_pages(start_url, csv_filename):
    # Check if the file exists to avoid overwriting, and if it exists, open it in read mode
    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # If file doesn't exist, write the header
        if not file_exists:
            writer.writerow(['Thread Title'])

        url = start_url
        while url:
            url = get_page_data(url, writer)  # Scrape current page and get the next page URL
            if not url:
                break  # If no next page is found, stop scraping


# Starting URL (the first page of the plugin support page)
start_url = 'https://wordpress.org/support/plugin/akismet/page/29/'
csv_filename = 'plugin_support_data.csv'

scrape_all_pages(start_url, csv_filename)