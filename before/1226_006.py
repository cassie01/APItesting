from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://baidu.com')#获取并打开网页
print(driver.title)#打印title
# assert 'goo' in driver.title
driver.find_element_by_id('kw').send_keys('仓鼠')
driver.find_element_by_id('su').click()#点击搜索，记得加括号

time.sleep(2)
result = driver.find_element_by_id('content_left').text####打印出搜索到的内容
print(result)

assert '仓鼠' in result