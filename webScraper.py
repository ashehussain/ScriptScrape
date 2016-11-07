from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from logger import logger
class webScraper(object):

    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chromeOptions.add_experimental_option("prefs", prefs)
        try:
            driver = webdriver.Chrome(executable_path=r"/Users/asheikhussain/Documents/chromedriver", chrome_options=chromeOptions)
        except exceptions.WebDriverException:


    def navigateToSite(self, website):
        driver.get("http://www.facebook.com")

    ##GET THE EMAIL ADDRESS
    email_input = driver.find_element_by_id("email")
    your_email = raw_input("Please enter your facebook email :")
    email_input.send_keys(your_email)

    ##GET THE PASSWORD
    password_input = driver.find_element_by_id("pass")
    your_password = raw_input("Please enter your facebook password :")
    password_input.send_keys(your_password)

    # LOGIN
    driver.find_element_by_id("loginbutton").click()

    # navigate to the humans of new york album page
    driver.get("http://www.facebook.com/pg/humansofnewyork/photos/?tab=album&album_id=102107073196735")

    # pull all the elements with the anchor tag
    elems = driver.find_elements_by_xpath("//a[@href]")

    for element in elems:
        link_val = element.get_attribute("href")
    if ("humansofnewyork/photos/a." in link_val):
        element.click()
    caption = driver.find_element_by_class_name("hasCaption")
    print caption.text
    caption.send_keys(Keys.ESCAPE)

    driver.close()

