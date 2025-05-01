# WP PLugin Issue Tracker

This project includes two components:
1. A **Streamlit dashboard** for visualizing and categorizing support issues.
2. A **data scraping script** (`data.py`) to scrape support threads from the Tutor plugin support page and save them into a CSV file for analysis.

## Features

### Support Dashboard (Streamlit)
- **Issue Categorization**: Visualize the distribution of support issues in various categories such as Course Issues, Checkout Problems, and more.
- **Filter by Category**: Select a category from the dropdown to view threads related to that category.
- **Pagination**: View support threads with pagination, allowing you to browse through multiple pages of threads efficiently.
- **Interactive Bar and Pie Charts**: The dashboard includes interactive charts to visualize support issue distribution across different categories.

### Data Scraping Script (`data.py`)
- **Web Scraping**: Scrapes support threads from the Tutor plugin support page on WordPress.
- **Pagination**: Handles scraping multiple pages automatically.
- **CSV Export**: Saves the scraped data (thread titles) into a CSV file (`tutor_plugin_support_data.csv`) for analysis and visualization.

## Requirements

To run this application, you'll need to install the following Python libraries:

- `pandas`: For handling the CSV data.
- `plotly`: For creating interactive visualizations.
- `streamlit`: For building the interactive web application.
- `requests`: For making HTTP requests to scrape the data.
- `beautifulsoup4`: For parsing and extracting data from HTML pages.

You can install these dependencies using `pip`:

```bash
pip install pandas plotly streamlit requests beautifulsoup4
