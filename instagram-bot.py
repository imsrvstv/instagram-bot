un = 'your username'
pw = 'your password'

link = 'https://instagram.com/'

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('./ChromeDriver/chromedriver.exe')
browser.get(link)

browser.implicitly_wait(20)

username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')

username.send_keys(un)
password.send_keys(pw)

password.send_keys(Keys.ENTER)

time.sleep(5)
browser.get(link+un)

elem = browser.find_element_by_partial_link_text('following')
elem.click()

n = int(input('Enter Number of Peoples To Unfollow: '))
while(n != 0):
	browser.find_element_by_xpath("//button[text()='Following']").click() 
	time.sleep(0.5)
	browser.find_element_by_xpath("//button[text()='Unfollow']").click()
	time.sleep(0.5)
	n -= 1