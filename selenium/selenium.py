from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

import time

PATH = "F:\py\selenium practice\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

#search = driver.find_element_by_id("twotabsearchtextbox")
#search.send_keys("phones")
#search.send_keys(Keys.RETURN)

driver.find_element(By.XPATH,"//input[contains(@id,'twotabsearchtextbox')]").send_keys("iphone")
driver.find_element(By.XPATH,"//input[@value='Go']").click()
driver.find_element(By.XPATH,"//span[text()='Apple']").click()
phonenames = driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
prices = driver.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")
#ratings = driver.find_elements(By.XPATH,"//i[contains(@class,'a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom')]")
#del ratings[-4:]

phlist = []
prlist = []


for phone in phonenames:
	#print(phone.text)
	phlist.append(phone.text)

for price in prices:
	#print(price.text)	
	prlist.append(price.text)
#print("_________-")
#for rate in ratings:
#	print(rate.text)

finallist = zip(phlist,prlist)
for i in finallist:
	print(i)

wb = Workbook()
m1 = wb.active

for j in finallist:
	m1.append(j)

wb.save("Final.xlsx")
print("done")