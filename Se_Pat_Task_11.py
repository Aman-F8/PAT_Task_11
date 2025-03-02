from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure you have the chromedriver installed
driver.get("https://jqueryui.com/droppable/")  # Replace with the actual webpage URL

# Maximize window
driver.maximize_window()

# Switch to the iframe containing the drag-and-drop elements
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,"demo-frame"))

# Locate the source (drag box) and target (drop box)
source_element = driver.find_element(By.ID, "draggable")  # give drag box ID (Find the draggable element by its ID)
target_element = driver.find_element(By.ID, "droppable")  # give drop box ID (Find the droppable element by its ID)

# Perform drag and drop action
actions = ActionChains(driver) #Create an ActionChains object to perform complex actions
actions.drag_and_drop(source_element, target_element).perform() # Drag the source element and drop it onto the target element

time.sleep(3)
driver.switch_to.default_content()
# Close the browser
driver.quit()