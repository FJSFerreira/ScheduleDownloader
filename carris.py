import requests

from bs4 import BeautifulSoup

URL = 'https://carris.pt'
page = requests.get(URL + '/viaje/carreiras')
soup = BeautifulSoup(page.content, 'html.parser')

lines = soup.find_all(class_='results-container')

i = 1

for line in lines:
	line_page = requests.get(URL + line['href'])
	line_soup = BeautifulSoup(line_page.content, 'html.parser')
	
	pdf_url = URL + line_soup.find(class_='icons-detail-route').find('a')['href']
	
	pdf_file = requests.get(pdf_url)
	
	f = open(f'{i:03}.pdf', 'wb')
	f.write(pdf_file.content)
	i += 1