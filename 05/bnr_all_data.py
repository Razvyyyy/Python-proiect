from selemium import webdriver
from selenium.webdriver.chrome.service import Service
from wedriver_manager.chrome import ChromeDriverManager


option = webdriver.ChromeOptions()
option.add_argument('start-maimized')
drver = webdriver.Chrome(service=Service(ChromeDriverManager().install))
drver.get('https://www.bnr.ro/files/xml/nbrfxrates2022.htm')
table = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
lista = table.text.split('\n')
print(lista)