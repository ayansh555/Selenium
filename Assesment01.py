import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)

# # ques 1
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
#
# driver.find_element('xpath', '(//a[contains(text(),"Books")])[1]').click()
# time.sleep(1)
#
# driver.find_element('xpath', '(//input[@value="Add to cart"])[1]').click()
# time.sleep(1)
#
# driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
# time.sleep(1)
#
# product = driver.find_element('xpath', '//a[@class="product-name"]')
#
# if product.is_displayed():
#     print("Product is present in the cart")
# else:
#     print("Product is not present in the cart")

##Question-02
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(1)
# driver.find_element('xpath', "//a[contains(text(),'Electronics')]").click()
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Cell phones')])[4]").click()

##Question-03

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# waitObj = WebDriverWait(driver, 20)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(1)
#
# driver.find_element('xpath', '//button[text()="Start"]').click()
#
# waitObj.until(EC.visibility_of_element_located(('xpath', '//h4[text()="Hello World!"]')))
#
# text = driver.find_element('xpath', '//h4[text()="Hello World!"]').text
# print(text)

##Question-4

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# wait = WebDriverWait(driver, 10)
# time.sleep(2)
# remove_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', "//button[text()='Remove']"))
# )
# remove_btn.click()
# add_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', "//button[text()='Add']"))
# )
# add_btn.click()

# ##Question-05

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver.get("https://demoqa.com/select-menu")
# driver.maximize_window()
# wait = WebDriverWait(driver,10)
#
# dropdown = wait.until(EC.element_to_be_clickable(("id","withOptGroup")))
# dropdown.click()
#
# option = wait.until(EC.element_to_be_clickable(("xpath","//div[text()='Group 2, option 1']")))
# option.click()
#
# selected_value = driver.find_element("xpath","//div[contains(@class,'singleValue')]").text
#
# print("Selected Value:", selected_value)
#
# if selected_value == "Group 2, option 1":
#     print("Verification Passed")
# else:
#     print("Verification Failed")

##Question-06
# from selenium.webdriver.support.ui import Select
# driver.get("https://demoqa.com/select-menu")
# time.sleep(1)
# dropdown = Select(driver.find_element('id', "cars"))
# dropdown.select_by_visible_text("Volvo")
# dropdown.select_by_visible_text("Saab")
# dropdown.select_by_visible_text("Opel")
#
# for option in dropdown.all_selected_options:
#     print(option.text)

##Question-07

# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://demoqa.com/menu/")
# time.sleep(1)
# actions = ActionChains(driver)
# main_item2 = driver.find_element('xpath', "//a[text()='Main Item 2']")
# actions.move_to_element(main_item2).perform()
#
# sub_sub_list = driver.find_element('xpath', "//a[text()='SUB SUB LIST »']")
# actions.move_to_element(sub_sub_list).perform()
#
# sub_sub_item1 = driver.find_element('xpath', "//a[text()='Sub Sub Item 1']")
# sub_sub_item1.click()


##Question-08

# from selenium.webdriver.common.action_chains import ActionChains
#
# ac = ActionChains(driver)
#
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# time.sleep(2)
#
# source = driver.find_element("xpath",'//div[@id="draggable"]')
# target = driver.find_element("xpath","//div[@id='droppable']")
#
# ac.drag_and_drop(source,target).perform()
# time.sleep(2)
#
# text = driver.find_element("xpath","//div[@id='droppable']/p").text
# print(text)
#
# time.sleep(1)
# driver.close()

##Question-9

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element('xpath', "//button[text()='Click for JS Confirm']").click()
# time.sleep(1)
# alert = driver.switch_to.alert
# alert.accept()
# result = driver.find_element('id', "result").text
# print(result)
# result == "You clicked: Ok":
#     print("Verification Passed")
# else:
#     print("Verification Failed")

##Question-10
# driver.get("https://the-internet.herokuapp.com/upload")
# path = r'C:\Users\KIIT\PycharmProjects\selenium_training\files\Book1.xlsx'
# time.sleep(1)
# driver.find_element('id', "file-upload").send_keys(path)
# time.sleep(1)
# driver.find_element('id', "file-submit").click()
# time.sleep(1)
# driver.find_element('id', "file-submit").click()
# uploadedFile = driver.find_element("id","uploaded-files").text
# print(uploadedFile)



