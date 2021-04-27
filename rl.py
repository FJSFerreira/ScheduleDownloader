import requests

from bs4 import BeautifulSoup

URL = 'https://rodoviariadelisboa.pt/'
page = requests.get(URL + 'horarios')
soup = BeautifulSoup(page.content, 'html.parser')

lines = soup.find_all(class_='trajecto')

i = 1

for line in lines:
	line_page = requests.get(URL + 'horarios' + line['href'])
	line_soup = BeautifulSoup(line_page.content, 'html.parser')
	
	files = line_soup.find_all(class_='verHorarios')
	
	for file in files:
		png_page = requests.get(URL + file['href'])
		png_soup = BeautifulSoup(png_page.content, 'html.parser')
		png_url = png_soup.find('img')['src'].replace('&w=960&f=png', '')
		png_file = requests.get(URL + png_url)
		
		f = open(f'{i:03}.png', 'wb')
		f.write(png_file.content)
		i += 1