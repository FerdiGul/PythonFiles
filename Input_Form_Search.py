#Ferdi Gül
#Python 
#Tested in Kali Linux 2017

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.google.com.tr')
elem = browser.find_element_by_name("q") # q is the form name of google seek bar 
elem.send_keys("Frdi_Gul Twitter")
elem.send_keys(Keys.RETURN)
#browser.close()
