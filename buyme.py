import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome(executable_path="c:\\data\\webdriver\\chromedriver.exe")
chrome_driver.implicitly_wait(10)
chrome_driver.get("https://buyme.co.il")
chrome_driver.maximize_window()

# Find the enter / registration button and click on it.
chrome_driver.execute_script("arguments[0].click();",chrome_driver.find_element_by_xpath('//header[@class="m-page-header"]//span[2]'))
# chrome_driver.execute_script("arguments[0].click();",chrome_driver.find_element_by_xpath('//*[@id="ember591"]/div/ul[1]/li[3]'))

# click on registration button
chrome_driver.execute_script("arguments[0].click();",chrome_driver.find_element_by_xpath('//span[@class="text-btn"]'))


chrome_driver.find_element_by_xpath('//*[@id="ember1041"]').send_keys("Aaaaaa Bbbbb")
chrome_driver.find_element_by_xpath('//*[@id="ember1043"]').send_keys("aaa152@bbb.com")
chrome_driver.find_element_by_xpath('//*[@id="valPass"]').send_keys("Aaaa1234")
chrome_driver.find_element_by_xpath('//*[@id="ember1047"]').send_keys("Aaaa1234")

# Agree to the term and condition
chrome_driver.execute_script("arguments[0].click();",chrome_driver.find_element_by_xpath('//*[@id="ember1048-id"]'))

# Don't want to received updates
chrome_driver.execute_script("arguments[0].click();",chrome_driver.find_element_by_xpath('//*[@id="ember1050-id"]'))

# registration button

chrome_driver.execute_script("arguments[0].click();",chrome_driver.find_element_by_xpath('//button[@class="ui-btn orange large"]'))
# time.sleep(2)
# #
# # choose the cost range of the gift
# chrome_driver.find_element_by_xpath('//*[@id="ember664_chosen"]').click()
# chrome_driver.find_element_by_xpath('//*[@id="ember664_chosen"]/div/ul/li[4]').click()
#
# # choose the area of the gift
# chrome_driver.find_element_by_xpath('//*[@id="ember679_chosen"]').click()
# chrome_driver.find_element_by_xpath('//*[@id="ember679_chosen"]/div/ul/li[2]').click()
# # Wait for the page load will end.
#
# # choose the type of the gift
# chrome_driver.find_element_by_xpath('//*[@id="ember689_chosen"]').click()
# chrome_driver.find_element_by_xpath('//*[@id="ember689_chosen"]/div/ul/li[3]').click()
#
# # click on "find me a gift"
# chrome_driver.find_element_by_xpath('//*[@id="ember724"]').click()
#
# # choose the specific gift.
# chrome_driver.find_element_by_xpath('//*[@id="ember1180"]/div/div[2]').click()
#
# # enter the cost that i want to update on the gift and accept the order.
# chrome_driver.find_element_by_xpath('//*[@id="ember1246"]').send_keys("300")
# chrome_driver.find_element_by_xpath('//*[@id="ember1245"]/div[2]/div/button').click()
#
#
# # Enter the name of the person that should receive the gift
# chrome_driver.find_element_by_xpath('//*[@id="ember1324"]').send_keys("Moshe Moshe")
# # Enter the name of the person that send the gift
# chrome_driver.find_element_by_xpath('//*[@id="ember1326"]').send_keys("David David")
#
# # choose the type of the event.
# chrome_driver.find_element_by_xpath('//*[@id="ember1328_chosen"]/a').click()
# chrome_driver.find_element_by_xpath('//*[@id="ember1328_chosen"]/div/ul/li[3]').click()
#
# # update the bless. first clear the exit text before.
# chrome_driver.find_element_by_xpath('//*[@id="ember1350"]/textarea').clear()
# chrome_driver.find_element_by_xpath('//*[@id="ember1350"]/textarea').send_keys("sdsdsdsd sdsds dsdsds")
#
# # upload image from c:\
# chrome_driver.find_element_by_xpath('//*[@id="ember1359"]').send_keys('C:/data/tulip.jpg')
#
#
# # update the email that I want to send the gift
# chrome_driver.find_element_by_xpath('//*[@id="ember1291"]/div[4]/div/div[1]/div[2]/div/button/span').click()
# chrome_driver.find_element_by_xpath('//*[@id="ember1797"]').send_keys('adael.cohen@gmail.com')
# chrome_driver.find_element_by_xpath('//*[@id="ember1799"]/div[4]/div/div[3]/div/div[2]/button[2]').click()
