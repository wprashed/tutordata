# WP Plugin Issues Tracker

This project allows you to scrape data from the WordPress support forum for specific plugins, categorize the issues, and visualize the categorized data in an interactive web interface using Streamlit and Plotly.

Live Demo: https://wppluginissuetracker.streamlit.app/

## Requirements

- Python 3.x
- `requests`
- `BeautifulSoup4`
- `csv`
- `pandas`
- `plotly`
- `streamlit`

You can install the necessary packages by running the following command:

```bash
pip install requests beautifulsoup4 pandas plotly streamlit
```

## Scraping Plugin Data

### `data.py`

This script is responsible for scraping the support page for a specific plugin from WordPress.org. It extracts thread titles related to the plugin and saves them in a CSV file. 

### Steps to scrape data for a specific plugin:

1. **Find the Plugin's Support URL**:  
   Navigate to the WordPress support page for the plugin you want to scrape. For example, the Akismet plugin's support URL might look like this: `https://wordpress.org/support/plugin/akismet/`. The URL structure typically includes the plugin name followed by the `/support/plugin/` path.

2. **Modify the Start URL in the Script**:  
   Open `data.py` and modify the `start_url` variable to point to the support page for your desired plugin. For example, if you want to scrape data for the `akismet` plugin, change the `start_url` to:
   
   ```python
   start_url = 'https://wordpress.org/support/plugin/akismet/page/1/'
   ```

   Note: You can change the page number (`page/1`, `page/2`, etc.) to scrape multiple pages.

3. **Run the Scraping Script**:  
   Once the URL is set, run the script by executing the following command in your terminal:

   ```bash
   python data.py
   ```

4. **CSV Output**:  
   The script will scrape the plugin support forum and store the thread titles in a CSV file (`plugin_support_data.csv`). Each thread title is saved in the CSV for further processing and categorization.

#### Key Features of `data.py`:
- **Pagination**: Automatically handles pagination and scrapes multiple pages of the plugin support forum.
- **CSV Output**: Data is stored in a CSV file (`plugin_support_data.csv`) with each thread title.
- **Resumes Scraping**: If the script is run again, it will append the new data to the existing CSV without overwriting previous entries.

---

## Visualizing the Data

### `app.py`

This Streamlit app allows you to visualize the scraped data and categorize the issues based on keywords.

### Key Features of `app.py`:
- **Bar Chart**: Visualizes the number of issues per category.
- **Pie Chart**: Displays the distribution of issues across different categories.
- **Category Filtering**: Users can filter threads by category using a dropdown menu.
- **Pagination**: Displays the threads in a paginated format (10 threads per page).
- **Dynamic Interaction**: The app updates dynamically when selecting different categories or navigating between pages.

### Steps to run the visualization app:

1. Ensure that you have the `plugin_support_data.csv` file from running `data.py`.
2. Run the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

3. The app will launch in your default web browser, displaying the interactive charts and the filtered thread data.

---

## Creating Issue Categories

The script in `app.py` uses a predefined list of categories based on specific keywords in thread titles. You can modify the categories and keywords to tailor them to your needs.

### Default Categories:

- **Akismet Issues**: Keywords related to spam, comments, CAPTCHA, etc.
- **PHP/Version Compatibility**: Keywords related to PHP, version issues, etc.
- **Plugin Compatibility**: Keywords related to plugin and theme conflicts.
- **Spam Detection & Filtering**: Keywords related to spam detection and filtering issues.
- **User Access & Registration**: Keywords related to user registration, login, etc.
- **Error Handling & Debugging**: Keywords related to errors, warnings, debugging issues.
- **API & Server Issues**: Keywords related to API and server issues.
- **Performance & Speed**: Keywords related to site performance and speed.
- **Translation & Localization**: Keywords related to translation and language.
- **Feature Requests & Suggestions**: Keywords related to feature requests and suggestions.
- **Security & Protection**: Keywords related to security issues and vulnerabilities.
- **Others**: For any thread that does not fit into the above categories.

### Modify or Add Custom Categories:

To modify or add new categories based on your data:
1. **Open `app.py`** and locate the `categories` dictionary. This contains the keyword-to-category mappings.
2. **Add a New Category**: To add a new category, simply add a new entry in the dictionary with a name and a list of relevant keywords. For example:

   ```python
   "Custom Category": ["custom", "example", "new", "feature"]
   ```

3. **Re-run the Streamlit app**: Once you’ve added or modified categories, re-run the Streamlit app to see the updated categorization.

---

## Example Output

When you run the `app.py` Streamlit app, you will see:
- A bar chart showing the number of issues per category.
- A pie chart displaying the distribution of issues.
- A list of threads for the selected category, with pagination controls to navigate through the data.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to fork this repository, open issues, or submit pull requests for improvements or bug fixes.
