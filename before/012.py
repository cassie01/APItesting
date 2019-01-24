from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://search.jd.com/Search?keyword=shouj&enc=utf-8&wq=shouj&pvid=ab2aab857b5d422d911c85df91aca3a0")
eles = driver.find_elements_by_css_selector("li.gl-item div.p-price")
# print(len(eles))

for i in range(len(eles)):
    print(eles[i].text)