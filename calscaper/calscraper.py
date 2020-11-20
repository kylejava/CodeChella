import requests
from bs4 import BeautifulSoup

# Returns a list of urls formatted as a string
# page_num : INT -> page id of plants
def get_images_by_page(page_num):
	target = 'https://calscape.org/photos/{0}'.format(page_num)
	payload = requests.get(target)

	soup = BeautifulSoup(payload.text, 'lxml')
	divs = soup.find_all(class_='big_image hide')

	image_urls = [url.find('img')['src'] for url in divs]

	return image_urls

def get_names_for_images(page_num):
	target = 'https://calscape.org/photos/{0}'.format(page_num)
	payload = requests.get(target)
	soup = BeautifulSoup(payload.text, 'lxml')
	header = soup.find(id="plant_photos")
	print(header)


get_names_for_images(1)
