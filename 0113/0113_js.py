from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.ctrip.com/')
start_date = '2019-01-20'

js_script ='document.querySelector("#HD_CheckIn").value = "{}"'.format(start_date)

print(js_script)
driver.execute_script(js_script)