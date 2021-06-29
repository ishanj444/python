from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PATH = "F:\py\selenium practice\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://www.flipkart.com/")

try:
	driver.find_element_by_xpath("//button[contains(text(),'✕')]").click()
except:
	pass
sleep(3)
driver.find_element(By.XPATH,"//body/div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Samsung Galaxy S10")
driver.find_element_by_tag_name("button").click()
sleep(1)
driver.find_element(By.XPATH,"//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[3]/div[1]/a[1]").click()
sleep(1)
driver.find_element(By.XPATH,"//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/section[3]/label[1]/div[2]/div[1]/img[1]").click();
sleep(1)
driver.find_element(By.XPATH,"//div[contains(text(),'Price -- High to Low')]").click()
sleep(1)
names = driver.find_elements(By.XPATH,"//div[contains(@class,'_4rR01T')]")
prices = driver.find_elements(By.XPATH,"//div[contains(@class,'_30jeq3 _1_WHN1')]")
links = driver.find_elements(By.XPATH,"//a[@class='_1fQZEK']")
#print(links.text)
sleep(3)
#links = [elem.get_attribute('href') for elem in elems]


for name in names:
	print(name.text)

for price in prices:
	print(price.text)	

for link in links:
	print(link.get_attribute("href"))