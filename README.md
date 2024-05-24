# AutoInsta

## Description
AutoInstaExcel is a Python-based automation project that uses Selenium to automate the process of logging into Instagram, fetching the list of followers for specified accounts, and storing this data in an Excel file. This project is intended for study purposes only.

## Features
- Automated login to Instagram using provided credentials.
- Fetches the list of followers for specified Instagram accounts.
- Stores the follower data in an Excel file for easy access and analysis.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Selenium
- pandas (for handling Excel files)
- OpenPyXL (for working with Excel files in pandas)
- ChromeDriver (compatible with your version of Chrome)

## Installation
1. **Clone the Repository**
    ```sh
    git clone https://github.com/Manish-Kumarrrr/AutoInsta.git
    ```
    or
    Download the repository as a ZIP file and extract it: If you prefer, you can download the repository as a ZIP file and extract it to your local machine.
  
2. **Install Required Packages**
    ```sh
    pip install pandas selenium openpyxl
    ```

3. **Download ChromeDriver**
    Download the version of ChromeDriver that matches your version of Google Chrome from the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads). Ensure that the downloaded `chromedriver` executable is placed in a directory that's in your system's PATH.

## Usage
1. **Update the Script with Your Credentials and Target Usernames**

    Open the `auto_insta_excel.py` file and replace the following placeholders:
    ```python
    USERNAME = 'your_username'
    PASSWORD = 'your_password'
    TARGET_USERNAMES = ['target_username1', 'target_username2']
    chrome_driver_path = "./chromedriver.exe"
    ```

2. **Run the Script**
    Execute the script in your Python environment:
    ```sh
    pip install papermill
    papermill AutoInsta.ipynb executed_notebook.ipynb
    ```

## Script Explanation
The script performs the following steps:
1. Sets up the Selenium WebDriver using ChromeDriver.
2. Navigates to the Instagram login page and logs in using the provided credentials.
3. Navigates to each target username's profile and scrapes the followers list.
4. Saves the collected followers' usernames to both CSV and Excel files.

## Sample Output
- `username.csv`: Contains the list of followers in CSV format.
- `result.xlsx`: Contains the list of followers in Excel format.

## Troubleshooting

### Common Issues

1. **ChromeDriver Version Mismatch**
    - Ensure that the version of ChromeDriver you downloaded matches your installed version of Google Chrome. Check your Chrome version by navigating to `chrome://settings/help` in your Chrome browser.

2. **Element Not Found**
    - If the script cannot find certain elements, Instagram might have changed their webpage structure. Verify and update the CSS selectors in the script accordingly.

3. **Login Issues**
    - Make sure your Instagram credentials are correct.
    - If Instagram detects unusual login activity, it might prompt for additional verification. Manually log in through a browser to resolve any such issues before running the script again.

4. **Rate Limiting**
    - Instagram has rate limits to prevent abuse. If the script runs too quickly, it might get temporarily blocked. Adding random delays and avoiding frequent runs can help mitigate this.

### Debugging Steps

1. **Enable Browser Logging**
    - Uncomment the following line in your script to see detailed logs from the browser:
    ```python
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')  # Adjust log level as needed
    driver = webdriver.Chrome(service=chrome_service, options=options)
    ```

2. **Take Screenshots**
    - Add a screenshot command to capture the browser state when an error occurs:
    ```python
    driver.save_screenshot('screenshot.png')
    ```

3. **Print HTML Source**
    - Print the HTML source of the page to understand the current state of the DOM:
    ```python
    print(driver.page_source)
    ```

## Important Considerations
- **Use Responsibly**: Automating interactions with websites, especially social media platforms, should be done responsibly and within the terms of service of the website.
- **Rate Limits**: Be mindful of rate limits and avoid sending too many requests in a short period, which might get your account temporarily or permanently banned.
- **Privacy**: Ensure that you’re not violating any privacy norms or regulations while using or sharing the collected data.

## License
This project is for educational purposes only. Ensure you comply with Instagram's terms of service and privacy policies while using this script.

---
