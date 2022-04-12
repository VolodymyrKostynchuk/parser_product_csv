from bs4 import BeautifulSoup

import csv 
import requests


def get_src_site():
	url = 'https://www.sochetaizer.ru/goods/caloricity?page=55'
	headers = {
		'accept': '*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
	}
	req = requests.get(url, headers=headers)
	src = req.text 
	return src 


def create_html():
	src = get_src_site()
	with open('data\\index.html', mode='w', encoding='utf-8') as f:
		f.write(src) 


def get_html_text():
	with open('data\\index.html', encoding='utf-8') as f:
		src = f.read()
		return src 


def main():
	create_html()
	print('[+] HTML created')
	src = get_html_text()

	soup = BeautifulSoup(src, 'lxml')
	product_info = soup.find('div', class_='goods-table common-list').find_all('div', 'goods-table-row')
	data = []
	for item in product_info:
		element = item.find_all('div', class_='goods-table-cell')
		name = element[0].text
		calories = element[1].text
		proteins = element[2].text
		fat = element[3].text
		carbohydrates = element[4].text

		with open('data\\data.csv', mode='a', newline='', encoding='cp1251') as f:
			writer = csv.writer(f, delimiter=';')
			writer.writerow((
				name,
				calories,
				proteins,
				fat,
				carbohydrates
			))


if __name__ == '__main__':
	main()