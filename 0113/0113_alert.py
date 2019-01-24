from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get('http://39.107.96.138:3000/signin')


driver.find_element_by_id('name').send_keys('user1')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_class_name('span-primary').click()
driver.find_element_by_xpath('//*[@id="topic_list"]/div[2]/div/a').click()
driver.find_element_by_css_selector('#manage_topic > a.delete_topic_btn > i').click()#元素定位不准确，稍后再看
print(Alert(driver).text)
Alert(driver).accept()