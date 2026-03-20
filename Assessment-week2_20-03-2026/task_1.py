from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


# Open Amazon
# Verify page title and current URL
# Locate the category dropdown (next to search bar)
# Select "Books" using Select class
# Enter "Harry Potter" in search and press Enter
# Use explicit wait to wait until results are visible
# Get all product titles using find_elements
# Print first 5 product names
# Click on the first product


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

wait = WebDriverWait(driver, 15)

driver.get("https://www.amazon.in")
driver.maximize_window()

print("Title:", driver.title)
print("URL:", driver.current_url)

dropdown = wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
sleep(2)
select = Select(dropdown)
select.select_by_visible_text("Books")
sleep(2)
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
sleep(2)
search_box.send_keys("Harry Potter")
search_box.send_keys(Keys.ENTER)
sleep(2)
products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']//h2//span")))

print("\nFirst 5 Products:")
for i in products[:5]:
    print(i.text)

products[0].click()

driver.quit()



