from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Replace 'Your_Username' and 'Your_Password' with your Instagram credentials
USERNAME = 'Your_Username'
PASSWORD = 'Your_Password'
# Replace 'target_username' with the username of the profile you want to scrape
TARGET_USERNAME = 'target_username'

# Set up the webdriver (choose the appropriate driver for your browser)
chrome_driver_path="C:\\Users\\manis\\OneDrive\\Desktop\\Randhir\\chromedriver.exe"


# Set up the Chrome service with the executable path
chrome_service = Service(executable_path=chrome_driver_path)

# Set up the webdriver using the specified service
driver = webdriver.Chrome(service=chrome_service)
# Make sure you have Chrome WebDriver installed and in your PATH

# Navigate to the Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Wait for the login page to load
time.sleep(12)

# Locate the username and password fields, and login button
username_field = driver.find_element_by_name('username')
password_field = driver.find_element_by_name('password')
login_button = driver.find_element_by_xpath("//button[@type='submit']")

# Input your credentials and login
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
login_button.click()

# Wait for the logged-in page to load
time.sleep(5)

# Navigate to the target profile page
driver.get(f'https://www.instagram.com/{TARGET_USERNAME}/')

# Wait for the profile page to load
time.sleep(2)

# Scroll to load more posts (you can adjust the number of scrolls as per your requirement)
num_scrolls = 3
for _ in range(num_scrolls):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

# Find and scrape the titles of the top posts
post_titles = []
posts = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']//a")
for post in posts:
    post_titles.append(post.get_attribute("title"))

# Print the scraped titles
for idx, title in enumerate(post_titles, 1):
    print(f"{idx}. {title}")

# Close the browser window
driver.quit()
