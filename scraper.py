from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('')

time.sleep(5)

username = browser.find_element("id","username")
username.send_keys("")
password = browser.find_element("id","password")
password.send_keys("")
time.sleep(5)
browser.find_element("xpath","//button[contains(., 'Вход')]").click()
time.sleep(5)

html = browser.page_source
browser.quit()

soup = BeautifulSoup(html, 'html.parser')
homeworks = soup.find_all('div', class_='homework-item')
text='Срок'

for i in homeworks:
    hw = homeworks.find('td', class_='title').find('span', class_='titleline').find('a')

