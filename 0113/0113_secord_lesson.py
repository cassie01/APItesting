from selenium import webdriver
import requests
import time
driver = webdriver.Chrome()
# driver.get('http://www.shgjj.com/')

# image = driver.find_element_by_id('img1')
# image.screenshot_as_png('./1.png')

# requests


#############百度上传图片
#################快捷键
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# driver.get('https://www.baidu.com/')

# driver.find_element_by_id('kw').send_keys('hahahah')
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# time.sleep(3)
# ActionChains(driver).key_down(Keys.BACKSPACE).perform()
# time.sleep(3)

# driver.quit()
#############滑动   boss直聘
driver.get('https://login.zhipin.com/')
aa = driver.find_element_by_css_selector('form>div:nth-child(4) >div.nc_wrapper>div>span')
ActionChains(driver).move_to_drag_and_drop(324,0)
################iframe
# driver.get('https://login.anjuke.com/login/form?history=aHR0cHM6Ly9zaGFuZ2hhaS5hbmp1a2UuY29tLz9waT1QWi1iYWlkdS1wYy1hbGwtYmlhb3Rp')
# driver.switch_to_frame('iframeLoginIfm')
# driver.find_element_by_id('phoneIpt').send_keys('11122')
# driver.find_element_by_id('smsIpt').send_keys('333')

