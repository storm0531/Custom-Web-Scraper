import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

page_url = "https://example"
extract_attribute = "class"
webdriver_path = "c:/user/.../geckodriver.exe"

tag_name = "div"
id_to_find = "siteSub"
class_to_find = "title"
# name_to_find = "username"


#scrapping with beautiful soup
response = requests.get(page_url)
page_text = response.text
soup = BeautifulSoup(page_text,"html.parser")
# print(soup)

tags = soup.find(name=tag_name,class_=class_to_find,id=id_to_find)
print(tags.get(extract_attribute))

# selected = soup.select_one(selector=f"{tag_name} .{class_to_find} #{id_to_find}")
# print(selected.get(extract_attribute))

#<--------------------------  scrapping with selenuim web boot  -------------------------------------->
#constants for selenium

driver = webdriver.Firefox(executable_path=webdriver_path)
driver.get(page_url)

# finder_tag = driver.find_element(By.TAG_NAME,tag_name)
finder_id = driver.find_element(By.ID,id_to_find)
# finder_class = driver.find_element(By.CLASS_NAME,class_to_find)
# finder_name = driver.find_element(By.NAME,id_to_find)

# print( finder_tag.get_attribute(extract_attribute) )
print( finder_id.get_attribute(extract_attribute) )
# print( finder_class.get_attribute(extract_attribute) )
# print( finder_name.get_attribute(extract_attribute) )

#for beautiful to scrap
# content = driver.page_source
# soup = BeautifulSoup(content,"html.parser")

driver.quit()
