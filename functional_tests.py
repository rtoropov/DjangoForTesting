from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Roma\chromedriver\chromedriver.exe')
driver.get("http://localhost:8000")
print(driver.title)
assert 'Django' in driver.title


driver.quit()
