import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager


search_term = input("Enter term: ")



chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('headless');


os.mkdir(f'../Themes/{search_term}')

prefs = {"download.default_directory" : f'../Themes/{search_term}'}
chromeOptions.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(executable_path='chromedriver',chrome_options=chromeOptions)
driver = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)




url = f'https://www.cleanpng.com/free/{search_term}.html'



response = requests.get(url)


soup = BeautifulSoup(response.text, 'lxml')
links = soup.find_all('a')[21:41:2]


links = [str(l).split('href="')[1].split('"')[0] for l in links]
links = [f'https://www.cleanpng.com{l}download-png.html' for l in links]


for i, link in enumerate(links):
	driver.get(link)
	time.sleep(2)





while len(os.listdir(f'../Themes/{search_term}')) < 10 or any(  filename.endswith('.crdownload') for filename in os.listdir(f'../Themes/{search_term}')):
       print(len(os.listdir(f'../Themes/{search_term}')))


for i, filename in enumerate(os.listdir(f'../Themes/{search_term}')):
	os.rename(f'../Themes/{search_term}/{filename}', f'../Themes/{search_term}/{i}.png')



# html_file = open(f'./audioCapture.html', 'r')


# html_file = open(f'./audioCapture.html', 'r')
# list_of_lines = html_file.readlines()
# list_of_lines[53] =  f'\t\tvar folder = "../Themes/{search_term}";\n';
# html_file = open(f'./audioCapture.html', "w")
# html_file.writelines(list_of_lines)
# html_file.close()
