import pathlib
import requests
from bs4 import BeautifulSoup

# [Description]
# Returns a list of urls formatted as a string
# If payload is specified, page_num value is ignored.
#
# [Inputs]
# page_num : INT -> page id of plants
# payLoad : HTTP Response code -> 1xx, 2xx, ..., 5xx
def get_images_by_page(page_num=None, payload=None):
	if payload is None:
		target = 'https://calscape.org/photos/{0}'.format(page_num)
		payload = requests.get(target)

	soup = BeautifulSoup(payload.text, 'lxml')
	divs = soup.find_all(class_='big_image hide')

	image_urls = ['http:' + url.find('img')['src'] for url in divs]
	
	return image_urls

# [Description]
# Gets name of plant by page num
# If payload is specified, page_num value is ignored.
#
# [!!!WARNINGS!!!] 
# Could possibly could return a blank name!
#
# [Inputs]
# page_num : INT -> page id of plant
def get_name_for_images(page_num=None, payload=None):
	if payload is None:
		target = 'https://calscape.org/photos/{0}'.format(page_num)
		payload = requests.get(target)
	
	soup = BeautifulSoup(payload.text, 'lxml')
	header = soup.find('h2')

	return header.contents[0][14:].strip()

# [Description]
# Gets payload of webpage
# Returns a request object
#
# [Remarks]
# This is only created so you do not need to import requests again.
def get_payload_for_page(page_num):
	target = 'https://calscape.org/photos/{0}'.format(page_num)
	payload = requests.get(target)

	return payload

# [Description]
# Downloads an image located at the specified resource location.
#
# [Inputs]
# url : STRING -> specific resource location
# path : STRING -> location to be saved at
def download_image(path, url):
	with requests.get(url, stream=True) as r:
		with open(path, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)

# [Description]
# Downloads images located at the specified resource location.
# Creates a new directory (named after the plant) in the location of the given script.
#
# [Inputs]
# page_num : INT -> page number id
def download_images(page_num):
	target = 'https://calscape.org/photos/{0}'.format(page_num)
	payload = requests.get(target)

	image_urls = get_images_by_page(payload=payload)
	plant_name = get_name_for_images(payload=payload)

	pathlib.Path('images/{}/'.format(plant_name)).mkdir(parents=True, exist_ok=True)

	print('Downloading images for {}'.format(plant_name))
	image_num = 0
	for url in image_urls:
		print('... Downloading image_{} at {}'.format(image_num, target))
		download_image('images/{}/img_{}.jpeg'.format(plant_name, image_num), url)
		image_num = image_num + 1

download_images(10)