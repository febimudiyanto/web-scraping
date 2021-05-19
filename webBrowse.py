from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')



# single input
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('hello')
showMessageButton =  driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

# two input

field1 = driver.find_element_by_xpath('//*[@id="sum1"]')
field1.send_keys('3')

field2 = driver.find_element_by_xpath('//*[@id="sum2"]')
field2.send_keys('7')

submitAdd  = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
submitAdd.click()